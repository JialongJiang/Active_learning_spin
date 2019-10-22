num_spin = 8;
j_mat = zeros(num_spin);
h_vec = zeros(num_spin, 1);

j_mat(2: num_spin + 1: end) = - 1;
j_mat(1, num_spin) = - 1; 
j_mat = j_mat + j_mat';
inten = 3;
j_mat = j_mat * inten;

% h_test1 = ones(num_spin, 1);
% h_test1(1: 2: end) = - 1;
% h_test2 = cos((1: num_spin) * pi / 2)'; 
h_test1 = [1, 1, - 1, - 1, 1, 1, - 1, - 1]';
h_test2 = [1, - 1, 1, - 1, 1, - 1, 1, - 1]';

fish_chain = fisher_inf_exact(j_mat, h_vec);
% fish_chain = fisher_inf_exact(j_mat, inten * h_test);
sub_ind = cumsum([1, (num_spin - 1) : - 1: 2]);
sub_ind(num_spin) = num_spin - 1;


options = optimoptions(@fminunc, 'Display', 'iter');
objfun1 = @(xx) fisher_trinv(fish_mask(fisher_inf_exact(j_mat, xx * h_test1), sub_ind), num_spin, 1e-16);
[inten1, fval, exitflag, output] = fminunc(objfun1, inten, options);

cfish1 = fish_mask(fisher_inf_exact(j_mat, inten1 * h_test1), sub_ind);
objfun2 = @(xx) fisher_trinv(fish_mask(fisher_inf_exact(j_mat, xx * h_test2), sub_ind) + cfish1, num_spin, 1e-16);
[inten2, fval, exitflag, output] = fminunc(objfun2, inten, options);

h_pert(:, 1) = inten1 * h_test1; 
h_pert(:, 2) = inten2 * h_test2; 
fish_ori = fish_mask(fisher_inf_exact(j_mat, h_vec), sub_ind);
fish_pert1 = cfish1; 
fish_pert2 = fish_pert1 + fish_mask(fisher_inf_exact(j_mat, inten2 * h_test2), sub_ind);
rec_eigs = zeros(num_spin, 3); 
[eigv, eigd] = eig(fish_ori); 
rec_eigs(:, 1) = diag(eigd); 
[eigv, eigd] = eig(fish_pert1); 
rec_eigs(:, 2) = diag(eigd); 
[eigv, eigd] = eig(fish_pert2); 
rec_eigs(:, 3) = diag(eigd); 
figure
semilogy(rec_eigs)


num_test = 20; 
inten_list = linspace(0, 5, num_test); 
rec_inten = zeros(2, num_test); 
rec_trinv = zeros(3, num_test); 
jori = j_mat / inten; 


for ii = 1: num_test
    cinten = inten_list(ii); 
    cjmat = cinten * jori; 
    
    objfun1 = @(xx) fisher_trinv(fish_mask(fisher_inf_exact(cjmat, xx * h_test1), sub_ind), num_spin, 1e-16);
    [inten1, fval, exitflag, output] = fminunc(objfun1, cinten, options);
    rec_trinv(1, ii) = objfun1(0); 
    rec_trinv(2, ii) = fval; 
    
    cfish1 = fish_mask(fisher_inf_exact(cjmat, inten1 * h_test1), sub_ind);
    objfun2 = @(xx) fisher_trinv(fish_mask(fisher_inf_exact(cjmat, xx * h_test2), sub_ind) + cfish1, num_spin, 1e-16);
    [inten2, fval, exitflag, output] = fminunc(objfun2, cinten, options);
    rec_trinv(3, ii) = fval; 
    
    rec_inten(1, ii) = inten1; 
    rec_inten(2, ii) = inten2; 
    
end

figure
semilogy(inten_list, rec_trinv)

rec_corrs = zeros(num_spin, num_spin, 1); 
rec_corrs(:, :, 1) = exact_moments(j_mat, h_vec); 
rec_corrs(:, :, 2) = exact_moments(j_mat, h_pert(:, 1)); 
rec_corrs(:, :, 3) = exact_moments(j_mat, h_pert(:, 2)); 
figure
subplot(1, 3, 1)
imagesc(rec_corrs(:, :, 1))
caxis([- 1, 1])
subplot(1, 3, 2)
imagesc(rec_corrs(:, :, 2))
caxis([- 1, 1])
subplot(1, 3, 3)
imagesc(rec_corrs(:, :, 3))
caxis([- 1, 1])

%{
imagesc(fish_mask(fisher_inf_exact(j_mat, h_pert(:, 1)), sub_ind))
caxis([- 1, 1])
imagesc(fish_mask(fisher_inf_exact(j_mat, h_pert(:, 2)), sub_ind))
caxis([- 1, 1])
%}
