'''
MONTHS PROGRAM
--------------
Write a user-input statement where a user enters a month number 1-12.
From the user input number, slice the string below in your program to print the three month abbreviation.
Keep repeating this until the user enters a non 1-12 number to quit.
Once the user quits, print "Goodbye!"
'''

months = "JanFebMarAprMayJunJulAugSepOctNovDec"

done = False
while not done:
    try:
        m=int(input("Please enter a month number (1-12):"))
    except ValueError:
        print("\nPlease enter an integer!\n")
        continue
    if 0<m<13:
        print(months[m*3-3:m*3])
    else:
        print("Not an option")
        break





# list = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
# month = int(input("Choose a Month 1-12:"))-1
#
# print(list[month])
