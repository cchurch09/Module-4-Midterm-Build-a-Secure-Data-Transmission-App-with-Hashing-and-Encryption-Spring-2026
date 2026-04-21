#Cailli Church
#SDEV245 Spring 2026
#MOD 4 Midterm Build a Secure Data Transmission App with Hashing and Encryption

import hashlib #need to import so I can use the SHA
from cryptography.fernet import Fernet #part of AES
user_message = input("Enter your secert message:    ")   #Accepts user input (e.g., a message or file)
message_bytes = user_message.encode() #converting message

#Hashing portion that will help the I in CIA as it creates that one way value
original_hash = hashlib.sha256(message_bytes).hexdigest()  #Hashes the input using SHA-256 to ensure integrity
print("Orginal SHA-256 Hash:    ")
print(original_hash)

key = Fernet.generate_key()   #talk about in the explanations for later

cipher = Fernet(key)    #ask tutor more about cipher still a little confused 
print("Generated Symmetric Key: ")
print(key.decode())

#Encrypts the input using symmetric encryption (e.g., AES)     
encrypted_message = cipher.encrypt(message_bytes) #portion of the Confidentiality of CIA
print("Ecrypted Message:    ")
print(encrypted_message.decode())

#Decrypts the content and verifies its integrity via hash comparison
decrypted_message= cipher.decrypt(encrypted_message)
print("Decrypted Message:   ")
print(decrypted_message.decode())

#Hashing decryption portion for the one key
decrypted_hash = hashlib.sha256(decrypted_message).hexdigest()
print("Decrypted Message SHA256 Hash:   ")
print(decrypted_hash)

#Making sure hash match. Goes with the intergrity aspect
if original_hash == decrypted_hash:
    print("Verified!")
else:
    print("Warning! Altered Message!")
