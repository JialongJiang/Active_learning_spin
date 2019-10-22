function [dist] = devi_distance(net1, net2, h_vec)
%Compute the large deviation distance between two networks
%   Detailed explanation goes here
netm = (net1 + net2) / 2;
dist = - log(para_parti(netm, h_vec))...
       + (log(para_parti(net1, h_vec)) + log(para_parti(net2, h_vec))) / 2;

end

