# Accidentally I messed up this quote from Richard Feynman.
# Two words are out of place
# Your task is to fix it by swapping the right words with code

# Also, print the sentence to the output with spaces in between.

words = ["What" , "I" , "do" , "create," , "I" , "cannot" , "not" , "understand."]
a , b = words.index("do") , words.index("cannot")
words[a] , words[b] = words[b] , words[a]
print(" ".join(words))
