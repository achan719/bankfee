## This program will calculate the total bank fees based on the 
# number of checks entered 

##  $10 per month plus the below fees per check
##  -----
##  Under 11 checks / $0.10 each
##  12 -30 checks / $0.08 each 
##  31 - 59 checks / $0.06 each
##  Over 60 checks / $0.03 each

#%%
print("This will calculate the total bank fees based on the number of checks.")
print("*Please note that there will be an additional $10.00 bank charge.*\n")

fee = 10.0

# input
num = int(input("Enter Number of Checks: "))

# calculation
if num > 0:
    if num < 20:
        fee += (num * .10)
        print("Fees: $0.10")
    elif num < 39:
        fee += (num * .08)
        print("Fees: $0.08")
    elif num < 59:
        fee += (num * .06)
        print("Fees: $0.06")
    else:
        fee += (num * .03)
        print("Fees: $0.03")

# output
if num < 0: 
    print("Error! Enter a Valid Number")
else: 
    print("Number of Checks: ", num)
    print("Total Charge: $", format(fee, '.2f'))


# %%
