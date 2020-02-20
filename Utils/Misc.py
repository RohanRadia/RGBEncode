def to_ascii(text: str):  # define required arguments
    ascii_array = []  # array to store letters once converted to ascii

    for letter in text:  # loops through every letter in the text variable
        ascii_array.append(ord(letter))  # turns the letter into ascii value and appends to ascii_array

    return ascii_array


def from_ascii(ascii_list: list):  # define required arguments
    output_text = ''  # blank string to store letters once converted from ascii

    for value in ascii_list:  # loops through all values in ascii_list variable
        output_text += chr(value)  # turns ascii value into letter and concatenates with output_text

    return output_text


def to_three(ascii_list: list):  # define required arguments
    three_list = []  # array to store groups of 3 ascii values

    for i in range(len(ascii_list)):  # loops performed are equal to the length of ascii_list
        if (i % 3) == 0:  # if the current value of i is equal to 0...
            three_list.append([])  # ... then add append a new list to three_list

        three_list[-1].append(ascii_list[i])  # append the value from ascii_list in position i into the mini list
        # stored in the last position of three_list

    while len(three_list[-1]) is not 3:  # if the length of the mini ascii list in the last position is not 3 then...
        three_list[-1].append(0)  # append 0

    return three_list  # output should be similar to: [[1, 2, 3], [4, 5, 6], [7]]


def from_three(three_list: list):  # define required arguments
    ascii_list = []  # array to store all ascii values

    while three_list[-1][-1] is 0:  # while the last value of the last mini list is 0 then...
        three_list[-1].pop(-1)  # remove that value from the list

    for array in three_list:  # loop through arrays in three_list
        for value in array:  # for each value in array...
            ascii_list.append(value)  # ... append the value to ascii_list

    return ascii_list


# Vigenère cipher encrypt method
def encrypt(string: str, key: str = " "):  # define required arguments
    encrypted_chars = []  # array to store all encoded letters in

    for i in range(len(string)):  # loops through all letter in string
        key_c = key[i % len(key)]  # each iteration it loops through the encryption key
        encrypted_c = chr(ord(string[i]) + ord(key_c) % 256)  # each iteration it loops through the ascii alphabet to
        # locate the encrypted character - essentially: chr(ord(letter) + ord(key))
        encrypted_chars.append(encrypted_c)  # appends each encrypted character to the encrypted_chars list

    encrypted_string = ''.join(encrypted_chars)  # append all encrypted characters into a single string

    return encrypted_string


# Vigenère cipher decrypt method
def decrypt(string: str, key: str = " "):  # define required arguments
    decrypted_chars = []

    for i in range(len(string)):  # loops through all letter in string
        key_c = key[i % len(key)]  # each iteration it loops through the encryption key
        decrypted_c = chr((ord(string[i]) - ord(key_c) + 256) % 256)  # each iteration it loops through the ascii
        # alphabet to locate the decrypted character - essentially: chr(ord(letter) - ord(key))
        decrypted_chars.append(decrypted_c)  # appends each decrypted character to the decrypted_chars list

    decrypted_string = ''.join(decrypted_chars)  # append all decrypted characters into a single string

    return decrypted_string
