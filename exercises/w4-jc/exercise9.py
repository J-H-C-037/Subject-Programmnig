"""Create a program asking to enter the coordinates of a point in a plane, i.e. two integer
values, x and y, not equal to zero. The program must print the quadrant where this point lies (1
st quadrant if
x>0 and y>0, 2
nd
if x<0 and y>0, etc.) (Note: you can use the flow diagram of practice 2). For example for (1,1)
it must print: 1st. If x or y are zero it must print "The values are not valid" and finish.

"""

x = int(input("Enter the coordinate x: "))
y = int(input("Enter the coordinate y: "))


if (x > 0):
    if (y > 0):
        print("1st Quadrant")
    else:
        print("4th Quadrant")
elif(x < 0):
    if(y > 0):
        print("2nd Quadrant")
    else:
        print("3rd Quadrant")
else:
    print("The values are not valid")