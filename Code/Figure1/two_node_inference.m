%fish_fun = @(j, h1, h2) (4 * exp(2 * j) * (exp(2 * h1) + exp(2 * h2) + exp(4 * h1 + 2 * h2) ...
%    + exp(2 * h1 + 4 * h2))) ./ (1 + exp(2 * (h1 + h2)) + exp(2 * (h1 + j)) + ...
%    exp(2 * (h2 + j))) .^ 2;

fish_fun = @(j, h1, h2) 4 * (1 + exp(2 * (h1 + h2))) .* (exp(2 * (h1 + j)) + exp(2 * (h2 + j)))...
    ./ (1 + exp(2 * (h1 + h2)) + exp(2 * (h1 + j)) + ...
    exp(2 * (h2 + j))) .^ 2;
jj = - 1;
prange = 3; num_gird = 100;
xx = linspace(- prange, prange, num_gird); 
yy = linspace(- prange, prange, num_gird);
[xxm , yym] = meshgrid(xx, yy);
zz = fish_fun(jj, xxm, yym);

figure
surf(xxm, yym, zz, 'edgecolor', 'none')

line_para = linspace(0, 4, 100) / 2;
fish_plus = fish_fun(jj, line_para, line_para);

fish_minus = fish_fun(jj, line_para, - line_para);
figure
plot(line_para, fish_plus)
hold on
plot(line_para, fish_minus)

corr_fun = @(j, h1, h2) ((1 + exp(2 * (h1 + h2))) - (exp(2 * (h1 + j)) + exp(2 * (h2 + j))))...
    ./ (1 + exp(2 * (h1 + h2)) + exp(2 * (h1 + j)) + ...
    exp(2 * (h2 + j)));
corr_plus = corr_fun(jj, line_para, line_para); 
corr_minus = corr_fun(jj, line_para, - line_para); 
figure
plot(line_para, corr_plus)
hold on
plot(line_para, corr_minus)

j_mat = ones(2) * jj; 
j_mat(1: 3: end) = 0; 
[prob_ori, samp] = para_distribution(j_mat, [0; 0]); 

options = optimoptions(@fminunc, 'Display', 'iter');
inten0 = jj; 
objfun = @(inten) - fish_fun(jj, inten, - inten);
[inten, fval, exitflag, output] = fminunc(objfun, inten0, options);
h_pert = [1; - 1] * abs(inten); 
[prob_pert, samp] = para_distribution(j_mat, h_pert);
figure
semilogy(prob_ori, 'o')
hold on
semilogy(prob_pert, 'o')


rec_inten = linspace(0, 4, 100); 
rec_fishinv = 1 ./ fish_fun(rec_inten, 0, 0); 
figure
semilogy(rec_inten, rec_fishinv)
hold on
semilogy(rec_inten, ones(size(rec_fishinv)))
