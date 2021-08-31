weight = int(input("Weight: "))
tounit = input("To Which Unit? (K)ilograms or (P)ounds: ")
# Kilograms should multiply by 0.45, because it lowers the number by multiplying it less times than 1
if tounit == "P" or "p":
    print(weight / 0.45)
# pounds should divide by 0.45, because it increases the number by dividing it more times than 1
elif tounit == "K" or "k":
    print(weight * 0.45)
