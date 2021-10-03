#1. Write a  python program to display a user entered 'Good Afternoon' using input function.

name = input('Enter your name: ')
print('Good Afternoon, ' + name)


#2. Write a program to fill in a letter template given below with name and date
letter = '''
            Dear <|NAME|>,
            You are selected!

            Date: <|DATE|>
        '''
a = input('Enter your name: ')
date = input('Enter Date: ')
letter = letter.replace("<|NAME|>", a)
letter = letter.replace("<|DATE|>", date)
print(letter)




#3. write a program to detect double spaces in a string.

st = "There is a string with double  spaces"
doubleSpaces = st.find("  ")
print(doubleSpaces)


#4. Replace double spaces with single space
st = st.replace("  ", " ")
print(st)


#5. Write a program to format the following letter using escape sequence character.

letter = 'Dear Nadia, This  Python course you are learning is nice'
print(letter)
formatter = 'Dear Nadia,\n\t This  Python course you are learning is nice. \nThank you for learning'
print(formatter)