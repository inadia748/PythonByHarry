#3. Write a program to generate multiplication tables. From 2 to 20 and write it into the different files. Place these files in a folder for a 13-year old.

for i in range(2,21):
    with open(f"tables/Multiplication_table_of_{i}.txt",'w') as f:
        for j in range(1,11):
            f.write(f"{i} X {j} = {i*j}\n")
            # if j != 10:
                #f.write('\n')
    break #break will take only the multiplication table of 2, if you remove 'break', it will generate multiplication table files from 2 to 20.
