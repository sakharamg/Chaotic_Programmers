def find_prime(n,m):
    ''' find_prime(n,m) should return the
        the count of prime number between n and m
        (inclusive of n and m)

        return integer
    '''
    import math
    prime_count=0
    for dividend in range (n,m+1):
    	if dividend<=1:
    		continue
    	is_prime=1
    	for divisor in range(2,math.floor(math.sqrt(dividend))+1):
    		if dividend%divisor==0:
    			is_prime=0
    			break;
    	if(is_prime==1):
    		prime_count+=1
    return prime_count
    

