function [ fishinfo ] = fisher_inf( samp, freq )
%Compute the empirical fisher information
%   Detailed explanation goes here

[num_spin, num_sample] = size(samp);
if ~exist('freq', 'var')
    freq = 1 / num_sample * ones(1, num_sample);
end
sq_spin = num_spin * num_spin;
mat1 = reshape(samp, [], num_spin, num_sample);
mat2 = reshape(samp, num_spin, [], num_sample);
premat = reshape(mat1 .* mat2, sq_spin, num_sample);
mat4 = freq .* premat * premat'; 

corr = freq .* samp * samp';
corr2 = reshape(corr, sq_spin, 1);
corr4 = corr2 * corr2';

fishinfo = mat4 - corr4;
aux_mat = reshape((1: sq_spin), num_spin, num_spin)';
node_list = reshape(tril(aux_mat), sq_spin, 1);
node_list(node_list == 0) = [];
fishinfo = clear_node(fishinfo, node_list);
%det(fishinfo)
%disp(log(rcond(fishinfo)))
end

