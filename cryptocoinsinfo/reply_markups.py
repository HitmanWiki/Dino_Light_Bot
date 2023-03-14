from telegram import KeyboardButton, ReplyKeyboardMarkup

# create userkeyboard, resize = true, autohide=false
keyboard_p1 = [[KeyboardButton("Website"), KeyboardButton("Chart")],
            [KeyboardButton("Coin_Discovery"), KeyboardButton("Buy_Now")],
            [KeyboardButton("Twitter"), KeyboardButton("page 2 ➡")]]

keyboard_p2 = [[KeyboardButton("Bitcoin"), KeyboardButton("Ethereum")],
            [KeyboardButton("Shiba"), KeyboardButton("Dai")],
            [KeyboardButton("⬅ page 1"), KeyboardButton("page 3 ➡")]]

keyboard_p3 = [[KeyboardButton("NEO"), KeyboardButton("Monero")],
            [KeyboardButton("Stellar"), KeyboardButton("EOS")],
            [KeyboardButton("⬅ page 2"), KeyboardButton("feedback")]]

reply_markup_p1 = ReplyKeyboardMarkup(keyboard_p1, True, False)
reply_markup_p2 = ReplyKeyboardMarkup(keyboard_p2, True, False)
reply_markup_p3 = ReplyKeyboardMarkup(keyboard_p3, True, False)
