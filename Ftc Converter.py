#  Name : Farenhite to Celcius Converter
#  IGN : Xenavex | Hatakechop3
#  Discord : 𝐗𝐞𝐧𝐚𝐯𝐞𝐱#6886
#  Twitter : @Xenavex
#  Website : Bit.ly/Hatakeall

print("Farenheit to Celcius & Viceverta Converter")
deter=(input("Enter ftc or ctf: "))
if deter == "ftc":
    f1=float(input("Enter the Farenheit Degrees: "))
    ftc=(f1-32)*5/9
    print("The Converter Celcius is",ftc)
elif deter == "ctf":
    c1=float(input("Enter the Celcius Degrees:"))
    ctf=(c1*9/5)+32
    print("The Converter Celcius is",ctf)
else:
    print("ftc or ctf determiners only")

print("Thank You")

# End Of Code