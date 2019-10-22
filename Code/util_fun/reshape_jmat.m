function [j_mat] = reshape_jmat(j_vec)
%Convert the J vector to the shape of matrix 
%   Detailed explanation goes here
num_j = size(j_vec, 1);
num_spin = (sqrt(num_j * 8 + 1) + 1) / 2;
sq_spin = num_spin ^ 2; 

aux_mat = reshape((1: sq_spin), num_spin, num_spin)';
node_list = reshape(triu(aux_mat, 1), sq_spin, 1);
node_list(node_list == 0) = [];
aux_ind = sort(node_list);

j_prevec = zeros(sq_spin, 1);
j_prevec(aux_ind) = j_vec; 
j_mat = reshape(j_prevec, num_spin, num_spin);
j_mat = j_mat + j_mat.';

end

