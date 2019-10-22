num_spin = size(j_mat, 1);
h_vec = zeros(num_spin, 1); 
real_fish = fisher_inf_exact(j_mat, h_vec);
[realv, reald] = eig(real_fish);
num_j = size(real_fish, 1);


creal_fish = real_fish;
options = optimoptions(@fminunc, 'Display', 'iter');
rec_fish = zeros(num_j, num_j, num_iter);
rec_vec = zeros(num_spin, num_iter + 1); 


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
    % [realv, reald] = eig(creal_fish);
    % rec_realv(:, :, ii) = realv; 
    % rec_reald(:, ii) = diag(reald); 
    % rec_fish(:, :, ii) = creal_fish;
end



%{


indj = index_jvec(num_spin);
indj(:, 3) = 3 * group16(indj(:, 1)) + group16(indj(:, 2));

group16 = @(ii)  and(5 < ii, ii < 11) + 2 * (ii > 10);

[~, idx] = sort(indj(:, 3));
indj = indj(idx, :);
line_indj = sub2ind([num_spin, num_spin], indj(:, 1), indj(:, 2));
j_vec = reshape_jvec(j_mat);
plot(j_vec(idx))

imagesc(realv(:, idx)')
colormap(redblue)
caxis([-0.5, 0.5])
figure
plot(j_vec(idx))

[ecorr, emean] = exact_moments(j_mat, h_vec);
imagesc(ecorr)
colormap(redblue)
caxis([- 1, 1])


%}