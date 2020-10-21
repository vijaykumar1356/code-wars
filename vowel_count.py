#Return the number (count) of vowels in the given string.
#We will consider a, e, i, o, u as vowels for this Kata (but not y).
#The input string will only consist of lower case letters and/or spaces.

def get_count(input_str):
    num_vowels = 0
    if len(input_str) == 0:
        return 0
    else:
        for i in input_str:
            if i in "aeiouAEIOU":
                num_vowels += 1       
    return num_vowels
    # return sum(c in "aeiouAEIOU" for c in input_str)

print(get_count(input()))