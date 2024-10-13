import os
from cryptography.fernet import Fernet

def load_key():
    return open("C:\\Users\\Administrator\\Downloads\\BT_EthHack-main\\BT_EthHack-main\\encryption_key.key", "rb").read()

def decrypt_file(file_name, key):
    fernet = Fernet(key)
    with open(file_name, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = fernet.decrypt(encrypted_data)
    with open(file_name, "wb") as file:
        file.write(decrypted_data)

def decrypt_directory(directory):
    key = load_key()
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            decrypt_file(file_path, key)

if __name__ == "__main__":
    directory_to_decrypt = r"C:\BT_LT"
    decrypt_directory(directory_to_decrypt)
