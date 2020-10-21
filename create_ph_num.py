# Write a function that accepts an array of 10 integers (between 0 and 9), 
# that returns a string of those numbers in the form of a phone number.
# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"


def create_phone_number(n):
    return f"({''.join(list(map(str, n[:3])))}) {''.join(list(map(str, n[3:6])))}-{''.join(list(map(str, n[6:])))}"



#def create_phone_number(n):
#	return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)