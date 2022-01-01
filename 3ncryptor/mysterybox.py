import random as r
def converter(a):
    with open(a,"r") as f:
        f = list(f.read())
        for i in reversed(range(len(f))):
            if f[i] == '\\':
                if f[i+1] == 'n':
                    f[i] = '\n'
                    f[i+1] = '`'
                    f.remove('`')
                    break
        for j in reversed(range(len(f))):
            if f[j] == '\\':
                if f[j+1] == 't':
                    f[j] = '\t'
                    f[j+1] = '`'
                    f.remove('`')
                    break
        return f

def updater(dictionary,text,d): #Updates the file "dictionary.txt" which contains all possible characters.If this program is passed a file with new characters it updates dictionary.txt.
    with open(d,"a") as j:
        garbage_bin = []
        for i in range(len(text)):
            if text[i] not in dictionary:
                if text[i] not in garbage_bin:
                    garbage_bin.append(text[i])
                    j.write(text[i])
def keygen(filename,dicti1):            #It loads all the elements in dictionary.txt into a list and randomizes this list to produce the encryption key which is then saved in a file called "encryptionkeys.txt"(different from "encryptionkey.txt")
    alpha = dicti1
    copy = alpha[:-2]
    r.shuffle(copy)
    alpha[:-2] = copy
    alpha = "".join(alpha)
    with open("encryptionkeylist.txt","a") as f:
        f.write(filename + " : " + alpha + "\n\n\n")
    return list(alpha)

def encrypt(a,b,dicti,dicti1):                  #this will read the file that you wish to encrypt and put it into a list in the same order.Then compares the encryption key provided and the list from dictionary.txt
    if b == 0:                                  #and replaces characters in the file of some index in the list with their corresponding value in the encryptionkey like ( a,b,c,d,e,f) ---> (b,f,,e,a,d,c)
        print("Enter encryption key into encryptionkey.txt\n")                                                                                                          
        choice_3 = int(input("press 1 if you have done so"))
        if choice_3 == 1:
            key = converter("encryptionkey.txt")
    if b == 1:
        print("Generating encryption keys.....")
        key = keygen(a,dicti1)
    with open(a,"r") as fp:
        fp = fp.read()
        fp = list(fp)
        for i in range(len(fp)):
            try:
                fp[i] = key[dicti.index(fp[i])]
            except IndexError:
                 print(i)
    with open(a,"w") as f:
        f.write("".join(fp))
    print("Your file has now b33n 3ncrpdt!?\n\n")
    print("your encryption key is \n\n %s \n\n do not forget this code.\n\n"%("".join(key)))
    print("YOU WILL FIND THE ENCRYPTION KEY TO YOUR FILE IN 'encrptionkeylist.txt")
def decrypt(a,key,dicti):                       #does the opposite of the previous function( encryption key needs to be pasted in "encryption key.txt" b4 using)
    input("ENTER ENCRYPTION KEY INTO 'encryptionkey.txt\n\nIF YOU HAVE DONE SO PRESS ENTER\n")
    with open(a,"r") as fp:
        fp = fp.read()
        fp = list(fp)
        for i in range(len(fp)):
            try:
                fp[i] = dicti[key.index(fp[i])]
            except ValueError:
                raise Exception("Key invalid")
    with open(a,"w") as f:
        f.write("".join(fp))
    print("y0vr #fil3 has now been decrypted!\n\n")
def main():
    choice =  int(input("Enter\n 0 -->  encryption\n 1 --> decryption\n 2 --> encrypt multiple files\n 3 --> Decrpyt multiple files\n 4 --> Quit\n\n\n DO NOT USE OPTIONS 2 and 3 as they are still under development\n\nENTER INPUT\n"))
    if choice == 0:
            file_name = str(input("Enter txt file that you would like to encrypt or decrypt\n"))
            dicti = converter("dictionary.txt")
            dicti_1 = converter("dictionary.txt")
            text = converter(file_name)
            updater(dicti,text,"dictionary.txt")
            choice_2 = int(input("Would you like to manually encrypt(choose 0) or generate encryption keys(choose 1)?"))
            encrypt(file_name,choice_2,dicti,dicti_1)
            input("PRESS ENTER IF YOU HAVE READ EVERYTHING ABOVE\n\n")
            main()
    if choice == 1:
            file_name = str(input("Enter txt file that you would like to encrypt or decrypt\n"))
            #encryption_key_loc = input("Enter encryption key location")
            dicti = converter("dictionary.txt")
            decrypt(file_name,converter("encryptionkey.txt"),dicti)
            input("PRESS ENTER IF YOU HAVE READ EVERYTHING ABOVE\n\n")
            main()
    if choice == 4:
        print("quitting from program")
        return
main()

    
