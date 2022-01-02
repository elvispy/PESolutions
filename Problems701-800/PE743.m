% Try to solve PE 743
% This is equal to calculate 
% sum_{j = 0}^{k} ncr(k, j) * 2^(jn/k) * ncr(k-j, (k-j)/2) (j even only)
% for 
% n = 1e+16
% k = 1e+8
% p = 1e+9 +7
function res = PE743(k, n, p)
    %factorialNumInverse = zeros(k, 1, 'uint64');
    %factorial = zeros(k, 1, 'uint64'); % factorial(ii) = ii!
    %naturalnumInverse = zeros(k, 1, 'uint64');
    k = uint64(k);
    n = uint64(n);
    p = uint64(p);
    partialfacts = zeros(k, 1, 'uint64');

    partialfacts(k) = 1;
    for jj = (k-1):-1:1
        if mod(jj, 1e+7) == 0
            disp(jj)
        end
        partialfacts(jj) = mod(partialfacts(jj+1) * (jj+1), p);
    end
%     naturalnumInverse(1) = 1;
%     naturalnumInverse(2) = (p+1)/2;
%     for ii = 3:k
%         [~, x] = gcd(ii, p);
%         naturalnumInverse(ii) = mod(x, p);
%         %naturalnumInverse(ii) = mod(p - mod((naturalnumInverse(mod(p, ii))*p - 1)/ii, p), p);
%     end
    
%     factorialNumInverse(1) = 1;
%     factorialNumInverse(2) = (p+1)/2;
%     for ii = 3:(p-1)
%         factorialNumInverse(ii) = mod(naturalnumInverse(ii) * factorialNumInverse(ii-1), p);
%     end
%     
%     disp('Inverse Factorial, done!');
%     
%     KK = 1;
%     for ii = 1:k
%         KK = mod(KK * ii, p);
%     end
    C = uint64(n/k);
    MM =modExp(2, C, p);
    T2 = modExp(MM, mod(k, 2), p); % Term 2
    T3 = uint64(1); % Term 3
    for ii = 1:floor((k-1)/2)
        T3 = mod(ii * mod(T3 * ii, p), p);
    end
    [~, x] = gcd(int64(T3), int64(p));
    T3 = uint64(mod(x, int64(p)));
    
    aux = mod(partialfacts(1) * mod(T3 * T2, p), p);
    res  = aux;
    for jj = (mod(k, 2)+2):2:k
        if mod(jj, 1e+7) < 2
            disp(jj);
        end
        T2 = mod(MM * mod(T2 * MM, p), p);
        T3 = mod(T3 * mod(((k-jj + 2)/2)^2, p), p);
        aux = mod(partialfacts(jj) * mod(T2*T3, p), p);
        res = mod(res + aux, p);
    end
end

function y = modExp( b, e, p )
% Fast modular exponentiation e.g.: y = b^e mod n

if (p == 1)
y = 0;
return
end
p = uint64(p);
b = uint64(b);
e = uint64(e);
residuals = zeros(1, 65, 'uint64'); residuals(1) = b; 
ii = uint64(1);
y = uint64(1);
while 2^ii <= e
    b = mod(b*b, p);
    residuals(ii+1) = b;
    ii = ii + 1;
end
while e > 0
    while 2^ii > e
        ii = ii - 1;
    end 
    y = mod(y * residuals(ii+1), p);
    e = e - 2^ii;
end
    
    
% y = uint64(1);
% b = mod(b,n);
% while ( e > 0 )
%     
% if ( mod(e,2) == 1)
% y = mod((y * b),n);
% end
% e = bitshift(e,-1);
% b = mod( (b * b),n ) ;
% end
end