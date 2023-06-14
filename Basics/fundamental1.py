print("Twinkle, twinkle, little star,\n\t\tHow I wonder what you are!\n\t\t\tUP above the world so high,\n\t\t\tLike a diamond in the sky.\nTwinkle,twinkle, little star,\n\t\tHow I wonder what you are!")
import sys
print("Python version")
print(sys.version)
print("Version info.")
print(sys.version_info)
import datetime
now=datetime.datetime.now()
print("Current date and time : ")
print(now.strftime("%Y-%m-%d %H:%M%S"))
from math import pi
r=float(input("Input the radius of the circle:"))
print("The area of the circle with radius "+str(r)+" is: "+str(pi*r**r))
