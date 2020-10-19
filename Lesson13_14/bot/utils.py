import json
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from .config import CATEGORY_TAG, PRODUCT_TAG
from .keyboards import START_KB
from .texts import BUY_ADD


def check_message_match(message, text):
    return message.text == START_KB[text]


def check_call_tag_match(call, tag):
    return json.loads(call.data)['tag'] == tag


def generate_categories_kb(categories_qs):
    buttons = []
    kb = InlineKeyboardMarkup()
    for c in categories_qs:
        data = json.dumps(
            {
                'id': str(c.id),
                'tag': CATEGORY_TAG
            }
        )
        buttons.append(InlineKeyboardButton(c.title, callback_data=data))
    kb.add(*buttons)
    return kb


def generate_product_kb(product):
    kb = InlineKeyboardMarkup()
    data = json.dumps(
        {
            'id': str(product.id),
            'tag': PRODUCT_TAG
        }
    )
    button = InlineKeyboardButton(BUY_ADD, callback_data=data)
    kb.add(button)
    return kb


def generate_discount_products_kb(discount_products_qs):
    buttons = []
    kb = InlineKeyboardMarkup()
    for dp in discount_products_qs:
        data = json.dumps(
            {
                'id': str(dp.id)
            }
        )
        buttons.append(InlineKeyboardButton(dp.title, callback_data=data))
    kb.add(*buttons)
    return kb
