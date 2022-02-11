
# Work by Seven, Trading-Tigers.com
#
#     ______               ___                 _______                                          
#    /_  __/________ _____/ (_)___  ____ _    /_  __(_)___ ____  __________ _________  ____ ___ 
#     / / / ___/ __ `/ __  / / __ \/ __ `/_____/ / / / __ `/ _ \/ ___/ ___// ___/ __ \/ __ `__ \
#    / / / /  / /_/ / /_/ / / / / / /_/ /_____/ / / / /_/ /  __/ /  (__  )/ /__/ /_/ / / / / / /
#   /_/ /_/   \__,_/\__,_/_/_/ /_/\__, /     /_/ /_/\__, /\___/_/  /____(_)___/\____/_/ /_/ /_/ 
#    _       __      ____     __ /____/   _____    /____/                                       
#   | |     / /___ _/ / /__  / /_   | |  / /__ \                                                
#   | | /| / / __ `/ / / _ \/ __/   | | / /__/ /                                                
#   | |/ |/ / /_/ / / /  __/ /_     | |/ // __/                                                 
#   |__/|__/\__,_/_/_/\___/\__/     |___//____/                                                 
#                                                                                               
# Welcome to my chaos,
# there is still a lot to do.
# Current not 100% stable, please report all Errors/Bugs and Window closes @ISSUES in github repro.


from logging import exception
import sys
import threading, webbrowser #threading; used to lock db, if more threads work with db.
from datetime import datetime
import webbrowser as web1

#PyQT5 imports
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


from app_imports import *


class WorkerSignals(QObject):
    result = pyqtSignal(bool, str)


class AWorker(QRunnable):
    def __init__(self, fn, *args, **kwargs):
        super(AWorker, self).__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

    @pyqtSlot()
    def run(self):
        try:
            str_data = self.fn(*self.args, **self.kwargs) # All functions passed to AWorker need str data return, if function fails, need to be return the error str.
            self.signals.result.emit(True, str(str_data))
        except:
            self.signals.result.emit(False, str(str_data))




class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.db = DBFunctions(self)
        self.ui = Ui_MainWindow()
        self.sec = SECFunctions(self)
        self.api = APIFunctions(self)
        self.ui.setupUi(self)
        self.threadpool = QThreadPool.globalInstance()
        self.fillAllTokensList()
        
        self.setWindowTitle('Trading Tigers Wallet')
        Sidebar.labelTitle(self, 'Trading Tigers Wallet')
        startSize = QSize(1100, 825)
        self.resize(startSize)
        self.setMinimumSize(startSize)
        self.setMaximumSize(startSize)

        
        #Global Variables
        self.currentSlippage = 3
        self.minSlippage = 1
        self.currentSwapGAS = 6
        #Slider Connected
        self.ui.slider_gasSend.valueChanged.connect(self.SliderValueChangedSendTokens)
        self.ui.slider_GasGwei_Swap.valueChanged.connect(self.SliderValueChangedSwapTokens)
        self.ui.slider_Slippage_Swap.valueChanged.connect(self.SliderValueChangedSwapTokensSlippage)

        #tableSizeingtable 
        self.ui.tableWidget_AllTokensinDB.setColumnWidth(0,48)
        self.ui.tableWidget_AllTokensinDB.setColumnWidth(1,140)
        self.ui.tableWidget_AllTokensinDB.setColumnWidth(2,440)
        self.ui.tableWidget_AllTokensinDB.setColumnWidth(3,140)
        self.ui.tableWidget_AllTokensinDB.setColumnWidth(4,120)


        self.ui.tableWidget_AllActivTokens.setColumnWidth(0,64)
        self.ui.tableWidget_AllActivTokens.setColumnWidth(1,100)
        self.ui.tableWidget_AllActivTokens.setColumnWidth(2,280)
        self.ui.tableWidget_AllActivTokens.setColumnWidth(3,150)
        self.ui.tableWidget_AllActivTokens.setColumnWidth(4,150)
        self.ui.tableWidget_AllActivTokens.setColumnWidth(4,150)


        self.ui.tableWidget_transactions.setColumnWidth(0,120)
        self.ui.tableWidget_transactions.setColumnWidth(1,75)
        self.ui.tableWidget_transactions.setColumnWidth(2,75)
        self.ui.tableWidget_transactions.setColumnWidth(3,100)
        self.ui.tableWidget_transactions.setColumnWidth(4,100)
        self.ui.tableWidget_transactions.setColumnWidth(5,360)
        self.ui.tableWidget_transactions.setColumnWidth(6,100)


        self.ui.tableWidget_Provider_Options.setColumnWidth(0,60)
        self.ui.tableWidget_Provider_Options.setColumnWidth(1,80)
        self.ui.tableWidget_Provider_Options.setColumnWidth(2,160)
        self.ui.tableWidget_Provider_Options.setColumnWidth(3,80)
        self.ui.tableWidget_Provider_Options.setColumnWidth(4,80)
        self.ui.tableWidget_Provider_Options.setColumnWidth(5,80)

        self.ui.tableWidget_OpenLimitOrders.setColumnWidth(0,100)
        self.ui.tableWidget_OpenLimitOrders.setColumnWidth(1,100)
        self.ui.tableWidget_OpenLimitOrders.setColumnWidth(2,100)
        self.ui.tableWidget_OpenLimitOrders.setColumnWidth(3,100)
        #self.ui.tableWidget_OpenLimitOrders.setColumnWidth(3,80)
      

        #HIDE THINGS
        self.ui.frame_show_PrivKey.hide()
        self.ui.widget_wrong_pw.hide()
        self.ui.label_add_Token_Error.hide()
        self.ui.label_SwapWayC.hide()
        self.ui.frame_InputTokenInfos.hide()
        self.ui.frame_OutPutTokenInfos.hide()
        self.ui.frame_SwapWayC.hide()
        self.ui.pushButton_approve_token.hide()
        self.ui.pushButton_Confirm_Swap.hide()
        self.ui.lineEdit_Swap_Error.hide()
        self.ui.lineEdit_add_provider_Error.hide()
        self.ui.pushButton_TxBscView.hide()
        self.ui.pushButton_LoggoutEverywere.hide()
        self.ui.pushButton__limit_approve_token.hide()
        self.ui.pushButton__limit_approve_tigs_toRouter.hide()
        self.ui.pushButton_Confirm_LimitOrder.hide()

        self.ui.pushButton_TokenSite.hide()#  ==============================> # OVERVIEW, need more QThread experience to make it running into background.

        self.ui.frame_add_Provider.hide()


        self.ui.pushButton_Add_NewProvider.clicked.connect(lambda: self.OpenAddProvider())
        self.ui.pushButton_add_ProviderCancel.clicked.connect(lambda: self.CloseAddProvider())

        #self.ui.stackedWidget.setMinimumWidth(20)
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_unlock)
        
        #COMBOBOXES
        self.ui.comboBox_swap_from_ASSET.activated[str].connect(lambda: self.getInputToken())
        self.ui.comboBox_swap_to_ASSET.activated[str].connect(lambda: self.getOutputToken())


        self.ui.comboBox_sending_Asset.activated[str].connect(lambda:self.getSendAsset())

        self.ui.comboBox_select_swap.activated[str].connect(lambda: self.getSwap(False))
        self.ui.comboBox_select_swap_LimitOrders.activated[str].connect(lambda: self.getSwapLimit())

        self.ui.btn_toggle_menu.clicked.connect(lambda: Sidebar.slideMenu(self, 200, True))
        self.ui.comboBox_Accounts.addItems(self.db.Accounts)
        self.ui.pushButton_limit_BuyOrder.clicked.connect(lambda: self.openLimitBuy())
        self.ui.pushButton_limit_SellOrder.clicked.connect(lambda: self.openLimitSell())

        #LINEEDIT
        self.ui.lineEdit_SendAmount.textChanged.connect(lambda: self.getSendAmount())
        self.ui.pushButton_TxBscView.clicked.connect(lambda: self.buttonOpenBSCExplorer())
        self.ui.lineEdit_Swap_from_Amount.textChanged.connect(self.getSwapInputAmount)
        self.ui.lineEdit_Swap_to_Amount.textChanged.connect(self.getSwapOutputAmount)
        self.ui.input_add_TokenAddresse.textChanged.connect(lambda: self.getAddTokenInfos())
        self.ui.pushButton_approve_Confirm.clicked.connect(lambda: self.WaitTransactionWindow())


        self.ui.pushButton_Swap_changeInputTokenToOutputToken.clicked.connect(lambda: self.swappingChangeInputToOutputToken())

        self.ui.pushButton_LoggoutEverywere.clicked.connect(lambda: self.LogOut())
        #BUTTONS 
        self.ui.pushButton_add_ProviderSubmit.clicked.connect(lambda: self.addNewProvider())
        self.ui.input_password.returnPressed.connect(self.ui.pushButton_Unlock_Wallet.click)
        self.ui.pushButton_Unlock_Wallet.clicked.connect(self.UnlockWallet)
        self.ui.pushButton_Create_Wallet.clicked.connect(self.Create_WalletWindow)
        self.ui.pushButton_Import_Wallet.clicked.connect(self.Import_WalletWindow)
        self.ui.pushButton_EnableDisableTokens.clicked.connect(self.EnableDisableTokenSide)
        self.ui.pushButton_back_wallet.clicked.connect(self.BackToSettings)
        self.ui.btn_Send_BNBTOKEN.clicked.connect(self.SendButton)
        self.ui.pushButton_Export_Private_Key.clicked.connect(self.showPrivKey)
        self.ui.pushButton_copy_PrivateKey.clicked.connect(lambda: QApplication.clipboard().setText(self.web3.clearprivKey))
        self.ui.pushButton_Hide_PrivKeyframe.clicked.connect(self.closePrivKey)
        
        self.ui.pushButton_Cancel_SwapConfirm.clicked.connect(self.SwapConfirmCancelButton)
        self.ui.pushButton_TXCancel.clicked.connect(self.backToSending)
        self.ui.pushButton_TokenSite.clicked.connect(self.ToTokenOverView)
        self.ui.pushButton_toAddTokenOverview.clicked.connect(self.ToAddTokenOverView)
        self.ui.pushButton_back_Alltokens.clicked.connect(self.EnableDisableTokenSide)
        self.ui.pushButton_save_token.clicked.connect(self.saveToken)
        self.ui.pushButton_Confirm_Swap.clicked.connect(self.confirmSwap)
        
        self.ui.label_SwapWayA.setPixmap(self.initDefaultTokenPixmap())
        self.ui.label_SwapWayB.setPixmap(self.initDefaultTokenPixmap())
        self.ui.label_SwapWayC.setPixmap(self.initDefaultTokenPixmap())

        try:
            self.web3 = WEB3Functions(self)
        except:
            pass

        def moveWindow(event):
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()
        self.ui.frame_label_top_btns.mouseMoveEvent = moveWindow
        Sidebar.LoadFeatures(self)
        self.show()
    

    def LogOut(self):
        del self.web3
        self.reinitWeb3()
        self.ui.pushButton_LoggoutEverywere.hide()
        Sidebar.clearMenu(self)
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_unlock)

#Soon, Too mutch Tokens with high gas usage, we execute the transactions for them.
    def openLimitBuy(self):
        self.ui.stackedWidget_limitOrders.setCurrentWidget(self.ui.stackedWidget_Page_LimitBuy)

    def openLimitSell(self):
        self.ui.stackedWidget_limitOrders.setCurrentWidget(self.ui.stackedWidget_Page_LimitSell)

    def showPrivKey(self):
        self.ui.frame_show_PrivKey.show()
        self.ui.lineEdit_Secret_Key.setText(str(self.web3.clearprivKey))

    def closePrivKey(self):
        self.ui.frame_show_PrivKey.hide()

    def OpenAddProvider(self):
        try:
            self.ui.lineEdit_add_provider_Error.hide()
        except:
            pass
        self.ui.lineEdit_add_provider_Error.clear()
        self.ui.frame_add_Provider.show()

    def CloseAddProvider(self):
        try:
            self.ui.lineEdit_add_provider_Error.hide()
        except:
            pass
        self.ui.frame_add_Provider.hide()    

   
    def saveCreatedWallet(self):
        if self.ui.input_create_walletname.displayText() != "":
            if self.ui.input_create_walletpw.displayText() != "":
                key = self.web3.newWallet()
                address = self.web3.addressfromKey(key)
                self.db.insertAccount(
                    WALLETNAME=self.ui.input_create_walletname.displayText(),
                    KEY=self.sec.encryptstr(PW=self.ui.input_create_walletpw.text(), KEY=key),
                    ADDRESS=address
                    )
                self.ui.input_create_walletname.clear()
                self.ui.input_create_walletpw.clear()
                self.ui.widget_Save_your_Key.show()
                self.ui.widget_Save_your_Key.setDisabled(False)
                self.ui.pushButton_Copy_SKEY.clicked.connect(lambda: QApplication.clipboard().setText(key) )
                self.ui.textBrowser_skey.setText(key)
                self.ui.pushButton_create_wallet.hide()

    def saveImportWallet(self):
        if self.ui.input_import_walletname.text() != "":
            if self.ui.input_import_walletpw.displayText() != "":
                if self.ui.input_import_key.displayText() != "":
                    try:
                        key = self.ui.input_import_key.text()
                        address = self.web3.addressfromKey(key=key)
                        self.db.insertAccount(WALLETNAME=self.ui.input_import_walletname.displayText(), KEY=self.sec.encryptstr(PW=self.ui.input_import_walletpw.text(),KEY=key), ADDRESS=address)
                        self.ui.frame_imported_replay.show()
                        self.ui.textBrowser_imported_address.setText(address)
                        self.ui.pushButton_import_wallet.hide()
                    except Exception as e:
                        self.ui.frame_Invalid_key.show()
                        print(e)
                    finally:
                        self.ui.input_import_walletname.clear()
                        self.ui.input_import_walletpw.clear()
                        self.ui.input_import_key.clear()
                        

    def back_to_login_window(self):
        try:
            self.ui.widget_Save_your_Key.hide()
            self.ui.pushButton_create_wallet.show()
        except:
            pass
        try:
            self.ui.frame_imported_replay.show()
            self.ui.pushButton_import_wallet.show()
        except:
            pass
        self.db.getAccounts()
        self.ui.comboBox_Accounts.clear()
        self.ui.comboBox_Accounts.addItems(self.db.Accounts)
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_unlock)

    def Create_WalletWindow(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_Create_Account)
        self.ui.pushButton_create_wallet.clicked.connect(self.saveCreatedWallet)
        self.ui.widget_Save_your_Key.hide()
        self.ui.pushButton_back_Login.clicked.connect(self.back_to_login_window)
        
    def Import_WalletWindow(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_import_Secret_Key)
        self.ui.pushButton_import_wallet.clicked.connect(self.saveImportWallet)
        self.ui.frame_imported_replay.hide()
        self.ui.frame_Invalid_key.hide()
        self.ui.pushButton_back_Login_2.clicked.connect(self.back_to_login_window)
    
    def reinitWeb3(self):
        self.web3 = WEB3Functions(self)
    
    def UnlockWallet(self):
        dbkey = self.db.getKeyfromWalletname(WALLETNAME=self.ui.comboBox_Accounts.currentText())
        status = self.sec.decryptstr(PW=self.ui.input_password.text(), ENCRYPTKEY=dbkey)
        self.ui.input_password.clear()
        if status[0] == True:
            self.ui.pushButton_LoggoutEverywere.show()
            try:
                self.ui.widget_wrong_pw.hide()
            except:
                pass
            self.reinitWeb3()
            self.web3.Save_key_to_hex(priv=status[1])
            self.ui.label_top_clean.setText(str('Logged in with: ') + str(self.ui.comboBox_Accounts.currentText()))
            self.address = self.db.getAddressfromWalletname(self.ui.comboBox_Accounts.currentText())
            pixmap = QPixmap()
            pixmap.loadFromData(self.api.getQRImage(address=self.address), 'png')  
            xpixmap = pixmap.scaled(320, 320, Qt.KeepAspectRatio) 
            self.ui.label_qrCode_self_address.setPixmap(xpixmap)
            self.ui.pushButton_copy_self_address.clicked.connect(lambda: QApplication.clipboard().setText(self.address))
            self.ui.output_self_address.setText(self.address.lower())
            self.initAccount()
            Sidebar.addNewMenu(self, "Wallet", "btn_wallet", "url(:/Fontawsome/icons/fontawsome/wallet.png)", True)
            Sidebar.addNewMenu(self, "Send", "btn_send", "url(:/Fontawsome/icons/fontawsome/wallet_send.png)", True)
            Sidebar.addNewMenu(self, "Swapping", "btn_swapping", "url(:/Fontawsome/icons/fontawsome/swapping.png)", True)
            Sidebar.addNewMenu(self, "Transactions", "btn_transactions", "url(:/Fontawsome/icons/fontawsome/history-transactions.png)", True)
            Sidebar.addNewMenu(self, "Settings", "btn_settings", "url(:/Fontawsome/icons/fontawsome/cog-solid.png)", False)
            #Sidebar.addNewMenu(self, "Limit Swapps", "btn_limitorders", "url(:/Fontawsome/icons/fontawsome/OrderBook.png)", True)# most style is done!

            Sidebar.selectStandardMenu(self, "btn_wallet")
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
        else:
            self.ui.widget_wrong_pw.show()
            self.ui.input_password.clear()


    def refreshPrices(self):
        self.BNBbalance = self.web3.getETHBalance()[0]
        self.BNBprice  = self.web3.getETHPrice()[0]
        self.TIGSPrice = self.web3.getTIGSUSDPrice()[0]
        self.TIGSBalance = self.web3.getTIGSBalance()[0]
        self.ui.output_Tigs_balance.setText(str('%.08f' % self.TIGSBalance)) 
        self.ui.output_TigsBalance_in_usd.setText(str('%.02f' % (float(self.TIGSPrice) * float(self.TIGSBalance))+ str(' $')))
        self.ui.output_TIGSPRICE.setText(str('%.03f' % self.TIGSPrice ) + str(' $')) 
        self.ui.output_BNBBalance.setText(str('%.08f' % self.BNBbalance ))
        self.ui.output_BNBBalance_in_usd.setText(str('%.02f' % (float(self.BNBbalance) * float(self.BNBprice)) + str(' $')))
        self.ui.output_BNBPrice.setText(str('%.02f' % self.BNBprice )+ str(' $'))


    def initAccount(self):
        self.web3.initAccount(self.address)
        self.refreshPrices()
        print('succesfull initAccount!')
        
    def initTokenPixmapIcon(self, Tokensymbol):
        pixmap = QPixmap()
        pixmap.loadFromData(self.db.SelectFromWhereIs(Select='LOGOURI', From='TOKENS', Where='SYMBOL', Is=Tokensymbol))  
        pixmap = pixmap.scaled(46, 46, Qt.KeepAspectRatio)
        return QIcon(pixmap)

    def initDefaultTokenPixmap(self):
        pixmap = QPixmap()
        pixmap.loadFromData(self.db.SelectFromWhereIsCONTRACTS(Select='image', From='SwapContracts', Where='NAME', Is="ERC20"))  
        pixmap = pixmap.scaled(64, 64, Qt.KeepAspectRatio)
        return pixmap

    def initTokenPixmap(self, Tokensymbol):
        pixmap = QPixmap()
        pixmap.loadFromData(self.db.SelectFromWhereIs(Select='LOGOURI', From='TOKENS', Where='SYMBOL', Is=Tokensymbol))  
        pixmap = pixmap.scaled(64, 64, Qt.KeepAspectRatio)
        return pixmap

    def initTokenPixmapConfirm(self, Address):
        try:
            pixmap = QPixmap()
            pixmap.loadFromData(self.db.SelectFromWhereIs(Select='LOGOURI', From='TOKENS', Where='address', Is=Address))  
            pixmap = pixmap.scaled(64, 64, Qt.KeepAspectRatio)
            return pixmap
        except Exception as e:
            try:
                pixmap = QPixmap()
                Tokensymbol = self.web3.getTokenSymbol(Address)
                pixmap.loadFromData(self.db.SelectFromWhereIs(Select='LOGOURI', From='TOKENS', Where='SYMBOL', Is=Tokensymbol))  
                pixmap = pixmap.scaled(64, 64, Qt.KeepAspectRatio)
                return pixmap
            except Exception as e:
                pixmap = QPixmap()
                pixmap.loadFromData(self.db.SelectFromWhereIsCONTRACTS(Select='image', From='SwapContracts', Where='NAME', Is="ERC20"))  
                pixmap = pixmap.scaled(64, 64, Qt.KeepAspectRatio)
                return pixmap

    def initSwapPixmap(self,Swapname):
        pixmap = QPixmap()
        pixmap.loadFromData(self.db.SelectFromWhereIsCONTRACTS(Select='IMAGE', From='SwapContracts', Where='NAME',Is=Swapname), 'png')  
        pixmap = pixmap.scaled(46, 46, Qt.KeepAspectRatio)
        return QIcon(pixmap)

    def initTokens(self):
        self.ui.comboBox_sending_Asset.clear()
        #self.ui.comboBox_sending_Asset.addItem('Select Token!')
        for token in self.db.SelectFrom(Select='SYMBOL', From='TOKENS'):
            if int(self.db.SelectFromWhereIs(Select='ACTIV', From='TOKENS', Where='SYMBOL',Is=token[0])) == 1:
                a,b = self.initTokenPixmapIcon(Tokensymbol=token[0]), token[0]
                self.ui.comboBox_sending_Asset.addItem(a,b)


    def initSwapToTokens(self, disabled):
        self.ui.comboBox_swap_to_ASSET.clear()
        #self.ui.comboBox_swap_to_ASSET.addItem('Select Token!')       
        for token in self.db.SelectFrom(Select='SYMBOL', From='TOKENS'):
            if int(self.db.SelectFromWhereIs(Select='ACTIV', From='TOKENS', Where='SYMBOL',Is=token[0])) == 1:
                a,b = self.initTokenPixmapIcon(Tokensymbol=token[0]), token[0]
                if str(b) != str(disabled):
                    self.ui.comboBox_swap_to_ASSET.addItem(a,b)
        self.getOutputToken()


    def initSwapFromTokens(self, disabled):
        self.ui.comboBox_swap_from_ASSET.clear()
        self.ui.lineEdit_Swap_to_AssetBalance.clear()
        self.ui.lineEdit_Swap_to_BalanceInUSD.clear()
        #self.ui.comboBox_swap_from_ASSET.addItem('Select Token!')
        for token in self.db.SelectFrom(Select='SYMBOL', From='TOKENS'):
            if int(self.db.SelectFromWhereIs(Select='ACTIV', From='TOKENS', Where='SYMBOL',Is=token[0])) == 1:
                a,b = self.initTokenPixmapIcon(Tokensymbol=token[0]), token[0]
                if str(b) != str(disabled):
                    self.ui.comboBox_swap_from_ASSET.addItem(a,b)
        self.getInputToken()

    def initSwaps(self):
        self.ui.comboBox_select_swap.clear()
        for swap in self.db.SelectFromContracts(Select='NAME', From='SwapContracts'):
            a,b = self.initSwapPixmap(Swapname=swap[0]), swap[0]
            if b != "ERC20":
                self.ui.comboBox_select_swap.addItem(a,b)
        self.getSwap(False)
    

    def initSwapsLimit(self):
        self.ui.comboBox_select_swap_LimitOrders.clear()
        for swap in self.db.SelectFrom(Select='Name', From='LimitOrderContracts'):
            a,b = self.initSwapPixmap(Swapname=swap[0]), swap[0]
            if b != "ERC20":
                self.ui.comboBox_select_swap_LimitOrders.addItem(a,b)


    def getSendAmount(self):
        try:
            self.SendAmount = float(self.ui.lineEdit_SendAmount.text())
        except:
            pass # if not float he pass and fallback to nothing.
        #TODO:
        # - replace "," with "." | forbid letters
            
        try:            
            if float(self.SendAmount):
                if self.AssetUSD == 'Not Listed':
                    self.AssetUSD = float(0)
                elif float(self.SendAmount) > float(self.SendAssetBalance):
                    self.ui.lineEdit_SendAmount.setText(str('%.08f' % self.SendAssetBalance))
                    self.SendAmountinUSD = float(self.AssetUSD) * float(self.SendAmount)
                    self.ui.lineEdit_SendAmountUSD.setText(str('%.02f' % self.SendAmountinUSD) + str(' $'))
                    print('sendAmount is :', self.SendAmount)
                else:
                    self.SendAmountinUSD = float(self.AssetUSD) * float(self.SendAmount)
                    self.ui.lineEdit_SendAmountUSD.setText(str('%.02f' % self.SendAmountinUSD) + str(' $'))
                    print('sendAmount is :', self.SendAmount)
            elif self.SendAmount == str:
                print("bad input")
        except exception as e:
            print(e)



    def getSendAsset(self):
        self.sendAsset = self.ui.comboBox_sending_Asset.currentText()       
        if self.sendAsset == 'BNB':
            self.SendAssetBalance = self.web3.getETHBalance()[0]
            self.AssetUSD = self.web3.getETHPrice()[0]
        else:    
            self.sendAssetAddress = self.db.SelectFromWhereIs("ADDRESS", "TOKENS", "SYMBOL", f"{self.sendAsset}")
            self.SendAssetBalance = self.web3.getTokenBalance(self.sendAssetAddress)[0]
            self.AssetUSD = self.web3.getTokenUSDPrice(self.sendAssetAddress)[0]
        self.ui.lineEdit_SendAsset_Balance.setText(str('%.08f' % self.SendAssetBalance))
        AssetBalanceUSD = float(self.SendAssetBalance) * float(self.AssetUSD)
        self.ui.lineEdit_SendBalanceUSD.setText(str('%.02f' % AssetBalanceUSD + str(" $")))
        print('sendAsset is :',self.sendAsset)


    def swappingChangeInputToOutputToken(self):
        self.ui.lineEdit_Swap_from_Amount.clear()
        self.ui.lineEdit_Swap_to_Amount.clear()
        tempFromToken = self.ui.comboBox_swap_from_ASSET.currentText()
        tempToToken = self.ui.comboBox_swap_to_ASSET.currentText()
        self.ui.comboBox_swap_from_ASSET.setCurrentText(str(tempToToken))   
        self.getInputToken()   
        self.ui.comboBox_swap_to_ASSET.setCurrentText(str(tempFromToken))
        self.getOutputToken()   

    
    def openSwapConfirm(self):
        self.ui.label_swap_outputToken.setText(str(self.outputTokenName))
        self.ui.label_swap_inputToken.setText(str(self.inputTokenName))
        a = False
        b = False
        c = False
        d = False
        for address in self.outputWay:
            if a == False:
                self.ui.label_SwapWayA_confirm.setPixmap(self.initTokenPixmapConfirm(address))
                self.ui.label_SwapWayA_confirm.show()
                self.ui.frame_138.show()
                a = True
            elif b == False:
                self.ui.label_SwapWayB_confirm.setPixmap(self.initTokenPixmapConfirm(address))
                self.ui.label_SwapWayB_confirm.show()
                b = True
            elif c == False:
                self.ui.label_SwapWayC_confirm.setPixmap(self.initTokenPixmapConfirm(address))
                self.ui.label_SwapWayC_confirm.show()
                self.ui.frame_SwapWayC_2.show()
                c = True
            elif d == False:
                self.ui.label_SwapWayD_confirm.setPixmap(self.initTokenPixmapConfirm(address))
                self.ui.label_SwapWayD_confirm.show()
                self.ui.frame_SwapWayC_3.show()
                d = True
        if c == False:
            self.ui.label_SwapWayC_confirm.hide()
            self.ui.frame_SwapWayC_2.hide()
        if d == False:
            self.ui.label_SwapWayD_confirm.hide()
            self.ui.frame_SwapWayC_3.hide()
        self.ui.output_swapspendAmount.setText(str('%.08f' % self.SwapInputAmount))
        swapInputUSD = float(self.SwapInputAmount) * float(self.SwapInputTokenUSD)
        self.ui.output_swapspendAmountUSD.setText(str('%.02f' % swapInputUSD) + " $")
        self.MinOutput = self.takeSlippage(self.outputQuantinity, self.currentSlippage)
        swapOutputUSD = float(self.MinOutput) * float(self.SwapOutputTokenUSD)
        self.ui.output_swapminreceivedAmount.setText(str('%.08f' % self.MinOutput))
        self.ui.output_swapminreceivedAmountUSD.setText(str('%.02f' % swapOutputUSD) + " $")
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_swapping_Confirm)


    def getSwap(self, bool):
        self.swap = self.ui.comboBox_select_swap.currentText()
        self.ManageApproveButton()
        if bool:
            self.CleanSwapp()
        print('swap is :', self.swap)


    def getSwapLimit(self):
        self.swapLimit = self.ui.comboBox_select_swap_LimitOrders.currentText()
        print('swap for Limit Orders is :',self.swapLimit)


    def showSwapError(self, e):
        self.ui.lineEdit_Swap_Error.show()
        self.ui.lineEdit_Swap_Error.setText(str(e))
    

    def initInputToken(self):
        print("iSIPT")
        try:
            self.swapInputToken = self.ui.comboBox_swap_from_ASSET.currentText()
            print(self.swapInputToken)
            if self.swapInputToken == 'BNB':
                self.InputTokenBalance = self.web3.getETHBalance()[0]
                self.inputTokenAddress = self.web3.WETH
                self.inputTokenName = "Binance Coin"
                self.inputTokenPriceBNB = 1
            else:    
                self.inputTokenAddress = self.web3.getChecksumAddress(self.db.SelectFromWhereIs("ADDRESS", "TOKENS", "SYMBOL", f"{self.swapInputToken}"))
                self.InputTokenBalance = self.web3.getTokenBalance(self.inputTokenAddress)[0]
                self.inputTokenName = self.db.SelectFromWhereIs("NAME", "TOKENS", "SYMBOL", f"{self.swapInputToken}") #self.web3.getTokenName(self.inputTokenAddress)
                self.inputTokenPriceBNB = self.web3.getTokenPriceETH(self.inputTokenAddress, self.swap)[0]
        except Exception as e:
            print(str(e))
            self.showSwapError(e)



    def getInputToken(self):
        print("gSIPT")
        try:
            self.ui.lineEdit_Swap_Error.hide()
        except:
            pass
        try:
            self.ui.lineEdit_Swap_from_Amount.clear()
            self.ui.lineEdit_Swap_to_Amount.clear()
            self.ui.lineEdit_Swap_from_AmountInUSD.clear()
            self.ui.lineEdit_Swap_to_AmountInUSD.clear()
        except:
            pass

        self.initInputToken()
        self.ui.lineEdit_Swap_from_AssetBalance.setText(str('%.08f' % self.InputTokenBalance))
        self.SwapInputTokenUSD = self.web3.getTokenUSDPrice(self.inputTokenAddress)[0]
        TokenBalanceUSD = float(self.InputTokenBalance) * float(self.SwapInputTokenUSD)
        self.ui.lineEdit_Swap_from_BalanceInUSD.setText(str('%.02f' % TokenBalanceUSD) + " $")
        try:
            self.buy_tax_In, self.sell_tax_In, honeypot = self.web3.checkToken(self.inputTokenAddress, self.swap)
            self.ui.frame_InputTokenInfos.show()
            self.ui.lineEdit_InputToken_BuyTax.setText(str(self.buy_tax_In) + " %")
            self.ui.lineEdit_InputToken_SellTax.setText(str(self.sell_tax_In) + " %")
            self.ui.lineEdit_InputToken_BuyTax.setStyleSheet(Sidebar.getResetStyleTokenTax())
            self.ui.lineEdit_InputToken_SellTax.setStyleSheet(Sidebar.getResetStyleTokenTax())
            if int(self.sell_tax_In) > 10: 
                self.ui.lineEdit_InputToken_SellTax.setStyleSheet(Sidebar.getRedStyleTokenTax())
            if int(self.buy_tax_In) > 10: 
                self.ui.lineEdit_InputToken_BuyTax.setStyleSheet(Sidebar.getRedStyleTokenTax())
        except Exception as e:
             self.showSwapError(e)
        self.ui.label_SwapWayA.setPixmap(self.initTokenPixmap(self.swapInputToken))
        self.initSwapToTokens(self.swapInputToken)
        self.ManageApproveButton()




    def initOutputToken(self):
        print("iSOPT")
        try:
            self.swapoutputToken = self.ui.comboBox_swap_to_ASSET.currentText()
            print(self.swapoutputToken)

            if self.swapoutputToken == 'BNB':
                self.outputTokenBalance = self.web3.getETHBalance()[0]
                self.outputTokenAddress = self.web3.WETH
                self.outputTokenName = "Binance Coin"
                self.outputTokenPriceBNB = 1
            else:    
                try:
                    self.outputTokenAddress = self.web3.getChecksumAddress(self.db.SelectFromWhereIs("ADDRESS", "TOKENS", "SYMBOL", f"{self.swapoutputToken}"))
                    self.outputTokenBalance = self.web3.getTokenBalance(self.outputTokenAddress)[0]
                    self.outputTokenName = self.db.SelectFromWhereIs("NAME", "TOKENS", "SYMBOL", f"{self.swapoutputToken}") # self.web3.getTokenName(self.outputTokenAddress)
                    self.outputTokenPriceBNB = self.web3.getTokenPriceETH(self.outputTokenAddress, self.swap)[0]
                except Exception as e:
                    self.ui.lineEdit_Swap_to_AssetBalance.clear()
                    self.ui.lineEdit_Swap_to_BalanceInUSD.clear()
                    
        except Exception as e:
            print(str(e))
            self.showSwapError(e)




    def getOutputToken(self):
        print("gSOPT")
        try:
            self.ui.lineEdit_Swap_Error.hide()
        except:
            pass
        try:
            self.ui.lineEdit_Swap_from_Amount.clear()
            self.ui.lineEdit_Swap_to_Amount.clear()
            self.ui.lineEdit_Swap_from_AmountInUSD.clear()
            self.ui.lineEdit_Swap_to_AmountInUSD.clear()
        except:
            pass
        self.initOutputToken()

        self.ui.lineEdit_Swap_to_AssetBalance.setText(str('%.08f' % self.outputTokenBalance))
        self.SwapOutputTokenUSD = self.web3.getTokenUSDPrice(self.outputTokenAddress)[0]
        TokenBalanceUSD = float(self.outputTokenBalance) * float(self.SwapOutputTokenUSD)
        self.ui.lineEdit_Swap_to_BalanceInUSD.setText(str('%.02f' % TokenBalanceUSD)+ " $")
        try:
            self.buy_tax_Out, self.sell_tax_Out, honeypot = self.web3.checkToken(self.outputTokenAddress, self.swap)
            self.ui.frame_OutPutTokenInfos.show()
            self.ui.lineEdit_OutputToken_BuyTax.setText(str(self.buy_tax_Out) + " %")
            self.ui.lineEdit_OutputToken_SellTax.setText(str(self.sell_tax_Out) + " %")
            self.minSlippage = int(self.sell_tax_In + self.buy_tax_Out + 1)
            self.ui.lineEdit_OutputToken_BuyTax.setStyleSheet(Sidebar.getResetStyleTokenTax())
            self.ui.lineEdit_OutputToken_SellTax.setStyleSheet(Sidebar.getResetStyleTokenTax())
            if int(self.sell_tax_Out) > 10: 
                self.ui.lineEdit_OutputToken_SellTax.setStyleSheet(Sidebar.getRedStyleTokenTax())
            if int(self.buy_tax_Out) > 10: 
                self.ui.lineEdit_OutputToken_BuyTax.setStyleSheet(Sidebar.getRedStyleTokenTax())
            self.SliderValueChangedSwapTokensSlippage()
            self.ui.label_SwapWayB.setPixmap(self.initTokenPixmap(self.swapoutputToken))
            

        except Exception as e:
            print(e)
        
    
    def getSwapInputAmount(self):
        try:
            self.ui.lineEdit_Swap_to_Amount.textChanged.disconnect()
        except:
            pass

        try:
            self.SwapInputAmount = float(self.ui.lineEdit_Swap_from_Amount.text())
            if type(self.SwapInputAmount) == float or int:
                print("F-gSIA")
                self.SwapInputAmountinUSD = float(self.SwapInputTokenUSD) * float(self.SwapInputAmount)
                self.ui.lineEdit_Swap_from_AmountInUSD.setText(str('%.03f' % self.SwapInputAmountinUSD) + str(' $'))
                print('InputAmount is :', self.SwapInputAmount)
                self.calcSwapOutput()
        except Exception as e:
            print(e)
            pass

        try:
            self.ui.lineEdit_Swap_to_Amount.textChanged.connect(self.getSwapOutputAmount)
        except:
            pass



    def getSwapOutputAmount(self):
        try:
            self.ui.lineEdit_Swap_from_Amount.textChanged.disconnect()
        except:
            pass

        try:
            self.SwapOutputAmount = float(self.ui.lineEdit_Swap_to_Amount.text())
            if type(self.SwapOutputAmount) == float or int:
                print("F-gSOA")
                self.SwapOutputAmountinUSD = float(self.SwapOutputTokenUSD) * float(self.SwapOutputAmount)
                self.ui.lineEdit_Swap_to_AmountInUSD.setText(str('%.03f' % self.SwapOutputAmountinUSD) + str(' $'))
                print('OutputAmount is :', self.SwapOutputAmount)
                self.calcSwapInput()
        except Exception as e:
            print(e,)

        try:
            self.ui.lineEdit_Swap_from_Amount.textChanged.connect(self.getSwapInputAmount)
        except:
            pass





    def calcSwapOutput(self):
        inputInBNB = float(self.SwapInputAmount) * float(self.inputTokenPriceBNB)
        outputTokens = self.takeSlippage(float(inputInBNB) / float(self.outputTokenPriceBNB), self.currentSlippage)
        self.SwapOutputAmount =  '%.08f' % outputTokens
        self.outputQuantinityUSD = float(outputTokens) * float(self.SwapOutputTokenUSD)
        self.ui.lineEdit_Swap_to_Amount.setText(str('%.08f' % outputTokens))
        self.ui.lineEdit_Swap_to_AmountInUSD.setText(str('%.02f' % self.outputQuantinityUSD) + " $") 



    def calcSwapInput(self):
        outputInBNB = float(self.SwapOutputAmount) * float(self.outputTokenPriceBNB)
        inputTokens = float(outputInBNB) / float(self.inputTokenPriceBNB)
        self.SwapInputAmount = '%.08f' % inputTokens
        self.inputQuantinityUSD = float(inputTokens) * float(self.SwapInputTokenUSD)
        self.ui.lineEdit_Swap_from_Amount.setText(str('%.08f' % inputTokens))
        self.ui.lineEdit_Swap_from_AmountInUSD.setText(str('%.02f' % self.inputQuantinityUSD) + " $")



    def ManageApproveButton(self):
            try:
                if self.swapInputToken != 'BNB':
                    try:
                        Approved = self.web3.checkisApprove(self.inputTokenAddress, self.SwapInputAmount, self.swap)
                    except:
                        self.SwapInputAmount = 1
                        Approved = self.web3.checkisApprove(self.inputTokenAddress, self.SwapInputAmount, self.swap)
                    if Approved == True:
                        self.ui.pushButton_approve_token.hide()
                        self.ui.pushButton_Confirm_Swap.show()
                    else:
                        self.ui.pushButton_approve_token.show()
                        self.ui.pushButton_Confirm_Swap.hide()
                        try:
                            self.ui.pushButton_approve_token.clicked.disconnect()
                        except:
                            pass
                        self.ui.pushButton_approve_token.clicked.connect(self.approveSwap)
                else:
                    self.ui.pushButton_approve_token.hide()
                    self.ui.pushButton_Confirm_Swap.show()
            except Exception as e:
                print(e)
                

    def qouteSwapInput(self):
        if str(self.outputTokenAddress) == str(self.web3.WETH):
            self.outputAmount = self.web3.getOutputfromTokentoETH(self.inputTokenAddress, self.SwapInputAmount, self.swap)
        elif str(self.inputTokenAddress) == str(self.web3.WETH):
            self.outputAmount = self.web3.getOutputfromETHtoToken(self.outputTokenAddress, self.SwapInputAmount, self.swap)
        else:
            self.outputAmount = self.web3.getOutputfromTokentoToken( self.inputTokenAddress, self.outputTokenAddress, self.SwapInputAmount, self.swap)
        self.outputQuantinity = self.outputAmount[0]
        self.outputWay = self.outputAmount[2]
        

    def confirmSwap(self):
        self.qouteSwapInput()
        self.openSwapConfirm()
        try:
            if str(self.inputTokenAddress) == str(self.web3.WETH):
                self.SgRawTX, Fee = self.web3.createfromETHtoTokenTX(self.outputTokenAddress, self.SwapInputAmount, self.swap, self.currentSlippage, self.currentSwapGAS)
            elif str(self.outputTokenAddress) == str(self.web3.WETH):
                self.SgRawTX, Fee = self.web3.createfromTokentoETHTX(self.inputTokenAddress, self.SwapInputAmount, self.swap, self.currentSlippage, self.currentSwapGAS)
            else:
                self.SgRawTX, Fee = self.web3.createfromTokentoTokenTX(self.inputTokenAddress, self.outputTokenAddress, self.SwapInputAmount, self.swap, self.currentSlippage, self.currentSwapGAS)
            self.ui.output_swap_GasBNB.setText(str('%.08f' % Fee))
            feeUSD = float(self.web3.getETHPrice()[0]) * float(Fee)
            self.ui.output_swap_GasUSD.setText(str('%.02f' % feeUSD) + "$")
            try:
                self.ui.pushButton_SwapConfirm.clicked.disconnect()
            except:
                pass
            try:
                self.ui.pushButton_SwapConfirm.show()
            except:
                pass
            self.ui.pushButton_Cancel_SwapConfirm.setText(str("Cancel"))
            try:
                self.ui.pushButton_back_To_Main.clicked.disconnect()
            except:
                pass
            self.ui.pushButton_back_To_Main.clicked.connect(self.backToSwapWithClean)
            self.ui.pushButton_SwapConfirm.clicked.connect(self.confirmSwapButtonClick)
        except Exception as e:
            self.ui.pushButton_SwapConfirm.hide()
            self.ui.pushButton_Cancel_SwapConfirm.setText(str(e))
            

    def confirmSwapButtonClick(self):
        self.CleanSwapButton()
        self.WaitTransactionWindow()


    def buttonOpenBSCExplorer(self):
        BSCTXURL = f"https://bscscan.com/tx/{self.TXHEX}"
        webbrowser.open(BSCTXURL)
        
        
    def approveSwap(self):
        self.SgRawTX, swappaddress, Fee = self.web3.approveToken(self.inputTokenAddress, self.swap, self.currentSwapGAS)
        name = self.web3.getTokenName(self.inputTokenAddress)
        self.ui.label_approve_TokenName.setText(str(name))
        self.ui.label_approv_tokenLogo.setPixmap(self.initTokenPixmapConfirm(self.inputTokenAddress))
        self.ui.output_approve_Address.setText(str(swappaddress))
        self.ui.output_approve_GasBNB.setText(str('%.08f' % Fee))
        feeUSD = float(self.web3.getETHPrice()[0]) * float(Fee)
        self.ui.output_approve_FeeUSD.setText(str('%.02f' % feeUSD) + "$")
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_approve_Confirm)
        try:
            self.ui.pushButton_approve_Confirm.clicked.diconnect()
        except:
            pass
        try:
            self.ui.pushButton_approve_cancel.clicked.diconnect()
        except:
            pass  
        self.ui.pushButton_approve_cancel.clicked.connect(self.SwapConfirmCancelButton)
        try:
            self.ui.pushButton_approve_cancel.clicked.diconnect()
        except:
            pass
        self.ui.pushButton_back_To_Main.clicked.connect(self.backToSwapWithApproveRefresh)


    def backToSwapWithClean(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_swapping)
        self.CleanSwapp()
        self.ManageApproveButton()


    def backToSwapWithApproveRefresh(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_swapping)
        self.ManageApproveButton()


    def takeSlippage(self, amount, slippage):
        return amount - ((amount*slippage) / 100)


    def CleanSwapp(self):
        try:
            self.ui.lineEdit_Swap_from_Amount.clear()
        except:
            pass
        try:
            self.ui.lineEdit_Swap_to_Amount.clear()
            self.ui.lineEdit_Swap_from_AmountInUSD.clear()
            self.ui.lineEdit_Swap_to_AmountInUSD.clear()
            self.ui.lineEdit_Swap_from_AssetBalance.clear()
            self.ui.lineEdit_Swap_to_AssetBalance.clear()
            self.ui.lineEdit_Swap_from_BalanceInUSD.clear()
            self.ui.lineEdit_Swap_to_BalanceInUSD.clear()
        except:
            pass
        self.initSwaps()
        self.initSwapFromTokens("")



    def Button(self):
        btnWidget = self.sender()
        if btnWidget.objectName() == "btn_wallet":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
            Sidebar.resetStyle(self, "btn_wallet")
            Sidebar.labelPage(self, "Wallet")
            self.refreshPrices()
            btnWidget.setStyleSheet(Sidebar.selectMenu(btnWidget.styleSheet()))

        if btnWidget.objectName() == "btn_send":
            self.initTokens()
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_sending)
            try:self.ui.lineEdit_Send_InfoField.hide()
            except:pass
            Sidebar.resetStyle(self, "btn_send")
            Sidebar.labelPage(self, "Send")
            btnWidget.setStyleSheet(Sidebar.selectMenu(btnWidget.styleSheet()))

        if btnWidget.objectName() == "btn_transactions":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_transactions)
            Sidebar.resetStyle(self, "btn_transactions")
            Sidebar.labelPage(self, "Transactions")
            self.fillTXList()
            btnWidget.setStyleSheet(Sidebar.selectMenu(btnWidget.styleSheet()))

        if btnWidget.objectName() == "btn_swapping":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_swapping)
            self.CleanSwapp()
            Sidebar.resetStyle(self, "btn_swapping")
            Sidebar.labelPage(self, "Swapping")
            btnWidget.setStyleSheet(Sidebar.selectMenu(btnWidget.styleSheet()))

        if btnWidget.objectName() == "btn_settings":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_settings)
            Sidebar.resetStyle(self, "btn_settings")
            Sidebar.labelPage(self, "Settings")
            self.fillProviderList()
            btnWidget.setStyleSheet(Sidebar.selectMenu(btnWidget.styleSheet()))

        if btnWidget.objectName() == "btn_limitorders":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_limitOrders)
            Sidebar.resetStyle(self, "btn_limitorders")
            Sidebar.labelPage(self, "Limit Orders")
            btnWidget.setStyleSheet(Sidebar.selectMenu(btnWidget.styleSheet()))


    def initTokenTablePixmap(self,Tokensymbol):
        try:
            imageLabel = QLabel()
            imageLabel.setText('')
            imageLabel.setScaledContents(True)
            pixmap = QPixmap()
            pixmap.loadFromData(self.db.SelectFromWhereIs(Select='LOGOURI', From='TOKENS', Where='NAME', Is=Tokensymbol),'png')  
            pixmap = pixmap.scaled(90, 90,  Qt.KeepAspectRatio) 
            imageLabel.setPixmap(pixmap)
            return imageLabel
        except Exception as e:
            print(e)

    def getTokenTablePixmap(self, TokenSymbol):
        try:
            imageLabel = QLabel()
            imageLabel.setText('')
            imageLabel.setScaledContents(True)
            pixmap = QPixmap()
            pixmap.loadFromData(self.db.SelectFromWhereIs(Select='LOGOURI', From='TOKENS', Where='SYMBOL', Is=TokenSymbol),'png')  
            pixmap = pixmap.scaled(90, 90,  Qt.KeepAspectRatio) 
            imageLabel.setPixmap(pixmap)
            return imageLabel
        except:
            imageLabel = QLabel()
            imageLabel.setText('')
            imageLabel.setScaledContents(True)
            pixmap = QPixmap()
            pixmap.loadFromData(self.db.SelectFromWhereIs(Select='image', From='swapcontracts', Where='name', Is="ERC20"),'png')  
            pixmap = pixmap.scaled(90, 90,  Qt.KeepAspectRatio) 
            imageLabel.setPixmap(pixmap)
            return imageLabel

    def SwapConfirmCancelButton(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_swapping)
        

    def enableDisabled(self,name):
        try:
            status = self.db.SelectFromWhereIs(Select='activ',From='TOKENS', Where='NAME', Is=name)
            if status == 0:
                self.db.UpdateWhereIsTo(Update='TOKENS', Set='ACTIV', To='1' , Where='NAME', Is=name)
            if status == 1:
                self.db.UpdateWhereIsTo(Update='TOKENS', Set='ACTIV', To='0' , Where='NAME', Is=name)
            self.fillAllTokensList()
        except Exception as e:
            print(e)
            self.fillAllTokensList()


    def getAddTokenInfos(self):
        tokenAddress = self.ui.input_add_TokenAddresse.displayText()
        if len(tokenAddress) > 41:
            try:
                tokenAddress = self.web3.getChecksumAddress(tokenAddress)
                Decimals = self.web3.getTokenDecimal(tokenAddress)
                Name = self.web3.getTokenName(tokenAddress)
                Symbol = self.web3.getTokenSymbol(tokenAddress)
                self.ui.input_add_TokenAddresse.setText(tokenAddress)
                self.ui.input_add_TokenName.setText(Name)
                self.ui.input_add_TokenSymbol.setText(Symbol)
                self.ui.input_add_TokenDecimals.setText(str(Decimals))
            except Exception as e:
                print(e)

    def saveToken(self):
        Token = self.ui.input_add_TokenAddresse.displayText()
        if len(Token) > 41:
            TokenName = self.ui.input_add_TokenName.displayText()
            TokenSymbol = self.ui.input_add_TokenSymbol.displayText()
            TokenDecimals = self.ui.input_add_TokenDecimals.displayText()
            TokenIMG = self.ui.input_add_Token_IMGURL.displayText()
            booler = self.db.addToken(TokenName, TokenSymbol, Token, TokenDecimals, TokenIMG)
            if booler == False:
                self.ui.label_add_Token_Error.setText("Token Symbol\nallready used!")
                self.ui.label_add_Token_Error.show()
            if booler == True:
                self.ui.label_add_Token_Error.setStyleSheet(u"""
                font: bold;
                font-size: 18px;
                color:rgb(19, 150, 16);
                border-radius: 15px;
                background-color: rgb(33, 37, 43);
                qproperty-alignment: AlignCenter;
                """)
                self.ui.label_add_Token_Error.setText("Sucessfully\nAdded!")
                self.ui.label_add_Token_Error.show()
                self.ui.input_add_TokenAddresse.clear()
                TokenName = self.ui.input_add_TokenName.clear()
                TokenSymbol = self.ui.input_add_TokenSymbol.clear()
                TokenDecimals = self.ui.input_add_TokenDecimals.clear()
                TokenIMG = self.ui.input_add_Token_IMGURL.clear()
        else:
            self.ui.label_add_Token_Error.setText("Wrong\nToken\nAddress!")
            self.ui.label_add_Token_Error.show()


    def delete(self, name):
        self.db.deleteToken(name)
        self.fillAllTokensList()
        

    def createDeleteButton(self, name):
        button = QPushButton()
        button.setText("DELETE")
        button.setStyleSheet(u"""
        QPushButton {
            font: bold;
	        font-size: 14px;
            color: rgb(220, 161, 1);
	        border-radius: 15px;
            background-color: rgb(33, 37, 43);
	        border: 6px solid rgb(33, 37, 43);
            }
        QPushButton:hover {
        	background-color: rgb(39, 44, 54);
            }
        QPushButton:pressed {	
        	background-color: rgb(85, 170, 255);
            }
        """)
        #button.setMaximumSize(80,40)
        button.resize(80, 40)
        button.clicked.connect(lambda: self.delete(name))
        return button


    def createWeb1ButtonBSCScan(self, name):
        button = QPushButton()
        button.setText("Show TX")
        button.setStyleSheet(u"""
        QPushButton {
            font: bold;
	        font-size: 14px;
            color: rgb(220, 161, 1);
	        border-radius: 12px;
            background-color: rgb(33, 37, 43);
	        border: 6px solid rgb(33, 37, 43);
            }
        QPushButton:hover {
        	background-color: rgb(39, 44, 54);
            }
        QPushButton:pressed {	
        	background-color: rgb(85, 170, 255);
            }
        """)
        #button.setMaximumSize(80,40)
        button.resize(80, 40)
        button.clicked.connect(lambda: web1.open(name))
        return button


    def createCheckBox(self,bool,name):
        checkbox =  QCheckBox()
        checkbox.setChecked(bool)
        checkbox.stateChanged.connect(lambda: self.enableDisabled(name))
        return checkbox


    def fillAllTokensList(self):
        self.ui.tableWidget_AllTokensinDB.setRowCount(1)
        try:
            row = 1
            alltokens = len(self.db.SelectFrom(Select='NAME', From='TOKENS')) + 10 # +10 for placeholder, to avoid bad Style.
            self.ui.tableWidget_AllTokensinDB.setRowCount(alltokens)
            for token in self.db.SelectFromWithOption(Select='*', From='TOKENS',OrderBy='activ', ASC=False):
                try:
                    self.ui.tableWidget_AllTokensinDB.setCellWidget(row, 0, self.initTokenTablePixmap(Tokensymbol=token[1]))
                    self.ui.tableWidget_AllTokensinDB.setItem(row, 1,  QTableWidgetItem(token[2]))
                    self.ui.tableWidget_AllTokensinDB.setItem(row, 2,  QTableWidgetItem(token[1]))
                    if token[2].lower() != "tigs":
                        if token[2].lower() != "bnb":
                            if token[2].lower() != "busd":
                                if token[2].lower() != "usdt":
                                    self.ui.tableWidget_AllTokensinDB.setCellWidget(row, 4, self.createDeleteButton(name=token[2]))                
                                    if int(token[7]) == 0:
                                        self.ui.tableWidget_AllTokensinDB.setCellWidget(row, 3, self.createCheckBox(bool=False,name=token[1]))
                                    if int(token[7]) == 1:
                                        self.ui.tableWidget_AllTokensinDB.setCellWidget(row, 3, self.createCheckBox(bool=True,name=token[1]))
                    row=row+1
                except Exception as e:
                    print(e)

        except Exception as e:
            print(e)

###################################
#    SITES
###################################

    def EnableDisableTokenSide(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_EnableDisableTokens)
        self.fillAllTokensList()
        Sidebar.labelPage(self, "Manage Tokens")
        try:
            self.ui.label_add_Token_Error.hide()
        except:
            pass

    def BackToSettings(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_settings)
        Sidebar.labelPage(self, "Settings")

    def backtoMain(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
        Sidebar.labelPage(self, "Overview")

    def backToSending(self):
        self.initTokens()
        self.CleanALL()
        try:
            self.ui.lineEdit_Send_InfoField.hide()
        except:
            pass
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_sending)
        Sidebar.labelPage(self, "Send")

    def SetupTokenOverview(self):
        row = 1
        for token in self.db.SelectFrom(Select='SYMBOL', From='TOKENS'):
            if int(self.db.SelectFromWhereIs(Select='ACTIV', From='TOKENS', Where='SYMBOL',Is=token[0])) == 1:
                row += 1
        self.ui.tableWidget_AllActivTokens.setRowCount(row)
        self.fillIndex = 1
        for token in self.db.SelectFrom(Select='SYMBOL', From='TOKENS'):
            self.fillToken = token
            self.fillNextTokenOverviewToken()
            self.fillIndex = self.fillIndex + 1

    def fillNextTokenOverviewToken(self):
        return self.fillTokenOverview(self.fillToken, self.fillIndex)


    def fillTokenOverview(self, token, i):
        try:
            tokenAddress = self.db.SelectFromWhereIs(Select='ADDRESS', From='TOKENS', Where='SYMBOL',Is=token[0])
            print(token[0], tokenAddress)
            if token[0] == "BNB":
                tokenName = "Binance Coin"
                tokenBalance = self.web3.getETHBalance()[0]
                tokenPriceUSD =self.web3.getETHPrice()[0]
                tokenBalanceinUsd = float(tokenBalance) * float(tokenPriceUSD)
                return "ok"
            else:
                tokenName = self.web3.getTokenName(tokenAddress)
                tokenBalance = self.web3.getTokenBalance(tokenAddress)[0]
                tokenPriceUSD =self.web3.getTokenUSDPrice(tokenAddress)[0]
                tokenBalanceinUsd = float(tokenBalance) * float(tokenPriceUSD)
                print(tokenName)
                print(tokenBalance)
                print(tokenPriceUSD)
                print(tokenBalanceinUsd)
                print(token[0], tokenName, tokenBalance, tokenPriceUSD, tokenBalanceinUsd)

            pixmap = self.getTokenTablePixmap(token[0])

            self.ui.tableWidget_AllActivTokens.setCellWidget(i, 0, pixmap )
            self.ui.tableWidget_AllActivTokens.setItem(i, 1,  QTableWidgetItem(token[0]))
            self.ui.tableWidget_AllActivTokens.setItem(i, 2,  QTableWidgetItem(tokenName))
            self.ui.tableWidget_AllActivTokens.setItem(i, 3,  QTableWidgetItem(str(tokenPriceUSD)))
            self.ui.tableWidget_AllActivTokens.setItem(i, 4,  QTableWidgetItem(str(tokenBalance)))
            self.ui.tableWidget_AllActivTokens.setItem(i, 5,  QTableWidgetItem(str(tokenBalanceinUsd)))
            return "ok"

        except Exception as e:  
            print(e)
            return str(e)

    def ToTokenOverView(self):
        self.SetupTokenOverview()
        Sidebar.labelPage(self, "Token Overview")
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_TokenOverview)

    def ToAddTokenOverView(self):
        Sidebar.labelPage(self, "ADD TOKEN")
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_addToken)

    def WaitTransactionWindow(self):
        try:
            self.ui.pushButton_TxBscView.hide()
        except:
            pass
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_WaitingForConfirm)
        self.ui.lineEdit_Info_Confirmation.setText('Wait for confirms..')
        self.movie = QMovie(r'logos/Spinner.gif')
        self.ui.label_Waiting_Confirm.setMovie(self.movie)
        self.movie.start()

        worker = AWorker(self.executeTX)
        worker.signals.result.connect(self.txResult)
        self.threadpool.start(worker)

        
    def txResult(self, a, b):
        try:
            if a == True:
                self.TXSuccessIMG(b)
            elif a == False:
                self.TXFailIMG(b)
        finally:
            del self.SgRawTX

    def executeTX(self):
        return self.web3.sendRawTransactionAndWaiteConfirm(self.SgRawTX)

    def ConfirmSite(self, symbol, receiver, amount, fee):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_confirm)
        Sidebar.labelPage(self, "Confirm")
        self.ui.label_send_TokenName.setText(str(self.db.SelectFromWhereIs(Select='NAME', From='TOKENS', Where='SYMBOL', Is=symbol)))
        self.ui.output_send_TokenAmount.setText(str('%.08f' % amount))
        self.ui.output_send_rece.setText(receiver)
        self.ui.output_send_TokenGasBNB.setText(str('%.08f' % fee))
        self.ui.output_send_TokenUSD_2.setText(str(self.ui.lineEdit_SendAmountUSD.text()))
        self.ui.output_send_FeeUSD.setText(str('%.02f' % (float(fee) * float(self.BNBprice)))+ str(' $'))
        try:
            self.CleanSend()
        except:
            pass
        self.ui.pushButton_SendConfirm.clicked.connect(self.WaitTransactionWindow)
        

    def refreshAllTokens(self):
        self.fillAllTokensList()
        print('filled')

    def SendButton(self):
        try:self.ui.lineEdit_Send_InfoField.hide()
        except:pass
        symbol = self.ui.comboBox_sending_Asset.currentText()

        receiver = self.ui.lineEdit_send_receiver.text()
        try:
            amount = float(self.ui.lineEdit_SendAmount.text())
        except:
            amount = self.ui.lineEdit_SendAmount.text()
        if len(receiver) == 42:
            if isinstance(amount, (int, float)) == True:
                try:
                    self.SgRawTX, Fee = self.web3.checkSendAssetAndCreateTX(receiver, symbol, amount, self.currentSwapGAS)
                    self.ConfirmSite(symbol,receiver,amount, Fee)
                except:
                    self.ui.lineEdit_Send_InfoField.show()
                    self.ui.lineEdit_Send_InfoField.setText('Please check Input Token')   
                try:
                    self.ui.pushButton_back_To_Main.clicked.disconnect()
                except:
                    pass
                self.ui.pushButton_back_To_Main.clicked.connect(self.backToSending)
            else:
                self.ui.lineEdit_Send_InfoField.show()
                self.ui.lineEdit_Send_InfoField.setText('Please check Amount (e.g. 0.001 or 1)')        
        else:
            self.ui.lineEdit_Send_InfoField.show()
            self.ui.lineEdit_Send_InfoField.setText('Please check receive address')


    def SliderValueChangedSendTokens(self):
        currentValue = self.ui.slider_gasSend.value()
        self.ui.lineEdit_gasSendGwei.setText(str(currentValue) + str(' Gwei'))


    def SliderValueChangedSwapTokens(self):
        self.currentSwapGAS = self.ui.slider_GasGwei_Swap.value()
        self.ui.output_GasGwei_Swap.setText(str(self.currentSwapGAS) + str(' Gwei'))


    def SliderValueChangedSwapTokensSlippage(self):
        self.currentSlippage = self.ui.slider_Slippage_Swap.value()
        if self.currentSlippage < self.minSlippage:
            self.currentSlippage = self.minSlippage
            self.ui.slider_Slippage_Swap.setValue(self.minSlippage)
        self.ui.output_Slippage_Swap.setText(str(self.currentSlippage) + str(' %'))


    def TXSuccessIMG(self, txWait):
        pixmap = QPixmap(r'logos/success.png')
        pixmap = pixmap.scaled(300, 300,  Qt.KeepAspectRatio)
        self.ui.label_Waiting_Confirm.setPixmap(pixmap)
        self.ui.lineEdit_Info_Confirmation.setText('Successfully')
        try:
            self.ui.lineEdit_Info_Confirmation.setText(str(txWait))
            self.TXHEX = txWait
            self.ui.pushButton_TxBscView.show()
        except Exception as e:
            print(e)


    def TXFailIMG(self, error):
        pixmap = QPixmap(r'logos/fail.png') 
        pixmap = pixmap.scaled(300, 300,  Qt.KeepAspectRatio) 
        self.ui.label_Waiting_Confirm.setPixmap(pixmap)
        self.ui.lineEdit_Info_Confirmation.setText(str(error)) 
        

    def eventFilter(self, watched, event):
        if watched == self.le and event.type() == QEvent.MouseButtonDblClick:
            print("pos: ", event.pos())

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
        if event.buttons() == Qt.LeftButton:
            pass
            #print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            pass
            #print('Mouse click: RIGHT CLICK')
        if event.buttons() == Qt.MidButton:
            pass
            #print('Mouse click: MIDDLE BUTTON')
    
    #def resizeEvent(self, event):
    #    self.resizeFunction()
    #    return super(MainWindow, self).resizeEvent(event)
   
    
    def CleanSwapButton(self):
        self.ui.pushButton_SwapConfirm.clicked.disconnect()
        self.CleanALL()

    def CleanSwapApproveButtonSwap(self):
        self.ui.pushButton_approve_token.clicked.disconnect()
        self.CleanALL()

    def CleanSend(self):
        self.ui.pushButton_SendConfirm.clicked.disconnect()
        self.CleanALL()

    def CleanALL(self):
        self.ui.lineEdit_SendAmount.clear()
        self.ui.lineEdit_SendAmountUSD.clear()
        self.ui.lineEdit_send_receiver.clear()
        self.ui.lineEdit_Swap_from_Amount.clear()
        self.ui.lineEdit_Swap_from_AmountInUSD.clear()
        self.ui.lineEdit_Swap_to_Amount.clear()
        self.ui.lineEdit_Swap_to_AmountInUSD.clear()


    def fillTXList(self):
        try:
            i = 0
            txns = self.api.getTXList(self.address)
            rowlenght = len(txns)
            self.ui.tableWidget_transactions.setRowCount(rowlenght)
            for l in txns:
                i += 1
                blockNumber = l['blockNumber']
                timeStamp = datetime.utcfromtimestamp(int(l['timeStamp'])).strftime('%Y-%m-%d %H:%M:%S')
                txhash = l['hash']
                gas = l['gas']
                gasPrice = l['gasPrice']
                gasUsed = l['gasUsed']
                bnb = float(int(l['value']) / (10**18))
                gas =  float(int(gasPrice)*int(gasUsed) / (10**18))
                bnbvalue = str('%.08f' % bnb) + " BNB"
                realgas = str('%.08f' % gas) + " BNB"
                confirmations = l['confirmations']
                bscLink = f"https://bscscan.com/tx/{txhash}"
                self.ui.tableWidget_transactions.setItem(i, 0, QTableWidgetItem(timeStamp))
                self.ui.tableWidget_transactions.setItem(i, 1, QTableWidgetItem(confirmations))
                self.ui.tableWidget_transactions.setItem(i, 2, QTableWidgetItem(blockNumber))
                self.ui.tableWidget_transactions.setItem(i, 3, QTableWidgetItem(bnbvalue))
                self.ui.tableWidget_transactions.setItem(i, 4, QTableWidgetItem(realgas))
                self.ui.tableWidget_transactions.setItem(i, 5, QTableWidgetItem(txhash))
                self.ui.tableWidget_transactions.setCellWidget(i, 6, self.createWeb1ButtonBSCScan(bscLink))
        except Exception as e:
            print(e)


    def fillProviderList(self):
        self.ui.tableWidget_Provider_Options.setRowCount(1)
        allProviders = self.db.SelectFrom("*","Providers")
        self.ui.tableWidget_Provider_Options.setRowCount(len(allProviders) + 1)
        print(len(allProviders))
        i = 0
        for Provider in allProviders:
            try:
                i += 1
                print(Provider)
                Name = Provider[1]
                RPC = Provider[2]
                Default = Provider[3]
                Feedback = web3FeedbackCheck().runTest(Provider[2])
                if Default == 1:
                    checkedWidget = self.checkBoxProvider(True, RPC)
                else:
                    checkedWidget = self.checkBoxProvider(False, RPC)
                    self.ui.tableWidget_Provider_Options.setCellWidget(i, 5, self.createDeleteProviderButton(RPC))

                self.ui.tableWidget_Provider_Options.setCellWidget(i, 0, checkedWidget)
                self.ui.tableWidget_Provider_Options.setItem(i, 1, QTableWidgetItem(str(Name)))
                self.ui.tableWidget_Provider_Options.setItem(i, 2, QTableWidgetItem(str(RPC)))
                self.ui.tableWidget_Provider_Options.setItem(i, 3, QTableWidgetItem(str(Feedback[3])))
                self.ui.tableWidget_Provider_Options.setItem(i, 4, QTableWidgetItem(str(Feedback[1])+ " MS"))
            except:
                i -= 1


    def createDeleteProviderButton(self, RPC):
        button = QPushButton()
        button.setText("DELETE")
        button.setStyleSheet(u"""
        QPushButton {
            font: bold;
	        font-size: 14px;
            color: rgb(220, 161, 1);
	        border-radius: 15px;
            background-color: rgb(33, 37, 43);
	        border: 6px solid rgb(33, 37, 43);
            }
        QPushButton:hover {
        	background-color: rgb(39, 44, 54);
            }
        QPushButton:pressed {	
        	background-color: rgb(85, 170, 255);
            }
        """)
        #button.setMaximumSize(80,40)
        button.resize(80, 40)
        button.clicked.connect(lambda: self.deleteProvider(RPC))
        return button


    def deleteProvider(self, RPC):
        self.db.deleteRPC(RPC)
        self.fillProviderList()


    def checkBoxProvider(self, bool, NewMainProvider):
        checkbox = QCheckBox()
        checkbox.setChecked(bool)
        if bool != True:
            checkbox.stateChanged.connect(lambda: self.enableDisableMainProvider(NewMainProvider))
        return checkbox      


    def enableDisableMainProvider(self, NewMainProvider):
        self.db.setDefaultProvider(NewMainProvider)
        self.web3.refreshWEB3()
        self.fillProviderList()



    def addNewProvider(self):
        Name = self.ui.input_add_ProviderName.text()
        if len(Name) >= 1:
            URL = self.ui.input_add_ProviderURL.text()
            Feedback = web3FeedbackCheck().runTest(URL)
            try:
                if Feedback[0] == True:
                    Added = self.db.addProvider(Name, URL)
                    if Added == True:
                        self.ui.frame_add_Provider.hide()
                        self.ui.input_add_ProviderName.clear()
                        self.ui.input_add_ProviderURL.clear()
                        self.fillProviderList()
                    else:
                        self.ui.lineEdit_add_provider_Error.setText("RPC Allready in DB!")
                        self.ui.lineEdit_add_provider_Error.show()

                else:
                    self.ui.lineEdit_add_provider_Error.setText("Not Supported or No Respone!")
                    self.ui.lineEdit_add_provider_Error.show()

            except Exception as e:
                print(e)
                self.ui.lineEdit_add_provider_Error.setText("Check Provider is Online!")
                self.ui.lineEdit_add_provider_Error.show()

        else:
            self.ui.lineEdit_add_provider_Error.setText("Check Name!")
            self.ui.lineEdit_add_provider_Error.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    QFontDatabase.addApplicationFont('fonts/segoeui.ttf')
    QFontDatabase.addApplicationFont('fonts/segoeuib.ttf')
    window = MainWindow()
    sys.exit(app.exec_())