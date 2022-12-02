'''
DECRYPTION PROGRAM
------------------
An ENCRYPTION program was used to generate the following secret code. The encryption program converted each character 
of the string into its ASCII decimal number, applied a +/-20 algorithm to it and then converted it back to
characters. Your task is to write a DECRYPTION program to decipher the following secret code. Don't waste time changing 
your program 40 times. Use a FOR loop from -20 to +20 to generate all the possibilities in one run of your program.

Extra Challenge: Instead of printing out 41 lines of text to look at, can you determine a way to just print out the decrypted line only
along with the shift number?
'''
Secret_Message="Lxwp{j}~uj}rxw|*)bx~)l{jltnm)}qn)lxmn7)]qn)ox{ln)r|)\][XWP)r}q)x~*"

#
# for decrypt in range (-20,20):
#     chr("Lxwp{j}~uj}rxw|*)bx~)l{jltnm)}qn)lxmn7)]qn)ox{ln)r|)\][XWP)r}q)x~*")

    # print("1. Encrypt \n2. Decrypt")
    # text = input("Choose an option")
    # if text == "1":
    #     encrypted = ' '
    #     word = input("Enter a word to encrypt")
    #     for letter in word:
    #         i = ord(letter) + 5
    #         newletter = chr(i)
    #         encrypted += newletter
    #
    #     print(encrypted)
    #     reselect = input("Would you like to use again?")
    #     if reselect == "no" or reselect == "n":
    #         done = True
    #     else:
    #         print("")
    # elif text == "2":

for x in range(-20, 21):
    encrypted = ' '
    s = 0
    for letter in Secret_Message:
            i = ord(letter)
            i += x
            newletter = chr(i)
            if newletter == " ":
                s+=1
            encrypted += newletter
    if s>2:
        print(str(x)+'    '+ encrypted)
