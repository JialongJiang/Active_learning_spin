function [cur_j, cur_h] = black_box_function(corr_mat, mean_mat)
%UNTITLED3 Summary of this function goes here
%   Detailed explanation goes here

%% Attach real data here 
rec_all_corr = corr_mat; 
rec_mean = mean_mat; 

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




end

