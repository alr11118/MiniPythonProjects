numeralInput = input("Enter the roman numerals you want to convert: ")

def romanToInt(numeral):
    finalInteger = 0
    if "CM" in numeral:
        finalInteger += 900
        numeral = numeral.replace("CM", "")
    if "CD" in numeral:
        finalInteger += 400
        numeral = numeral.replace("CD", "")
    if "XC" in numeral:
        finalInteger += 90
        numeral = numeral.replace("XC", "")
    if "XL" in numeral:
        finalInteger += 40
        numeral = numeral.replace("XL", "")
    if "IX" in numeral:
        finalInteger += 9
        numeral = numeral.replace("IX", "")
    if "IV" in numeral:
        finalInteger += 4
        numeral = numeral.replace("IV", "")
    for i in numeral:
        if i == "M":
            finalInteger += 1000
        elif i == "D":
            finalInteger += 500
        elif i == "C":
            finalInteger += 100
        elif i == "L":
            finalInteger += 50
        elif i == "X":
            finalInteger += 10
        elif i == "V":
            finalInteger += 5
        elif i == "I":
            finalInteger += 1
    print("The roman numerals translates to: " + str(finalInteger))

romanToInt(numeralInput)
