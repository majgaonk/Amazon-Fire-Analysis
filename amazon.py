import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt

df = pd.read_csv ("amazon.csv" , thousands = ".", encoding="ISO-8859-1", header=0)

#check if file loaded properly
#print (df.head())

#number of row and columns
#print (df.shape)

#check for any nul or NaN values 
#print (df.isnull().sum()) 
#print (df.isna().sum())

#map the month col to english month names
#print (df['month'].unique())
month_map ={'Janeiro':"Jan", 'Fevereiro':"Feb", 'Mar�o':"Mar", 'Abril':"April", 'Maio':"May", 'Junho':"June", 'Julho':"July", 'Agosto':"Aug",
 'Setembro':"Sept", 'Outubro':"Oct", 'Novembro':"Nov", 'Dezembro':"Dec"}
df ['month'] = df['month'].map (month_map)

print (df["number"].value_counts())

#print (df['month'].unique())

#for every state, total number of fires over the years
#Option 1
#state_sum = df.groupby (["state", "year"]).agg ({"number":sum}).unstack()

#adding a total column for every state
#state_sum['total_fires'] = state_sum["number"].sum (axis = 1) ; same as below 
#state_sum['total_fires'] = state_sum.sum (axis = 1)

#state_sum = state_sum.droplevel (0, axis=1) #the groupby resulted in a mutli index column with "number" as top level and year's second level

#Option 2 : the below achieves the same as Option 1
#state_sum = pd.pivot_table (df, index="state", columns="year", values="number", aggfunc="sum", margins=True, margins_name="total").sort_index()

#print (state_sum.head())


#Get the top 5 states with most fires and plot thier number of fires over the year
#top_5 = df.groupby ("state").agg ({"number":sum}).sort_values (by = "number", ascending = False).iloc [:5, :]

#names_list = top_5.index.tolist()

#df_subset = df[df['state'].isin(names_list) ].loc [:, ["state", "year", "number"]].reset_index(drop=True)

#df_subset = df.query ("state.isin(@names_list)")

#df_subset_pivot = pd.pivot_table (df_subset, index = "year", columns="state", values="number", aggfunc = "sum")
#df_subset_pivot.plot (kind="line", xticks = range (df_subset_pivot.index[0], df_subset_pivot.index[-1], 2))

#plot total fires for every state
#state_sum['total_fires'].plot (kind = "bar")
#plt.show()

#Fires per year 
#year_sum = df.groupby ("year").agg ({"number":sum})

#print (year_sum.head())
#state_sum = state_sum.droplevel (0, axis=1)

#year_sum.plot (kind="bar", legend = False, title = "Total Fires Per Year")

#Fires per month
#fires_per_month = df.groupby("month").agg ({"number" : "sum"})  #returns a dataframe

#fires_per_month = df.groupby("month")["number"].sum()  # returns a series 
#fires_per_month = df.groupby("month").number.sum() # returned a series

month_list = df['month'].unique().tolist()

#fires_per_month = fires_per_month.reindex (month_list)  #above groupby returns results sorted by month, so april would appear before jan, we dont want that

#plt_axes = fires_per_month.plot (kind = "bar", legend=False, title = "Amazon Forest fires Per Month (1998 - 2017)", xlabel = "Month", ylabel = "Number of Forest fires")

#plt.ticklabel_format (axis = "y", style = "plain")

#for i, num in enumerate(fires_per_month['number']):
#    print (i, num)
#    plt.text(
#        i,
#        num,
#        num,
#        ha='center')
#plt.show()

#MultiIndexing examples

multi_index_df = df.set_index (["state", "year", "month"]).sort_index()


#fires in Acre in 2000
fires_in_Acre_in_2000 = multi_index_df.loc [("Acre", 2000, slice(None)), "number"].sum()

#print ("Total fires in Acre in year 2000 : {0}".format (fires_in_Acre_in_2000))

#fires in Acre in the month of September and October

fires_in_Acre_in_Sept_Oct = multi_index_df.loc [("Acre", slice(None), ["Sept", "Oct"]), "number"].sum()


#print ("Total fires in Acre in the month of Sept and Oct : {0}".format (fires_in_Acre_in_Sept_Oct))

#how many fires have occured in the month of August
total_fires_in_august = multi_index_df.xs ("Aug", level = "month").number.sum()

total_fires_in_august = multi_index_df.loc [(slice(None), slice(None), "Aug"), "number"].sum() #another way to get total fires in august without using xs method

#print ("Total fires in the month of August : {0}".format (total_fires_in_august))

