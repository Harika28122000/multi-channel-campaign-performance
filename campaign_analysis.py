import pandas as pd
df=pd.read_csv("data/campaign_performance.csv")
df["CTR"]=df["clicks"]/df["impressions"]
df["CVR"]=df["conversions"]/df["clicks"]
df["CAC"]=df["spend"]/df["conversions"]
df["ROAS"]=df["revenue"]/df["spend"].replace(0,pd.NA)
summary=df.groupby("channel").agg(spend=("spend","sum"),revenue=("revenue","sum"),conversions=("conversions","sum"),clicks=("clicks","sum"),impressions=("impressions","sum")).reset_index()
summary["CTR"]=summary["clicks"]/summary["impressions"]
summary["CAC"]=summary["spend"]/summary["conversions"]
summary["ROAS"]=summary["revenue"]/summary["spend"].replace(0,pd.NA)
print(summary.sort_values("ROAS",ascending=False))
