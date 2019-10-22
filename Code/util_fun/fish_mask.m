function [fish] = fish_mask(fish, subind)
%Delete the inrelevant dimensions
%   Detailed explanation goes here

fish = fish(:, subind); 
fish = fish(subind, :); 

end

