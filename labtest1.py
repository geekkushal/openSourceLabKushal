import sys
sys.path.append(r'C:\Users\22104038\AppData\Roaming\Python\Python312\site-packages')

import matplotlib.pyplot as pl
import numpy as np

#i8 -> 64 bit integer

# Define the product cateogary
product_dtype = [('E', 'i8'),   # electronics
                 ('G', 'i8'),       #groceries
                 ('C', 'i8'),    #clothing
                 ('F', 'i8'), # furniture
                 ('S', 'i8')]     #stationery


#part 1 - store in numpy array and find sum of all cateogaries
#  Product List
products = np.array([
    (120,500,230,75,45),
    (130,520,210,80,40),
    (125,530,220,70,50),
    (140,540,200,90,60)
], dtype=product_dtype)

Esum = np.sum(products['E'])
Gsum = np.sum(products['G'])
Csum = np.sum(products['C'])
Fsum = np.sum(products['F'])
Ssum = np.sum(products['S'])

print(" Product list: ",products)
print()
print("Electronics sale sum = ",Esum)
print("Groceries sale sum = ",Gsum)
print("CLothing sale sum = ",Csum)
print("Furniture sale sum = ",Fsum)
print("Stationery sale sum = ",Ssum)
print()

#part 2- total sales per week and average sales per week

W1sum = sum(products[0])
W2sum = sum(products[1])
W3sum = sum(products[2])
W4sum = sum(products[3])

print(" Week 1 total sales = ",W1sum)
print(" Week 2 total sales = ",W2sum)
print(" Week 3 total sales = ",W3sum)
print(" Week 4 total sales = ",W4sum)

Eavg = np.mean(products['E'])
Gavg = np.mean(products['G'])
Cavg = np.mean(products['C'])
Favg = np.mean(products['F'])
Savg = np.mean(products['S'])

print(" Electronics average sale : ",Eavg)
print(" Electronics average sale : ",Gavg)
print(" Electronics average sale : ",Cavg)
print(" Electronics average sale : ",Favg)
print(" Electronics average sale : ",Savg)

#part 3 - plot

week = np.array([1,2,3,4])
week1 = np.array([120,130,125,140])

#pl.plot(week,week1,color='r')


week = np.array([1,2,3,4])
week2 = np.array([500,520,530,540])

#pl.plot(week,week2,color='g')


week = np.array([1,2,3,4])
week3 = np.array([230,210,220,200])

#pl.plot(week,week3,color='b')


week = np.array([1,2,3,4])
week4 = np.array([110,130,155,170])

#pl.plot(week,week4,color='m')

#pl.title("Week wise sales by products ")


#part 4 - hihest and mininmum sales and visualize total strength in bar chart

L = [[Esum,"Electroncis"],[Gsum,"Groceries"],[Fsum,"Furniture"],[Csum,"CLothing"],[Ssum,"Stationery"]]
L.sort()

print(L)
print(" Minimum sale => ",L[0])
print(" Maximum sale => ",L[4])

x = input("Enter to print bar chart ")

p1 = [120,130,140,125]
p2 = [500,520,530,540]
p3 = [230,210,220,200]
p4 = [75,80,85,90]
p5 = [45,50,55,60]

p = [1,2,3,4]
pl.bar(p,p1,color='r',width=0.3)
pl.bar(p,p2,color='g',width=0.3)
pl.bar(p,p3,color='y',width=0.3)
pl.bar(p,p4,color='m',width=0.3)
pl.bar(p,p5,color='b',width=0.3)

pl.xlabel("Products ")
pl.ylabel("Sales")

pl.show()




