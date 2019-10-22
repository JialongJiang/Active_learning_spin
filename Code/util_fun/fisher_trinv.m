function [trinv] = fisher_trinv(fish_mat, num_eig, epsilon)
%Compute the trace of inverse of Fisher information matrix 
%   Detailed explanation goes here

if ~ exist('epsilon', 'var')
    epsilon = 1e-6;
end

if ~ exist('num_eig', 'var')
    num_eig = size(fish_mat, 1);
end

%num_eig = size(fish_mat, 1);
[~, eigd] = eig(fish_mat);

eigds = diag(eigd);
eigds = sort(eigds, 'descend');
eigdsn = eigds(1: num_eig); 
trinv = sum(1 ./ (epsilon + eigdsn));

end

