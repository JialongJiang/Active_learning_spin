it_round = 1;

cfishd = data_fishd(:, it_round, :);
rfishd = data_realfishd(:, it_round, :);
loglog(rfishd(:), cfishd(:), 'o')

aux_matrix = (1: num_j)' * ones(1, num_j);
aux_matrix2 = aux_matrix .^ 2;
data_vspread = zeros(num_j, num_round, num_data);
for ii = 1: num_round
    for jj = 1: num_data
        cdata = data_fishinnop(:, :, ii, jj);
        %test = data_realfishv(:, :, ii, jj)' * data_fishv(:, :, ii, jj);
        prob_dist = cdata .^ 2;
        cmean = sum(prob_dist .* aux_matrix);
        cmean2 = sum(prob_dist .* aux_matrix2);
        %centropy = - sum(prob_dist .* log(prob_dist), 1);
        cspread = cmean2 - cmean .^ 2;
        data_vspread(:, ii, jj) = cspread';
    end
end

imagesc(data_fishinnop(:, :, 5, 1) .^ 2)
cspread = data_vspread(:, 1, :);
loglog(rfishd(:), cspread(:), 'o')
      
        