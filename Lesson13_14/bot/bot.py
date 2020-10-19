import json
from .config import TOKEN, CATEGORY_TAG, PRODUCT_TAG
from .keyboards import START_KB
from .utils import (
    abc,
    check_message_match,
    check_call_tag_match,
    generate_categories_kb,
    generate_product_kb,
    generate_discount_products_kb)
from .texts import GREETINGS, PICK_CATEGORY, PICK_DISCOUNT_PRODUCT
from ..models.models import Category, Product
from telebot import TeleBot
from telebot.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
)

bot = TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [KeyboardButton(button) for button in START_KB.values()]
    kb.add(*buttons)
    bot.send_message(
        message.chat.id,
        GREETINGS,
        reply_markup=kb
    )


@bot.message_handler(func=lambda m: check_message_match(m, 'category'))
def show_categories(message):
    kb = generate_categories_kb(Category.get_root_categories())
    bot.send_message(
        message.chat.id,
        PICK_CATEGORY,
        reply_markup=kb
    )


@bot.message_handler(func=lambda m: check_message_match(m, 'discount'))
def show_discount_products(message):
    kb = generate_discount_products_kb(Product.get_discount_products())
    bot.send_message(
        message.chat.id,
        PICK_DISCOUNT_PRODUCT,
        reply_markup=kb
    )


@bot.callback_query_handler(func=lambda c: check_call_tag_match(c, CATEGORY_TAG))
def categories(call):
    category = Category.objects.get(id=json.loads(call.data)['id'])
    if category.subcategories:
        kb = generate_categories_kb(category.subcategories)
        bot.edit_message_text(
            category.title,
            call.message.chat.id,
            message_id=call.message.message_id,
            reply_markup=kb
        )
    else:
        for product in Product.get_category_products(category):
            kb = generate_product_kb(product)
            bot.send_message(
                call.message.chat.id,
                f'{product.title}\nОписание: \n{product.description}\nЦена: {product.price}',
                reply_markup=kb
            )
