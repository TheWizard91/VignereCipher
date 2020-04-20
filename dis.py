def display(key):
    
    """Will display the how Vignere is implemented and a beautiful text-based GUI
    pre: key is selfexplanatory
    post:wisplay user the key table."""
    
    key = 'davinci';
    
    alpha = "abcdefghijklmnopqrstuvwxyz";

    counter1 = counter2 = 0;
    
    l = [];
    
    key_title = "YOUR KEY TABLE.\n";
    
    text1 = "Emmanuel Kofi Agyapong (The_wizard91).";
    text2 = "Class: CSI 33.\n";
    text3 = "Bronx Community College.";
    text4 = "Instrctor : Natalia Novak.\n";
    text5 ="Presents Vignere Chiper.\n";
    text6 = "What is the Vignere chipper and how it works?\
    The Vignere chipper is just a series of Cesare chippers.\
    What it does is to shift the letters of the keywords by one.\
    Then, compare the index od the letter at the key and\
    the one at the alphabet you will get the decoded message."
    text7 = "Here is the key table with the letter shifted according to the\
    indef of the keyword you have entered.\n"
    
    #Appending to a list the shifting of the letters from the alphabetic table
    #this way we can show how Vignere has created the key table used to hack
    #his own chipper. In a nut shell each letter in the key is shited by 1
    #and if we reach the end the, the shift occure from index 0 to index of
    #were the letter is poeitioned in the alphabet. To avoid going through
    #painful nested loops and conditional statements I deided to use indexing and
    #to create a formula that will fit our case.

    print("{0}{1:^55}".format(text1, text2))
    print("{0}{1:^85}".format(text3, text4))
    print("{0:^70}".format(text5))
    print("{0}".format(text6))
    print("{0}".format(text7))
    for letter in key:

    #apending the alpabet from index of the letter in the key to z + the rest that we are missing
        l.append(alpha[alpha.index(key[counter1]) : ] + alpha[ : alpha.index(key[counter1])]);#i.e. d to z + 'abc' since d is the thid element in the list abc were 
        counter1 += 1;                                                          # left off and we need to find a way to put them in the back
                                                                                             # run program with a key that a d to see.
    print("{0:^50}".format(key_title));# printing YOUR KEY TABLE.
    
    l.insert(0,alpha);

    #Printing everying with spaces and next line so
    #the user get to see it better.
    for key_row in l:
        for letter in key_row:
            print(letter+" ", end='');
            counter2 += 1;
            if counter2 == 26:
                counter2 = 0;
                print('\n');
                
    print("Please note that firts I'm printing the letter from the alphabet.\n")
    print("Then, you have the table with all the charcaters shifted by 1.\n")
    print("Therefore do not consider the first line of the table as you key table.\n")
    print("So now try to see if you can hack it using the table.\n")
    print("Thanks for using my program (^.^).\n")
    print("Oh, and don't froget to check the files..\n")
