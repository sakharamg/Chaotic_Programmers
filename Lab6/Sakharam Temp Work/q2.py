class TWODMAT:
    def nor_mat(arr):
        #arr- a matrix of a given dimension MxN
        import numpy as np
        return np.round((np.array(arr)-np.mean(np.array(arr),axis=0))/np.std(np.array(arr),axis=0),2)
        
    def sum_fil(arr,k):
        #arr-array of shape (n) 
        #k-kernal size
        import numpy as np
        return np.cumsum(np.pad(arr, (0, k-1), 'constant', constant_values=(0,0)),axis=0)-np.cumsum(np.pad(arr, (k, 0), 'constant', constant_values=(0,0)))[0:len(arr)+k-1]
        
    def top_pos(arr,k):
        #arr-a matrix of shape (m,n). 
        #k-top k values
	return np.flip(np.argsort(arr))[:,:k]
if __name__ == '__main__':
