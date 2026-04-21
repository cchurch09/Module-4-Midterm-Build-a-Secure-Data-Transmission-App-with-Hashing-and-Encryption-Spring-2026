1.Write a short explanation describing how their solution upholds confidentiality, integrity, and availability
2.Explain the role of entropy and key generation in their implementation

1. Within the code it uses AES encryption which is part of the confindentiality portion of CIA. As it ensures only a person with the key can read the message. On line 11 I use SHA 256 hashing to ensure the integrity of the code by comparing the hashes to ensure that they are the same. Then finally for the Availibilty it ensures only authorized users are able to obtain the data by the data is decrypted with the correct key.

2. Within that Fernet we have the Entropy that helps ensures that the code is getting a random key
making sure that encryption can be unpredictable. Then for the key generations is ensuring that  we
can make sure of the random number generator ensuring that the information is harder to hack into.