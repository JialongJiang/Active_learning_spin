% Input: n * n * N correlation matrix. n * N mean matrix
% n is the number of variables, N is the number of perturbation experiments 

%% Prepare synthetic data
num_spin = 12; 
j_mat = random_graph(num_spin, 1.2, 1.2);
plot_graph(j_mat)
num_round = 5; 
h_vec = randn(num_spin, num_round) * 1.4; 
rec_all_corr = zeros(num_spin, num_spin, num_round); 
rec_mean = zeros(num_spin, num_round); 

for ii = 1: num_round
    cur_sample = make_spin_sample(j_mat, h_vec(:, ii), 5e5, 1e4);
    rec_all_corr(:, :, ii) = (cur_sample * cur_sample') / 5e5;
    rec_mean(:, ii) = mean(cur_sample, 2);
    subplot(1, num_round, ii)
    imagesc(rec_all_corr(:, :, ii))    
end

%% Attach real data here 

num_epoch = 1e4; 
stepsz = 0.1; 
samplingsz = 5e3; 
samplingmix = 1e3; 


num_round = size(rec_all_corr, 3); 
num_spin = size(rec_all_corr, 1); 
exter_h = 0; 
if ~exist('j_mat', 'var')
    j_mat = zeros(num_spin); 
end
if ~exist('h_vec', 'var')
    h_vec = zeros(num_spin, num_round); 
end
train_dat = struct('round', num_round, 'epoch', num_epoch, 'j_mat', j_mat,...
    'h_vec', h_vec, 'corrs', rec_all_corr, 'means', rec_mean, 'decayp', 0.3,...
    'stepsz', stepsz, 'counter', 1, 'exter_h', exter_h,...
    'samplingsz', samplingsz, 'samplingmix', samplingmix, 'rec_gap', 50,...
    'lam_l2', 0, 'lam_l1', 0);


[cur_j, cur_h, datf] = learn_parameters_kbox(zeros(num_spin), zeros(num_spin, num_round), train_dat);

figure
subplot(1, 2, 1)
imagesc(cur_h)
caxis([-2, 2])
subplot(1, 2, 2)
imagesc(h_vec)
caxis([-2, 2])

[jj, hh] = black_box_function(rec_all_corr, rec_mean); 

