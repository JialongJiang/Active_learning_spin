num_spin = size(j_mat, 1);
h_vec = zeros(num_spin, 1); 
real_fish = fisher_inf_exact(j_mat, h_vec);
[realv, reald] = eig(real_fish);
num_j = size(real_fish, 1);


creal_fish = real_fish;
options = optimoptions(@fminunc, 'Display', 'iter');
rec_fish = zeros(num_j, num_j, num_iter + 1);
rec_vec = zeros(num_spin, num_iter + 1); 
rec_fish(:, :, 1) = real_fish; 

for ii = 2: num_iter + 1
    regu_const = 1e-6;
    cflag = 1; 
    while cflag
            xx0 = randn(num_spin, 1) * 2; % Starting guess
            objfun = @(xx) fisher_trinv(fisher_inf_exact(j_mat, xx) + creal_fish, num_j, regu_const);  
        try  
            [xx, fval, exitflag, output] = fminunc(objfun, xx0, options);
        catch
            regu_const = regu_const * 5; 
            continue
        end
        cflag = 0; 
    end
    creal_fish = creal_fish + fisher_inf_exact(j_mat, xx);
    rec_vec(:, ii) = xx;
    rec_fish(:, :, ii) = creal_fish;
end
