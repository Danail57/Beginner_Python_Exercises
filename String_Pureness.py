#Write a program that checks whether a series of strings are "pure".
#A string is considered pure if it does not contain any of the following characters:
#- A comma 
#- A period 
#- An underscore 

number_of_strings = int(input())
for current_strings in range(number_of_strings):
    current_string = input()
    if ',' in current_string or\
            '.' in current_string or\
            '_' in current_string:
        print(f"{current_string} is not pure!")
    else:
        print(f'{current_string} is pure.')
