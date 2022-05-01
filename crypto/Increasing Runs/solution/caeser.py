global primes
primes=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229]
k=0
def encrypt(text,k,primes):
    result = ""
    # transverse the plain text
    for i in range(len(text)):
        char = text[i]
        # Encrypt uppercase characters in plain text
        print(primes[k])
        if (char.isupper()):
            result += chr((ord(char) + primes[k]-65) % 26 + 65)
            k+=1
        # Encrypt lowercase characters in plain text
        elif (char=='_' or char=='{' or char=='}' or char=='!' ):
            result +=char

        else:
            result += chr((ord(char) + primes[k] - 97) % 26 + 97)
            k+=1

    return result
#check the above function
text = "{Congrats!!!_You_are_our_lucky_winner}"
s = 4

print ("Plain Text : " + text)
print ("Shift pattern : " + str(s))
print ("Cipher: " + encrypt(text,k,primes))