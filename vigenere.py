#Philip Wells
#COSC 4367.001
#Homework #2
#Date of Submission 09/17/2023


def checkKeyFormatting(key):
    if key.isupper() == 0:
        raise Exception("Error: Key is not in uppercase format.")

    if key.isalpha() == 0:
        raise Exception('Error: Key contains character(s) that are NOT letters.')

def generateKey(plaintext,key): #function to iterate key until the length is equal to the length of the plaintext
    key = list(key)
    if len(key) == len(plaintext): #if key length matches plaintext length already, returns key
        return key
    else:
        for i in range (len(plaintext) - len(key)): #else, append key onto the end of itself until it reaches length of plaintext
            key.append(key[i % len(key)])
    return('' . join(key))
            
    
def encrypt(plaintext, key) :
    
    altPlaintext = '' #empty string to place values from plaintext that are letters
    for i in plaintext:
        if ord(i) in range(97,123) or ord(i) in range(65,91): #check ith character in plaintext, and if letter, add to emtpy string 
            altPlaintext += i
    plaintext = altPlaintext #changing original plaintext to updated 'letter-only' plaintext   
    if plaintext.isupper() == 0 : #checks for all characters to be uppercase
        plaintext = plaintext.upper() #converts the plaintext to uppercase if not already
    
    ciphertext = ''
    for i in range(len(plaintext)): 
        c = ord(plaintext[i]) + (ord(key[i]) - ord('A')) #adding ascii values of ith character in key and plaintext to get ciphertext
        if c > ord('Z'): #checking ascii value to ensure returned ciphertext value is A - Z
            c = c - 26

        ciphertext += chr(c)

    return ciphertext
        

def decrypt(ciphertext, key):

    if ciphertext.isalpha() == 0:
        raise Exception('Error: Ciphertext conatins non-letter characters')
    
    plaintext = ''
    for i in range(len(ciphertext)): 
        p = ord(ciphertext[i]) - (ord(key[i]) - ord('A')) #subtracting of ascii values of ith character in key and ciphertext to get ciphertext
        if p <  ord('A'): #checking ascii value to ensure returned plaintext value is A - Z
            p = p + 26

        plaintext += chr(p)

    return plaintext
        


if __name__ == '__main__' :

    plaintext = input("Please enter your message to encrypt: ")
    keyword = input("Please enter a single word in uppercase letters to use for our key: ")
    
    checkKeyFormatting(keyword)

    key = generateKey(plaintext,keyword)

    ciphertext = encrypt(plaintext,key)
    print("Ciphertext: ", ciphertext)

    originalText = decrypt(ciphertext,key)
    print("Decrypted message: " , originalText)


    
    
    
    
