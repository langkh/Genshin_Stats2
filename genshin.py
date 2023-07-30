import pandas as pd
import matplotlib.pyplot as plt
path = "https://raw.githubusercontent.com/langkh/data/main/Genshin_Stats2.csv"
df = pd.read_csv(path)
df.info()
df
df.plot(subplots = True, figsize =(15,15))
df1 = df.groupby(['Character','Lv']).mean()
pd.set_option('display.max_rows',10)
df1.sort_values(['Lv','Base ATK'],ascending=False)#Will use later
df1 = df.groupby(['Character','Lv']).mean()
pd.set_option('display.max_rows',574)
df1.sort_values(['Lv','Base DEF'],ascending=False).head(574)
df90 = df[df.Lv==90]
df90.hist()
dps_car = df[df['Main role']=='DPS']
DPS_chars = dps_car.pivot_table(values='Base ATK',index='Lv',columns='Element',aggfunc=sum)
DPS_chars.plot()#finds which element with highest base atk for dps roles (based on all the characters in that element)
cryo_char = df[df['Element']=='Cryo']
cryo_chars = cryo_char.pivot_table(values='Base ATK',index='Lv',columns='Character',aggfunc=sum)
cryo_chars.plot()#Looks within characters attack in cryo element
exemplar = df1.pivot_table(values='Base ATK',index='Lv',columns='Character',aggfunc=sum)
characters = exemplar[["Ayaka","Xiao","Eula","Shogun","Diluc","Barbara","Noelle","Sara","Sucrose","Hutao"]]#Info from top 5 and last 5 in first table
characters.plot()
elementtype = df.groupby('Element')
elementtype.hist()#looks at different stats in each element
avg_by_element = df.pivot_table(index = 'Lv',columns='Element',values='Base DEF')
avg_by_element #looks at DEF stat
avg_by_element['diff']=avg_by_element['Geo'] - avg_by_element['Pyro']
avg_by_element #looks at DEF stat between geo and pyro
avg_by_element['diff']=avg_by_element['Anemo'] - avg_by_element['Electro']
avg_by_element #looks at DEF stat between anemo and electro
