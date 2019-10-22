function [ freq, ordered_sample ] = para_distribution( j_mat, h_vec, ifplot )
%Show distribution from spin net parameters
%   This function computes the Boltzmann distribution with given J matrix
%   and h magnetization.
if ~ exist('ifplot')
    ifplot = 0;
end

num_spin = size(j_mat, 1);

bin_ordered_sample = de2bi(0: 2 ^ num_spin - 1, num_spin)';
ordered_sample = bin_ordered_sample * 2 - 1;
ordered_energy = h_vec' * ordered_sample...
    + sum(j_mat * ordered_sample .* ordered_sample) / 2; 
ordered_exp = exp(- ordered_energy);
partition = sum(ordered_exp);
freq = ordered_exp / partition;

if ifplot
    xx = 0: 2 ^ num_spin - 1;
    scatter(xx, freq)
    %hold off
end
end

