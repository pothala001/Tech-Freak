#write a python code for removing vowels in a string. Only small lettered vowels to be removed

import re

given_string = 'I love coding in python'

#Method1 - conventional loop method
result_string = ''

for i in range(len(given_string)):
    if given_string[i] in ['a','e','i','o','u']:
        i = i + 1
    else:
        result_string = result_string + given_string[i]
        i = i + 1

print(result_string)

#Method2 - using list comprehensions
result2 = ''
result2 = result2.join([x if x not in ['a','e','i','o','u'] else '' for x in given_string])
print(result2)


#Method3 - using regular expresions
result3 = re.sub(r'[aeiou]','',given_string)
print(result3)
