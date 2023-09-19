# Write a program to reverse the a string without using reverse built-in function
given_sentence = 'I am learning python'
word_list = given_sentence.split(' ')

reversed_string = ''

for x in word_list[::-1]:
    reversed_string += x + ' '

print(reversed_string) #expected output: 'python learning am I' 
print(given_sentence[::-1]) #expected output: 'nohtyp gninrael ma I'
