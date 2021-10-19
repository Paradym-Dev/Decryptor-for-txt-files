from cryptography.fernet import Fernet

with open(".\\Config\\Enc.key", "rb") as Enc:
    key = Enc.read()
f = Fernet(key)
with open('.\\Config\\enc_db.txt', 'rb') as encrypted_file:
    encrypted = encrypted_file.read()
decrypted = f.decrypt(encrypted)
with open('.\\Config\\dec_db.txt', 'wb') as decrypted_file:
    decrypted_file.write(decrypted)
