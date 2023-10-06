# Progrom that converts a Roman numeral into an integer

roman = {'I': 1,
         'V': 5,
         'X': 10,
         'L': 50,
         'C': 100,
         'D': 500,
         'M': 1000
         }

number = input('Enter Roman number in upper cases: ')

dec_num = 0
i = 0

while i < len(number):
    if i + 1 < len(number) and roman[number[i]] < roman[number[i + 1]]:
        dec_num += roman[number[i + 1]] - roman[number[i]]
        i += 2
    else:
        dec_num += roman[number[i]]
        i += 1

print(dec_num)
