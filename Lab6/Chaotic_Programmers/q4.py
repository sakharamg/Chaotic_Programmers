import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import seaborn as sns
import sys


def get_data_org(input_path, allowed_org_types):
	"""
	Input: 
	inp_input_pathfile: String 
	[It is the address of the input csv file.]
	    
	allowed_org_types: List 
	[It contains the list of org types allowed]. 
	
	Aim:
	Returns a dataframe only consisting values from allowed org types
	
	Output:
	filtered_df = pandas.dataframe
	[A dataframe only consisting values from allowed org types]

	"""
	dataframe = pd.read_csv(input_path)
	filtered_df = dataframe.loc[(dataframe['Organization type'].isin(allowed_org_types))]
	return filtered_df


def get_data_methods(input_path, allowed_methods):
	"""
	Input: 
	    inp_input_pathfile: String 
	    [It is the address of the input csv file.]
	    
	    allowed_org_types: List 
	    [It contains the list of org types allowed]. 
	        
	Aim:
	Returns a dataframe only consisting values from allowed methods
	
	Output:
	filtered_df = pandas.dataframe
	[A dataframe only consisting values from allowed methods]

	"""
	dataframe = pd.read_csv(input_path)
	filtered_df = dataframe.loc[(dataframe['Method'].isin(allowed_methods))]
	return filtered_df


def format_organization_data(data_frame, org_type):
	"""
	Input: 
	data_frame: pandas.dataframe 
	[Dataframe containing only the allowed org_types and methods]
	
	org_type: String 
	[It receives the current org type to be processed]. 
	
	
	Aim:
	Returns a set of years and number of records for that year in particular org_type
	
	Output:
	updated_x_plots : pandas.dataframe
	[Contains list of years for that org_type]

	updated_y_plots : pandas.dataframe
	[Returns average number of records for that year for a particular org_type. nan value is inserted if no value is present]

	"""
	data_frame.Year = pd.Categorical(data_frame.Year)
	grouped_df = data_frame.groupby(['Organization type','Year'], as_index = False)['Records'].mean()
	grouped_filtered_df = grouped_df.loc[(grouped_df['Organization type'] == org_type)]
	updated_x_plots = grouped_filtered_df['Year']
	updated_y_plots = grouped_filtered_df['Records']
	return updated_x_plots, updated_y_plots


def plot_organization_data(filtered_df, allowed_org_types):
	"""
	Input: 
		filtered_df: pandas.dataframe 
		[Dataframe containing only the allowed org_types and methods]
	
		allowed_org_types: List 
		[It contains the list of org types allowed]. 
	
	
	Aim:
		Loop through all allowed org_types, and for each org_type plot a line showing the mean no. of data breach records per year for that type.
	
	Output:
		organization.png, is the image of the plot generated and it is stored in PWD

	"""
	mpl.style.use('default')
	fig, ax = plt.subplots(figsize = (12, 6))
	for org_type in allowed_org_types:
		xplot, yplot = format_organization_data(filtered_df, org_type)
		ax.plot(xplot, yplot, label = org_type)
		ax.set_yscale('log')
	ax.legend(title = "Organization type", loc = 'lower right',fontsize="8")
	plt.title("Type of organizations affected by Data breaches per year")
	plt.xlabel("Year")
	plt.ylabel("Records")
	fig.savefig('organization.png')
	plt.clf()

def plot_methods_data(filtered_df):
	"""
	Input: 
		filtered_df: pandas.dataframe 
		[Dataframe containing only the allowed org_types and methods]
	    
	Aim:
		Plot a boxplot for each method of data breach, showing the min and max records of data breach for each year.
    
	Output:
		method.png, is the image of the plot generated and it is stored in PWD.    	

	"""
	sns.boxplot(x='Year', y='Records', hue='Method',data=filtered_df)
	plt.yscale('log')
	plt.legend(loc='upper left', title = "Method",fontsize="8")
	plt.title("Type of Methods used for Data breaching per year")
	plt.savefig('method.png')
	plt.clf()



input_path = sys.argv[2]
allowed_org_types = ['academic', 'financial', 'gaming', 'government', 'healthcare', 'military', 'retail', 'tech', 'telecoms', 'web']
allowed_methods = ['hacked', 'poor security', 'lost', 'accidentally published', 'inside job']
filtered_df_org = get_data_org(input_path, allowed_org_types)
filtered_df_methods = get_data_methods(input_path,  allowed_methods)
plot_organization_data( filtered_df_org, allowed_org_types)
plot_methods_data(filtered_df_methods)
