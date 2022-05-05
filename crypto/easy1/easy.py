from string import ascii_uppercase as letters

key = "IWILLNOTPLAYIPL"

encryptedFlag = "KKINSRGWDYTNTPJ"

flag= "COACHESDONTPLAY"
# flag="CRYPTOISFUN"
alphabet = []
for i in letters:
    alphabet.append(i)

solvedFlag = []

for v, k in zip(encryptedFlag, key):
    sol = alphabet[(alphabet.index(v) - alphabet.index(k))]
    solvedFlag.append(sol)

print("picoCTF{" + ''.join(solvedFlag) + "}")


#encryptedFlag - key = FLAG