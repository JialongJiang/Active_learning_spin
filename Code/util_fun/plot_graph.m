function [ ] = plot_graph( cur_j, cur_h, jmax, topn )
%Plot a spin graph
%   The width represents strength and the color is the sign.

cur_j = 0.5 * (cur_j + cur_j');
%num_spin = size(cur_j, 1);
sorted = sort(abs(cur_j(:)));
%topn = 100;
if exist('topn', 'var')
    thres = sorted(end - topn);
    cur_j(abs(cur_j) < thres) = 0;
end

G = graph(cur_j);
max_wid = 7;
if ~ exist('jmax', 'var')
    jmax = max(abs(G.Edges.Weight));
end
G.Edges.LWidths = max_wid * min(1, abs(G.Edges.Weight) / jmax);
%load('network_config', 'xd', 'yd')
%pp = plot(G, 'XData', xd, 'YData', yd);
pp = plot(G);

nl = pp.NodeLabel;
pp.NodeLabel = '';
xd = get(pp, 'XData');
yd = get(pp, 'YData');
text(xd, yd, nl, 'FontSize', 16, 'HorizontalAlignment','left', 'VerticalAlignment','middle')

pp.LineWidth = G.Edges.LWidths;
posi_path = G.Edges.Weight > 0;
nege_path = G.Edges.Weight < 0;
edge_color = zeros(size(posi_path, 1), 3);
edge_color(posi_path, 1) = 1;
edge_color(nege_path, 3) = 1;
pp.EdgeColor = edge_color;

end

