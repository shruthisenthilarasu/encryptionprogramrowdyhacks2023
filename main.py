import random
import string
chars = string.punctuation + string.ascii_letters + " " + string.digits


chars = list(chars)
key = chars.copy()

random.shuffle(key)
#encrypt = input("what do you want to encrypt: ")
#decrypt = input("what do you want to decrypy: ")
#decision= input ("do you want to encrypt or decrypt: ")
#print (chars)
print("key is below")
print ("".join(key))
# encrypt






def encrypt(plain_text, cipher_text):
  for letter in plain_text: 
    index = chars.index(letter)
    cipher_text += key[index]
    print(f"{index}")
    #dictionary[]
  print(f"original message: {plain_text}")
  print(f" encrypted message: {cipher_text}")

  #decrypt
def decrypt(cipher_text, key):
  plain_text = ""
            
  for letter in cipher_text: 
    index = key.index(letter)
    plain_text += chars[index]
  print(f" encrypted message: {cipher_text}")    
  print(f"original message: {plain_text}")
    
answerValid = False
while not answerValid:
 #print(f"chars: {chars}")
        #print(f"key: {key}")
        #decrypt = input ("what do you want to decrypt: ")
  dicision= input ("Do you want to encrypt or decrypt: ")


  if dicision.upper() == "ENCRYPT":
    answerValid = True
  #encrypt = input("what do you want to encrypt: ")
    plain_text = input("Enter message to encrypt: ")
    cipher_text = ""
    encrypt(plain_text, cipher_text)
    
  
 
  #       #decrypt
  elif dicision.upper() == "DECRYPT":
    answerValid = True
    encryption_key = input("Enter encryption key: ")
  # encryption_key = "f]$1Vy-JcA@X5n2hK8,~pRq7(o6rLTI0)9!=Dsj+vH3i\"QS;M4bz>&#etlF|.{*Um\BOd:^'WG/Y}Nu[ZCx_P<gwa%k`E?"
    cipher_text = input("Enter message to decrypt: ")
    decrypt(cipher_text, encryption_key)        

  else:
    print("Try Again")

