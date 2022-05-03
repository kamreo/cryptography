from cryptography import Cryptography
from fastapi import FastAPI
from . import Cryptography
from pydantic import BaseModel

class Body(BaseModel):
    value: str


app = FastAPI()
cryptography = Cryptography()

#symetric

@app.get("/symetric/key")
def generate_symetric_key():
    """Returns randomly generated symetric key as HEX"""
    return Cryptography.gen_sym_key()

@app.post("/symetric/key/")
def set_symetric_key(body: Body):
    """Sets given symetric HEX key on a server"""
    return Cryptography.set_sym_key(body.value)

@app.post("/symetric/encode")
def encode_message_symmetric(body: Body):
    """Accepts message and returns encrypted string as a response"""
    return cryptography.encrypt_sym(body.value)

@app.post("/symetric/decode")
def decode_message_symmetric(body: Body):
    """Accepts encrypted message and returns decrypted one"""
    return cryptography.decrypt_sym(body.value)

#asymetric

@app.get("/asymetric/key")
def generate_asymetric_key():
    """Returns new public and private key as HEX and sets it on server"""
    return cryptography.gen_asym_key()

@app.post("/asymetric/key")
def set_asymetric_key(body: Body):
    """sets given public and private key on server as HEX"""
    return Cryptography.set_asym_keys(body.value)

@app.post("/asymetric/encode")
def decode_message_symmetric(body: Body):
    """encrypts given message"""
    return cryptography.encrypt_asym(body.value)

@app.post("/asymetric/decode")
def decode_message_symmetric(body: Body):
    """decrypts given message"""
    return cryptography.decrypt_asym(body.value)
