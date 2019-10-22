num_spin = 3;
num_j = 3;
h_vec = zeros(num_spin, 1);
num_config = 27;
load('three_node')

topo_list = [1, 2, 3, 6, 9, 26, 27];
num_topo = size(topo_list, 2);

num_div = 100; num_sample = num_div ^ 2;
num_div2 = num_sample;
axx2 = linspace(-1, 1, num_div);
axx3 = linspace(-1, 1, num_div);
[cor2, cor3] = meshgrid(axx2, axx3);

rec_trinv = zeros(num_topo, num_sample);
rec_inten = zeros(num_topo, num_sample);
rec_fish = zeros(num_topo, num_j, num_j);
opt_option = struct('TolX', 1e-2);
rec_bestdir = zeros(num_topo, num_spin);
rec_bestinten = zeros(num_topo, 1);
rec_energy = zeros(num_topo, 2 ^ num_spin);

ori_energy = zeros(num_topo, 2 ^ num_spin);
ori_fish = zeros(num_topo, num_j, num_j);
num_line = 200;
list_inten = linspace(0, 10, num_line);
rec_land = zeros(num_topo, num_line);
% lamb_list = [1, 0];
lamb_list = 0.1 * ones(1, num_topo);

for it_topo = 1: num_topo
    lamb = lamb_list(it_topo);
    j_mat = rec_net(:, :, topo_list(it_topo));

    for it_samp = 1: num_div2
        if mod(it_samp, 1000) == 1
            disp(it_samp)
        end
        cur_cor23 = [cor2(it_samp); cor3(it_samp)];
        if norm(cur_cor23) >= 1
            rec_inten(it_topo, it_samp) = NaN;
            rec_trinv(it_topo, it_samp) = NaN;
            continue
        end
        mag_dir = [sqrt(1 - norm(cur_cor23)); cur_cor23];
        fun_hand = @(inten) fisher_trinv(fisher_inf_exact(j_mat, h_vec + inten * mag_dir)) + lamb * inten;
        [best_inten, trinv_val] = fminbnd(fun_hand, 0, 40, opt_option);
        if trinv_val > 1e5
            [best_inten, trinv_val] = fminbnd(fun_hand, 0, 10, opt_option);
        end   
        rec_trinv(it_topo, it_samp) = trinv_val - lamb * best_inten;
        rec_inten(it_topo, it_samp) = best_inten;
    end

    [minvar, minind] = min(abs(rec_trinv(it_topo, :))); 
    cur_inten = rec_inten(it_topo, minind);
    cur_cor23 = [cor2(minind); cor3(minind)];
    cur_dir = [sqrt(1 - norm(cur_cor23)); cur_cor23];
    
    rec_bestdir(it_topo, :) = cur_dir;
    rec_bestinten(it_topo) = cur_inten;
    
    ori_energy(it_topo, :) = make_spectrum(j_mat, h_vec);
    ori_fish(it_topo, :, :) = fisher_inf_exact(j_mat, h_vec);
    
    cur_fish = fisher_inf_exact(j_mat, h_vec + cur_inten * cur_dir);
    rec_fish(it_topo, :, :) = cur_fish;
    rec_energy(it_topo, :) = make_spectrum(j_mat, cur_inten * cur_dir);
    
    for jj = 1: num_line
        rec_land(it_topo, jj) = fisher_trinv(fisher_inf_exact(j_mat, h_vec + list_inten(jj) * cur_dir));
    end
    
    ctrinv = reshape(rec_trinv(it_topo, :), num_div, num_div);
    surf(cor2, cor3, log(ctrinv), 'LineStyle','none')
    drawnow

end

for it_topo = 1: num_topo
    rec_mintrinv(it_topo) = min(rec_trinv(it_topo, :));
    rec_oritrinv(it_topo) = fisher_trinv(squeeze(ori_fish(it_topo, :, :)));
    
end

rec_ctrinv = [rec_oritrinv; rec_mintrinv];

%{
cur_dir = [- 1; 1; 1] / sqrt(3);

fun_hand = @(inten) fisher_trinv(fisher_inf_exact(j_mat, h_vec + inten * cur_dir));
[cur_inten, trinv_val] = fminbnd(fun_hand, 0, 40, opt_option);
               
rec_bestdir(it_topo, :) = cur_dir;
rec_bestinten(it_topo) = cur_inten;
    
cur_fish = fisher_inf_exact(j_mat, h_vec + cur_inten * cur_dir);
rec_fish(it_topo, :, :) = cur_fish;
rec_energy(it_topo, :) = make_spectrum(j_mat, cur_inten * cur_dir);

for jj = 1: num_line
    rec_land(it_topo, jj) = fisher_trinv(fisher_inf_exact(j_mat, h_vec + list_inten(jj) * cur_dir));
end    
%}



    