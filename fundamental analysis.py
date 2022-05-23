import numpy as np
import bs4
import requests
import pandas as pd
import csv
import seaborn as sns
import matplotlib.image as mpimg
from PIL import Image
import cv2
from skimage.io import imread
import matplotlib.pyplot as plt
from IPython.display import display, Image

----------------------------------------------------------------------------------------------------------------------------
set50_file = "/content/set50.txt"
stocks = []
with open(set50_file) as csv_file:
   csv_reader = csv.reader(csv_file, delimiter=',')
   for row in csv_reader:     
     stock = row[0]
     stocks.append(stock)
     #print(f"Working with {stock}")
		 
----------------------------------------------------------------------------------------------------------------------------
len(stocks)
stocks
----------------------------------------------------------------------------------------------------------------------------
HL_all = []
for stock in stocks:
  data_stock = requests.get('https://www.set.or.th/set/companyhighlight.do?symbol='+ stock + '&ssoPageId=5&language=en&country=US')

  soup = bs4.BeautifulSoup(data_stock.text)
  path = soup.find('div',{'class':'table-responsive'})
  rows = path.find_all('tr')
  ls = [] # list to store text of all elements in all the rows.
  
  for i, row in enumerate(rows):
      # Find all elements in this row.
      # Each element is enclosed by either <th> or <td> tag.
      if i==0 or i==13:
          elements = row.find_all('th')
      else:
          elements = row.find_all('td')
      
      # list to store text of all the elements in this row:
      ls_elements_in_row = []
      
      for element in elements:
          text = element.text
          ls_elements_in_row += [text]
      ls += [ls_elements_in_row]
  
  df = pd.DataFrame(ls[1::])
  df.columns = ls[0]
  HL_all.append(df)
	
	
-----------------------------------------------------------------------------------------------------------------------------------------
	
print("Enter your name's stock:")
name_stock = input()
-----------------------------------------------------------------------------------------------------------------------------------------
index = stocks.index(name_stock)
index
-------------------------------------------------------------------------------------------------------------------------------------------
HL_all[index]
--------------------------------------------------------------------------------------------------------------------------------------
print("What do you want to look:")
name_value = input()
--------------------------------------------------------------------------------------------------------------------------------------
name_value
----------------------------------------------------------------------------------------------------------------------------------------
Date = []
VAR = []
for i in range(len(HL_all[0].loc[HL_all[0]['Period  as of'] == name_value].values[0])):
  if i == 0:
    title_x = HL_all[0].loc[HL_all[0]['Period  as of'] == 'Statistics as of'].values[0][i]
    title_y = HL_all[0].loc[HL_all[0]['Period  as of'] == name_value].values[0][i]
  else:
    y = HL_all[0].loc[HL_all[0]['Period  as of'] == 'Statistics as of'].values[0][i].replace("\xa0","")
    x = float(HL_all[0].loc[HL_all[0]['Period  as of'] ==name_value].values[0][i].replace("\xa0","0"))
    Date.append(y)
    VAR.append(x)
-------------------------------------------------------------------------------------------------------------------------------------
x = np.arange(len(Date));
y = np.asarray(VAR)
my_xticks = np.asarray(Date)
plt.figure(figsize=[15, 10])
plt.xticks(x, my_xticks, rotation=0, fontsize='large')
plt.plot(x, y)
plt.xlabel(title_x)  
plt.ylabel(title_y) 
plt.show()
------------------------------------------------------------------------------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(15, 10))
ax = sns.barplot(x=Date, y=VAR)
plt.xlabel(title_x)  
plt.ylabel(title_y) 
plt.show()
-------------------------------------------------------------------------------------------------------------------------------------------------
print("How many years do you want to hold:")
ans = input()
year_hold = int(ans)

DCF_allstock = 0
DCFPP_ratio = 0

if len(HL_all[index].columns)-2  >=  2:
  Num_year = len(HL_all[index].columns)-2
  Present_price = float(HL_all[index].loc[HL_all[index]['Period  as of'] == 'Last Price(Baht)'].values[0][Num_year+1].replace(",", ""))
  date_Present_price = HL_all[index].loc[HL_all[index]['Period  as of'] == 'Statistics as of'].values[0][Num_year+1]

  EPS_temp = []
  Growth_rate_temp = []
  for year in range(Num_year):
    EPS_temp.append(float(HL_all[index].loc[HL_all[index]['Period  as of'] == 'EPS (Baht)'].values[0][year+1].replace(",", "")))
  for year in range(Num_year - 1):
    Growth_rate_temp.append((EPS_temp[year+1]-EPS_temp[year])*100/EPS_temp[year])
  Growth_rate = np.mean(Growth_rate_temp)
      
  temp = 0
  for t in range(year_hold+1):
    temp = temp + (((1+(Growth_rate/100))/(1+0.05))**t)
  DCF_Price = temp*EPS_temp[-1]
  DCF_allstock = DCF_Price
  DCFPP_ratio = DCF_Price/Present_price
else:
  DCF_allstock = 0
  DCFPP_ratio = 0

print(f"Discount cash flow : {DCF_allstock}")
print(f"Discount cash flow per stock price : {DCFPP_ratio}")

if DCFPP_ratio>=1 :
  print("Buy!!!")
  display(Image(filename='/content/BUY.jpg', width=500, height=300))

else:
  print("NO!!!")
  display(Image(filename='/content/NO.jpg', width=500, height=300))
	
