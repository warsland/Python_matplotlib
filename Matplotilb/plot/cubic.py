import matplotlib.pyplot as plt

x_values=[1,2,3,4,5]
y_values=[x**3 for x in x_values]

plt.scatter(x_values,y_values,c=(102/255,204/255,255/255),s=10)

plt.title("Cubic Values",fontsize=40)
plt.xlabel("Values",fontsize=20)
plt.ylabel("Cubic of Values",fontsize=20)

plt.tick_params(axis='both',labelsize=10)
plt.savefig('Five Cubic of Values.png')
plt.show()

x_values=list(range(1,5001))
y_values=[x**3 for x in x_values]
plt.title("Cubic Values",fontsize=40)
plt.xlabel("Values",fontsize=20)
plt.ylabel("Cubic of Values",fontsize=20)

plt.tick_params(axis='both',labelsize=10)
plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,s=10)
plt.savefig('Cubic of Values.png',bbox_inches='tight')
plt.show()
