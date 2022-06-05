import pandas as pd
import plotly.express as px
df=pd.read_csv('C:/Users/khada/Downloads/python/class 103/csv files/Copy+of+data+-+data.csv')
graph=px.scatter(df,x='date',y='cases',color='country')
graph.show()