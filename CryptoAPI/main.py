from typing import Optional
from fastapi import FastAPI
from . import Cryptography

app = FastAPI()

#symetric

@app.get("/symetric/key")
def generate_symetric_key():
    """Returns randomly generated symetric key as HEX"""
    return {Cryptography.gen_sym_key()}

@app.post("/symetric/key/")
def set_symetric_key():
    """Sets given symetric HEX key on a server"""
    return {"Hello": "World"}

@app.post("/symetric/encode")
def encode_message_symmetric():
    """Accepts message and returns encrypted string as a response"""
    return {"Hello": "World"}

@app.post("/symetric/decode")
def decode_message_symmetric():
    """Accepts encrypted message and returns decrypted one"""
    return {"Hello": "World"}

#asymetric

@app.get("/asymetric/key")
def generate_symetric_key():
    """Returns new public and private key as HEX and sets it on server"""
    return {"Hello": "World"}

@app.get("/asymetric/key/ssh")
def set_symetric_key():
    """returns public and private key as HEX in OpenSSH format"""
    return {"Hello": "World"}

@app.post("/asymetric/key")
def encode_message_symmetric():
    """sets given public and private key on server as HEX"""
    return {"Hello": "World"}

@app.post("/asymetric/verify")
def decode_message_symmetric():
    """using current private key, signs given message and returns it signed"""
    return {"Hello": "World"}

@app.post("/asymetric/sign")
def decode_message_symmetric():
    """using current public key, verifies if given message was encrypted by it"""
    return {"Hello": "World"}

@app.post("/asymetric/encode")
def decode_message_symmetric():
    """encrypts given message"""
    return {"Hello": "World"}

@app.post("/asymetric/decode")
def decode_message_symmetric():
    """decrypts given message"""
    return {"Hello": "World"}






@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
