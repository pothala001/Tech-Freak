# Write a program to reverse (words/letters) in a string without using reverse function

#Method1
given_sentence = 'I am learning python'
word_list = given_sentence.split(' ')

reversed_string = ''

for x in word_list[::-1]:
    reversed_string += x + ' '

print(reversed_string.strip()) # reverse the words
print(given_sentence[::-1]) # reverse the letters

#Method2
reversed_string2 = ' '.join(given_sentence.split(' ')[::-1]) # reverse the words single liner code
print(reversed_string2)

