![TradingTigers](https://trading-tigers.com/logos/TradingTigers.png)  
---
## Installation docs for Binance Smart Chain DeFi Wallet by Trading-Tigers.com 

# Install on Linux:
Open a Terminal:
```shell
sudo apt-get update
sudo apt-get install git build-essential python3-dev python3-pip -y
git clone https://github.com/Trading-Tiger/BSC_TradingTigersWalletV2
cd BSC_TradingTigersWalletV2
python3 -m pip install -r requirements.txt

```
# Install on Windows:
Install from code is a bit more complicated or make it simple and download from [RELEASES](https://github.com/Trading-Tiger/BSC_TradingTigersWalletV2/releases) installer.  

- You need Microsoft Visual C++ Build Tools, Git, Python3 installed on your machine and added to your path.
When you have made sure that this is installed, open a CMD and paste the following:
```shell
git clone https://github.com/Trading-Tiger/BSC_TradingTigersWalletV2
cd BSC_TradingTigersWalletV2
python3 -m pip install -r requirements.txt

```


# Start:
Before the first start, you must rename in "database the User-Data.db.example" to "User-Data.db".
```shell
mv database/USER-DATA.db.example database/USER-DATA.db

```

When the installations commands have run through without error, you can Start.

```shell
python3 main.py

```
