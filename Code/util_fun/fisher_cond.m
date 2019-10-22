function [mycond] = fisher_cond(fish_mat, epsilon)
%Compute the condition number of Fisher information matrix
%   Detailed explanation goes here

if ~ exist('epsilon', 'var')
    epsilon = 1e-15;
end

[~, eigd] = eigs(fish_mat);
eigds = diag(eigd);
mycond = eigds(1) / (eigds(end) + epsilon);

end

