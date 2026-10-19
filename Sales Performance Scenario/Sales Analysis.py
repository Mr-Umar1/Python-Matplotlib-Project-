import numpy as np
import matplotlib.pyplot as plt
month=["Jan","Feb","Mar","Apr","May","Jun","Jul","Agu","Sep","Oct","Nov","Dec"]
sales=[125000,138000,142000,155000,149000,172000,185000,179000,195000,210000,225000,240000]
plt.plot(month,sales,marker='o',linestyle='--',color='r',label='Sales Performance')
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Sales Analysis")
plt.legend()
plt.show()

product=["Laptop","Mobile","Tablet","Monitor","Keyboard","Mouse"]
sales=[450000,680000,320000,275000,125000,85000]
plt.bar(product,sales,color='g')
plt.title("Product Sales Performance")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.show()

advertising=[10,15,20,25,30,35,40,45,50,55]
revenue=[120,145,170,190,225,250,280,300,340,365]
a=[20,40,60,80,90,100,120,140,160,180]
plt.scatter(advertising,revenue,s=a,color='y',marker='o')
plt.title("Spend Revenue Scatter Plot")
plt.xlabel("Advertising(Thousand)")
plt.ylabel("Revenue(Thousand)")
plt.show()

salary=[22000,25000,27000,28000,30000,32000,35000,36000,38000,40000,42000,45000,47000,50000,52000,55000,58000,60000,65000,70000]
plt.hist(salary,bins=5,color='b',edgecolor='black')
plt.title("Salary Distribution Of Employee")
plt.xlabel("Salary")
plt.ylabel("Employee")
plt.grid(True)
plt.show()

month=["Jan","Feb","Mar","Apr","May","Jun"]
orders=[1200,1450,1380,1750,2100,2350]
revenue=[240000,290000,275000,350000,420000,470000]
marketing_spend=[40000,45000,43000,55000,65000,70000]
plt.plot(month,revenue,marker='o',linestyle='-',color='orange',label='Monthly Revenue Trend')
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.legend()
plt.show()

plt.bar(month,orders,color='skyblue')
plt.title("Monthly Order Analysis")
plt.xlabel("Month")
plt.ylabel("Orders")
plt.show()

a=[40,60,80,100,120,140]
plt.scatter(marketing_spend,revenue,s=a,color='red',marker='o')
plt.title("Marketing Spend & Revenue")
plt.xlabel("Marketing Spend")
plt.ylabel("Revenue")
plt.show()

x=[revenue]
y=[orders]
z=[month]
plt.plot(month,revenue,marker='o',linestyle='--',label='Over Revenue Orders')
plt.plot(month,orders,marker='s',linestyle='-',label='Over Six Months')
plt.title("Over Six Month Analysis")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.legend()
plt.show()





