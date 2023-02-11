from dice.die import Die
import matplotlib.pyplot as plt

die=Die()
results=[]
for roll_num in range(1000):
    result=die.roll()
    results.append(result)
frequencies=[]
for value in range(1,die.num_sides+1):
    frequencie=results.count(value)
    frequencies.append(frequencie)
plt.plot(range(1,die.num_sides+1),frequencies,c=(102/255,204/255,255/255),linewidth=5)
plt.title("Result of rolling a D6 die 1000 times",fontsize=24)
plt.xlabel("Values",fontsize=14)
plt.ylabel("Times",fontsize=14)
plt.tick_params("both",labelsize=14)
plt.savefig("plot.png",bbox_inches="tight")
plt.show()
