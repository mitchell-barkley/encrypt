# Program Description: ASCII Encryption
# Written By: Mitchell Barkley
# Written On: Aug 18th 2023

# Libraries
import base64

# Functions


def password_encrypt():
    while True:
        text = input("Enter the password to be encrypted: ")
        key = int(input("Enter an integer for the key: "))

        if not isinstance(text, str):
            raise TypeError("Error")
        elif not isinstance(key, int):
            raise TypeError("Error")
        else:
            password = "".join([chr(ord(something) + key) for something in text])
            print()
            print(f"Encrypted password: {password}")
            print()
        continue_pass = input("Press enter to encrypt another password. (End to quit): ").title()
        if continue_pass == "End":
            break
    print()


def base_64():
    while True:
        word = input("Enter the string to be encrypted: ")
        if word == "":
            print("Error - Cannot be left blank.")

        word_bytes = word.encode("ascii")

        base64_bytes = base64.b64encode(word_bytes)
        base64_string = base64_bytes.decode("ascii")

        print(f"Base 64 Encrypted string: {base64_string}")
        print()
        continue_64 = input("Press enter to encrypt another string to Base64 (End to quit): ").title()
        if continue_64 == "End":
            break
    print()


def caesar_encrypt():
    while True:
        word = input("Enter the string to be encrypted: ")
        if word == "":
            print("Error - Cannot be left blank.")
        key = int(input("Enter the Key: "))

        result = ""
        for i in word:
            if i.isupper():
                result += chr((ord(i) + key - 65) % 26 + 65)
            else:
                result += chr((ord(i) + key - 97) % 26 + 97)

        print(f"Caesar Encrypted string: {result}")
        print()
        continue_cae = input("Press enter to encrypt another string to Caesar (End to quit): ").title()
        if continue_cae == "End":
            break
    print()


def hex_encrypt():
    while True:
        word = input("Enter the string to be encrypted: ")
        if word == "":
            print("Error - Cannot be left blank.")

        finished = ""
        h_word = ""
        length = len(word)
        for i in range(0, length):
            if word[i] == " ":
                h_word = "20"
            elif word[i] == "!":
                h_word = "21"
            elif word[i] == "#":
                h_word = "22"
            elif word[i] == "$":
                h_word = "23"
            elif word[i] == "%":
                h_word = "24"
            elif word[i] == "&":
                h_word = "25"
            elif word[i] == "'":
                h_word = "26"
            elif word[i] == "(":
                h_word = "27"
            elif word[i] == ")":
                h_word = "28"
            elif word[i] == "*":
                h_word = "29"
            elif word[i] == "+":
                h_word = "2A"
            elif word[i] == ",":
                h_word = "2B"
            elif word[i] == "-":
                h_word = "2C"
            elif word[i] == ".":
                h_word = "2D"
            elif word[i] == "/":
                h_word = "2E"
            elif word[i] == "0":
                h_word = "2F"
            elif word[i] == "1":
                h_word = "30"
            elif word[i] == "2":
                h_word = "31"
            elif word[i] == "3":
                h_word = "32"
            elif word[i] == "4":
                h_word = "33"
            elif word[i] == "5":
                h_word = "34"
            elif word[i] == "5":
                h_word = "35"
            elif word[i] == "6":
                h_word = "36"
            elif word[i] == "7":
                h_word = "37"
            elif word[i] == "8":
                h_word = "38"
            elif word[i] == "9":
                h_word = "39"
            elif word[i] == ":":
                h_word = "3A"
            elif word[i] == ";":
                h_word = "3B"
            elif word[i] == "<":
                h_word = "3C"
            elif word[i] == "=":
                h_word = "3D"
            elif word[i] == ">":
                h_word = "3E"
            elif word[i] == "?":
                h_word = "3F"
            elif word[i] == "@":
                h_word = "40"
            elif word[i] == "A":
                h_word = "41"
            elif word[i] == "B":
                h_word = "42"
            elif word[i] == "C":
                h_word = "43"
            elif word[i] == "D":
                h_word = "44"
            elif word[i] == "E":
                h_word = "45"
            elif word[i] == "F":
                h_word = "46"
            elif word[i] == "G":
                h_word = "47"
            elif word[i] == "H":
                h_word = "48"
            elif word[i] == "I":
                h_word = "49"
            elif word[i] == "J":
                h_word = "4A"
            elif word[i] == "K":
                h_word = "4B"
            elif word[i] == "L":
                h_word = "4C"
            elif word[i] == "M":
                h_word = "4D"
            elif word[i] == "N":
                h_word = "4E"
            elif word[i] == "O":
                h_word = "4F"
            elif word[i] == "P":
                h_word = "50"
            elif word[i] == "Q":
                h_word = "51"
            elif word[i] == "R":
                h_word = "52"
            elif word[i] == "S":
                h_word = "53"
            elif word[i] == "T":
                h_word = "54"
            elif word[i] == "U":
                h_word = "55"
            elif word[i] == "V":
                h_word = "56"
            elif word[i] == "W":
                h_word = "57"
            elif word[i] == "X":
                h_word = "58"
            elif word[i] == "Y":
                h_word = "59"
            elif word[i] == "Z":
                h_word = "5A"
            elif word[i] == "[":
                h_word = "5B"
            elif word[i] == "^":
                h_word = "5C"
            elif word[i] == "_":
                h_word = "5D"
            elif word[i] == "`":
                h_word = "5E"
            elif word[i] == "a":
                h_word = "5F"
            elif word[i] == "b":
                h_word = "60"
            elif word[i] == "c":
                h_word = "61"
            elif word[i] == "d":
                h_word = "62"
            elif word[i] == "e":
                h_word = "63"
            elif word[i] == "f":
                h_word = "64"
            elif word[i] == "g":
                h_word = "65"
            elif word[i] == "h":
                h_word = "66"
            elif word[i] == "i":
                h_word = "67"
            elif word[i] == "j":
                h_word = "68"
            elif word[i] == "k":
                h_word = "69"
            elif word[i] == "l":
                h_word = "6A"
            elif word[i] == "m":
                h_word = "6B"
            elif word[i] == "n":
                h_word = "6C"
            elif word[i] == "o":
                h_word = "6D"
            elif word[i] == "p":
                h_word = "6E"
            elif word[i] == "q":
                h_word = "6F"
            elif word[i] == "r":
                h_word = "70"
            elif word[i] == "s":
                h_word = "71"
            elif word[i] == "t":
                h_word = "72"
            elif word[i] == "u":
                h_word = "73"
            elif word[i] == "v":
                h_word = "74"
            elif word[i] == "w":
                h_word = "75"
            elif word[i] == "x":
                h_word = "76"
            elif word[i] == "y":
                h_word = "77"
            elif word[i] == "z":
                h_word = "78"
            elif word[i] == "{":
                h_word = "79"
            elif word[i] == "|":
                h_word = "7A"
            elif word[i] == "}":
                h_word = "7B"
            finished = finished + h_word

        print()
        print(f"Encrypted string: {finished}")
        print()
        continue_hex = input("Press enter to encrypt another string to Hexadecimal (End to quit): ").title()
        if continue_hex == "End":
            break
    print()


def binary_encrypt():
    while True:
        word = input("Enter the string to be encrypted: ")
        if word == "":
            print("Error - Cannot be left blank.")

        finished = ""
        h_word = ""
        length = len(word)
        for i in range(0, length):
            if word[i] == " ":
                h_word = "00100000"
            elif word[i] == "!":
                h_word = "00100001"
            elif word[i] == "#":
                h_word = "00100010"
            elif word[i] == "$":
                h_word = "00100011"
            elif word[i] == "%":
                h_word = "00100100"
            elif word[i] == "&":
                h_word = "00100101"
            elif word[i] == "'":
                h_word = "00100110"
            elif word[i] == "(":
                h_word = "00100111"
            elif word[i] == ")":
                h_word = "00101000"
            elif word[i] == "*":
                h_word = "00101001"
            elif word[i] == "+":
                h_word = "00101010"
            elif word[i] == ",":
                h_word = "00101011"
            elif word[i] == "-":
                h_word = "00101100"
            elif word[i] == ".":
                h_word = "00101101"
            elif word[i] == "/":
                h_word = "00101110"
            elif word[i] == "0":
                h_word = "00101111"
            elif word[i] == "1":
                h_word = "00110000"
            elif word[i] == "2":
                h_word = "00110001"
            elif word[i] == "3":
                h_word = "00110010"
            elif word[i] == "4":
                h_word = "00110011"
            elif word[i] == "5":
                h_word = "00110100"
            elif word[i] == "5":
                h_word = "00110101"
            elif word[i] == "6":
                h_word = "00110110"
            elif word[i] == "7":
                h_word = "00110111"
            elif word[i] == "8":
                h_word = "00111000"
            elif word[i] == "9":
                h_word = "00111001"
            elif word[i] == ":":
                h_word = "00111010"
            elif word[i] == ";":
                h_word = "00111011"
            elif word[i] == "<":
                h_word = "00111100"
            elif word[i] == "=":
                h_word = "00111101"
            elif word[i] == ">":
                h_word = "00111110"
            elif word[i] == "?":
                h_word = "00111111"
            elif word[i] == "@":
                h_word = "01000000"
            elif word[i] == "A":
                h_word = "01000001"
            elif word[i] == "B":
                h_word = "01000010"
            elif word[i] == "C":
                h_word = "01000011"
            elif word[i] == "D":
                h_word = "01000100"
            elif word[i] == "E":
                h_word = "01000101"
            elif word[i] == "F":
                h_word = "01000110"
            elif word[i] == "G":
                h_word = "01000111"
            elif word[i] == "H":
                h_word = "01001000"
            elif word[i] == "I":
                h_word = "01001001"
            elif word[i] == "J":
                h_word = "01001010"
            elif word[i] == "K":
                h_word = "01001011"
            elif word[i] == "L":
                h_word = "01001100"
            elif word[i] == "M":
                h_word = "01001101"
            elif word[i] == "N":
                h_word = "01001111"
            elif word[i] == "O":
                h_word = "01010000"
            elif word[i] == "P":
                h_word = "01010001"
            elif word[i] == "Q":
                h_word = "01010010"
            elif word[i] == "R":
                h_word = "01010011"
            elif word[i] == "S":
                h_word = "01010100"
            elif word[i] == "T":
                h_word = "01010101"
            elif word[i] == "U":
                h_word = "01010110"
            elif word[i] == "V":
                h_word = "01010111"
            elif word[i] == "W":
                h_word = "01011000"
            elif word[i] == "X":
                h_word = "01011001"
            elif word[i] == "Y":
                h_word = "01011010"
            elif word[i] == "Z":
                h_word = "01011011"
            elif word[i] == "[":
                h_word = "01011100"
            elif word[i] == "^":
                h_word = "01011101"
            elif word[i] == "_":
                h_word = "01011110"
            elif word[i] == "`":
                h_word = "01011111"
            elif word[i] == "a":
                h_word = "01100000"
            elif word[i] == "b":
                h_word = "01100001"
            elif word[i] == "c":
                h_word = "01100010"
            elif word[i] == "d":
                h_word = "01100011"
            elif word[i] == "e":
                h_word = "01100100"
            elif word[i] == "f":
                h_word = "01100101"
            elif word[i] == "g":
                h_word = "01100110"
            elif word[i] == "h":
                h_word = "01100111"
            elif word[i] == "i":
                h_word = "01101000"
            elif word[i] == "j":
                h_word = "01101001"
            elif word[i] == "k":
                h_word = "01101010"
            elif word[i] == "l":
                h_word = "01101011"
            elif word[i] == "m":
                h_word = "01101100"
            elif word[i] == "n":
                h_word = "01101101"
            elif word[i] == "o":
                h_word = "01101110"
            elif word[i] == "p":
                h_word = "01101111"
            elif word[i] == "q":
                h_word = "01110000"
            elif word[i] == "r":
                h_word = "01110001"
            elif word[i] == "s":
                h_word = "01110010"
            elif word[i] == "t":
                h_word = "01110011"
            elif word[i] == "u":
                h_word = "01110100"
            elif word[i] == "v":
                h_word = "01110101"
            elif word[i] == "w":
                h_word = "01110110"
            elif word[i] == "x":
                h_word = "01110111"
            elif word[i] == "y":
                h_word = "01111000"
            elif word[i] == "z":
                h_word = "01111001"
            elif word[i] == "{":
                h_word = "01111010"
            elif word[i] == "|":
                h_word = "01111011"
            elif word[i] == "}":
                h_word = "01111100"
            finished = finished + h_word + "\n"

        print()
        print(f"Encrypted string: \n{finished}")
        print()
        continue_bin = input("Press enter to encrypt another string to Hexadecimal (End to quit): ").title()
        if continue_bin == "End":
            break
    print()


def oct_encrypt():
    while True:
        word = input("Enter the string to be encrypted: ")
        if word == "":
            print("Error - Cannot be left blank.")

        finished = ""
        h_word = ""
        length = len(word)
        for i in range(0, length):
            if word[i] == " ":
                h_word = "40"
            elif word[i] == "!":
                h_word = "041"
            elif word[i] == "#":
                h_word = "042"
            elif word[i] == "$":
                h_word = "043"
            elif word[i] == "%":
                h_word = "044"
            elif word[i] == "&":
                h_word = "045"
            elif word[i] == "'":
                h_word = "046"
            elif word[i] == "(":
                h_word = "047"
            elif word[i] == ")":
                h_word = "050"
            elif word[i] == "*":
                h_word = "051"
            elif word[i] == "+":
                h_word = "052"
            elif word[i] == ",":
                h_word = "053"
            elif word[i] == "-":
                h_word = "054"
            elif word[i] == ".":
                h_word = "055"
            elif word[i] == "/":
                h_word = "056"
            elif word[i] == "0":
                h_word = "057"
            elif word[i] == "1":
                h_word = "060"
            elif word[i] == "2":
                h_word = "061"
            elif word[i] == "3":
                h_word = "062"
            elif word[i] == "4":
                h_word = "063"
            elif word[i] == "5":
                h_word = "064"
            elif word[i] == "5":
                h_word = "065"
            elif word[i] == "6":
                h_word = "066"
            elif word[i] == "7":
                h_word = "067"
            elif word[i] == "8":
                h_word = "070"
            elif word[i] == "9":
                h_word = "071"
            elif word[i] == ":":
                h_word = "072"
            elif word[i] == ";":
                h_word = "073"
            elif word[i] == "<":
                h_word = "074"
            elif word[i] == "=":
                h_word = "075"
            elif word[i] == ">":
                h_word = "076"
            elif word[i] == "?":
                h_word = "077"
            elif word[i] == "@":
                h_word = "100"
            elif word[i] == "A":
                h_word = "101"
            elif word[i] == "B":
                h_word = "102"
            elif word[i] == "C":
                h_word = "103"
            elif word[i] == "D":
                h_word = "104"
            elif word[i] == "E":
                h_word = "105"
            elif word[i] == "F":
                h_word = "106"
            elif word[i] == "G":
                h_word = "107"
            elif word[i] == "H":
                h_word = "110"
            elif word[i] == "I":
                h_word = "111"
            elif word[i] == "J":
                h_word = "112"
            elif word[i] == "K":
                h_word = "113"
            elif word[i] == "L":
                h_word = "114"
            elif word[i] == "M":
                h_word = "115"
            elif word[i] == "N":
                h_word = "116"
            elif word[i] == "O":
                h_word = "117"
            elif word[i] == "P":
                h_word = "120"
            elif word[i] == "Q":
                h_word = "121"
            elif word[i] == "R":
                h_word = "122"
            elif word[i] == "S":
                h_word = "123"
            elif word[i] == "T":
                h_word = "124"
            elif word[i] == "U":
                h_word = "125"
            elif word[i] == "V":
                h_word = "126"
            elif word[i] == "W":
                h_word = "127"
            elif word[i] == "X":
                h_word = "130"
            elif word[i] == "Y":
                h_word = "131"
            elif word[i] == "Z":
                h_word = "132"
            elif word[i] == "[":
                h_word = "133"
            elif word[i] == "^":
                h_word = "134"
            elif word[i] == "_":
                h_word = "135"
            elif word[i] == "`":
                h_word = "136"
            elif word[i] == "a":
                h_word = "137"
            elif word[i] == "b":
                h_word = "140"
            elif word[i] == "c":
                h_word = "141"
            elif word[i] == "d":
                h_word = "142"
            elif word[i] == "e":
                h_word = "143"
            elif word[i] == "f":
                h_word = "144"
            elif word[i] == "g":
                h_word = "145"
            elif word[i] == "h":
                h_word = "146"
            elif word[i] == "i":
                h_word = "147"
            elif word[i] == "j":
                h_word = "150"
            elif word[i] == "k":
                h_word = "151"
            elif word[i] == "l":
                h_word = "152"
            elif word[i] == "m":
                h_word = "153"
            elif word[i] == "n":
                h_word = "154"
            elif word[i] == "o":
                h_word = "155"
            elif word[i] == "p":
                h_word = "156"
            elif word[i] == "q":
                h_word = "157"
            elif word[i] == "r":
                h_word = "160"
            elif word[i] == "s":
                h_word = "161"
            elif word[i] == "t":
                h_word = "162"
            elif word[i] == "u":
                h_word = "163"
            elif word[i] == "v":
                h_word = "164"
            elif word[i] == "w":
                h_word = "165"
            elif word[i] == "x":
                h_word = "166"
            elif word[i] == "y":
                h_word = "167"
            elif word[i] == "z":
                h_word = "170"
            elif word[i] == "{":
                h_word = "171"
            elif word[i] == "|":
                h_word = "172"
            elif word[i] == "}":
                h_word = "173"
            finished = finished + h_word

        print()
        print(f"Encrypted string: {finished}")
        print()
        continue_oct = input("Press enter to encrypt another string to Octal (End to quit): ").title()
        if continue_oct == "End":
            break
    print()
    print()


# Main
print()
while True:
    print("    ASCII ENCRYPTION PROGRAM")
    print()
    print("    CHOOSE YOUR ENCRYPTION/DECRYPTION METHOD")
    print()
    print("1 - ASCII Key Encryption")
    print("2 - Base 64 Encryption")
    print("3 - Caesar Encryption")
    print("4 - Hexadecimal Encryption")
    print("5 - Binary Encryption")
    print("6 - Octal Encryption")
    print("7 - QUIT PROGRAM")
    print()
    menu = input("Please select an option (1-7): ")
    print()

    if menu == "1":
        option = password_encrypt()
    elif menu == "2":
        option = base_64()
    elif menu == "3":
        option = caesar_encrypt()
    elif menu == "4":
        option = hex_encrypt()
    elif menu == "5":
        option = binary_encrypt()
    elif menu == "6":
        option = oct_encrypt()
    elif menu == "7":
        break
