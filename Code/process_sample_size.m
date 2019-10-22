num_spin = size(rec_net, 1); 
num_j = num_spin * (num_spin - 1) / 2; 
rec_fish_eigs = zeros(num_rep, num_round, num_j); 
% rec_ftrinv = zeros(3, 10, 6); 
for it_rep = 1: num_rep
    cfish = 0; 
    j_mat = rec_net(:, :, it_rep); 
    cpert = rec_pert{it_rep}; 
    for it_rnd = 1: num_round
        xx = cpert(:, it_rnd); 
        cfish = cfish + fisher_inf_exact(j_mat, xx);
        [eigv, eigd] = eig(cfish); 
        rec_fish_eigs(it_rep, it_rnd, :) = diag(eigd); 
        rec_ftrinv(3, it_rep, it_rnd) = sum(1 ./ diag(eigd));         
        %semilogy(diag(eigd))
        
    end
end


rec_size_curve = zeros(num_testsize, num_rep, num_round, 5); 
for ii = 1: num_testsize   
    for jj = 1: num_rep
        cdat = rec_sizedata{ii, jj}; 
        for kk = 1: num_round
            cdatn = cdat{kk}; 
            rec_size_curve(ii, jj, kk, 1) = cdatn.rec_l2(end); 
            rec_size_curve(ii, jj, kk, 5) = cdatn.rec_mean(end); 
            rec_size_curve(ii, jj, kk, 2: 4) = cdatn.rec_topk(end, :); 
        end
    end
end
plot(squeeze(rec_size_curve(4, :, :, 1))')



