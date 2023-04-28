#make a list for the yes option in asking the user again
yes_user_input = ["Y" , "y" , "Yes" , "YES"]
#make the list for the no option in asking the user again
no_user_input = ["N" , "n" , "No" , "NO"]
#open a file to make a text file called mylife.txt
with open("mylife.txt" , "a") as mylife_file:
    #create a loop to ask what to put in the file
    while True:
        #ask the user for the input in the file
        user_line_input = str(input("Enter a line to add to your file: "))
        #write the input of the user in the file
        mylife_file.write(user_line_input + "\n")
        #ask the user if he/she wants to put more lines
        #check the answer in the ask user again