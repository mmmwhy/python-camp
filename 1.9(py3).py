import os, base64
from hashlib import sha256
from hmac import HMAC
def encrypt_password(password, salt=None):
    """Hash password on the fly."""
    if salt is None:
        salt = os.urandom(8)  # 64 bits.
    assert 8 == len(salt)
    assert isinstance(salt, bytes)
    assert isinstance(password, str)
    
    if isinstance(password, str):
        password = password.encode('UTF-8')
    assert isinstance(password, bytes)
    result = password
    for i in range(10):
        result = HMAC(result, salt, sha256).digest()
    return salt + result
def validate_password(hashed, input_password):
    return hashed == encrypt_password(input_password, salt=hashed[:8])
if __name__ == "__main__":
    hashed = encrypt_password('secret password')
    assert validate_password(hashed, 'secret password')
    print (hashed)
    print (base64.b64encode(hashed))
    print (base64.b64decode(base64.b64encode(hashed)))
