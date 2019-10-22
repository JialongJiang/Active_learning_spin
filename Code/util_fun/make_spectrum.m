function [energies] = make_spectrum(j_mat, h_vec)
%Compute the energy spectrum of given J and h 
%   Detailed explanation goes here

num_spin = size(j_mat, 1);
bin_ordered_sample = de2bi(0: 2 ^ num_spin - 1, num_spin)';
ordered_sample = bin_ordered_sample * 2 - 1;
energies = h_vec' * ordered_sample...
    + sum(j_mat * ordered_sample .* ordered_sample) / 2; 

end

