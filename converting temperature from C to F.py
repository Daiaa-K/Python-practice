# inputting the temp in format 50(c or f)
temp = input("enter the temperature you want converted C or F? : ")
degree = int(temp[:-1])
convention = temp[-1]

# converting temperature to F

if convention.lower() == "c":
    print("Converting from C to F...")
    converted_temp = (9* degree + (32*5))/5
    print(f"{degree}C converted to F is {converted_temp:+.2f}F")

# converting temperature to C

elif convention.lower() == "f":
    print("Converting from F to C")
    converted_temp = (5 * (degree - 32)) / 9
    print(f"{degree}F converted to C is {converted_temp:+.2f}C")
else:
    print("wrong temperature entered")