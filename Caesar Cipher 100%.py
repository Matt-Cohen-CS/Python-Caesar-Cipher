"""
Decoding an imported doc using the Ceasar Cipher. Also, asking for input from user
to encode their messages.

Names: Matthew Cohen, Alexander Hampp, Justin Sierra, Dominick Tarabocchia

Date: 11/25/2017
"""
# Importing the ciphered document and making it an array.
file = open ('projectC_cipher1.txt')

""" Test plan, 1st test print(file)"""

filearray = []
print("This is your deciphered document!\n")
for line in file.readline():
    filearray.append(line)    
# Declaring filler variables
var1 = 0
variable = 0
# Finding the most repeated letter, this is for the shift! Why 97? Check the next comment!
for alpha in range(0,26):
    index = alpha
    var = filearray.count(chr(index + 97))
    if var > var1:
       var1 = var
       variable = index
""" Test plan, 2nd test print(index) print(variable) """

# Adding 97 to the most repeated letter so it equals its' ASCII code
variable = variable + 97
""" Test plan, 2nd test print(index) print(variable) """

# This will be the number we will subtract from each letter. A.K.A the shift
shift = abs(variable - ord('e'))
""" Test plan, 3rd test print(shift)"""

# Subtracting the shift from each letter
for line in filearray:
    letter =  ord(line)
    """ Test plan, 4th test print(letter)"""
    letter = letter - shift
    """ Test plan, 4th test print(letter)"""
# This will ensure all letters will be in range, if they get subtracted not within the ASCII numberic code
    
    if letter < 97:
        letter = letter + 26
    letter = chr(letter)
    """ Test plan, last tests print(letter)"""
# This will ensure spaces get printed out right.
    if letter == "0":
        letter = " "
        """ Test plan, last tests print(letter)"""
# The final deciphered document

    print (letter, end="")
    
plaintextarray = []   
# Finding out if user wants to cipher inputted text
go = True

while(go):
    plaintext1 =input("\n\nWould you like to input text to be ciphered (Y/N) ")
    if plaintext1.lower() == "y":
        plaintext = input("\nPlease enter what you would like to be ciphered (Note: if\nyou input numbers or puncutations they will not be ciphered!)\n")
        plaintextold = plaintext
        # Appending the inputed text to an array
        for letter in plaintext:          
           plaintextarray.append(letter)
           """ Test Plan / Second half. Second test: print (plaintextarray)"""                   
        while(go):        
             shift = int(input("\nPlease enter a shift from (1-26) "))
             
             if shift>=1 and shift<=26:
                # Lowercasing all inputted letters, and adding the shift to it
                for letter1 in plaintextarray:
                    letter1 = letter1.lower()                    
                    letter1 = ord(letter1)                                       
                    letter1 = letter1 + shift
                    # This gets rid of all punctuation
                    if letter1>0 and letter1 <97:
                        letter1 = chr(letter1)
                        letter1 = 0
                        
                    # If the ASCII number goes over 122 we need to subtract 26 because it will equal that letter
                    if letter1 > 122:
                       letter1 = letter1 - 26                                       
                    letter1 = chr(letter1)
                    
                    # This gets rid of all the spaces and makes them just spaces not characters
                    # This is in this position because if its in any other place there will be a casting error 
                    if ord(letter1) - shift == 32:
                       letter1 = " "
                    # Plaintext ciphered.
                    print(letter1,end="")
                    
                print(": This is your ciphered text")    
                print("\n\n",plaintextold," : was your original text")
                
                plaintextarray = [] # Resets the array
                break # ends the second "go" loop
                             
             else:
                print("\nThe shift must be from range 1 to 26")
                continue # Starts this loop over
    elif plaintext1.lower() == "n":
        print("\nThe program has ended!")
        go = False # Will end loop
    else:
        print("\nYou need to either enter Y for yes or N for no.\n")
        continue # Starts loop over

