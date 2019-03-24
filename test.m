close all;

x = [1:20]';
m = 2;
b = 5;

y =  m*x + b;

y =  y + randn(size(x));
A = [x ones(size(x))];
mb_estimate = A\y