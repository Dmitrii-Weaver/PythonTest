import pandas as pd
carsDf = pd.read_csv(
    "D:\\Python\\Articles\\pandas\\automobile-dataset\\Automobile_data.csv")
carsDf = carsDf.sort_values(by=['price', 'horsepower'], ascending=False)
carsDf.head(5)
