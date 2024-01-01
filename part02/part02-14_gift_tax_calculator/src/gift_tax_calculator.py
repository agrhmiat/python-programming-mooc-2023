# Write your solution here

gift = int(input("Value of gift: "))

if gift < 5000:
    tax = 0
elif gift < 25000:
    tax = 100
    tax_rate = 0.08
    amount = (tax + (gift - 5000) * tax_rate)
elif gift < 55000:
    tax = 1700
    tax_rate = 0.10
    amount = (tax + (gift - 25000) * tax_rate)
elif gift < 200000:
    tax = 4700
    tax_rate = 0.12
    amount = (tax + (gift - 55000) * tax_rate)
elif gift < 1000000:
    tax = 22100
    tax_rate = 0.15
    amount = (tax + (gift - 200000) * tax_rate)
else:
    tax = 142100
    tax_rate = 0.17
    amount = (tax + (gift - 1000000) * tax_rate)

if tax == 0:
    print("No tax!")
else:
    print(f"Amount of tax: {amount} euros")
