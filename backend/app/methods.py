# import numpy as np
# import pandas as pd

# import os
# for dirname, _, filenames in os.walk('/content/traffic.csv'):
#     for filename in filenames:
#         os.path.join(dirname, filename)

# data = pd.read_csv("../content/traffic.csv")
# data["DateTime"]= pd.to_datetime(data["DateTime"])
# data = data.drop(["ID"], axis=1) #dropping IDs

# # Normalize Function
# def Normalize(df,col):
#     average = df[col].mean()
#     stdev = df[col].std()
#     df_normalized = (df[col] - average) / stdev
#     df_normalized = df_normalized.to_frame()
#     return df_normalized, average, stdev

# # Differencing Function
# def Difference(df,col, interval):
#     diff = []
#     for i in range(interval, len(df)):
#         value = df[col][i] - df[col][i - interval]
#         diff.append(value)
#     return diff

