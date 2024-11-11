
#  Name : Simple Balance Sheet Calculator
#  IGN : Xenavex | Hatakechop3
#  Discord : 𝐗𝐞𝐧𝐚𝐯𝐞𝐱
#  Twitter : @Xenavex
#  Website : Bit.ly/Hatakeall

# Intro

print("Calculates if the Balance Sheet is in Deficit or Surplus")

# User Input

Closing=float(input("Enter the Closing Balance:"))
Opening=float(input("Enter the Opening Balance:"))
Sale=float(input("Enter the Sale Amount:"))
Expense=float(input("Enter the Expense For the Day:"))
Collection=float(input("Enter the Collected Balance:"))
Othergains=float(input("Enter the Unexpected / Other Gains Received Today:"))
Otherlosses=float(input("Enter the Unexpected / Other Losses Received Today:"))

# Calculation

Answer = ((Closing)-(Opening)-(Sale)+(Expense)-(Collection)-(Othergains)+(Otherlosses))

if Answer>30000:
    print(Answer,"is the Excess")
elif Answer<0:
    print(Answer,"is the Deficit")
else:
    print(Answer,"amt of variation is okay")

# Exit Module

print("Goodbye")
input("Press Enter to exit")

# End Of Code