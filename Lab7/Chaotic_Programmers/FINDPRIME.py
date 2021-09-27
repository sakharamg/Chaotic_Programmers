def find_prime(n,m):
    ''' find_prime(n,m) should return the
        the count of prime number between n and m
        (inclusive of n and m)

        return integer
    '''
    import math
    pcount=0
    for B in range (n,m+1):
    	if B<=1:
    		continue
    	flag=1
    	for A in range(2,math.floor(math.sqrt(B))+1):
    		if B%A==0:
    			flag=0
    			break
    	if(flag==1):
    		pcount+=1
    return pcount
