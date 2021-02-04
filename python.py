import plotly.express as px
import pandas as pd
table=pd.read_csv("Copy+of+data+-+data (1).csv")
print(table)
graph=px.scatter(table,x="date",size="cases",color="Country",size_max=10)
graph.show()