#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      emmanuel.agyapong
#
# Created:     20/04/2017
# Copyright:   (c) emmanuel.agyapong 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Vignere(object):

    """A Vignere chiper class"""

    def __init__(self, key):

        self._r = ''#using it for decoding

        self._text = None# using it for incoding

        self._key = key

        self._alpha = "abcdefghijklmnopqrstuvwxyz"

#Public methods:
    
#--------------------------------------------------------------------------------

    #Getting the plain text
    def get_text_to_encode(self, plain_text):

        """Will get plain text from user."""

        self._text = plain_text

#--------------------------------------------------------------------------------

    #Getting the decoded text
    def get_text_to_decode(self, encoded_message = None):

        """Decodinf methos helper will get text to encode
        and will return it to decoding method.
        Pre: encoded_message is encoded messgase."""
        
        #You said that I have to separate the encoding and decoding
        #methods since they should not be interacting. In this method
        #I let the user enter a encoded message if they have one
        #if not then, the code will use the instance varaible self._text
        #to the decoding method bellow.
        
        if encoded_message != None:

            self._r = encoded_message
            
        else:
            
            #In here they do not enter any input.
            self._r = self._text

#--------------------------------------------------------------------------------

    #Returning encoded message
    def return_encoded_message(self):

        """Will return the encoded message."""

        return_the_encoded_message = self._encode_text()

        self._text = return_the_encoded_message#Needed this line because self._text is called later in encode text as parameter.

        return return_the_encoded_message

#--------------------------------------------------------------------------------

    #Returning decoded message
    def return_decoded_message(self):

        """Will return decoded message."""

        return self._decode_text()

#--------------------------------------------------------------------------------

    #Eliminating punctuation
    def _text_with_no_punctuation(self):

        """Will return the text without any punctuation
        Post: Will eliminate any punctuation on the test (side effect)."""

        #rswp standes for returning string without any punctuation.
        rswp = ""#selfexplanatory trying to get rid of punctuaition.

        #Concatenating the letter in the text to rswp.
        for alphabetic_letter in self._text:
            if alphabetic_letter not in self._alpha:
                pass
            else:
                rswp += alphabetic_letter
        return rswp

#--------------------------------------------------------------------------------

#Private method

    #Encoding method
    def _encode_text(self):

        """Will encode the plain text.
        Post: Will return the encoded message."""
        
        text = self._text_with_no_punctuation()
        encode_message = ""
        key_lenght = len(self._key)
        key_index = text_index = 0

        #a: alphabetic letter in index
        #b: letter in key index
        a = b = 0

        #Initiating the encoding proccess
        while True:

            #Pairing indices of text and key so
            #that we crate the encoded message.
            if text_index == len(text):
                text_index = text_index = 0
                break
            elif key_index >= key_lenght:
                key_index = 0
            else:
                a = self._alpha.index(text[text_index])
                b = self._alpha.index(self._key[key_index])
                print('self._key[key_index] = ',self._key[key_index])
                print("b = ",b)
                encode_message += self._alpha[(a + b) % 26]
                key_index += 1
                text_index += 1

        return encode_message

#--------------------------------------------------------------------------------

    #Decoding method
    def _decode_text(self):

        """Will decod the text.
        Post: Will return the decoded message."""

        encoded_message = self._r
##        print("self._r = ", self._r)
##        print("ecoded message = ",encoded_message)
        decode_message = ""
        key_index = text_index = 0

        # a = extraxting index of letter in text
        # b = extraxting index of letter in key
        # c = tot index value from subtractinga and b
        a = b = c = 0

        while True:

            #Pairing indeces of text and key so
            #that we crate the decoded message.
            if text_index == len(encoded_message):
                break
            if key_index >= len(self._key):
                key_index = 0
            if key_index == len(self._key):
                key_index -= 1
            a = self._alpha.index(encoded_message[text_index])
            b = self._alpha.index(self._key[key_index])
            c = a - b

            #Decoding assembling.
            if c >= 0:
                decode_message += self._alpha[c % 26]
            else:
                #d=c
                c += 26
                decode_message += self._alpha[c]
            text_index += 1
            key_index += 1

        return decode_message
