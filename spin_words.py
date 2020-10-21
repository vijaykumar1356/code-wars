# Code Wars 6kyu problem
# Function that takes in a string of one or more words, and returns the same string,
# but with all five or more letter words reversed
def spin_words(sentence):
    # sep = sentence.strip().split()
    # result = []
    # for word in sep:
    #     result.append(word if len(word)<5 else word[::-1])
    # return " ".join(result)
    return " ".join([x if len(x)<5 else x[::-1] for x in sentence.split()])

print(spin_words(input()))