amount=int(input("how much do you have?"))
applePrc=int(input("how much is the price of an apple?"))

appleQntty=amount//applePrc
change=amount%applePrc
print(f"You can buy {appleQntty} apples and your change is {change} pesos.")