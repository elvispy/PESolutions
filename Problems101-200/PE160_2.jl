# PE 160
# Idea: 
# Calculate the product of all numbers of the form 2^k 5^l * p, where p is odd.
# 1) First the cases when l >= k. Here, we only multiply by p, with p = 1, 3, 7, 9... 10^12/(2^k*5^l)
#    There are L=floor((10^12/5^l*2^k -1)/2) odd numbers, and floor(L/5) of them are multiple of 5. Call this number Q = Q(l, k)
# 2) There are (l-k) * Q multiples of two that have to be deleted. 
# 3) Now we analyze the k > l cases. Here we have to delete the multiples of two to match the multiples of five that were 
let 
    EXP=12;

    N = 100000/2; N = ceil(Int64, N-N/5);
    dp = zeros(Int64, (N, )); dp[1] = 1;
    ii = 1; idx = 2;
    while 2*ii+1 < 100000
        
        if mod(2*ii+1, 5) == 0
            ii+=1;
            continue
        end
        dp[idx] = mod((2 * ii + 1) * dp[idx-1], 100000);
        idx+=1; ii+=1;
    end
    dp = dp[1:(idx-1)];


    function prod(M, dp=dp)
        # This function calculates the last five digits of the product of the first M odd numbers that are
        # coprime with 5.
        N = 40000 # After this, we have repeating patters (50000th odd number is 100001 ≡ 1 (mod 10^5))
        exponent = floor(Int64, M/N);
        remainder = mod(M, N);
        return mod(powermod(dp[end], exponent, 100000) * dp[remainder + (remainder == 0)], 100000);
    end
    function auto(k, l, EXP)
        N = 10^EXP/(2^k * 5^l);
        aux = floor(Int64, (N+1)/2); # Counting odd numbers
        aux = aux - floor(Int64, (N/5-1)/2)-1; # Taking out multiples of five
        return prod(aux), aux
    end

    function manual(k, l, EXP)
        # Calculates manually the contribution of the odd primes coprime to 5.
        # That is, the product mod 10^5 of the ones that are less than 10^EXP
        
        ii = 0;
        my_prod = 1;
        while 2^k * 5^l * (2*ii + 1) <= 10^EXP
            if mod(2*ii+1, 5) == 0
                ii+=1;
                continue;
            end
            my_prod = mod(my_prod * (2*ii+1), 100000);
            ii+=1;
        end
        println(ii)
        return my_prod
    end
    #println(manual(3, 1, 5))
    #println(auto(3, 1, 5))

    k = 0;
    l = 0;
    debt = 0; # Number of powers of five that have to be cancelled out
    product = 1; # Final product mod 10000
    while k <= EXP
        # Considering numbers of the form 2^k* 5^l 
        # Counting how many of them are there
        prodd, aux = auto(k, l, EXP)
        product = mod(product *  prodd, 100000);
        debt += (l-k) * aux;
        l+=1;
        if 2^k * 5^l > 10^EXP
            k+=1; l = k;
        end
    end

    # Now we pay the debt (i. e. k > l)
    k = 1; l = 0;
    while l <= EXP
        # Considering numbers of the form 2^k* 5^l 
        # Counting how many of them are there
        prodd, aux = auto(k, l, EXP)
        product = mod(product *  prodd, 100000);
        if (k-l)* aux >= debt
            # We are in position to pay full debt
            aux2 = powermod(2, (k-l)*aux-debt, 100000);
            product = mod(product *  aux2, 100000);
            debt = 0;
        elseif debt > 0
            debt -= (k-l)* aux # Still paying the debt
        end
        k+=1;
        if 2^k * 5^l > 10^EXP
            l+=1; k = l+1;
        end
    end
    println("El resultado es $product")

end # let end