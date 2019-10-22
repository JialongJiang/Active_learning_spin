function [cmat] = normalize_graph(cmat, averg)
%Normalize the connection intensity of the graph to the given average
%   Detailed explanation goes here
nonz_mat = cmat(cmat ~= 0); 
scale_fact = averg / mean(abs(nonz_mat)); 
cmat = cmat * scale_fact; 


end

