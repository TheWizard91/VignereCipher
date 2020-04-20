#from VignereCipherProjectPackage.cipher import Vignere;
from cipher import *
#garbage just trying to display stiff nicely.
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
    text6 = "What is the Vignere chipper and how it works?\n\
The Vignere chipper is just a series of Cesare chippers.\n\
What it does is to shift the letters of the keywords by one.\n\
Then, compare the index od the letter at the key and\n\
the one at the alphabet you will get the decoded message."
    text7 = "Here is the key table with the letter shifted according to the\
keyword you have entered.\n"
    
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
    print("{0:^100}".format(key_title));# printing YOUR KEY TABLE.    
    print("{0:^20}***First line not a part of the table use it to find tp find the key.\n".format(""));
    l.insert(0,alpha);

    #Printing everying with spaces and next line so
    #the user get to see it better.
    for key_row in l:
        
        for letter in key_row:
            
            #if the letter is the letter of the key then capitalize it.
            #else let it be lower case.
            if counter2 == 0:
                print("| ", end + "");
                print(letter.capitalize() + " ", end + "");
                counter2 += 1;
            elif counter2 != 0:
                print("| ", end + "");
                print(letter + " ", end + "");
                counter2 += 1;
                
            #We reached the end of the line
            # would love to have a new line
            if counter2 == 26:
                counter2 = 0;
                print('*\n');
                
    print("Please note that firts I'm printing the letter from the alphabet.\n")
    print("Then, you have the table with all the charcaters shifted by 1.\n")
    print("Therefore do not consider the first line of the table as you key table.\n")
    print("So now try to see if you can hack it using the table.\n")
    print("Thanks for using my program (^.^).\n")
    print("Oh, and don't froget to check the files..\n")

def main():

    """Testing the cipher."""

    #Opening the input file.
    in_file = input("Please enter input file name: ");
    open_file = open(in_file, "r");
    read_file = open_file.read();
    print("open_file=",open_file,"read_file=",read_file);
    open_file.close();
##    lowe_case_input = read_file.lower();
##    print('adfaFD',lowe_case_input)
    
    #text = "the eagle has landed"
    key = input("Would you enter key please: ");
    
    #Process the encodeing and decoding thing.
    a = Vignere(key);
    a.get_text_to_encode(read_file.lower());
    encoded_message = a.return_encoded_message();
    a.get_text_to_decode(encoded_message);
    decoded_message = a.return_decoded_message();
##    print("lest, ",encoded_message)
##    print("dfadsf",decoded_message)

    #Writting stuff to output file
    out_file = input("Please enter output file: ");
    open_file2 = open(out_file, "w");
    read_file2 = open_file2.write(encoded_message);
    open_file2.close();    
    display(key);

    results = input("Do you want to see how to calculate them? ").lower();

    #More rubish stuff here to display things nicelly.
    if results[0] == "y":
        counter = 0;
        alpha = "abcdefghijklmnopqrstuvwxyz";
        print();
        print("{0:^100}".format("RESULTS") + "\n");
        print("{0}{1},{2:^10}{3}{4},{5:^10}{6}{7}".format("decoded text = ", decoded_message, "", "encoded text = ", encoded_message, "", "key = ", key)+"\n");
        for i in range(len(decoded_message)):
    ##        print(decoded_message[i])
    ##        print(alpha.index(decoded_message[i]))
    ##        print(alpha.index(enoded_message))
            print("For letter {0} in plaintext index is: {1}, and for {2} in encoded text is: {3}. Subtract them you get {4} index of {5}.".format
                  (decoded_message[i],alpha.index(decoded_message[i]),encoded_message[i],alpha.index(encoded_message[i]), key[counter],alpha.index(key[counter]))+"\n");
            counter += 1;
            if counter == len(key):
                counter = 0;
    else:

        pass

    print("Terminating the program! Look up the table now:)..")
main()
