appleQntty=int(input("how many apples do you want to buy?"))
orangeQntty=int(input("how many oranges do you want to buy?"))

applePrc=20
orangePrc=35

appleTtl=appleQntty*applePrc
orangeTtl=orangeQntty*orangePrc
totalPrc=appleTtl+orangeTtl
print(f"The total amount is {totalPrc}.")