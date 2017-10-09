import requests
import misc
from poloniex import get_btc, get_dash, get_ltc, get_nxt, get_str, get_xmr, get_xrp, get_eth, get_etc, get_rep, get_zec, get_bch
from time import sleep

token = misc.token
print(token)

URL = 'https://api.telegram.org/bot'+token+'/'

global last_update_id
last_update_id = 0

def get_updates():
    url = URL+'getupdates'
    r = requests.get(url)
    return r.json()


def get_message():

    data = get_updates()
    last_object = data['result'][-1]
    current_update_id = last_object['update_id']

    global last_update_id
    if last_update_id != current_update_id:
        last_update_id = current_update_id

        chat_id = last_object['message']['chat']['id']
        message_text = last_object['message']['text']

        message = {'chat_id': chat_id,
                   'text': message_text}

        return message
    return None


def send_message(chat_id, text='Wait a second, please...'):
    url = URL+'sendmessage?chat_id={}&text={}'.format(chat_id, text)
    requests.get(url)


def main():
    # d = get_updates()

    while True:
        answer = get_message()
        if answer != None:
            chat_id = answer['chat_id']
            text = answer['text']

            if text == '/btc':
                send_message(chat_id, get_btc())
        if answer != None:
            chat_id = answer['chat_id']
            text = answer['text']

            if text == '/dash':
                send_message(chat_id, get_dash())
        if answer != None:
            chat_id = answer['chat_id']
            text = answer['text']

            if text == '/ltc':
                send_message(chat_id, get_ltc())
        if answer != None:
            chat_id = answer['chat_id']
            text = answer['text']

            if text == '/nxt':
                send_message(chat_id, get_nxt())
        if answer != None:
            chat_id = answer['chat_id']
            text = answer['text']

            if text == '/str':
                send_message(chat_id, get_str())
        if answer != None:
            chat_id = answer['chat_id']
            text = answer['text']

            if text == '/xmr':
                send_message(chat_id, get_xmr())
        if answer != None:
            chat_id = answer['chat_id']
            text = answer['text']

            if text == '/xrp':
                send_message(chat_id, get_xrp())
        if answer != None:
            chat_id = answer['chat_id']
            text = answer['text']

            if text == '/eth':
                send_message(chat_id, get_eth())
        if answer != None:
            chat_id = answer['chat_id']
            text = answer['text']

            if text == '/etc':
                send_message(chat_id, get_etc())
        if answer != None:
            chat_id = answer['chat_id']
            text = answer['text']

            if text == '/rep':
                send_message(chat_id, get_rep())
        if answer != None:
            chat_id = answer['chat_id']
            text = answer['text']

            if text == '/zec':
                send_message(chat_id, get_zec())
        if answer != None:
            chat_id = answer['chat_id']
            text = answer['text']

            if text == '/bch':
                send_message(chat_id, get_bch())
        if answer != None:
            pass

        else:
            continue

        sleep(3)

if __name__ == '__main__':
    main()