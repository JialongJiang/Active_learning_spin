function [ sorted ] = ranked_distribution( j_mat )
%The function plot the ranked distribution of interaction stength
%   Detailed explanation goes here

num_spin = size(j_mat, 1);
num_element = num_spin * (num_spin - 1) / 2;
triuj = triu(j_mat, 1);
sorted = sort(abs(triuj(:)), 'descend');
sorted(num_element + 1: end) = [];
plot(1: num_element, sorted)

end

