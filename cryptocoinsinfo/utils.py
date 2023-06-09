import logging
from logging.handlers import TimedRotatingFileHandler

from cryptocoinsinfo.reply_markups import *
from cryptocoinsinfo.config import *

# start logging to the file of current directory or º it to console
# logging.basicConfig(level=logging.INFO,
#                     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# module_logger = logging.getLogger(__name__)

# start logging to the file with log rotation at midnight of each day
formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')
handler = TimedRotatingFileHandler(os.path.dirname(os.path.realpath(__file__)) + '/../cryptocoinsinfobot.log',
                                   when='midnight',
                                   backupCount=10)
handler.setFormatter(formatter)
module_logger = logging.getLogger(__name__)
module_logger.addHandler(handler)
module_logger.setLevel(logging.INFO)
# end of log section


# the functions for logging handlers
def command_info(update):

    if update:
        us_message = str(update.effective_message.text) if update.effective_message.text else 'None'

        usr_name = update.message.from_user.first_name
        if update.message.from_user.last_name:
            usr_name += ' ' + update.message.from_user.last_name
        if update.message.from_user.username:
            usr_name += ' (@' + update.message.from_user.username + ')'

        us_chat_id = str(update.message.from_user.id) if update.message.from_user.id else 'None'

        module_logger.info("Has received a command \"{}\" from user {}, with id {}".format(us_message, usr_name, us_chat_id))


def message_info(update):

    if update:
        us_message = str(update.message.text) if update.message.text else 'None'

        usr_name = update.message.from_user.first_name
        if update.message.from_user.last_name:
            usr_name += ' ' + update.message.from_user.last_name
        if update.message.from_user.username:
            usr_name += ' (@' + update.message.from_user.username + ')'

        # old use of this user_name, bcz of an error in logs
        # us_first_name = str(update.message.from_user.first_name) if update.message.from_user.first_name else 'None'

        us_chat_id = str(update.message.from_user.id) if update.message.from_user.id else 'None'

        module_logger.info("Has received a message"
                           " \"{}\" from user {}, with id {}".format(us_message, usr_name, us_chat_id))


# work with a user's message from update
def text_simple(usr_msg_text):

    from cryptocoinsinfo.parse_apis import parse_api_coinmarketcapjson, parse_api_cryptocomparejson

    # always working with an uppercased text
    usr_msg_text = usr_msg_text.upper()

    menu_text_response = ''
    api_response1 = ''
    api_response2 = ''
    reply_markup_response = ''

    if "⬅ page 1".upper() == usr_msg_text:
        menu_text_response = 'page 1'
        reply_markup_response = reply_markup_p1

    elif "page 2 ➡".upper() == usr_msg_text or '⬅ page 2'.upper() in usr_msg_text:
        menu_text_response = 'page 2'
        reply_markup_response = reply_markup_p2

    elif "page 3 ➡".upper() == usr_msg_text:
        menu_text_response = 'page 3'
        reply_markup_response = reply_markup_p3

    elif "feedback".upper() == usr_msg_text:
        menu_text_response = 'Your Thoughts are Valuable For Us ' + YOUR_TELEGRAM_ALIAS \
                               + '\n\n🇬🇧 Send your opinion about the bot to ' + YOUR_TELEGRAM_ALIAS + ', please'
        reply_markup_response = reply_markup_p3

    # elif "settings" in usr_msg_text:
    #     text_response = 'coming soon... maybe'
    #     reply_markup_response = reply_markup_p3

    elif "Buy_Now".upper() == usr_msg_text:
        menu_text_response = '\n\n https://app.uniswap.org/#/swap?inputCurrency=ETH&outputCurrency=0xbbbddf9c6914bec7950ae6663eca9055aacec816'
        reply_markup_response = reply_markup_p1

    elif "Website".upper() == usr_msg_text:
        menu_text_response = '\n\n https://www.dinoegg.org/'
        reply_markup_response = reply_markup_p3

    elif "Chart".upper() == usr_msg_text:
        menu_text_response = '\n\n https://www.dextools.io/app/en/ether/pair-explorer/0x40091D14Cb8D8A4E5a32f7aD3D0Adff184a64B7F'
        reply_markup_response = reply_markup_p1

    elif "EOS".upper() == usr_msg_text:
        api_response1 = parse_api_coinmarketcapjson('EOS')
        api_response2 = parse_api_cryptocomparejson('EOS')
        reply_markup_response = reply_markup_p3

    elif "Coin_Discovery".upper() == usr_msg_text:
        menu_text_response = '\n\n https://coindiscovery.app/coin/dino-egg-ai/overview'
        reply_markup_response = reply_markup_p1

    elif "Bitcoin".upper() == usr_msg_text:
        api_response1 = parse_api_coinmarketcapjson('BTC')
        api_response2 = parse_api_cryptocomparejson('BTC')
        reply_markup_response = reply_markup_p2

    elif "Twitter".upper() == usr_msg_text:
        menu_text_response = '\n\n https://twitter.com/DinoEggAI'
        reply_markup_response = reply_markup_p1


    elif "Shiba".upper() == usr_msg_text:
        api_response1 = parse_api_coinmarketcapjson('SHIB')
        api_response2 = parse_api_cryptocomparejson('SHIB')
        reply_markup_response = reply_markup_p2

    elif "Dai".upper() == usr_msg_text:
        api_response1 = parse_api_coinmarketcapjson('DAI')
        api_response2 = parse_api_cryptocomparejson('DAI')
        reply_markup_response = reply_markup_p2

    elif "Ethereum".upper() == usr_msg_text:
        api_response1 = parse_api_coinmarketcapjson('ETH')
        api_response2 = parse_api_cryptocomparejson('ETH')
        reply_markup_response = reply_markup_p2

    elif "Monero".upper() == usr_msg_text:
        api_response1 = parse_api_coinmarketcapjson('XMR')
        api_response2 = parse_api_cryptocomparejson('XMR')
        reply_markup_response = reply_markup_p3

    elif "NEO".upper() == usr_msg_text:
        api_response1 = parse_api_coinmarketcapjson('NEO')
        api_response2 = parse_api_cryptocomparejson('NEO')
        reply_markup_response = reply_markup_p3

    elif "Stellar".upper() == usr_msg_text:
        api_response1 = parse_api_coinmarketcapjson('XLM')
        api_response2 = parse_api_cryptocomparejson('XLM')
        reply_markup_response = reply_markup_p3
    else:
        api_response1 = parse_api_coinmarketcapjson(usr_msg_text)
        api_response2 = parse_api_cryptocomparejson(usr_msg_text)

    return {'apiresponse1': api_response1, 'apiresponse2': api_response2,
            'menutextresponse': menu_text_response, 'replymarkupresponse': reply_markup_response}
