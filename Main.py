Number_1 = input("Select a number: ")
Number_2 = input("Select another number: ")
print("The numbers you selected are: " + Number_1 + " and " + Number_2)

shu_karvu = input("what you want to do: add, sub, mul or div: ")

if shu_karvu == "+":
    Number_3 = int(Number_1) + int(Number_2)
    print("The sum is " + str(Number_3))

if shu_karvu == "-":
    Number_3 = int(Number_1) - int(Number_2)
    print(" The difference is : " + str(Number_3))

if shu_karvu == "*":
    Number_3 = int(Number_1) * int(Number_2)
    print("The product is " + str(Number_3))

if shu_karvu == "/":
    Number_3 = int(Number_1) / int(Number_2)
    print(" The divident is : " + str(Number_3))

shu_karwavu_pachu = input(" what next?")

