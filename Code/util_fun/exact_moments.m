function [corr, aver] = exact_moments(j_mat, h_vec)
%Compute the exact correlation and mean for small network
%   Detailed explanation goes here

freq = para_distribution(j_mat, h_vec);
num_spin = size(j_mat, 1);
num_sample = 2 ^ num_spin;

bin_ordered_sample = de2bi(0: 2 ^ num_spin - 1, num_spin)';
samp = bin_ordered_sample * 2 - 1;
mat1 = reshape(samp, [], num_spin, num_sample);
mat2 = reshape(samp, num_spin, [], num_sample);
premat = mat1 .* mat2;
freq3 = reshape(freq, 1, 1, num_sample);
corr = sum(freq3 .* premat, 3);
aver = sum(samp .* freq, 2);

end

