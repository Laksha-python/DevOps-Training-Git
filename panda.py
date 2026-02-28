import pandas as pd
df=pd.read_csv('sales.csv')
df["date"]=pd.to_datetime(df["date"])
print(df)
print()

for row in df.itertuples():
    df["sales"]=df["quantity"]*df["price"]
print(df)

group=df.groupby("category")
total_sales=group["sales"].sum()
print(total_sales)
df['month']=df['date'].dt.to_period('M')
monthly_sales=df.groupby(['month'])['sales'].sum()
print(monthly_sales)
sales_permonth_category=df.groupby(['month','category'])['quantity'].sum()
print(sales_permonth_category)