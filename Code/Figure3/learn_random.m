start_id = 71; 
num_test = 10;
load('rec_netnn')
rec_id = zeros(num_test, 1);

%% Network parameters
% To use new network, just create varialbe of J matrix: j_mat and h vector:
% h_vec. 

%% Learning parameters
stepsz = 1e-1;
mixing_time = 1e5;
sample_size = 5e6;
%mixing_time = 5e3;
%sample_size = 1e4;
% Rounds of sampling data
num_round = 10;
% Learning steps after each sampling 
num_epoch = 10000;
% The choice of decay power over iterations
list_power = linspace(0.2, 0.5, num_round);
list_l2 = linspace(0, sqrt(0.05), num_round) .^ 2;
rec_gap = 200;

%% Record parameters
num_spin = size(rec_net, 1);
num_j = num_spin * (num_spin - 1) / 2;

rec_all_corr = zeros(num_spin, num_spin, num_round, num_test);
%rec_all_mean = zeros(num_spin, num_round);
rec_dir = zeros(num_spin, num_round, num_test);
rec_fish = zeros(num_j, num_j, num_round, num_test);
rec_realfish = zeros(num_j, num_j, num_round, num_test);
rec_curj = zeros(num_spin, num_spin, num_round, num_test);

num_rec = floor(num_epoch / rec_gap);
rec_l2 = zeros(num_rec, num_round, num_test);
rec_topk = zeros(num_rec, 3, num_round, num_test);


for it_net = 1: num_test

cur_id = it_net + start_id - 1;

rec_id(it_net) = cur_id;
j_mat = rec_net(:, :, cur_id);

% mat_edges = (j_mat ~= 0);
% num_edges = sum(sum(j_mat ~= 0)) / 2;

%% Learning setup
cur_j = zeros(num_spin);
cur_h = zeros(num_spin, 1);
% The counter controls for step size
counter = 1;
samplingsz = 5e3;
samplingszmat = 5e4;
samplingmix = 1e3;
%samplingsz = 2e3;
%samplingmix = 8e2;


rec_jgrad = zeros(num_spin, num_spin, num_round);
rec_hgrad = zeros(num_spin, num_round);

%% Search parameters

% curent fisher information 
cur_fish = zeros(num_j, num_j);
real_fish = zeros(num_j, num_j);

exter_h = zeros(num_spin, num_round);

train_dat = struct('round', 1, 'epoch', num_epoch, 'j_mat', j_mat,...
    'h_vec', h_vec, 'corrs', rec_all_corr(:, :, 1), 'decayp', 0.2,...
    'stepsz', stepsz, 'counter', 1, 'exter_h', zeros(num_spin, 1),...
    'samplingsz', samplingsz, 'samplingmix', samplingmix, 'rec_gap', rec_gap,...
    'gsteps', 2000, 'fish_samples', 5e5, 'fish_mix', 1e4, 'fish_epsi', 1e-3);
options = optimoptions(@fminunc, 'Display', 'iter', 'MaxFunctionEvaluations', 500);

for ii = 1: num_round

disp(ii)
%% Make samples
rec_sample = make_spin_sample(j_mat, h_vec + exter_h(:, ii), sample_size, mixing_time);
%[corr_sample, mean_sample] = exact_moments(j_mat, h_vec + rec_bestdir(:, ii) * rec_bestinten(ii));
rec_all_corr(:, :, ii, it_net) = (rec_sample * rec_sample') / sample_size;
%rec_all_mean(:, ii) = mean(rec_sample, 2);

train_dat.round = ii; train_dat.corrs = rec_all_corr(:, :, 1: ii, it_net);
train_dat.decayp = list_power(ii); 
counter = 1; %ii * 10; 
train_dat.exter_h = exter_h; 
train_dat.lam_l2 = list_l2(ii);
cur_j = zeros(num_spin, num_spin);
train_dat.epoch = num_epoch; % * sqrt(ii);
[cur_j, cur_h, datf] = learn_parameters(cur_j, cur_h, train_dat);

% Use Gaussian random field to do next round of perturbation
%rec_bestdir(:, ii + 1) = randn(num_spin, 1);
%rec_bestinten(ii + 1) = mean(abs(cur_j(:))) * num_spin;
% The counter for stepsize is reset to give large stepsize again

% Reset the step size parameter after having net data 

cur_fish = fisher_inf(rec_sample) + cur_fish;
real_fish = fisher_inf_exact(j_mat, h_vec + exter_h(:, ii)) + real_fish;

rec_fish(:, :, ii, it_net) = cur_fish;
rec_realfish(:, :, ii, it_net) = real_fish;
rec_l2(:, ii, it_net) = datf.rec_l2;
rec_topk(:, :, ii, it_net) = datf.rec_topk;
rec_curj(:, :, ii, it_net) = cur_j;

if ii == num_round
    break
end


objfunp = @(xx) fisher_trinv(fisher_inf_exact(cur_j, xx) + cur_fish, num_j, 1e-6);
objreal = @(xx) fisher_trinv(fisher_inf_exact(j_mat, xx) + real_fish, num_j, 1e-6);
cflag = 1;
while cflag
    try 
        xx0 = randn(num_spin, 1) * 2;
        [xx, fval, exitflag, output] = fminunc(objfunp, xx0, options);
        cflag = 0;
    catch
        disp('error')
        cflag = 1;
    end
end

exter_h(:, ii + 1) = xx;
rec_dir(:, ii + 1, it_net) = xx;

end

end