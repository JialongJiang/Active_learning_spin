num_spin = 16;
num_j = num_spin * (num_spin - 1) / 2;
h_vec = zeros(num_spin, 1);
inten = 1.5;
conn = num_spin / 4;
num_rep = 10;
% create_graph;


stepsz = 1e-1;
mixing_time = 1e5;
num_epoch = 10000;
samplingsz = 5e3;
samplingmix = 1e3;
sample_size = 5e6;

j_mat = rec_netn(:, :, 1); 
cfish = fisher_inf_exact(j_mat, h_vec);
rec_vec = h_vec; 

num_repeat = 10; 
%{
rec_perthat = zeros(num_spin, num_repeat); 
rec_pertori = zeros(num_spin, num_repeat); 
rec_estij = zeros(num_spin, num_spin, num_repeat); 
rec_estifish = zeros(num_j, num_j, num_repeat); 
%}
options = optimoptions(@fminunc, 'Display', 'iter', 'OptimalityTolerance', 1e-6);
    
for indii = 1: num_repeat    
    train_with_oracle; 
    esti_fish = fisher_inf(rec_sample); 
    rec_estifish(:, :, indii) = esti_fish; 
    rec_estij(:, :, indii) = cur_j; 
    
    regu_const = 1e-6;
    cflag = 1; 
    while cflag
            xx0 = randn(num_spin, 1) * inten; % Starting guess
            objfun = @(xx) fisher_trinv(fisher_inf_exact(cur_j, xx) + esti_fish, num_j, regu_const);  
        try  
            [xx, fval, exitflag, output] = fminunc(objfun, xx0, options);
        catch
            regu_const = regu_const * 2; 
            continue
        end
        cflag = 0; 
    end
    disp(xx)
    rec_perthat(:, indii) = xx; 
end

options = optimoptions(@fminunc, 'Display', 'iter', 'OptimalityTolerance', 1e-6);
for indii = 1: num_repeat    
    
    regu_const = 1e-6;
    cflag = 1; 
    while cflag
            xx0 = randn(num_spin, 1) * inten; % Starting guess
            objfun = @(xx) fisher_trinv(fisher_inf_exact(j_mat, xx) + cfish, num_j, regu_const);  
        try  
            [xx, fval, exitflag, output] = fminunc(objfun, xx0, options);
        catch
            regu_const = regu_const * 2; 
            continue
        end
        cflag = 0; 
    end
    rec_pertori(:, indii) = xx; 
end

rec_pertrand = inten * rand(num_spin, num_repeat); 
rec_fintrinv = zeros(num_repeat, 3); 
for indii = 1: num_repeat
    fish_hat = fisher_inf_exact(j_mat, rec_perthat(:, indii));
    fish_hatsum = fish_hat + cfish; 
    [eigv, eigd] = eig(fish_hatsum); 
    rec_fintrinv(indii, 1) = sum(1 ./ diag(eigd));   
    
    fish_ori = fisher_inf_exact(j_mat, rec_pertori(:, indii));
    fish_orisum = fish_ori + cfish; 
    [eigv, eigd] = eig(fish_orisum); 
    rec_fintrinv(indii, 2) = sum(1 ./ diag(eigd));  
    
    fish_rand = fisher_inf_exact(j_mat, rec_pertrand(:, indii));
    fish_randsum = fish_rand + cfish; 
    [eigv, eigd] = eig(fish_randsum); 
    rec_fintrinv(indii, 3) = sum(1 ./ diag(eigd));  
end

[eigv, eigd] = eig(cfish); 
ctrinv = sum(1 ./ diag(eigd)); 
    
semilogy(rec_fintrinv', 'o')
hold on
semilogy(1:3, ones(1, 3) * ctrinv); 

%{
esti_l2 = sqrt(sum((rec_estij - j_mat) .^ 2, [1, 2])); 
mean_l2 = mean(esti_l2);
gen_devi = randn(num_spin, num_spin, num_repeat); 
devi_l2 = sqrt(sum(gen_devi .^ 2, [1, 2])); 
gen_devin = gen_devi .* mean_l2 ./ devi_l2; 
rec_randj = gen_devin + j_mat; 
%}