%exter_h = zeros(num_spin, 6);
%exter_h(:, 2: 3) = rec_vec(:, 1: 2);
%exter_h(:, 5: 6) = rec_vec(:, 1: 2);
%exter_h(:, 2: 6) = rec_vec;

load('plot16oraclen')

for ii = 1: 6
    rec_sample = make_spin_sample(j_mat, h_vec + exter_h(:, ii), sample_size, mixing_time);
    %[corr_sample, mean_sample] = exact_moments(j_mat, h_vec + rec_bestdir(:, ii) * rec_bestinten(ii));
    rec_all_corr(:, :, ii) = (rec_sample * rec_sample') / sample_size;
    rec_fish(:, :, ii) = fisher_inf(rec_sample);
end

train_dat = struct('round', 6, 'epoch', num_epoch, 'j_mat', j_mat,...
    'h_vec', h_vec, 'corrs', rec_all_corr, 'decayp', 0.3,...
    'stepsz', stepsz, 'counter', 1, 'exter_h', exter_h,...
    'samplingsz', samplingsz, 'samplingmix', samplingmix, 'rec_gap', 50,...
    'lam_l2', 0);


% train_dat.round = ii;
[cur_j, cur_h, datf] = learn_parameters(zeros(num_spin), zeros(num_spin, 1), train_dat);
% rec_curj(:, :, ii) = cur_j; 
% rec_datf{ii} = datf;


%{
subplot(1, 2, 1)
imagesc(j_mat)
colormap(redblue)
caxis([- 2, 2])
subplot(1, 2, 2)
imagesc(cur_j2)
colormap(redblue)
caxis([- 2, 2])
%}