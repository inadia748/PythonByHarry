#5. It is similar to question 4. You have to censor a list of words.

words = ['donkey', 'fatty', 'asshole', 'idiot', 'stupid']

with open('sample.txt') as f:
    content = f.read()     

for word in words:
    content = content.replace(word, '#$%$@#')

with open('sample.txt', 'w') as f:
    f.write(content)