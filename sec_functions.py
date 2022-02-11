from main import *
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet, InvalidToken
import base64


class SECFunctions(MainWindow):
    def __init__(self,MainWindow):
        self.Main = MainWindow
        print('SECFunctions Successfully Loads')


    def genpwKey(self, PW):
        password = PW.encode("utf-8")  
        salt = b'SF93533FE44CFD9E25439F4D22DE5FFDF93533FE44CFD9E25439F4D22DE5FFD34DAE74D57C9A4F29EC4CD534C5453575AD9DC2E397725744755DC7474AF437D95FFE7A2DC9FF9929EFF4F92CDEF2CC7C34DAE74D57C9A4F29EC4CD534C5453575AD9DC2E397725744755DC7474AF437D95FFE7A2DC9FF9929EFF4F92CDEF2CC7C'
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        self.PWKEY = base64.urlsafe_b64encode(kdf.derive(password))



    def encryptstr(self, PW, KEY):
        self.genpwKey(PW)
        a = Fernet(self.PWKEY)
        return a.encrypt(KEY.encode())
        


    def decryptstr(self, PW, ENCRYPTKEY):
        self.genpwKey(PW)
        try:
            plaintext = Fernet(self.PWKEY).decrypt(ENCRYPTKEY)
            return True, plaintext.decode()
        except Exception as e:
            print(e)
            return False, e


