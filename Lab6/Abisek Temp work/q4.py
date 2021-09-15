import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import seaborn as sns
import sys


def get_data(input_path, allowed_org_types, allowed_methods):
	dataframe = pd.read_csv(input_path)
	filtered_df = dataframe.loc[(dataframe['Organization type'].isin(allowed_org_types)) & (dataframe['Method'].isin(allowed_methods))]
	return filtered_df


def format_organization_data(data_frame, org_type):
	data_frame.Year = pd.Categorical(data_frame.Year)
	grouped_df = data_frame.groupby(['Organization type','Year'], as_index = False)['Records'].mean()
	grouped_filtered_df = grouped_df.loc[(grouped_df['Organization type'] == org_type)]
	updated_x_plots = grouped_filtered_df['Year']
	updated_y_plots = grouped_filtered_df['Records']
	return updated_x_plots, updated_y_plots


def plot_organization_data(filtered_df, allowed_org_types):
	mpl.style.use('default')
	fig, ax = plt.subplots(figsize = (12, 6))
	for org_type in allowed_org_types:
		xplot, yplot = format_organization_data(filtered_df, org_type)
		ax.plot(xplot, yplot, label = org_type)
		ax.set_yscale('log')
	ax.legend(title = "Organization type", loc = 'lower right')
	plt.title("Type of organizations affected by Data breaches per year")
	plt.xlabel("Year")
	plt.ylabel("Records")
	fig.savefig('organization.png')
	plt.clf()

def plot_methods_data(filtered_df):
	sns.boxplot(x='Year', y='Records', hue='Method',data=filtered_df)
	plt.yscale('log')
	plt.legend(loc='upper left', title = "Method")
	plt.title("Type of Methods used for Data breaching per year")
	plt.savefig('method.png')
	plt.clf()



input_path = sys.argv[2]
print('input: ', input_path)
allowed_org_types = ['academic', 'financial', 'gaming', 'government', 'healthcare', 'military', 'retail', 'tech', 'telecoms', 'web']
allowed_methods = ['hacked', 'poor security', 'lost', 'accidentally published', 'inside job']

filtered_df = get_data(input_path, allowed_org_types, allowed_methods)
plot_organization_data( filtered_df, allowed_org_types)
plot_methods_data(filtered_df)