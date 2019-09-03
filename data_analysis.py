import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("avocado.csv")

df['Date'] = pd.to_datetime(df["Date"])

albany_df = df.copy()[ df['region'] == "Albany" ]


albany_df = albany_df.set_index('Date')
# albany_df.set_index('date', inplace=True)



albany_df.sort_index(inplace=True)

albany_df["AveragePrice"].rolling(25).mean().plot()

albany_df['price25ma'] = albany_df["AveragePrice"].rolling(25).mean()

print(df['region'].unique())


graph_df = pd.DataFrame()

for region in df['region'].unique():
    print(region)
    region_df = df.copy()[df['region'] == region]
    region_df.set_index('Date', inplace=True)
    region_df.sort_index(inplace=True)
    region_df['price25ma'] = region_df['AveragePrice'].rolling(25).mean()

    if graph_df.empty:
        graph_df = region_df["price25ma"]



plt.show()
