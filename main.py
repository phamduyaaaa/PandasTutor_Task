import pandas as pd
df = pd.read_csv("cities_population.csv")
df["Population"] = df["Population"].str.replace(",","").astype(int)
df["Area KM2"] = df["Area KM2"].str.replace("-May","").astype(int)
#Task_1
df_1 = df[["City","Population"]]
print("----------1----------\n",df_1.sort_values("Population").head(10))
print(df_1.sort_values("Population").tail(10))
#Task_2
df_2 = df[["Country","City","Population"]]
city_counts = df.Country.value_counts()
print("----------2----------\n",city_counts.loc[city_counts>=3])
#Task_3
city_counts = city_counts.sort_values(ascending=False)
print("----------3----------\n",city_counts.head())
#Task_4
df_4P = df[["City","Population"]]
df_4S = df[["City","Area KM2"]]
df_4P = df_4P.sort_values(by="Population").tail(20)
df_4S = df_4S.sort_values(by="Area KM2").tail(20)
print(df_4S)
print(df_4P)
df_topSP = pd.merge(df_4P,df_4S,on = "City")
print("----------4----------\n",df_topSP)
#Task_5
df_5 = df[["Country","Population","Area KM2"]]
df_5 = df_5.groupby("Country").sum()
df["Density"] = df["Population"]/df["Area KM2"]
print("----------5----------\n",df)
#Task_6
df_6 = pd.merge(df_2,city_counts,on="Country").sort_values(by="count",ascending =False)
df_6 = df_6.loc[df_6["count"]>1]
df_6 = df_6.groupby("Country").head(1)
print(df_6)
