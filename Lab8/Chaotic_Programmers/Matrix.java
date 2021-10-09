import java.lang.Float;
class Matrix{
	float[][] twoD_arr;
	Matrix(int i)
	{
		twoD_arr = new float[i][i];
	}
	Matrix(int i, float f)
	{
		twoD_arr = new float[i][i];
		for(int a=0;a<i;a++)
		{
			for(int b=0;b<i;b++)
			{
				twoD_arr[a][b]=f;
			}
		}
	}
	Matrix(int i, int j)
	{
		twoD_arr = new float[i][j];
	}
	Matrix(int i, int j, float f)
	{
		twoD_arr = new float[i][j];
		for(int a=0;a<i;a++)
		{
			for(int b=0;b<j;b++)
			{
				twoD_arr[a][b]=f;
			}
		}
	}
	void neg_elem(int i, int j)
	{
		try
		{
			twoD_arr[i][j]*=-1;
		}
		catch(Exception e)
		{
			System.out.println("Index out of bound");
		}
	}
	int[] mat_dim()
	{
		int dim[]=new int[2];
		dim[0]=twoD_arr.length;
		dim[1]=twoD_arr[0].length;
		return dim;
	}
	float[][] mat_sub(Matrix m)
	{
		int dim_arr1[]=mat_dim();
		int dim_arr2[]=m.mat_dim();
		float diff[][];
		if(dim_arr1[0]==dim_arr2[0] && dim_arr1[1]==dim_arr2[1])
		{
			diff=new float[dim_arr1[0]][dim_arr1[1]];
			for(int a=0;a<dim_arr1[0];a++)
			{
				for(int b=0;b<dim_arr1[1];b++)
				{
					diff[a][b]=twoD_arr[a][b]-m.twoD_arr[a][b];
				}
			}
		}
		else
		{
			System.out.println("Matrices cannot be subtracted");
			diff=new float[1][1];
		}
		return diff;
	}
	
	float[][] mat_mul(Matrix m)
	{
		int dim_arr1[]=mat_dim();
		int dim_arr2[]=m.mat_dim();
		float mul[][];
		if(dim_arr1[0]==dim_arr2[0] && dim_arr1[1]==dim_arr2[1])
		{
			mul=new float[dim_arr1[0]][dim_arr1[1]];
			for(int a=0;a<dim_arr1[0];a++)
			{
				for(int b=0;b<dim_arr1[1];b++)
				{
					mul[a][b]=twoD_arr[a][b]*m.twoD_arr[a][b];
				}
			}
		}
		else
		{
			System.out.println("Matrices cannot be multiplied");
			mul=new float[1][1];
		}
		return mul;
	}
	void additive_inv(Matrix m)
	{
		int dim_arr1[]=mat_dim();
		int dim_arr2[]=m.mat_dim();
		int flag=0;
		if(dim_arr1[0]==dim_arr2[0] && dim_arr1[1]==dim_arr2[1])
		{
			for(int a=0;a<dim_arr1[0];a++)
			{
				for(int b=0;b<dim_arr1[1];b++)
				{
					if(Float.compare(twoD_arr[a][b],-1*m.twoD_arr[a][b])!=0)
					{
						flag=-1;
						break;
					}
				}
				if(flag==-1)
				{
					break;
				}
			}
			if(flag==-1)
			{
				System.out.println("NO");
			}
			else
			{
				System.out.println("YES");
			}
		}
		else
		{
			System.out.println("NO");
		}
	}
	void mat_print()
	{
		int dim_arr1[]=mat_dim();
		int a,b;
		for(a=0;a<dim_arr1[0];a++)
		{
			for(b=0;b<dim_arr1[1];b++)
			{
				System.out.print(twoD_arr[a][b]+" ");
			}
			System.out.println();
		}
	}
}  
