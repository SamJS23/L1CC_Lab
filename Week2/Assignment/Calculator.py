print("Math calculator")
print("Arithmetic operators:")
print("1. + = first number added by the second number")
print("2. - = first number subtracted by the second number")
print("3. * = first number multiplied by the second number")
print("4. / = first number divided by the second number")
print("5. ** = first number to the power of the second number")
ao = input("Choose the arithmetic operator:")
x = input("Enter the first number:")
y = input("Enter the second number:")
if x=="" or y=="":
    print("")
else: 
    fn,sn = float(x), float(y)
if x=="" or y=="":
    print("")
elif ao =="1":
    print(fn+sn)
elif ao == "2":
    print(fn-sn)
elif ao == "3":
    print(fn*sn)
elif ao == "4":
    print(fn/sn)
elif ao == "5":
    print(fn**sn)


