import sys
import re 

"""
run this on the command line with the text to be decrypted
"""
    


def decrypt():
    ciphertext = sys.argv[1]
    plain = ""
    temp = [0, 0]
    for i in range(0, 25):
        for j in range(0, 25):
            for k in range(0, 25):
                for l in range(0, 25):
                    key = [i, j, k, l]
                    for el in range(0, ciphertext.len):
                        if(el%2 == 0):
                            temp[0] = ord(ciphertext[el])-97
                            temp[1] = ord(ciphertext[el+1])-97
                            plain += chr(((key[0]*temp[0] + key[1]*temp[1])%26)+97)
                            plain += chr(((key[2]*temp[0] + key[3]*temp[1])%26)+97)


    
        
    
    







if __name__ == "__main__":
    decrypt()
