%{
inten = 2.5;
conn = 3;
net8 = random_normalized_graph(8, conn, inten);
net12 = random_normalized_graph(12, conn, inten);
net16 = random_normalized_graph(16, conn, inten);

subplot(1, 3, 1)
plot_graph(net8)
subplot(1, 3, 2)
plot_graph(net12)
subplot(1, 3, 3)
plot_graph(net16)
save('network_size', 'net8', 'net12', 'net16')
%}

num_spin = 16;
h_vec = zeros(num_spin, 1);
inten = 2.5;
conn = num_spin / 4;
num_rep = 10;
% create_graph;
num_iter = 5;
num_round = num_iter + 1;

stepsz = 1e-1;
mixing_time = 1e5;
num_epoch = 10000;
samplingsz = 5e3;
samplingmix = 1e3;

size_list = [5e0, 5e1, 5e2, 5e3, 5e4, 5e5, 5e6];
num_testsize = size(size_list, 2);
rec_sizedata = cell(num_testsize, num_rep);
rec_pert = cell(num_rep, 1);
filen = ['sz_datanpp', num2str(num_spin)];


for it_sz = 1: num_testsize
    sample_size = size_list(it_sz);
    for cit_rep = 1: num_rep
        j_mat = rec_net(:, :, cit_rep);
        if isempty(rec_pert{cit_rep})
            learn_oracle;
            rec_pert{cit_rep} = rec_vec;
        else
            rec_vec = rec_pert{cit_rep};
        end
        train_with_oracle;
        rec_sizedata{it_sz, cit_rep} = rec_ctrain;
        
    end
    save(filen, 'rec_sizedata', 'rec_pert', 'rec_net')
end
