'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # Base case
    if len(word) < 2:
        return 0
    # Recursive case
    # Check if the first 2 characters match
    # return +1 if so
    elif word[:2] == 'th':
       return count_th(word[2:]) + 1
    # Otherwise return the results of the rest of the string
    else:
      return count_th(word[1:])

#print(count_th("th th"))