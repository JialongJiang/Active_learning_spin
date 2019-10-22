function [f_ind] = ind_convert(indx, indy, num_spin)
%Convert the index of matrix to the Fisher information index 
%   Detailed explanation goes here

up_diag = find(indx >= indy);
indx(up_diag) = []; indy(up_diag) = [];
aux_list = (num_spin - 1: - 1: 0);
add_ind = cumsum(aux_list); add_ind = [0, add_ind];
f_ind = add_ind(indx)' + indy - indx;

end

