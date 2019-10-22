function [cmat] = random_normalized_graph(num_node, conn, inten)
%Generate random graph with given expected connection number and average
%intensity
%   Detailed explanation goes here

cmatp = random_graph(num_node, 1, norminv(1 - conn / (num_node - 1) / 2)); 
cmat = normalize_graph(cmatp, inten); 

end

