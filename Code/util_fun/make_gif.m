function [ filename ] = make_gif( filename, gcf, ii, interval )
%Make gif from plot
%   Detailed explanation goes here
if ~ exist('interval', 'var') 
    interval = 0.1;
end

F=getframe(gcf);
I=frame2im(F);
[I, map]=rgb2ind(I, 256);

if ii == 1
    imwrite(I,map,filename,'gif', 'DelayTime', interval);
else
    imwrite(I,map,filename,'gif', 'WriteMode','append', 'DelayTime', interval);
end

end

