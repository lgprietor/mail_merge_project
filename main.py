#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

# with open("./Input/Letters/starting_letter.txt") as letter_file:
#     lines = letter_file.readlines()
#     print(lines)

# with open("./Input/Names/invited_names.txt") as names_file:
#     contents = names_file.read()
#
#     print(contents)

# 1) Let's create a names list using the invited_names file:

with open("./Input/Names/invited_names.txt") as names_file:
    names_list = names_file.readlines()
    adjusted_names = []

# 2) It's necessary to strip the names line in order to delete the "\n" characters and create a new adjusted list:

    for i in names_list:
        new_name = i.strip("\n")
        adjusted_names.append(new_name)
    print(names_list)
    print(adjusted_names)

# 3) Now, we need to extract the content of the original letter and adjust it with the specific name and then create the
# personalized letter:

with open("./Input/Letters/starting_letter.txt") as letter_file:

    letter_lines = letter_file.readlines()
    print(letter_lines)

    new_letter = []

    for i in adjusted_names:
        with open(f"letter_for_{i}", mode="w") as file:
            new_heading = letter_lines[0].replace("[name]",i)
            new_letter.append(new_heading)
            new_letter.extend(letter_lines[1:])
            content_letter = file.write(' '.join(new_letter))
            new_letter = []
            # print(content_letter)















# with open("./Input/Letters/starting_letter.txt") as letter_file:
#     lines = letter_file.readlines()
#     A = ' '.join(lines)
#     print(A)
#
#     name = lines[0].replace("[name]","Perro")




    # print(name)



#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp