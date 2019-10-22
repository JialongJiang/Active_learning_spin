function [parti] = para_parti(j_mat, h_vec)
%Coompute the partition function from interaction matrix
%   Detailed explanation goes here

num_spin = size(j_mat, 1);

bin_ordered_sample = de2bi(0: 2 ^ num_spin - 1, num_spin)';
ordered_sample = bin_ordered_sample * 2 - 1;
ordered_energy = h_vec' * ordered_sample...
    + sum(j_mat * ordered_sample .* ordered_sample) / 2; 
ordered_exp = exp(- ordered_energy);
parti = sum(ordered_exp);

end

