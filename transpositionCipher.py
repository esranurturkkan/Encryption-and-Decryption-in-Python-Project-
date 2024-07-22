import math

class TranspositionCipher(object):
    def __init__(self, key):
        self.key = key

    def encrypt_message(self, message):
        message_length = len(message)
        
        #Calculate the number of rows needed
        num_rows = math.ceil(message_length / self.key)
        
        #Create a list with enough space to hold the message and any additional padding
        encrypt_message=list(message)
        #Add spaces to the list if necessary to fill the grid
        while len(encrypt_message)< num_rows * self.key:
                encrypt_message+= " "

        encrypted_message_str=""
        
        #Construct the transposition using nested loops
        for col in range(self.key):
            for row in range(num_rows):
                index = row * self.key + col
                encrypted_message_str += encrypt_message[index]
              
        return encrypted_message_str

    def decrypt_message(self, message):
        message_length = len(message)
        
        #Calculate the number of rows needed
        num_rows = math.ceil(message_length / self.key)
        
        decrypt_message_str = ""

        #Construct the transposition using nested loops
        for col in range(num_rows):
            for row in range(self.key):
                index = row * num_rows + col
                decrypt_message_str += message[index]
       
        return decrypt_message_str

#Create an instance of the TranspositionCipher class with a user-defined key
key= int(input("Determine the number of columns you want to use for encryption: "))
cipher = TranspositionCipher(key)

#Encrypt a message
encrypted_messages= input("Enter the message you want to encrypt: ")
encrypted_message = cipher.encrypt_message(encrypted_messages)
print("Encrypted version of your message:", encrypted_message)  

#Decrypt the message
decrypted_message = cipher.decrypt_message(encrypted_message)
print("Decrypted version of your message:", decrypted_message)  