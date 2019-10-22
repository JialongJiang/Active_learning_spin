function [ind_jvec] = index_jvec(num_spin)
%Return the interacting spin each j represents
%   Detailed explanation goes here
num_j = num_spin * (num_spin - 1) / 2;
sq_spin = num_spin ^ 2; 

aux_mat = reshape((1: sq_spin), num_spin, num_spin)';
node_list = reshape(triu(aux_mat, 1), sq_spin, 1);
node_list(node_list == 0) = [];
aux_ind = sort(node_list);

ind_jvec = zeros(num_j, 2);

[ind_jvec(:, 1), ind_jvec(:, 2)] = ind2sub([num_spin, num_spin], aux_ind);

end

