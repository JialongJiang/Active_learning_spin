for ii = 1: 6
    subplot(2, 3, ii)
    imagesc(rec_all_corr(:, :, ii))
    caxis([- 1, 1])
end

figure
for ii = 1: 6
    subplot(2, 3, ii)
    imagesc(mean(rec_all_corr(:, :, 1: ii), 3))
    caxis([- 1, 1])
end