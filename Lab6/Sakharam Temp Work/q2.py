class TWODMAT:
    def nor_mat(arr):
        """
        Description:
        	Normalise the matrix "arr" along its columns. 
        	
        Arguments:
        	arr: MxN dimensional matrix (need not be numpy)
        
        Return:
        	Normalised numpy array
        """
        #arr- a matrix of a given dimension MxN
        import numpy as np
        return np.round((np.array(arr)-np.mean(np.array(arr),axis=0))/np.std(np.array(arr),axis=0),2)
        
    def sum_fil(arr,k):
        """
        Description:
        	Implement a sum-filter of 1-d integer array "arr"
        
        Arguments:
        	arr: array of shape (n)
        	k: kernel size
        
        Return:
        	an int array of shape (n+k-1) 
        """
        #arr-array of shape (n) 
        #k-kernal size
        import numpy as np
        return np.cumsum(np.pad(np.array(arr), (0, k-1), 'constant', constant_values=(0,0)),axis=0)-np.cumsum(np.pad(np.array(arr), (k, 0), 'constant', constant_values=(0,0)))[0:len(np.array(arr))+k-1]
        
    def top_pos(arr,k):
        """
        Description:
        	get the positions of top_k values of each row of the matrix "arr"
        	
        Arguments:
        	arr: a matrix of shape (m,n)
        	k: required number of top positions 
        
        Return:
        	an integer matrix of shape (m, k),
        """
        #arr-a matrix of shape (m,n). 
        #k-top k values
        import numpy as np
        return np.flip(np.argsort(np.array(arr)))[:,:k]
        
if __name__ == '__main__':
	pass
