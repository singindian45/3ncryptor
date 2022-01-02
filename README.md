Mysterybox.py is the main program.
How to use:

1)First put all files(mysterybox.py,encryptionkey.txt,dictionary.txt,encryptionkeylist.txt) in a common folder.

2)Run the program 

3)You will now be prompted to enter either 0,1,2,3,4

DO NOT ENTER OPTIONS 2 AND 3 AS THEY ARE STILL UNDER DEVELOPMENT

4)If you have chosen 0 then you wish to encrypt a particular file.You may choose any text file.But if this file contains any new characters which are not already present in dictionary.txt 
then it will throw an error.The reason is that even though the updater fucntion updates dictionary.txt the changes are not saved until the program stops.Hence running the program a second time will solve the problem.

5)the encryption key generated will be saved in "encryptionkeylist.txt".You may use this for decryption

6)If you have chosen 1 then you wish to decrypt a file. Copy the encryption key from "encryptionkeylist.txt" and paste it
into "encryptionkey.txt" without any extra characters(including spaces). Eg (ajsahskashkahsa) --> correct, (ajsahskashkahsa  ) --> wrong

7) ALWAYS COPY THE LATEST ENCRYPTION KEY ASSOCIATED WITH YOUR FILE. (Using a different encryption key will destroy all your data)

8) In the event that any mistake occurs during encryption or decryption and data has been lost,There is an option in encrypt() to manually encrypt the file using the encrption key of your choice.
This will allow you to retrace all the changes made.

9)Choose 4 to quit from the program.
