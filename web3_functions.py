from main import *
from web3 import Web3
from datetime import datetime
import secrets
from sha3 import keccak_256
from eth_keys import keys


class WEB3Functions(MainWindow):#MainWindow
    def __init__(self, MainWindow):
        self.Main = MainWindow
        self.setDefaultProvider()
        self.connectToCHAIN()
        self.connect()
        self.WETH = Web3.toChecksumAddress("0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c")#BSC => WBNB
        self.TIGS = Web3.toChecksumAddress("0x34faa80fec0233e045ed4737cc152a71e490e2e3")
        self.BUSD = Web3.toChecksumAddress("0xe9e7cea3dedca5984780bafc599bd69add087d56")
        self.ERC20_ABI = self.Main.db.getSwapABIFromName("ERC20")
        self.PancakeSwap = self.createSwapperInstance("PancakeSwap") # init it for Prices on Wallet overview
        print('WEB3Functions Successfully Loads')
    

    def refreshWEB3(self):
        self.setDefaultProvider()
        self.connectToCHAIN()

    def connectToCHAIN(self):
        if "ws" == str(self.RPC[:2]).lower():
            self.web3 = Web3(Web3.WebsocketProvider(self.RPC))
        elif "http" == str(self.RPC[:4]).lower():
            self.web3 = Web3(Web3.HTTPProvider(self.RPC))
    
    def setDefaultProvider(self):
        self.RPC = self.Main.db.getDefaultPROVIDER()


    def Save_key_to_hex(self, priv):
        self.clearprivKey = priv
        self.privkey = bytes.fromhex(priv)

    def fromWei(self, amount):
        return Web3.fromWei(int(amount), "ether")

    def toWei(self, amount):
        return Web3.toWei(amount, "ether")

    def newWallet(self):
        return keccak_256(secrets.token_bytes(32)).digest().hex()

    def connect(self):
        self.Main.ui.label_Connected.setText(str(self.web3.isConnected()))

    def createSwapperInstance(self, name):
        SWAPPER_ABI = self.Main.db.getSwapABIFromName(name)
        SWAPPER_ADDRESS = self.Main.db.getSwapperAddressFromName(name)
        return self.web3.eth.contract(Web3.toChecksumAddress(SWAPPER_ADDRESS), abi=SWAPPER_ABI)

    def initAccount(self, address):
        self.address = address
        
    def createTokenInstance(self, token):
        return self.web3.eth.contract(Web3.toChecksumAddress(token), abi=self.ERC20_ABI)

    def getETHPrice(self):
        raw_price = self.PancakeSwap.functions.getOutputfromTokentoToken(self.WETH,self.BUSD, 1 * (10**18)).call()[0]
        price = self.fromWei(raw_price)
        return price, raw_price

    def getETHBalance(self):
        raw_balance = self.web3.eth.getBalance(self.address)
        balance = self.fromWei(raw_balance)
        return balance, raw_balance

    def addressfromKey(self, key):
        privat = bytes.fromhex(key)
        public_key_hex = keys.PrivateKey(privat).public_key
        public_key_bytes = bytes.fromhex(str(public_key_hex)[2:])
        public_address = keys.PublicKey(public_key_bytes).to_address()
        return Web3.toChecksumAddress(public_address)

    def getBlockHigh(self):
        return self.web3.eth.block_number   

    def getTIGSUSDPrice(self):
        raw_price = self.PancakeSwap.functions.getOutputfromTokentoToken(self.TIGS, self.BUSD, 1 * (10**18)).call()[0]
        price = self.fromWei(raw_price)
        return price, raw_price 

    def getTokenUSDPrice(self, token):
        raw_price = self.PancakeSwap.functions.getOutputfromTokentoToken(Web3.toChecksumAddress(token), self.BUSD, 1 * (10**self.getTokenDecimal(token))).call()[0]
        price = self.fromWei(raw_price)
        return price, raw_price

    def getTokenBalance(self, token):
        tokeninstance = self.createTokenInstance(token)
        raw_balance = tokeninstance.functions.balanceOf(self.address).call()
        balance = raw_balance / (10**self.getTokenDecimal(token))
        return balance, raw_balance
    
    def getTIGSBalance(self):
        tokeninstance = self.createTokenInstance(self.TIGS)
        raw_balance = tokeninstance.functions.balanceOf(self.address).call()
        balance = self.fromWei(raw_balance)
        return balance, raw_balance

    def getTokenDecimal(self, token):
        tokeninstance = self.createTokenInstance(token)
        decimals = tokeninstance.functions.decimals().call()
        return decimals

    def getTokenName(self, token):
        tokeninstance = self.createTokenInstance(token)
        name = tokeninstance.functions.name().call()
        return name

    def getTokenSymbol(self, token):
        tokeninstance = self.createTokenInstance(token)
        symbol = tokeninstance.functions.symbol().call()
        return symbol

    def estimateGas(self, txn):
        gas = self.web3.eth.estimateGas(txn)
        gas = gas + (gas / 10)
        return gas

    def getTokenPriceETH(self, token_address, swap):
        token_address = self.getChecksumAddress(token_address)
        swapper = self.createSwapperInstance(swap) 
        quantity = 1 * (10**self.getTokenDecimal(token_address))
        call = swapper.functions.getOutputfromTokentoETH(
            token_address,
            int(quantity),
            ).call()
        raw_Amount = call[0] 
        Amount = call[0] / (10**18)
        Way = call[1]
        print(raw_Amount, Amount)
        return Amount, raw_Amount, Way

    def getOutputfromETHtoToken(self, token_address, quantity, swapp):
        token_address = self.getChecksumAddress(token_address)
        swapper = self.createSwapperInstance(swapp) 
        call = swapper.functions.getOutputfromETHtoToken(
            token_address,
            int(quantity * (10**18)),
            ).call()
        raw_Amount = call[0] 
        Amount = call[0] / (10**self.getTokenDecimal(token_address))
        Way = call[1]
        return Amount, raw_Amount, Way

    def getOutputfromTokentoETH(self, token_address, quantity, swapp):
        token_address = self.getChecksumAddress(token_address)
        quantity = quantity * (10**self.getTokenDecimal(token_address))
        swapper = self.createSwapperInstance(swapp) 
        call = swapper.functions.getOutputfromTokentoETH(
            token_address,
            int(quantity),
            ).call()
        raw_Amount = call[0] 
        Amount = call[0] / (10**18)
        Way = call[1]
        return Amount, raw_Amount, Way


    def getOutputfromTokentoToken(self, tokenA, tokenB, quantity, swapp):
        tokenA = self.getChecksumAddress(tokenA)
        tokenB = self.getChecksumAddress(tokenB)
        quantity = quantity * (10**self.getTokenDecimal(tokenA))
        swapper = self.createSwapperInstance(swapp) 
        call = swapper.functions.getOutputfromTokentoToken(
            tokenA,
            tokenB,
            int(quantity),
            ).call()
        raw_Amount = call[0] 
        Amount = call[0] / (10**self.getTokenDecimal(tokenB))
        Way = call[1]
        return Amount, raw_Amount, Way


    def createfromETHtoTokenTX(self, token_address, quantity, swap, slippage, gasPrice):
        print("createfromETHtoTokenTX")
        print("token_address",token_address)
        token_address = self.getChecksumAddress(token_address)
        swapper = self.createSwapperInstance(swap) 
        gasPrice = int(gasPrice*(10**9))
        tx = swapper.functions.fromETHtoToken(
            self.address,
            token_address,
            int(slippage)
            ).buildTransaction(
                {
                    'from': self.address, 
                    'gas': 5000000,
                    'gasPrice': gasPrice,
                    'nonce': self.web3.eth.getTransactionCount(self.address), 
                    'value': int(Web3.toWei(quantity,"ether"))
                })
        gas = int(self.estimateGas(tx))
        tx.update({ 'gas' : gas })
        signed_txn = self.web3.eth.account.sign_transaction(tx, self.privkey)
        fee = int(gas) * int(gasPrice)
        Fee = Web3.fromWei(int(fee),'ether')
        return signed_txn, Fee


    def createfromTokentoETHTX(self, token_address, quantity, swap, slippage, gasPrice):
        print("createfromTokentoETHTX")
        print("token_address",token_address)
        token_address = self.getChecksumAddress(token_address)
        quantity = quantity * (10**self.getTokenDecimal(token_address))
        swapper = self.createSwapperInstance(swap) 
        gasPrice = int(gasPrice*(10**9))

        tx = swapper.functions.fromTokentoETH(
            self.address,
            token_address,
            int(quantity),
            int(slippage)).buildTransaction({
                'from': self.address, 
                'gas': 5000000,
                'gasPrice': gasPrice,
                'nonce': self.web3.eth.getTransactionCount(self.address), 
                'value': 0})
        gas = int(self.estimateGas(tx))
        tx.update({ 'gas' : gas })
        signed_txn = self.web3.eth.account.sign_transaction(
            tx,
            self.privkey
        )
        fee = int(gas) * int(gasPrice)
        Fee = Web3.fromWei(int(fee),'ether')
        return signed_txn, Fee


    def createfromTokentoTokenTX(self, tokenA, tokenB, quantity, swap, slippage, gasPrice):
        quantity = int(quantity * (10**self.getTokenDecimal(tokenA)))
        swapper = self.createSwapperInstance(swap) 
        print("from",tokenA,"to", tokenB)
        gasPrice = int(gasPrice*(10**9))
        tx = swapper.functions.fromTokentoToken(
                self.address,
                Web3.toChecksumAddress(tokenA),
                Web3.toChecksumAddress(tokenB),
                quantity,
                int(slippage)).buildTransaction({
                    'from': self.address, 
                    'gasPrice': gasPrice,
                    'nonce': self.web3.eth.getTransactionCount(self.address), 
                    'value': 0})
        gas = int(self.estimateGas(tx))
        tx.update({'gas' : gas})
        signed_txn = self.web3.eth.account.sign_transaction(
            tx,
            self.privkey)
        fee = int(gas) * int(gasPrice)
        Fee = Web3.fromWei(int(fee),'ether')
        return signed_txn, Fee

    def getChecksumAddress(self, token_address):
        return Web3.toChecksumAddress(token_address)

    def checkToken(self, token_address, swap):
        swapper = self.createSwapperInstance(swap)     
        tokenInfos = swapper.functions.getTokenInformations(token_address).call()
        buy_tax = round((tokenInfos[0] - tokenInfos[1]) / tokenInfos[0] * 100) 
        sell_tax = round((tokenInfos[2] - tokenInfos[3]) / tokenInfos[2] * 100)
        if tokenInfos[5] and tokenInfos[6] == True:
            honeypot = False
        else:
            honeypot = True
        return buy_tax, sell_tax, honeypot

    def checkisApprove(self, token_address, swapAmount, swap):
        swappaddress = self.getChecksumAddress(self.Main.db.getSwapperAddressFromName(swap))
        tokeninstance = self.createTokenInstance(token_address)
        approvedAmount = tokeninstance.functions.allowance(self.address, swappaddress).call()
        minNeedApproved = int(swapAmount * (10**self.getTokenDecimal(token_address)))
        if approvedAmount > minNeedApproved:
            return True
        else:
            return False

    def approveToken(self, token_address, swap, gasPrice):
        swappaddress = self.getChecksumAddress(self.Main.db.getSwapperAddressFromName(swap))
        tokeninstance = self.createTokenInstance(token_address)
        gasPrice = int(gasPrice*(10**9))
        txn = tokeninstance.functions.approve(
                swappaddress,
                115792089237316195423570985008687907853269984665640564039457584007913129639935 # Max Approve
            ).buildTransaction(
                {
                    'from': self.address, 
                    'gas': 100000,
                    'gasPrice': gasPrice,
                    'nonce': self.web3.eth.getTransactionCount(self.address), 
                    'value': 0
                })
        gas = int(self.estimateGas(txn))
        txn.update({ 'gas' : gas })
        signed_txn = self.web3.eth.account.sign_transaction(
            txn,
            self.privkey
        )
        fee = gas*int(gasPrice)
        Fee = Web3.fromWei(fee, 'ether')
        return signed_txn, swappaddress, Fee


##################################################################################
#SENDING ETH & TOKENS
##################################################################################


    def CreateSend_ETHTX(self, receiver, amount, gasPrice):
        receiver = Web3.toChecksumAddress(receiver)
        txn = {
            'from': self.address,
            'nonce':self.web3.eth.getTransactionCount(self.address),
            'gasPrice': gasPrice, 
            'gas': 50000,
            "to": receiver,
            'value':Web3.toWei(amount,'ether')
            }
        gas = self.estimateGas(txn)
        txn['gas'] = int(gas)
        signed_txn = self.web3.eth.account.sign_transaction(txn ,self.privkey)
        fee = gas * gasPrice
        return signed_txn , fee
    

    def CreateSend_TokenTX(self, receiver, symbol, amount, gasPrice):
        receiver = Web3.toChecksumAddress(receiver)
        TokenAddress = Web3.toChecksumAddress(self.Main.db.SelectFromWhereIs(
            Select='Address', From='TOKENS', Where='SYMBOL', Is=symbol)
            )
        erc20 = self.web3.eth.contract(TokenAddress, abi=self.ERC20_ABI)
        Decimals = self.getTokenDecimal(TokenAddress)
        amount_uint256 = int(float(amount) * (10 ** Decimals))
        revAddress = Web3.toChecksumAddress(receiver)
        token_txn = erc20.functions.transfer(revAddress, amount_uint256).buildTransaction(
            {
                'from': self.address,
                'gas': 1000000,
                'gasPrice': gasPrice,
                'nonce': self.web3.eth.getTransactionCount(self.address)}
            )
        gas = self.estimateGas(token_txn)
        token_txn.update({ 'gas' : int(gas)})
        signed_txn = self.web3.eth.account.signTransaction(token_txn, private_key=self.privkey)
        fee = gas * gasPrice
        return signed_txn, fee



    def checkSendAssetAndCreateTX(self, receiver, symbol, amount, gasPrice):
        gasPrice = int(gasPrice * (10 ** 9))
        if symbol == 'BNB':
            SgRawTX = self.CreateSend_ETHTX(receiver, amount, gasPrice)
        else:
            SgRawTX = self.CreateSend_TokenTX(receiver, symbol, amount, gasPrice)
        Fee = Web3.fromWei(SgRawTX[1],'ether' )
        return SgRawTX[0], Fee



    def sendRawTransactionAndWaiteConfirm(self, SgRawTX):
        try:
            tx_hash = self.web3.eth.sendRawTransaction(SgRawTX.rawTransaction)
            txWait = self.web3.eth.wait_for_transaction_receipt(tx_hash)
            return str(txWait.transactionHash.hex())
        except Exception as e:
            return str(e)




class datetimeHandler():
    
    def getCurrentTimeStamp():
        return datetime.now()

    def toMS(microseconds):
        return microseconds / 1000



class web3FeedbackCheck():
    def runTest(self, RPC):
        self.RPC = RPC
        Supported = self.connectToCHAIN()
        if Supported == True:
            ResponseTime, chainID, currentBlock = self.getCHAINResponseTime()
            if int(chainID) == 56:
                return True, datetimeHandler.toMS(ResponseTime.microseconds), chainID, currentBlock
            else:
                return False
        else:
            return False

    def connectToCHAIN(self):
        if "ws" == str(self.RPC[:2]).lower():
            self.Web3 = Web3(Web3.WebsocketProvider(self.RPC))
            return True
        elif "http" == str(self.RPC[:4]).lower():
            self.Web3 = Web3(Web3.HTTPProvider(self.RPC))
            return True
        else:
            return False

    def getCHAINResponseTime(self):
        StartTime = datetimeHandler.getCurrentTimeStamp()
        chainID = self.Web3.eth.chain_id
        ResponseTime = datetimeHandler.getCurrentTimeStamp() - StartTime
        currentBlock = self.Web3.eth.blockNumber
        return ResponseTime, chainID, currentBlock

