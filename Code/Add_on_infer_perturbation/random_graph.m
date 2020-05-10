function [j_mat] = random_graph(num_node, gstd, gthre)
%Create random graph with Gaussian edge link with cutoff on small edges
%   Detailed explanation goes here
j_mat = randn(num_node) * gstd;
j_mat = (j_mat + j_mat.') / sqrt(2);
j_mat(abs(j_mat) < gthre) = 0;
j_mat(1: num_node + 1: end) = 0;

end

