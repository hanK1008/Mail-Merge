# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt


# TODO-1: Getting hold of invites_names.txt in main.py
with open("./Input/Names/invited_names.txt") as name_file:
    # print(name_file.read())
# TODO-2: Creating list of all name present in invited_name
    # name_list : name_file.readlines()  is giving /n in the last of each word so I used .read.splitlines
    name_list = name_file.read().splitlines()
    print(name_list)

# TODO-3: Getting hold of starting_letter.txt
with open("./Input/Letters/starting_letter.txt") as starting_letter:
    letter = starting_letter.read()
    letter.replace("Angela", "hanK")
    print(letter)
# Replace the [name] placeholder with the actual name.
# TODO-4: Get hold of [name] & replace with the name present in the list
# TODO-4.1: while replacing make sure you are creating new file.txt and updating in that file not in same file
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
