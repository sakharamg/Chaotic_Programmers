import functools as ft


''' implement a function for Sieve of Eratosthenes method for computing primes up to a specified number'''
def prime(n):
    ## write your code here
    """
    this functions takes a integer n as a argumnets
    returns a list of integers.
    """
    li = list(range(2, n+1))
    remover = lambda element, li: list(filter(lambda x: (( x < element**2) or (x % element != 0)), li))
    cleansed_list = list(map(lambda x: remover(x, li), li))
    intersection = lambda x, y : list(filter(lambda itr: itr in x, y))
    prime_list = ft.reduce((lambda x, y: intersection(x, y)), cleansed_list)
    return prime_list

if __name__ == "__main__":
    """Main function
    """	
    n=10
    L=prime(n)
    print(L)
