"""
RECORD CHECK  -  my version
===========================

Name  : Aahil Mustafa Nias
Lane  :  AI 
Date  :04/11/2026

Run it:   python template.py

"""

import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("records.csv")

df["percent"]=(df["value"]/df["limit"])*100
df["status"]=df["percent"].apply(lambda p: "OVER LIMIT" if p >= 100 else "WARNING" if p >= 90 else "OK")
print(df[df["status"]!="OK"])
print(df.groupby('status')['percent'].mean().round(1))
df.to_csv("over_limit.csv", index=False)
df["status"].value_counts().plot(kind="bar")
plt.savefig("status_counts.png")
plt.title("status")
plt.show()




