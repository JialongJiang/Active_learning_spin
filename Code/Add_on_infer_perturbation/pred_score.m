function [ sco ] = pred_score( cur_j, j_mat )
%Compute the score of J prediction 
%   Detailed explanation goes here

num_link = sum(j_mat(:) ~= 0);
thre2 = 1.5 * num_link;
thre1 = num_link;
thre3 = 2 * num_link;

cur_j = (cur_j + cur_j') / 2;
sorted = sort(abs(cur_j(:)));

sco(1) = rank_pred(sorted, thre1, cur_j, j_mat, num_link);
sco(2) = rank_pred(sorted, thre2, cur_j, j_mat, num_link);
sco(3) = rank_pred(sorted, thre3, cur_j, j_mat, num_link);



    function sco = rank_pred(sorted, thres, cur_j, j_mat, num_link)
        val = sorted(end - thres);
        cur_j(abs(cur_j) < val) = 0;
        sco = sum(sum(sign(cur_j .* j_mat))) / num_link;
    end

end

