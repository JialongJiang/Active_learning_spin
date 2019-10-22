function [fishinfo] = fisher_inf_exact(j_mat, h_vec)
% Compute the exact fisher information matrix from parameters
%   Detailed explanation goes here

[freq, samp] = para_distribution(j_mat, h_vec);
fishinfo = fisher_inf(samp, freq);

end

