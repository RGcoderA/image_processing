import matplotlib.pyplot
import numpy

myImage = matplotlib.pyplot.imread('flower.png')

height=myImage.shape[0]
width=myImage.shape[1]


for x in range(0, height-1):
    for y in range(0,width-1):

           # INSERT YOUR CODE HERE

imgplot = matplotlib.pyplot.imshow(myImage)
matplotlib.pyplot.show()