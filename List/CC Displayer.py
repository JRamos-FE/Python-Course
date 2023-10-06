# Program to display a credit card number

cardnum = input('Enter CC number: ')

lastDigits = cardnum[15::]

fourStars = '*' * 4 + ' '
displayNum = fourStars * 3 + lastDigits

print(displayNum)