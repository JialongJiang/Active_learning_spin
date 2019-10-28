start_id = 35; 
num_test = 15;
load('rec_netnnc')
% load('cdata1to27')
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
%rec_dir = zeros(num_spin, num_round, num_test);
rec_fish = zeros(num_j, num_j, num_round, num_test);
rec_curj = zeros(num_spin, num_spin, num_round, num_test);
num_rec = 2 * floor(num_epoch / rec_gap);
rec_l2 = zeros(num_rec, num_round, num_test);
rec_topk = zeros(num_rec, 3, num_round, num_test);


for it_net = 1: num_test

cur_id = data_id(it_net + start_id - 1);

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

ucorrs = zeros(num_spin);
for ii = 1: num_round

disp(ii)
%% Make samples
rec_sample = make_spin_sample(j_mat, h_vec, sample_size, mixing_time);
%rec_all_corr(:, :, ii, it_net) = (rec_sample * rec_sample') / sample_size;
%rec_all_mean(:, ii) = mean(rec_sample, 2);
ccorrs = (rec_sample * rec_sample') / sample_size;
rec_all_corr(:, :, ii, it_net) = ccorrs;
ucorrs = (ccorrs + ucorrs * (ii - 1)) / ii;
train_dat.round = 1; 
train_dat.corrs = ucorrs;
train_dat.decayp = 0.2; 
counter = 1; %ii * 10; 
train_dat.exter_h = exter_h; 
train_dat.lam_l2 = 0; %list_l2(ii);
cur_j = zeros(num_spin, num_spin);
train_dat.epoch = num_epoch + num_epoch * (ii - 1) / 9; % * sqrt(ii);
[cur_j, cur_h, datf] = learn_parameters(cur_j, cur_h, train_dat);

% Use Gaussian random field to do next round of perturbation
%rec_bestdir(:, ii + 1) = randn(num_spin, 1);
%rec_bestinten(ii + 1) = mean(abs(cur_j(:))) * num_spin;
% The counter for stepsize is reset to give large stepsize again

% Reset the step size parameter after having net data 

%cur_fish = fisher_inf(rec_sample) + cur_fish;
%real_fish = fisher_inf_exact(j_mat, h_vec + exter_h(:, ii)) + real_fish;

%rec_fish(:, :, ii, it_net) = cur_fish;

num_sz = size(datf.rec_l2, 1);
rec_l2(1 :num_sz, ii, it_net) = datf.rec_l2;
rec_topk(1 :num_sz, :, ii, it_net) = datf.rec_topk;
rec_curj(:, :, ii, it_net) = cur_j;
plot(rec_l2(:, :, it_net))
drawnow
end

end