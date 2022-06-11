from matplotlib import pyplot
import numpy

x = numpy.arange(-10,10,1)
y = x**2

pyplot.xlabel("x")
pyplot.ylabel("y")
pyplot.plot(x,y)

for num in x.tolist():
    pyplot.annotate(text='('+str(num)+','+str(num**2)+')',xy=(num,num**2),
                    arrowprops=dict(arrowstyle="->",connectionstyle="arc3,rad=0.5",color="k"))

pyplot.show()