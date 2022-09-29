# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt


# TODO-1: Getting hold of invites_names.txt in main.py
with open("./Input/Names/invited_names.txt") as name_file:
    # print(name_file.read())
# TODO-2: Creating list of all name present in invited_name
    # name_list : name_file.readlines()  is giving /n in the last of each word so I used .read.splitlines
    name_list = name_file.read().splitlines()
    # name_list = ['Aang', 'Zuko']                 #For testing list
    # print(name_list)

# TODO-3: Getting hold of starting_letter.txt

# Changing Angela with hanK
with open("./Input/Letters/starting_letter.txt") as starting_letter:  # opening the file
    letter = starting_letter.read()                # Reading letter and saving it in letter
    letter = letter.replace("Angela", "hanK")      # saving letter with replacing Angela with hanK

with open("./Input/Letters/starting_letter.txt", mode="w") as starting_letter: # opening the file in write mode
    starting_letter.write(letter)                  # writing the letter with replaced letter shown above

# Replace the [name] placeholder with the actual name.
# TODO-4: Get hold of [name] & replace with the name present in the list
# TODO-4.1: while replacing make sure you are creating new file.txt and updating in that file not in same file

# TDO-4.1.1: Getting hold of starting letter
for names in name_list:
    with open("./Input/Letters/starting_letter.txt") as starting_letter:  # opening the file
        letter = starting_letter.read()                # Reading letter and saving it in letter

        # letter = starting_letter.read()
        letter = letter.replace("[name]", names)
        file_name = f"Letter_for_{names}"
        with open(f"./Output/ReadyToSend/{file_name}.txt", mode="w") as output_file:
            # output_file = open(f"./Output/ReadyToSend/{file_name}.txt", mode="w")
            output_file.write(letter)

# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# https://pythonexamples.org/python-replace-string-in-file/

