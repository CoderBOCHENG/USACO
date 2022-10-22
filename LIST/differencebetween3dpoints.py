#method 1

pointA=[1,2,3]
pointB=[2,4,6]
pointC=[-3,4,5]
pointD=[3,4,5]

distance = ((pointA[0] -pointB[0])**2 + (pointA[1] -pointB[1])**2 + (pointA[2] -pointB[2])**2)**(1/2)
print(distance)



#method 2
import math
addition = ((pointC[0] -pointD[0])**2 + (pointC[1] -pointD[1])**2 + (pointC[2] -pointD[2])**2)
distance3 = math.sqrt(addition)
print(distance3)
