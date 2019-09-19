'''
    encrypts a message using the caesar cipher and prints
    the encrypted message
'''
def encrypt_caesar():
    plain_txt = input('Enter a one-word, lowercase message: ')
    distance = int(input('Enter the distance value: '))
    code = ''
    
    # loop through each character in the message
    for ch in plain_txt:
        # grab the ordinal value of the current character
        ordinal_val = ord(ch)
        # add the input distance to the ordinal value
        cipher_val = ordinal_val + distance
        
        # make sure cipher_val remains a lowercase letter
        if cipher_val > ord('z'):
            cipher_val = ord('a') + distance - (ord('z') - ordinal_val+1)
        
        # store the encrypted character
        code += chr(cipher_val)
        
    print(code)
    

'''
    decrypts a message using the caesar cipher and prints
    the decrypted message
'''
def decrypt_caesar():
    code = input('Enter the coded text: ')
    distance = int(input('Enter the distance value: '))
    plain_txt = ''
    
    for ch in code:
        ord_val = ord(ch)
        cipher_val = ord_val - distance
        
        if cipher_val < ord('a'):
            cipher_val = ord('z') - (distance - (ord('a') - ord_val-1))
        
        plain_txt += chr(cipher_val)
    
    print(plain_txt)
    

def main():
    encrypt_caesar()
    decrypt_caesar()


if __name__ == '__main__':
    main()