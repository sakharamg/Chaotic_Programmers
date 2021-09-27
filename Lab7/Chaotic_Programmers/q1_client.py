'''
write your code here.
import what ever neccesary from xmlrpc module and nothing else.
'''
from xmlrpc.client import ServerProxy
a=input("")
b=input("")
with ServerProxy("http://localhost:8080/") as proxy:
	print(proxy.find_prime(int(a),int(b)))
