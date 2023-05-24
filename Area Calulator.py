#  Name : Area & Perimeter Calculator Of Basic Shapes
#  IGN : Xenavex | Hatakechop3
#  Discord : 𝐗𝐞𝐧𝐚𝐯𝐞𝐱#6886
#  Twitter : @Xenavex
#  Website : Bit.ly/Hatakeall

print("Input Either of these")
print("circle|square|rectangle|triangle")

shape=(input("Enter the shape of which u want information of:"))

# Circle #
if shape == 'circle':
   cradius = float(input("Input the radius of circle:"))
   carea = (3.1415926535*cradius*cradius)
   print("Area Of Circle Is",carea)
   cperi = (2*3.1415926535*cradius)
   print("Circumference of circle is",cperi)
   
# Square #
elif shape == 'square':
   sside = float(input("Enter Side of Square:"))
   sarea = (sside*sside)
   print("Area of Square is",sarea)
   speri = (sside*4)
   print("Perimeter of square is",speri)
   
# Rectangle #
elif shape == 'rectangle':
    rsidel = float(input("Enter the Length of the rectangle:"))
    rsideb = float(input("Enter the Breadth of the rectangle:"))
    rarea = rsidel*rsideb
    print("Area of the rectangle is",rarea)
    rperi = (rsideb+rsidel)*2
    print("Perimeter of the rectangle is",rperi)
    
# Triangle #
elif shape == 'triangle':
    theight=float(input("Enter Height of triangle "))
    tbase=float(input("Enter Base of triangle "))
    tarea=(theight*tbase)/2
    print("Area of the triangle is",tarea)
    print("Sorry No implimentation of Perimeter")
else:
    print("Please use determiners of shape as given below")
    print("circle|square|rectangle|triangle")
    print("No use of capitals in determiners also as they are case sensitive")
print("Thank you")

# End Of Code