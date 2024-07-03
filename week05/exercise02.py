"""Create a function to calculate the area of a rectangle.

Instructions:

Define a function that takes two parameters, length and width.
Inside the function, multiply the length and width to calculate the area.
Use the return statement to return the calculated area."""


def area_rectangle(length, width):
    return length * width


leng = int(input("The length of rectangle: "))
wid = int(input("The width of rectangle: "))
print(f"The area of Rectangle is {area_rectangle(length=leng,width = wid)}")
