function [ rec_sample ] = make_spin_sample( j_mat, h_vec, sample_size, mixing_time, samp_weight )
%Sample configurations of spin
%   This function make spin samples at given parameter. The J and H shall be
%   scaled by the inverse tempreture beta. 

%% Network parameters
num_spin = size(j_mat, 1);

%% Sampling parameters
beta = 1;
rec_sample = ones(num_spin, sample_size);

%% Gibbs sampling
cur_spin = ones(num_spin, 1);
tot_sampling = mixing_time + sample_size;
if exist('samp_weight', 'var')
    rand_ind = randsample((1: num_spin), tot_sampling, true, samp_weight);
else   
    rand_ind = randi([1, num_spin], tot_sampling, 1);
end
rand_prob = rand(tot_sampling, 1);
for ii = 1: tot_sampling
    cur_ind = rand_ind(ii);
    diff_energy = - 2 * (j_mat(cur_ind, :) * cur_spin + h_vec(cur_ind))...\
        * cur_spin(cur_ind);        
    accept_prob = min(1, exp(- diff_energy * beta));
    if rand_prob(ii) < accept_prob 
        cur_spin(cur_ind) = - cur_spin(cur_ind);
    end    
    if ii > mixing_time
        rec_sample(:, ii - mixing_time) = cur_spin;
    end
end

end

