given_sentence = 'I am learning python'
word_list = given_sentence.split(' ')

reversed_string = ''

for x in word_list[::-1]:
    reversed_string += x + ' '

print(reversed_string)
print(given_sentence[::-1])
