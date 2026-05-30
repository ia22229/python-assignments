'''1.Find area of a circle 2.Find area of triangle 3.Find area of hexagon'''
raduis = float(input("Enter the raduis of circle : "))
areaC = 3.14*raduis**2
print('Area of circle : ',areaC)

base = float(input("Enter the base of triangle : "))
height = float(input("Enter the height of triangle : "))
areaT = 0.5*base*height
print('Area of triangle : ',areaT)

side = float(input("Enter the side of hexagon : "))
areaH = (1.5*3**0.5*side**2)
print('Area of hexagon : ',areaH)