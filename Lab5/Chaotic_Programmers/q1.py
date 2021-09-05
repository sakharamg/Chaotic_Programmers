
def nList(L,N):                           # taking List and number of splits from main
    # write ypur code here.
 import itertools
 #storing length of list in end
 list1=[]
 end=len(L)
 temp=[]
 for j in range(N):
    #in islice, j is the index from where to start and N is the no. of jumps/steps to be taken
    #islice will run till end of list and store jth value in new1 taking jumps of N
    temp=list(itertools.islice(L,j,end,N))
    list1.append(temp)

 return(list1)




def fib():
   a=0
   b=1
   while (1):
     yield a
     #yield is basically works like return here. it will give the value of a when next will be printed in main
     c=a+b
     a=b
     b=c
   


""" if __name__ == "__main__":
	
     L = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
     N = 3
     nList(L,N) """
