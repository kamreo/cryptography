from cryptography.fernet import Fernet
class Cryptography:
    def gen_sym_key():
        return Fernet.generate_key()