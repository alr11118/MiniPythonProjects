# Credit Card Validator Program

# 1. Remove any '-' or ' '
# 2. Add all digits in the odd places from right to left
# 3. Double every second digit from right to left
#.           (if resault is a two digit number, 
#             add the two digit number together to get a single digit.)
# 4. Sum the totals of step 1 and 2
# 5. If sum is divisable by 10, the credit card # is valid

sum_odd_digits = 0
sum_even_digits = 0
total = 0
# Step 1 
cardNumber = input("Enter a credit card number: ")
cardNumber = cardNumber.replace("-", "")
cardNumber = cardNumber.replace(" ", "")
cardNumber = cardNumber[::-1]

# Step 2
for x in cardNumber[::2]:
    sum_odd_digits += int(x)

# Step 3 
for x in cardNumber[1::2]:
    x = int(x)*2
    if x >= 10:
        sum_even_digits += (1+(x%10))
    else:
        sum_even_digits += x

# Step 4
total = sum_odd_digits + sum_even_digits

# Step 
if total%10 == 0:
    print("VALID")
else:
    print("INVALID")
    