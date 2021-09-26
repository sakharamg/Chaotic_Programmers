'''
write your code here.
import whatever neccessary from xmlrpc module, file containning function
which should be invoked when recieving request.
'''
from xmlrpc.server import SimpleXMLRPCServer
from FINDPRIME import find_prime

server = SimpleXMLRPCServer(("localhost", 8080))
server.register_function(find_prime, "find_prime")
server.serve_forever()
