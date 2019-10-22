function [ j_mat ] = clear_node( j_mat, nodes )
%Delete node by the given index 
%   Detailed explanation goes here

sorted = sort(nodes);
num_nodes = size(nodes, 1) * size(nodes, 2);
for ii = 0: num_nodes - 1
    j_mat(sorted(end - ii), :) = [];
    j_mat(:, sorted(end - ii)) = [];
end
%plot_graph(j_mat)

end

