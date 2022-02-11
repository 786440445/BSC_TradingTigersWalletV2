from main import *
import sqlite3, json


class DBFunctions(MainWindow):#MainWindow

    def __init__(self,MainWindow):
        self.Main = MainWindow
        self.db = r"database/Contracts.db"
        self.userDB = r"database/USER-DATA.db"
        self.Accounts = []
        self.createConnection()
        self.createCursor()
        self.getAccounts()
        self.lock = threading.Lock()
        print('DB Successfully Load')

    def __exit__(self):
        self.close_connection()

    def createConnection(self):
        self.conn = sqlite3.connect(self.userDB, check_same_thread=False)
        self.connContracts = sqlite3.connect(self.db, check_same_thread=False)

    def createCursor(self):
        self.cursor = self.conn.cursor()
        self.cursorContracts = self.connContracts.cursor()

    def insertAccount(self, WALLETNAME, KEY, ADDRESS):
        execu = "INSERT INTO ACCOUNTS (WALLETNAME, KEY, ADDRESS) VALUES ( ?, ?, ?)"
        self.cursor.execute(execu,(WALLETNAME,KEY,ADDRESS))
        self.commit()

    def getAccounts(self):
        self.Accounts = []
        execu = 'SELECT WALLETNAME FROM accounts'
        Accs = self.cursor.execute(execu).fetchall()
        for acc in Accs:
            self.Accounts.append(acc[0])

    def commit(self):
        self.conn.commit()
    
    def getKeyfromWalletname(self, WALLETNAME):
        execu = "SELECT KEY FROM accounts WHERE WALLETNAME='{}'".format(WALLETNAME)
        return self.cursor.execute(execu).fetchone()[0]

    def getAddressfromWalletname(self, WALLETNAME):
        execu = "SELECT ADDRESS FROM accounts WHERE WALLETNAME='{}'".format(WALLETNAME)
        address = self.cursor.execute(execu).fetchone()[0]
        return address

    def SelectFrom(self, Select, From):
        SF = "SELECT {} FROM {}".format(Select, From)
        select = self.cursor.execute(SF).fetchall()
        return select

    def SelectFromContracts(self, Select, From):
        SF = "SELECT {} FROM {}".format(Select, From)
        select = self.cursorContracts.execute(SF).fetchall()
        return select

    def SelectFromWithOption(self, Select, From, OrderBy, ASC):
        if ASC == False:
            ASC = "DESC"
        else:
            ASC = "ASC"
        SF = "SELECT {} FROM {} ORDER BY {} {}".format(Select, From, OrderBy, ASC)
        select = self.cursor.execute(SF).fetchall()
        return select

    def SelectFromWhereIs(self, Select, From, Where, Is):
        try:
            self.lock.acquire(True)
            execu = "SELECT {} FROM {} WHERE {}='{}'".format(Select, From, Where, Is)
            data = self.cursor.execute(execu).fetchone()[0]
            return data
        finally:
            self.lock.release()

    def SelectFromWhereIsCONTRACTS(self, Select, From, Where, Is):
        try:
            self.lock.acquire(True)
            execu = "SELECT {} FROM {} WHERE {}='{}'".format(Select, From, Where, Is)
            data = self.cursorContracts.execute(execu).fetchone()[0]
            return data
        finally:
            self.lock.release()

    def getTokenAddressfromSymbol(self, symbol):
        try:
            execu = "SELECT ADDRESS FROM TOKENS WHERE SYMBOL='{}'".format(symbol)
            ADDRESS = self.cursor.execute(execu).fetchone()[0]
            return ADDRESS
        except Exception as e:
            print(e)

    def getSwapABIFromName(self, swapname):
        execu = "SELECT ABI FROM SWAPCONTRACTS WHERE NAME='{}'".format(swapname)
        ABI = json.loads(self.cursorContracts.execute(execu).fetchone()[0])
        return ABI

    def getSwapperAddressFromName(self, swapname):
        execu = "SELECT ADDRESS FROM SWAPCONTRACTS WHERE NAME='{}'".format(swapname)
        ADDRESS = self.cursorContracts.execute(execu).fetchone()[0]
        return ADDRESS

    def UpdateWhereIsTo(self, Update, Set, To, Where, Is):
        self.cursor.execute("UPDATE {} SET {} = '{}' WHERE {}='{}'".format(Update, Set, To, Where, Is))
        self.commit()

    def deleteRPC(self, RPC):
        self.cursor.execute("DELETE FROM Providers WHERE ProviderURL='{}'".format(RPC))
        self.commit()

    def deleteToken(self, symbol):
        self.cursor.execute("DELETE FROM TOKENS WHERE SYMBOL='{}'".format(symbol))
        self.commit()

    def getDefaultPROVIDER(self):
        execu = "SELECT ProviderURL FROM Providers WHERE mainProvider='1'"
        PROVIDER = self.cursor.execute(execu).fetchone()[0]
        return PROVIDER
    
    def setDefaultProvider(self, ProviderURL):
        execu = "SELECT ProviderURL FROM Providers WHERE mainProvider='1'"
        PROVIDER = self.cursor.execute(execu).fetchone()[0]
        if str(PROVIDER) != str(ProviderURL):
            self.UpdateWhereIsTo(Update="Providers", Set="mainProvider", To="0", Where="ProviderURL", Is=PROVIDER)
            self.UpdateWhereIsTo("Providers", "mainProvider", "1", "ProviderURL", ProviderURL)

    def addProvider(self, Name, ProviderURL):
        lookup = self.cursor.execute("SELECT Name FROM Providers WHERE ProviderURL='{}'".format(ProviderURL)).fetchone()
        if lookup == None:
            self.cursor.execute("INSERT INTO Providers (Name, ProviderURL, mainProvider) VALUES ( ?, ?, ?)", (Name, ProviderURL, 0))
            self.commit()
            return True
        else:
            return False

    def addToken(self, name, symbol, address, decimals, logoURI):
        lookupToken = self.cursor.execute("SELECT NAME FROM TOKENS WHERE SYMBOL='{}'".format(symbol)).fetchone()
        try:
            logo = self.Main.api.getImage(url=logoURI)
        except:
            try:
                logo = self.Main.api.getImage(url=f"https://raw.githubusercontent.com/trustwallet/assets/master/blockchains/smartchain/assets/{address}/logo.png")
            except:
                logo = self.defaultLOGO()
        if lookupToken == None:
            self.cursor.execute("INSERT INTO Tokens (NAME, SYMBOL, ADDRESS, DECIMALS, LOGOURI) VALUES ( ?, ?, ?, ?, ?)", (name, symbol, address, decimals, logo))
            self.commit()
            return True
        else:
            return False


    def defaultLOGO(self):
        DEFAULTIMG = self.cursorContracts.execute("SELECT IMAGE FROM SWAPCONTRACTS WHERE NAME='ERC20'").fetchone()[0]
        return DEFAULTIMG
        