"""Create a list of any type. Assign one of its elements to another one (e.g. a[5] = a[3]). Print
both elements. Next, add a line changing the value of the second element, and print both
elements again. Does the first one also change? Why? What happens if the value of the first one
is changed?"""


a = [1,2,3,4]

b = [2,3,4,5]

b[3] = a[0]

print(a[0], b[3])

b[3] = 9

print(a[0], b[3])

print("The first one didn't change. If were changed, it would mean that a[0] and b[3] point to the same memory location inside the pc")