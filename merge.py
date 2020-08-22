import pandas as pd


def merge(csv1, csv2):

    corona = pd.read_csv(csv1)
    normal = pd.read_csv(csv2)

    print(corona.shape)
    print(normal.shape)

    data = corona.append(normal)

    print(data.shape)

    data.to_csv("COVID.csv")

merge("final_corona.csv", "final_normal.csv")
    

