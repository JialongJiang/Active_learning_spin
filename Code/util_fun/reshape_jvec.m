function [j_vec] = reshape_jvec(j_mat)
%Convert the J matrix to the form of vector without repeat 
%   Detailed explanation goes here
num_spin = size(j_mat, 1);
sq_spin = num_spin ^ 2; 
aux_mat = reshape((1: sq_spin), num_spin, num_spin)';
node_list = reshape(tril(aux_mat), sq_spin, 1);
node_list(node_list == 0) = [];
j_vec = reshape(j_mat, sq_spin, 1); 
j_vec(node_list) = [];


end

