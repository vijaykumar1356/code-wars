# Create a function taking a positive integer as its parameter and returning a string containing
#  the Roman Numeral representation of that integer. Modern Roman numerals are written 
# by expressing each digit separately starting with the left most digit
#  and skipping any digit with a value of zero. This code works upto 3999
# def solution(n):
#     roman = {1:'I', 2:'II' , 3:'III', 4:'IV', 5:'V',6:'VI', 7:'VII', 8:'VIII', 9:'IX',
#     10:'X', 20:'XX', 30:'XXX', 40:'XL', 50:'L', 60: 'LX', 70:'LXX', 80:'LXXX', 90:'XC', 100:'C',
#     200:'CC', 300:'CCC', 400:'CD', 500:'D', 600:'DC', 700:'DCC', 800:'DCCC', 900:'CM', 1000:'M',
#     2000:'MM',3000:'MMM', 0: ""
#     }
#     rank = 1
#     roman_str = []
#     while n != 0:
#         num = n%10
#         n = n//10
#         rom_num = roman[num*rank]
#         roman_str.append(rom_num)
#         rank *= 10
#     return "".join(roman_str[::-1])

# def solution(n):
#     roman_numerals={1:'I', 4:'IV', 5:'V', 9:'IX',
#     10:'X', 40:'XL', 50:'L', 90:'XC', 100:'C', 
#     400:'CD', 500:'D', 900:'CM', 1000:'M'}
#     roman_string = ""
#     for key in sorted(roman_numerals.keys(), reverse=True):
#         while n >= key:
#             roman_string += roman_numerals[key]
#             n -= key
#     return roman_string
def solution(n):
    roman_numerals = zip(('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I'),
           (1000, 900, 500,  400, 100,   90,  50,   40,  10,    9,   5,    4,   1))
    # roman_numerals={1:'I', 4:'IV', 5:'V', 9:'IX',
    # 10:'X', 40:'XL', 50:'L', 90:'XC', 100:'C', 
    # 400:'CD', 500:'D', 900:'CM', 1000:'M'}
    if n == 0:
        return ""
    # return next(roman_numerals[key] + (solution3(n-key)) for key in sorted(roman_numerals.keys(), reverse=True) if n>=key)
    return next(key + solution3(n-value) for key, value in roman_numerals if n>=value)



n = int(input())
print(solution(n))
