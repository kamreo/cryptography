from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import json 

class Cryptography:

    def __init__(self):
        self = self
        
    def gen_sym_key():
        return hex(Fernet.generate_key())
    
    def set_sym_key(key):
        file = open("sym.txt","w")
        file.write(key)
        file.close()

    def get_sym_key(self):
        file = open("sym.txt","r")
        key = fromhex(file.readline())
        file.close()
        return Fernet(key)

    def encrypt_sym(self, message):
        key = self.get_sym_key()
        return key.encrypt(message)
    
    def decrypt_sym(self, message):
        key = self.get_sym_key()
        return key.decrypt(message)

    def gen_asym_key(self):
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        public_key = private_key.public_key()
        keys = {
            "private_key" : hex(private_key),
            "public_key" :  hex(public_key)
        }
        json_data  =json.dumps(keys)
        self.set_asym_keys(json_data)
        return json_data

    def set_asym_keys(keys_val):
        keys = json.load(keys_val)
        private_key = fromhex(keys["private_key"])
        public_key = fromhex(keys["public_key"])

        pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )

        with open('private_key.pem', 'wb') as f:
            f.write(pem)

        pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

        with open('public_key.pem', 'wb') as f:
            f.write(pem)


    def get_asym_pub_key(self):
        with open("public_key.pem", "rb") as key_file:
            public_key = serialization.load_pem_public_key(
                key_file.read(),
                backend=default_backend()
            )
        return public_key

    def get_asym_private_key(self):
        with open("private_key.pem", "rb") as key_file:
            private_key = serialization.load_pem_private_key(
                key_file.read(),
                password=None,
                backend=default_backend()
            )
        return private_key

    def encrypt_asym(self, message):
        public_key = self.get_asym_pub_key()
        encrypted = public_key.encrypt(
            message,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return encrypted
    
    def decrypt_sym(self, encrypted):
        private_key = self.get_asym_private_key()

        original_message = private_key.decrypt(
            encrypted,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return original_message