from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("secret.key", "rb").read()

def encrypt_file(file_name, key):
    f = Fernet(key)
    with open(file_name, "rb") as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(file_name, "wb") as file:
        file.write(encrypted_data)

def decrypt_file(file_name, key):
    f = Fernet(key)
    with open(file_name, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(file_name, "wb") as file:
        file.write(decrypted_data)

generate_key()
key = load_key()

choice = input("Would you like to encrypt or decrypt a file? ").lower()
file_name = input("Enter the name of the file to encrypt: ")

if choice == "e":
    encrypt_file(file_name, key)
    print(f"File '{file_name}' has been encrypted!")
elif choice == "d":
    decrypt_file(file_name, key)
    print(f"File '{file_name}' has been decrypted!")
else:
    print("Invalid choice. Please try again.")