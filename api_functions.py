from main import *
import requests, json, qrcode
from io import BytesIO


class APIFunctions(MainWindow):
    def __init__(self,MainWindow):
        self.Main = MainWindow
        print('APIFunctions Successfully Loads')
        
    def getABI(self, address):
        url =  str('https://api.bscscan.com/api?module=contract&action=getabi&address=') + str(address)
        ABI = requests.get(url).json()['result']
        return ABI

    def getBNBPrice(self):
        res = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=binancecoin&vs_currencies=usd')
        j = json.loads(str(res.text))
        bnbprice = j['binancecoin']['usd']
        return bnbprice

    def getTXList(self,address):
        url = f"https://api.bscscan.com/api?module=account&action=txlist&address={address}&startblock=0&endblock=99999999&page=1&offset=50&sort=desc"
        res = requests.get(url).content
        jres = json.loads(res)["result"]
        return jres

    def getImage(self,url):
        res = requests.get(url)
        if not str(404) in str(res):
            data = res.content
            return data
        else:
            error # We want a error here for fallback, need better solution to handle with github, but first works.


    def getQRImage(self,address):
        qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=7,
        border=4,
        )
        qr.add_data(address)
        qr.make()
        qrc = qr.make_image(fill_color='#dba006',back_color='#21252b')
        buffered = BytesIO()
        qrc.save(buffered, format="PNG")
        img_str = buffered.getvalue()
        return img_str
