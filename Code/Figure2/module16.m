num_spin = 16;
obj_inten = 2;

j_mat = zeros(num_spin);
j_mat(1: 5, 1: 5) = - 1;
j_mat(6: 10, 6: 10) = - 1;
j_mat(11: 16, 11: 16) = - 1;
j_mat(1: num_spin + 1: end) = 0;

j_mat(1, 6) = 2;
j_mat(1, 11) = 2;
j_mat(1, 15) = 2;
j_mat(7, 14) = 2; j_mat(4, 10) = 2;
j_mat(5, 12) = 2; j_mat(16, 2) = 2;
j_mat(7, 12) = 2; j_mat(2, 9) = 2;
j_mat(13, 10) = 2;

j_mat(12, 16) = 1;
j_mat(2, 3) = 1;
j_mat(8, 10) = 1; j_mat(14, 15) = 1;
j_mat(7, 6) = 1; j_mat(11, 13) = 1;
j_mat(6, 8) = 1; j_mat(11, 12) = 1; j_mat(13, 15) = 1;
j_mat(11, 14) = 1; j_mat(4, 5) = 1;

j_mat = (j_mat + j_mat') / 2;


rng(20180125)
aux_mat = zeros(num_spin);
for ii = 2: num_spin
    for jj = 1: ii - 1
        curv = 0;
        while curv < 1
            curv = randn;
        end
        aux_mat(ii, jj) = curv;
        aux_mat(jj, ii) = curv;
    end
end

j_mat = j_mat .* aux_mat;
mean_inten = mean(abs(j_mat(j_mat ~= 0)));
j_mat = j_mat * obj_inten / mean_inten;
h_vec = zeros(num_spin, 1);
plot_graph(j_mat)

save('module16.mat', 'j_mat', 'h_vec')
