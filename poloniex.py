import requests



def get_btc():
    url = 'https://poloniex.com/public?command=returnTicker'
    response = requests.get(url).json()
    price = response['USDT_BTC']['last']
    return str(price) + ' usd'

def get_dash():
    url = 'https://poloniex.com/public?command=returnTicker'
    response = requests.get(url).json()
    price = response['USDT_DASH']['last']
    return str(price) + ' usd'

def get_ltc():
    url = 'https://poloniex.com/public?command=returnTicker'
    response = requests.get(url).json()
    price = response['USDT_LTC']['last']
    return str(price) + ' usd'

def get_nxt():
    url = 'https://poloniex.com/public?command=returnTicker'
    response = requests.get(url).json()
    price = response['USDT_NXT']['last']
    return str(price) + ' usd'

def get_str():
    url = 'https://poloniex.com/public?command=returnTicker'
    response = requests.get(url).json()
    price = response['USDT_STR']['last']
    return str(price) + ' usd'

def get_xmr():
    url = 'https://poloniex.com/public?command=returnTicker'
    response = requests.get(url).json()
    price = response['USDT_XMR']['last']
    return str(price) + ' usd'

def get_xrp():
    url = 'https://poloniex.com/public?command=returnTicker'
    response = requests.get(url).json()
    price = response['USDT_XRP']['last']
    return str(price) + ' usd'

def get_eth():
    url = 'https://poloniex.com/public?command=returnTicker'
    response = requests.get(url).json()
    price = response['USDT_ETH']['last']
    return str(price) + ' usd'

def get_etc():
    url = 'https://poloniex.com/public?command=returnTicker'
    response = requests.get(url).json()
    price = response['USDT_ETC']['last']
    return str(price) + ' usd'

def get_rep():
    url = 'https://poloniex.com/public?command=returnTicker'
    response = requests.get(url).json()
    price = response['USDT_REP']['last']
    return str(price) + ' usd'

def get_zec():
    url = 'https://poloniex.com/public?command=returnTicker'
    response = requests.get(url).json()
    price = response['USDT_ZEC']['last']
    return str(price) + ' usd'

def get_bch():
    url = 'https://poloniex.com/public?command=returnTicker'
    response = requests.get(url).json()
    price = response['USDT_BCH']['last']
    return str(price) + ' usd'

