def plotgraph(inp_file,out_file):
    """
    inp_file: String 
    [It is the address of the input csv file. Ex: "./data/csv_file.csv". CSV file consists of three columns for X, Y and Z axis respectively.]
    out_file: String 
    [address of jpg output file. Ex: "./results/output.jpg"]. 
    
    Aim: The task is to plot a 3D plot for the given csv file. 
    fig_size : (12*12)
    theme: "coolwarm"
    color_bar->shrink=0.5
    you can use bbox_inches='tight' while saving the file.
    You are allowed to use matplotlib and other supporting libraries like numpy etc.
    """
    pass
	
## program starts from here
    import matplotlib.pyplot as plt
    import csv
    import numpy as np
    x = []
    y = []
    z = []
    with open(inp_file,'r') as csvfile:
        plots = csv.reader(csvfile, delimiter = ',') #read the csv file which has three columns x,y and z
        next(plots) #skip the first line which has the column names
        for row in plots: #for each row 
        	x.append(float(row[0])) #get the first column
        	y.append(float(row[1])) #get the second column
        	z.append(float(row[2])) #get the third column
    # convert x,y,z into numpy array
    x=np.array(x)
    y=np.array(y)
    z=np.array(z)

    fig=plt.figure() #create a figure
    ax=fig.add_subplot(111,projection='3d') # figure with 1x1x1 size grids and project in 3d
    # pass all 3 axis, color based on z axis
    # set the coloring will be based on coolwarm theme and have circles (marker='o') of size 12
    p=ax.scatter(x,y,z,c=z,s=12,cmap="coolwarm",marker='o') 
    # Set all three labels
    ax.set_xlabel("X-axis",weight='bold')
    ax.set_ylabel("Y-axis",weight='bold')
    ax.set_zlabel("Z-axis",weight='bold')
    # hide the grid as in the sample image
    ax.grid(False)
    # display a colorbar and shrink to 1/2
    # padded the color bar so that it doesn't overlap with label just as shown in the sample image
    fig.colorbar(p,shrink=0.5,pad=0.1) # If it was supposed to be overlapped with the z-axis label then remove pad option from colorbar()
    # Change the angle to match with the sample image
    ax.view_init(azim=-60,elev=23) #I changed the angle to make it look like the sample image, please comment this line if changing the angle is not required
    fig.savefig(out_file, bbox_inches='tight') #save the figure into out_file
    # Return the file name
    output="./"+out_file
    return output
import sys
if __name__=="__main__":
    inp_file = sys.argv[1]
    out_file = sys.argv[2]
    plotgraph(inp_file,out_file)


