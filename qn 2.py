#Question 2(a)
#Using a function create a program that calculates the volume of a cylinder
import math
radius = int(input('Enter the radius of the cylinder:'))
height = int(input('Enter the height of the cylinder:'))
pie = math.pi
volume = pie *radius**2 *height
print(f'The volume of a cylinder of radius {radius} and height{height} is {volume:.2f}')

# def volume_of_a_cylinder ():
#     radius = int(input('Enter the radius of the cylinder:'))
#     height = int(input('Enter the height of the cylinder:'))
