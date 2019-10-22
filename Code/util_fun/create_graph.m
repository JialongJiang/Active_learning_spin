% num_spin = 8;
num_net = num_rep * 10;
rec_net = zeros(num_spin, num_spin, num_net);
obj_inten = inten;
h_vec = zeros(num_spin, 1);
rec_trinv = zeros(num_net, 1); 

for ii = 1: num_net    
    isConnected = 0;
    while ~isConnected
        j_mat = random_normalized_graph(num_spin, conn, inten); 
        bins = conncomp(digraph(j_mat), 'Type', 'weak');
        isConnected = all(bins == 1);
    end
    % plot_graph(j_mat);
    mean_inten = mean(abs(j_mat(j_mat ~= 0)));
    j_mat = j_mat * obj_inten / mean_inten;
    % cfish = fisher_inf_exact(j_mat, h_vec);
    % [fishv, fishd] = eig(cfish);
    % semilogy(diag(fishd))
    rec_net(:, :, ii) = j_mat;
    cfish = fisher_inf_exact(j_mat, h_vec);
    [eigv, eigd] = eig(cfish); 
    rec_trinv(ii) = sum(1 ./ diag(eigd));   
    
end
rec_net = rec_net(:, :, rec_trinv > 0); 
rec_trinv = rec_trinv(rec_trinv > 0); 
loginv = log(rec_trinv); 
logmean = mean(loginv); 
logstd = std(loginv);
wind = (loginv < logmean + logstd) .* (loginv > logmean - logstd); 
rec_netn = rec_net(:, :, wind == 1); 
rec_trinvn = rec_trinv(wind == 1); 
semilogy(rec_trinv)
hold on
semilogy(rec_trinv .* wind, 'o')
num_cand = size(rec_netn, 3); 
selind = randsample(num_cand, num_rep); 
rec_net = rec_netn(:, :, selind); 


