import pandas as pd
df = pd.read_csv(
    "D:\\Python\\Articles\\pandas\\automobile-dataset\\Automobile_data.csv")
car_Manufacturers = df.groupby('company')
priceDf = car_Manufacturers['company', 'price'].max()
priceDf
