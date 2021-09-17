import numpy as np

# ---- Task (a) -------
# Do as directed in function:
# 'my_list': a list of 25 integers
def avada_kedavra(my_list):
	# Create an array 'a0' from this list 'my_list'
    a0 = np.array(my_list)
	# print a0
    print("a0 at beginning:\n{}".format(a0))
	# reshape a0 to create a 5X5 matrix a1
    a1 = np.reshape(a0,(5,5))
	# print a1
    print("a1 at the beginning:\n{}".format(a1))
	# now, change the central element of a1 to 0
    a1[2,2] = 0
	# print a1
    print("a1 after change:\n{}".format(a1))

	# print a0
    print("a0 after changing a1:\n{}".format(a0))
    print("reshaping doesn't create a copy of array. It just returns another view. So, changing one changed the other")

	# make a copy of a1 and flatten it (call it a1cpy)
    a1cpy = np.array(a1,copy=True)
    a1cpy = a1cpy.flatten()
	# multiply each element of a1cpy by 0.7:
    a1cpy = a1cpy*0.7
	# print a1cpy:
    print("a1cpy\n{}".format(a1cpy))

	# print a1:
    print("a1 after changing its copy:\n{}".format(a1))


# ---- Task (b) -------
# Do as directed in function:
# 'my_integer': an even integer
def incendio(my_integer):
	# create an array 'arng0' of shape (3,2) containing consecutive even numbers starting from 'my_integer', arranged along rows
    
    arng0 = np.arange(my_integer,my_integer+13)
    arng0 = arng0[arng0%2==0]
    arng0 = arng0.reshape(3,2)
	# print arng0
    print("arng0\n{}".format(arng0))

	# create another array 'arng1' of shape ((4,3)) containing consecutive numbers starting from 'my_integer' arranged along columns:
    arng1 = np.arange(my_integer,my_integer+12)
    arng1 = np.reshape(arng1,(4,3),order='F')
	# print arng1
    print("arng1\n{}".format(arng1))

	# multiply transpose of arng0 with transpose of arng1 to get mult0:
    m0 = arng0.transpose()
    m1 = arng1.transpose()
    mult0 = m0.dot(m1) 
	# print mult0:
    print("mult0\n{}".format(mult0))

	# take min of mult0 along its rows and store it in v0:
    v0 = mult0.min(axis=1)
	# print v0's shape:
    print("shape of v0: \n{}".format(v0.shape))

	# reshape v0 to make it a column vector:
    v0 = v0.reshape(-1,1)
	# subtract v0 from each column of mult0 and store it in base0:
    base0 = mult0-v0
	# print base0
    print("base0\n{}".format(base0))

	# square all the elements present in base0
    base0 = base0*base0
	# store the sum of all elements of base0 in ans
    ans = base0.sum()
	# print ans
    print("ans : {}".format(ans))

# ---- Task (c) -------
# 'X': Three dimensional matrix with shape => {B,S,F}
# 'W': Two dimensional matrix with shape => {N,F}
# Your task is to perform matrix multiplication such that you get the result in desired shape
# You are not allowed to use any loop or transform function. 0 marks for not following the instructions 
# {B,S,F} [mat_mul] {N,F} get the result of shape {B,N,S}
# Return the numpy matrix after performing batch matrix multiplication (i.e) 'X' @ 'W'.T and transforming to shape {B,N,S} 
def reducio(X, W):
	pass

def reducio(X, W):
    out = (X @ W.T)
    return out.swapaxes(1,2)



# ---- Task (d) -------
# 'n': integer
# 'm': integer that divides n
# return type: int numpy Ndarray; dim: nxn
def alohomora(n, m):
    pass
    mones = np.ones([m,m],dtype = int)
    a = np.zeros([n,n],dtype=int)
    outerflag = True
    for i in range(0,n,m):
    	innerflag = outerflag
    	for j in range(0,n,m):
    		if innerflag==True:
    			a[i:i+m, j:j+m] = mones
    			innerflag= False
    			continue
    		else:
    			innerflag=True
    	outerflag = False
    
    return a

# ---- Task (e) -------
# 'P': string, eg. '2 2; 3 3' 
#after transformation into matrix gives
#P` = [[2,2]
#	  [3,3]]
# 'Q': string, eg. '1 1; 4 4'
# 'R': string, eg. '5 5; 6 6'
# 'S': string, eg. '7 7; 8 8'
# P,Q,R,S all will be of same shape
#  Task is to interpret the string to matrix and return the numpy matrix in the form [[P`,Q`],[R`,S`]] as given in the problem statement
# returns [[2 2 1 1],
#			[3 3 4 4],
#			[5 5 7 7],
#			[6 6 8 8]]
def glisseo(P,Q,R,S):
	a = np.matrix(P)
	b = np.matrix(Q)
	c = np.matrix(R)
	d = np.matrix(S)
	out1 = np.concatenate((a,b),axis = 1)
	out2 = np.concatenate((c,d),axis = 1)
	out = np.concatenate((out1,out2))
	# print(out)
	return out

# ---- Task (f) -------
# 'arr': float Ndarray; dim: Nx3, 
# 'theta': float; 0≤theta<360 (in degrees)
# 'axis': str; axis ∈ {'X','Y','Z'}
# return type: float Ndarray; dim: Nx3
def expelliarmus(arr, theta, axis):
	rad = np.radians(theta)
	arr=np.array(arr).astype(np.float)
	if axis == 'X':
		y2 = [np.round(e,2) for e in (arr[:,1]*np.cos(rad) - arr[:,2]*np.sin(rad)) ]
		
		arr[:,2] = [np.round(e,2) for e in (arr[:,1]*np.sin(rad) + arr[:,2]*np.cos(rad)) ]
		
		arr[:,1] = y2
	elif axis == 'Y':
		z2 = [np.round(e,2) for e in (arr[:,2]*np.cos(rad) - arr[:,0]*np.sin(rad)) ]
		
		arr[:,0] = [np.round(e,2) for e in (arr[:,2]*np.sin(rad) + arr[:,0]*np.cos(rad)) ]
		
		arr[:,2] = z2
	else:
		x2 = [np.round(e,2) for e in (arr[:,0]*np.cos(rad) - arr[:,1]*np.sin(rad)) ]
		
		arr[:,1] = [np.round(e,2) for e in (arr[:,0]*np.sin(rad) + arr[:,1]*np.cos(rad)) ]
		
		arr[:,0] = x2

	return arr
