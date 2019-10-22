function [ freq ] = samp_distribution( rec_sample, ifplot )
%This function computes empirical distribution
%   This function convert sample to binary variables and computes their
%   frequency. 
if ~ exist('ifplot', 'var')
    ifplot = 0;
end

[num_spin, sample_size] = size(rec_sample);
%% Test probility
bin_rec_sample = (rec_sample + 1) / 2;
aux_bin_vec = 2 .^ (0: num_spin - 1);
ind_rec_sample = aux_bin_vec * bin_rec_sample;
count_rec = tabulate(ind_rec_sample);
freq = zeros(2 ^ num_spin, 1);
freq(count_rec(:, 1) + 1) = count_rec(:, 2) / sample_size;

if ifplot
    xx = 0: 2 ^ num_spin - 1;
    scatter(xx, freq)
    %hold off
end
end

