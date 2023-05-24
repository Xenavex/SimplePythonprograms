#  Name : Ancient Debris to Netherite Calculator
#  IGN : Xenavex | Hatakechop3
#  Discord : 𝐗𝐞𝐧𝐚𝐯𝐞𝐱#6886
#  Twitter : @Xenavex
#  Website : Bit.ly/Hatakeall

debris=int(input('Enter The Amount Of Ancient Debris You Have currently :'))
x=debris/4
if debris%4!=0:
    y=str(x).split('.')
    #print(y[1])
    if y[1]=='25':
        print(y[0],'  U Have An Extra Ancient Debris ')
    elif y[1]=='5':
        print(y[0],'  U Have 2 Extra Ancient Debris ')
    elif y[1]=='75':
        print(y[0],'  1 More Extra Ancient Debris Needed For An Extra Netherite Ingot :D')
    #elif y[1]=='0':
       #pass
else:
    print(round(x))
    
# End Of Code