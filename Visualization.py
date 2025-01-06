'''Pie chart visualization'''
from matplotlib.pyplot import margins

# import matplotlib.pyplot as plt
# parties=['ADMK','DMK','TVK','VCK']
# seats  =[29,40,120,125]
# plt.pie(seats,labels=parties,autopct="%1.0f %%")
# plt.show()
'''more visualization in pie chart'''
# import matplotlib.pyplot as plt
# parties=['ADMK','DMK','TVK','VCK']
# seats  =[29,40,120,125]
# party_peak=[0,0,0,0.1]
# plt.pie(seats,labels=parties,autopct="%1.0f %%",shadow=True,explode=party_peak)
# plt.show()
'''How to display number instead of percentage in output'''
import matplotlib.pyplot as plt
# parties=['ADMK','DMK','TVK','VCK']
# seats  =[29,40,120,125]
# party_peak=[0,0,0,0.1]
# def absolute_data(val):
#     total=sum(seats)
#     return f'{int(val*total)/100}'
# plt.pie(seats,labels=parties,autopct=absolute_data,shadow=True,explode=party_peak)
# plt.show()
'''Density chart'''
# import matplotlib.pyplot as plt
# import seaborn as sns
# Virat_runs_scored=[29,4,5,10,100,101,33,45]
# plt.figure(figsize=(8,6))
# sns.kdeplot(Virat_runs_scored,fill=True,color='red')
# plt.show()
'''With few more attributes'''
# plt.title('Density plot',fontsize=16)
# plt.xlabel('Data value')
# plt.ylabel('Density')
# plt.show()
'''Machine learning visualization scatter plot'''
import matplotlib.pyplot as plt
x=[2,4,6,8,10]
y=[1,3,5,7,9]
# plt.figure(figsize=(6,6))
# plt.scatter(x,y)
# plt.show()
'''With more attributes'''
plt.scatter(x,y,color='purple',marker='^')
# plt.scatter(x,y,c=x,marker='^',cmap='magma')
# plt.scatter(x,y,c=x,cmap='rainbow')
plt.show()