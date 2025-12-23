#details of loan
money_owed = float(input("How much money do you owe, in dollars?\n")) # $50,000
apr= float(input("What is the annual percentage rate?\n")) # 3%
payment = float(input("What is your monthly payment, in dollars?\n")) # $1,000
months = int(input("How many months do you want to calculate?\n")) # 24

monthly_rate = apr / 100 / 12

#Calculate interest to pay
interst_paid = money_owed * monthly_rate 

# Add interest to money owed
money_owed = money_owed + interst_paid

# Subtract payment from money owed
money_owed = money_owed - payment

print("Paid", payment, "of which", interst_paid, "was interest.", end = " ")
print("Now I owe", money_owed)

#Make it more dynamic with a loop
for i in range (months):
    #Calculate interest to pay
    interst_paid = money_owed * monthly_rate 

    # Add interest to money owed
    money_owed = money_owed + interst_paid

    if (money_owed - payment < 0):
        print("The last payment is", money_owed)
        print("You paid off the loan in", i + 1, "months!")
        break


    # Subtract payment from money owed
    money_owed = money_owed - payment

    print("Paid", payment, "of which", interst_paid, "was interest.", end = " ")
    print("Now I owe", money_owed)