# Elice Greenberg

# This program:
# Greets the user in English
# Asks the user to choose from 1 of 3 spoken languages 
# Displays the greeting in the chosen language
# Allows re-entry if user doesn't follow instructions properly
# Exits


print('Hello There!')
#displays first sentence (greeting in English)
print('')
#spaces sentences
print('No speak English? No Problem!')
print('')
print('For Hebrew press 1- Leivrit lechaz 1')
print('For Russian press 2- Dlya Ruskee najimayiti 2')
print('For Italian press 3- Per Italiano stampa 3')
print('')
language = input()
#asks user to enter a number according to the desired language
while language != '1' and language != '2' and language != '3':
#this loop will allow user continuous trials until user follows instructions correctly
#if user has followed instructions, this loop will be skipped
#loop will be exited once user made a valid selection
    print('Your selection is invalid. Please select between 1, 2 or 3')
    #a message displayed as an error message, explaining to user that they have not followed instructions and restating instructions
    language = input()
    #allows the user to re-enter their selection
if language == '1':
    print('Shalom Leha!')
    #this message is displayed (greeting in Hebrew) if user selected this language by pressing 1 as per instructions
elif language == '2':
    print('Priviet Vam!')
    #this message is displayed (greeting in Russian) if user selected this language by pressing 2 as per instructions
else: print('Ciao Amico!')
#if none of the previous condition to what the user entered were true, the only option left is for the user to have entered the number 3
#therefor this message (greeting in Italian) will be displayed if user selected this language by pressing 3 as per instructions
