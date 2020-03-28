# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
Temp = np.linspace(298.15,1500,100)
Methane = list(map(lambda x: 1.702 + (9.081*10**-3)*x - (2.164*10**-6)*x**2,Temp))
Ethylene = list(map(lambda x: 1.424 + (14.394*10**-3)*x - (4.392*10**-6)*x**2,Temp))
Acetylene = list(map(lambda x: 6.132 + (1.952*10**-3)*x - (1.299*10**5)*x**-2,Temp))
Hexane = list(map(lambda x: 3.025 + (53.722*10**-3)*x - (16.791*10**-6)*x**2,Temp))
Water = list(map(lambda x: 3.470 + (1.450*10**-3)*x - (0.121*10**5)*x**-2,Temp))
for i in range(len(Temp)):
    Temp[i] = round(Temp[i],2)
    Methane[i] = round(Methane[i],3)
    Ethylene[i] = round(Ethylene[i],3)
    Acetylene[i] = round(Acetylene[i],3)
    Hexane[i] = round(Hexane[i],3)
    Water[i] = round(Water[i],3)

data = pd.DataFrame(data=Temp,index =range(1,101), columns=['Temp'])
data['Methane'], data['Ethylene'], data['Acetylene'], data['Hexane'], data['Water'] =Methane, Ethylene,Acetylene,Hexane,Water
print(data)
fig = plt.figure()
axes = fig.add_axes([1,1,1,1])
CH4 = axes.plot(data['Temp'],data['Methane'], 'r')
C2H4 = axes.plot(data['Temp'],data['Ethylene'], 'b')
C2H2 = axes.plot(data['Temp'],data['Acetylene'], 'g')
C6H14 = axes.plot(data['Temp'],data['Hexane'],'y')
H2O = axes.plot(data['Temp'],data['Water'])
axes.set_ylabel('Cp/R')
axes.set_xlabel('Temperature (K)')
axes.set_title('Temperature Dependence of Specific Heat Capacity')
plt.show()