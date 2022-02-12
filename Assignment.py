# import pandas as obj
# import numpy as np

# data = obj.read_csv("netflix.csv")
# print(data.head(n=10))
# print(data.tail)
# print(data.columns)
# print(data.loc[(data.rating == 'PG-13')])
# print(data.loc[(data.rating == "PG-13" ) & (data["release year"] == 2012)])
# print(data.loc[(data.rating == "PG-13" ),["title"]])
# print(data.iloc[[2,5],0:3])
# print(data.describe())

# print(int(data["user rating score"].mean()))
# print(data.replace(to_replace=np.nan, value =84.0,inplace=True))
# print(data.isnull().sum())


import pandas as obj
import numpy as np

data = obj.read_csv("Pokemon.csv")
# print(data["Type 1"].value_counts())
# print(data.sort_values("Defense"))
# print(data.sort_values(["HP","Defense"],ascending =[True,False]))
attack_mean = data["Attack"].mean()
def set_attack(val):
   if val < attack_mean:
       return "Attack Low"
   elif val == attack_mean:
       return "Attack neutral"
   else:
        return "Attack High"

data["Attack_high_low"]=data["Attack"].apply(set_attack)

HP_mean = data["HP"].mean()
def set_HP(val):
   if val < HP_mean:
       return "HP Low"
   elif val == HP_mean:
       return "HP neutral"
   else:
        return "HP High"

data["High_Low_HP"]=data["HP"].apply(set_HP)


Speed_mean = data["Speed"].mean()
def set_Speed(val):
   if val < Speed_mean:
       return "Speed Low"
   elif val == Speed_mean:
       return "Speed neutral"
   else:
        return "Speed High"

data["High_ Low_Speed"]=data["Speed"].apply(set_Speed)
print(data)