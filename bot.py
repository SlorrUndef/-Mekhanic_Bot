import bot_config
import telebot
from telebot import types
import time
import requests

# -------------------------------------
bot = telebot.TeleBot(bot_config.TOKEN)
# -------------------------------------

markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)  # create markup
hideBoard = types.ReplyKeyboardRemove()  # delete markup
markup.add('Матан', 'Ангем(не работает)')  # add something to markup


@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    check = False
    if not check:
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.3)
        bot.send_message(message.chat.id, 'Unnamed MM bot v1.0\n'
                                          'Чтобы узнать функционал бота набери\n /help.\n\n'
                                          'Отзывы, пожелания по работе, баги присылайте на\n'
                                          '@mansur_korigov')
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.1)
        msg = bot.send_message(message.chat.id, "Выбери предмет", reply_markup=markup)  # Message + markup
        bot.register_next_step_handler(msg, answer)
        check = True


def answer(message):
    text = message.text
    if text == 'Матан':
        bilety = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        bilety.add('Равномощные множества...', 'Аксиома полноты...', 'Лемма о вложенных отрезках...',
                   'Лемма Бореля-Лебега о конечном покрытии отрезка...', 'Предел последовательности...',
                   'Монотонные последовательности...', 'Критерий Коши сходимости последовательности.',
                   'Предел функции в точке. Эквивалентность определений предела функции по Коши и по Гейне.',
                   'Функции, бесконечно малые и бесконечно большие в точке...',
                   'Предельный переход и арифметические операции. Предельный переход и неравенства.',
                   'Предел композиции функции. Теорема о пределе монотонной функции на [a, +-∞) при x +∞(-∞).',
                   'Предел функции по базе. Критерий Коши существования предела функции по базе.',
                   'Непрерывность функции в точке...',
                   'Классификация точек разрыва. Разрывы монотонной функции.',
                   'Теорема о промежуточных значениях функции, непрерывной на отрезке.',
                   'Теоремы Вейерштрасса об ограниченности...',
                   'Теорема Кантора о равномерной непрерывности функции, непрерывной на отрезке.',
                   'Теорема об обратной функции.',
                   'Производная функции в точке. Дифференцируемость функции в точке. Связь между этими понятиями.',
                   'Арифметические операции и производная.',
                   'Производная композиции.  Производная обратной функции.',
                   'Производные и дифференциалы высших порядков. Формула Лейбница.',
                   'Теоремы Ферма и Ролля.',
                   'Теоремы Коши и Лагранжа о конечных приращениях.',
                   'Правила Лопиталя раскрытия неопределенностей.',
                   'Формула Тейлора с остаточным членом в форме Лагранжа.',
                   'Формула Тейлора с остаточным членом в форме Пеано...',
                   'Критерий монотонности функции на интервале...',
                   'Выпуклость функции. Точки перегиба...')
        msg = bot.send_message(message.chat.id, 'Выберите билет:', reply_markup=bilety)
        bot.register_next_step_handler(msg, bilety_func)
        check = True
    else:
        bot.send_message(message.chat.id, 'Не готово!', reply_markup=hideBoard)
        check = True

def bilety_func(message):
    text = message.text
    if text == 'Равномощные множества...':
        bot.send_chat_action(message.chat.id, 'upload_photo')
        doc_11 = "https://imgur.com/NNydzJ9"
        doc_12 = 'https://imgur.com/SX0wQNQ'
        doc_13 = 'https://imgur.com/pCpiqOg'
        doc_14 = 'https://imgur.com/SXFOFzg'
        doc_15 = 'https://imgur.com/QF1NmIH'
        doc_16 = 'https://imgur.com/cxrADYG'
        doc_17 = 'https://imgur.com/R3Ezqki'
        doc_18 = 'https://imgur.com/GhTolI1'
        doc_19 = 'https://imgur.com/RQ5byGo'
        doc_110 = 'https://imgur.com/SMs61de'
        doc_111 = 'https://imgur.com/NgqSqV5'
        doc_112 = 'https://imgur.com/ulDR09y'
        doc_113 = 'https://imgur.com/uZ2p2eJ'
        doc_114 = 'https://imgur.com/JAyUGxB'
        doc_115 = 'https://imgur.com/uqrCoYb'
        bot.send_photo(message.chat.id, photo=doc_11)
        bot.send_photo(message.chat.id, photo=doc_12)
        bot.send_photo(message.chat.id, photo=doc_13)
        bot.send_photo(message.chat.id, photo=doc_14)
        bot.send_photo(message.chat.id, photo=doc_15)
        bot.send_photo(message.chat.id, photo=doc_16)
        bot.send_photo(message.chat.id, photo=doc_17)
        bot.send_photo(message.chat.id, photo=doc_18)
        bot.send_photo(message.chat.id, photo=doc_19)
        bot.send_photo(message.chat.id, photo=doc_110)
        bot.send_photo(message.chat.id, photo=doc_111)
        bot.send_photo(message.chat.id, photo=doc_112)
        bot.send_photo(message.chat.id, photo=doc_113)
        bot.send_photo(message.chat.id, photo=doc_114)
        bot.send_photo(message.chat.id, photo=doc_115)
        bot.send_message(message.chat.id, 'Готово!', reply_markup=hideBoard)
    elif text == 'Аксиома полноты...':
        bot.send_chat_action(message.chat.id, 'upload_photo')
        doc_21 = 'https://imgur.com/fWvvTgI'
        doc_22 = 'https://imgur.com/pfZvcYr'
        doc_23 = 'https://imgur.com/0qeb89P'
        doc_24 = 'https://imgur.com/4lMfcI8'
        doc_25 = 'https://imgur.com/OqtnEQT'
        doc_26 = 'https://imgur.com/6mygv5v'
        doc_27 = 'https://imgur.com/YiUnuee'
        doc_28 = 'https://imgur.com/St7Fd80'
        bot.send_photo(message.chat.id, photo=doc_21)
        bot.send_photo(message.chat.id, photo=doc_22)
        bot.send_photo(message.chat.id, photo=doc_23)
        bot.send_photo(message.chat.id, photo=doc_24)
        bot.send_photo(message.chat.id, photo=doc_25)
        bot.send_photo(message.chat.id, photo=doc_26)
        bot.send_photo(message.chat.id, photo=doc_27)
        bot.send_photo(message.chat.id, photo=doc_28)
        bot.send_message(message.chat.id, 'Готово!', reply_markup=hideBoard)
    elif text == 'Лемма о вложенных отрезках...':
        bot.send_chat_action(message.chat.id, 'upload_photo')
        doc_31 = 'https://imgur.com/ZgDf64v'
        doc_32 = 'https://imgur.com/5o2Y9uv'
        bot.send_photo(message.chat.id, photo=doc_31)
        bot.send_photo(message.chat.id, photo=doc_32)
        bot.send_message(message.chat.id, 'Готово!', reply_markup=hideBoard)
    elif text == 'Лемма Бореля-Лебега о конечном покрытии отрезка...':
        bot.send_chat_action(message.chat.id, 'upload_photo')
        doc_41 = 'https://imgur.com/n4vQKJC'
        doc_42 = 'https://imgur.com/WKiGNH1'
        doc_43 = 'https://imgur.com/IVv4LkD'
        bot.send_photo(message.chat.id, photo=doc_41)
        bot.send_photo(message.chat.id, photo=doc_42)
        bot.send_photo(message.chat.id, photo=doc_43)
        bot.send_message(message.chat.id, 'Готово!', reply_markup=hideBoard)
    elif text == 'Предел последовательности...':
        bot.send_chat_action(message.chat.id, 'upload_photo')
        doc_51 = 'https://imgur.com/Yrlm5W6'
        doc_52 = 'https://imgur.com/fbccIG0'
        doc_53 = 'https://imgur.com/N8BAT6F'
        doc_54 = 'https://imgur.com/k96PuS2'
        doc_55 = 'https://imgur.com/FzMSqrU'
        doc_56 = 'https://imgur.com/Pf2zS1j'
        doc_57 = 'https://imgur.com/2kR8rGB'
        doc_58 = 'https://imgur.com/QojhfJP'
        doc_59 = 'https://imgur.com/NOfqos1'
        doc_510 = 'https://imgur.com/ui7z3yj'
        doc_511 = 'https://imgur.com/jhUfhDU'
        doc_512 = "https://imgur.com/gOH0NZf"
        bot.send_photo(message.chat.id, photo=doc_51)
        bot.send_photo(message.chat.id, photo=doc_52)
        bot.send_photo(message.chat.id, photo=doc_53)
        bot.send_photo(message.chat.id, photo=doc_54)
        bot.send_photo(message.chat.id, photo=doc_55)
        bot.send_photo(message.chat.id, photo=doc_56)
        bot.send_photo(message.chat.id, photo=doc_57)
        bot.send_photo(message.chat.id, photo=doc_58)
        bot.send_photo(message.chat.id, photo=doc_59)
        bot.send_photo(message.chat.id, photo=doc_510)
        bot.send_photo(message.chat.id, photo=doc_511)
        bot.send_photo(message.chat.id, photo=doc_512)
        bot.send_message(message.chat.id, 'Готово!', reply_markup=hideBoard)
    elif text == 'Монотонные последовательности...':
        bot.send_chat_action(message.chat.id, 'upload_photo')
        doc_61 = 'https://imgur.com/qmCwRfb'
        doc_62 = 'https://imgur.com/oMc8pap'
        doc_63 = 'https://imgur.com/fk2EnFF'
        doc_64 = 'https://imgur.com/9bdw3Ko'
        doc_65 = 'https://imgur.com/uba5Rgb'
        doc_66 = 'https://imgur.com/1BJ4OC5'
        bot.send_photo(message.chat.id, photo=doc_61)
        bot.send_photo(message.chat.id, photo=doc_62)
        bot.send_photo(message.chat.id, photo=doc_63)
        bot.send_photo(message.chat.id, photo=doc_64)
        bot.send_photo(message.chat.id, photo=doc_65)
        bot.send_photo(message.chat.id, photo=doc_66)
        bot.send_message(message.chat.id, 'Готово!', reply_markup=hideBoard)
    elif text == 'Критерий Коши сходимости последовательности.':
        bot.send_chat_action(message.chat.id, 'upload_photo')
        doc_71 = 'https://imgur.com/YJXqJst'
        bot.send_photo(message.chat.id, photo=doc_71)
        bot.send_message(message.chat.id, 'Готово!', reply_markup=hideBoard)
    elif text == 'Предел функции в точке. Эквивалентность определений предела функции по Коши и по Гейне.':
        bot.send_chat_action(message.chat.id, 'upload_photo')
        doc_81 = 'https://imgur.com/6gIANM4'
        doc_82 = 'https://imgur.com/Hga4JmK'
        doc_83 = 'https://imgur.com/6Is6krL'
        doc_84 = 'https://imgur.com/YvHyrN9'
        bot.send_photo(message.chat.id, photo=doc_81)
        bot.send_photo(message.chat.id, photo=doc_82)
        bot.send_photo(message.chat.id, photo=doc_83)
        bot.send_photo(message.chat.id, photo=doc_84)
        bot.send_message(message.chat.id, 'Готово!', reply_markup=hideBoard)
    elif text == 'Функции, бесконечно малые и бесконечно большие в точке...':
        bot.send_chat_action(message.chat.id, 'upload_photo')
        doc_91 = 'https://imgur.com/e9tM43L'
        doc_92 = 'https://imgur.com/6MoBBTi'
        doc_93 = 'https://imgur.com/rLpZXlx'
        doc_94 = 'https://imgur.com/vJDmLhO'
        bot.send_photo(message.chat.id, photo=doc_91)
        bot.send_photo(message.chat.id, photo=doc_92)
        bot.send_photo(message.chat.id, photo=doc_93)
        bot.send_photo(message.chat.id, photo=doc_94)
        bot.send_message(message.chat.id, 'Готово!', reply_markup=hideBoard)
    elif text == 'Предельный переход и арифметические операции. Предельный переход и неравенства.':
        doc_101 = 'https://imgur.com/P7VZYkb'
        doc_102 = 'https://imgur.com/t6hc4lJ'
        doc_103 = 'https://imgur.com/OOaiZDu'
        doc_104 = 'https://imgur.com/ZYuAUch'
        bot.send_photo(message.chat.id, photo=doc_101)
        bot.send_photo(message.chat.id, photo=doc_102)
        bot.send_photo(message.chat.id, photo=doc_103)
        bot.send_photo(message.chat.id, photo=doc_104)
        bot.send_message(message.chat.id, 'Готово!', reply_markup=hideBoard)
    elif text == 'Предел композиции функции. Теорема о пределе монотонной функции на [a, +-∞) при x +∞(-∞).':
        bot.send_chat_action(message.chat.id, 'upload_photo')
        doc_111 = 'https://imgur.com/0KRjJ2A'
        doc_112 = 'https://imgur.com/iTM8Wny'
        doc_113 = 'https://imgur.com/0CfxXLm'
        doc_114 = 'https://imgur.com/V85RAlc'
        doc_115 = 'https://imgur.com/ywJB9jw'
        doc_116 = 'https://imgur.com/xRYnWJo'
        bot.send_photo(message.chat.id, photo=doc_111)
        bot.send_photo(message.chat.id, photo=doc_112)
        bot.send_photo(message.chat.id, photo=doc_113)
        bot.send_photo(message.chat.id, photo=doc_114)
        bot.send_photo(message.chat.id, photo=doc_115)
        bot.send_photo(message.chat.id, photo=doc_116)
        bot.send_message(message.chat.id, 'Готово!', reply_markup=hideBoard)
    elif text == 'Предел функции по базе. Критерий Коши существования предела функции по базе.':
        bot.send_chat_action(message.chat.id, 'upload_photo')
        doc_121 = 'https://imgur.com/EuxA7Y7'
        doc_122 = 'https://imgur.com/GWZz1HA'
        doc_123 = 'https://imgur.com/sIZ0Dc5'
        doc_124 = 'https://imgur.com/pqGBb0t'
        bot.send_photo(message.chat.id, photo=doc_121)
        bot.send_photo(message.chat.id, photo=doc_122)
        bot.send_photo(message.chat.id, photo=doc_123)
        bot.send_photo(message.chat.id, photo=doc_124)
        bot.send_message(message.chat.id, 'Готово!', reply_markup=hideBoard)
    elif text == 'Непрерывность функции в точке...':
        bot.send_chat_action(message.chat.id, 'upload_photo')
        doc_131 = 'https://imgur.com/lKliWvW'
        doc_132 = 'https://imgur.com/Qc7sZRS'
        doc_133 = 'https://imgur.com/c5XkCWy'
        doc_134 = 'https://imgur.com/zE5lyoM'
        bot.send_photo(message.chat.id, photo=doc_131)
        bot.send_photo(message.chat.id, photo=doc_132)
        bot.send_photo(message.chat.id, photo=doc_133)
        bot.send_photo(message.chat.id, photo=doc_134)
        bot.send_message(message.chat.id, 'Готово!', reply_markup=hideBoard)
    elif text == 'Классификация точек разрыва. Разрывы монотонной функции.':
        bot.send_chat_action(message.chat.id, 'upload_photo')
        doc_141 = 'https://imgur.com/RUXOvNM'
        doc_142 = 'https://imgur.com/nqncVYT'
        doc_143 = 'https://imgur.com/AAHml02'
        bot.send_photo(message.chat.id, photo=doc_141)
        bot.send_photo(message.chat.id, photo=doc_142)
        bot.send_photo(message.chat.id, photo=doc_143)
        bot.send_message(message.chat.id, 'Готово!', reply_markup=hideBoard)
    elif text == 'Теорема о промежуточных значениях функции, непрерывной на отрезке.':
        bot.send_chat_action(message.chat.id, 'upload_photo')
        doc_151 = 'https://imgur.com/kdh1kVH'
        doc_152 = 'https://imgur.com/Tu4TN7C'
        bot.send_photo(message.chat.id, photo=doc_151)
        bot.send_photo(message.chat.id, photo=doc_152)
        bot.send_message(message.chat.id, 'Готово!', reply_markup=hideBoard)
    elif text == 'Теоремы Вейерштрасса об ограниченности...':
        bot.send_chat_action(message.chat.id, 'upload_photo')
        doc_161 = 'https://imgur.com/XOFwL4i'
        doc_162 = 'https://imgur.com/15RNVsm'
        bot.send_photo(message.chat.id, photo=doc_161)
        bot.send_photo(message.chat.id, photo=doc_162)
        bot.send_message(message.chat.id, 'Готово!', reply_markup=hideBoard)
    elif text == 'Теорема Кантора о равномерной непрерывности функции, непрерывной на отрезке.':
        bot.send_chat_action(message.chat.id, 'upload_photo')
        doc_171 = 'https://imgur.com/YeU1PHz'
        bot.send_photo(message.chat.id, photo=doc_171)
        bot.send_message(message.chat.id, 'Готово!', reply_markup=hideBoard)
    elif text == 'Теорема об обратной функции.':
        bot.send_chat_action(message.chat.id, 'upload_photo')
        doc_181 = 'https://imgur.com/yRHNyJB'
        doc_182 = 'https://imgur.com/T7wLkkj'
        doc_183 = 'https://imgur.com/kH0keow'
        bot.send_photo(message.chat.id, photo=doc_181)
        bot.send_photo(message.chat.id, photo=doc_182)
        bot.send_photo(message.chat.id, photo=doc_183)
        bot.send_message(message.chat.id, 'Готово!', reply_markup=hideBoard)
    elif text == 'Производная функции в точке. Дифференцируемость функции в точке. Связь между этими понятиями.':
        bot.send_chat_action(message.chat.id, 'upload_photo')
        doc_191 = 'https://imgur.com/LdB95Fe'
        doc_192 = 'https://imgur.com/CJ92Ujo'
        doc_193 = 'https://imgur.com/fBWALDg'
        doc_194 = 'https://imgur.com/Nbof5g9'
        doc_195 = 'https://imgur.com/7w0uqJ0'
        doc_196 = 'https://imgur.com/o3ViokJ'
        bot.send_photo(message.chat.id, photo=doc_191)
        bot.send_photo(message.chat.id, photo=doc_192)
        bot.send_photo(message.chat.id, photo=doc_193)
        bot.send_photo(message.chat.id, photo=doc_194)
        bot.send_photo(message.chat.id, photo=doc_195)
        bot.send_photo(message.chat.id, photo=doc_196)
        bot.send_message(message.chat.id, 'Готово!', reply_markup=hideBoard)
    elif text == 'Арифметические операции и производная.':
        bot.send_chat_action(message.chat.id, 'upload_photo')
        doc_201 = 'https://imgur.com/wvOhXR6'
        bot.send_photo(message.chat.id, photo=doc_201)
        bot.send_message(message.chat.id, 'Готово!', reply_markup=hideBoard)
    elif text == 'Производная композиции.  Производная обратной функции.':
        bot.send_chat_action(message.chat.id, 'upload_photo')
        doc_211 = 'https://imgur.com/FV5PCx4'
        doc_212 = 'https://imgur.com/HRQi2G6'
        bot.send_photo(message.chat.id, photo=doc_211)
        bot.send_photo(message.chat.id, photo=doc_212)
        bot.send_message(message.chat.id, 'Готово!', reply_markup=hideBoard)
    elif text == 'Производные и дифференциалы высших порядков. Формула Лейбница.':
        bot.send_chat_action(message.chat.id, 'upload_photo')
        doc_221 = 'https://imgur.com/du1A2as'
        doc_222 = 'https://imgur.com/QOniJgH'
        doc_223 = 'https://imgur.com/bA7a4WZ'
        bot.send_photo(message.chat.id, photo=doc_221)
        bot.send_photo(message.chat.id, photo=doc_222)
        bot.send_photo(message.chat.id, photo=doc_223)
        bot.send_message(message.chat.id, 'Готово!', reply_markup=hideBoard)
    elif text == 'Теоремы Ферма и Ролля.':
        bot.send_chat_action(message.chat.id, 'upload_photo')
        doc_231 = ''
        bot.send_message(message.chat.id, 'Не готово!', reply_markup=hideBoard)
    elif text == 'Теоремы Коши и Лагранжа о конечных приращениях.':
        bot.send_chat_action(message.chat.id, 'upload_photo')
        doc_241 = ''
        bot.send_message(message.chat.id, 'Не готово!', reply_markup=hideBoard)
    elif text == 'Правила Лопиталя раскрытия неопределенностей.':
        bot.send_chat_action(message.chat.id, 'upload_photo')
        doc_251 = ''
        bot.send_message(message.chat.id, 'Не готово!', reply_markup=hideBoard)
    elif text == 'Формула Тейлора с остаточным членом в форме Лагранжа.':
        bot.send_chat_action(message.chat.id, 'upload_photo')
        doc_261 = ''
        bot.send_message(message.chat.id, 'Не готово!', reply_markup=hideBoard)
    elif text == 'Формула Тейлора с остаточным членом в форме Пеано...':
        bot.send_chat_action(message.chat.id, 'upload_photo')
        doc_271 = ''
        bot.send_message(message.chat.id, 'Не готово!', reply_markup=hideBoard)
    elif text == 'Критерий монотонности функции на интервале...':
        bot.send_chat_action(message.chat.id, 'upload_photo')
        doc_281 = ''
        bot.send_message(message.chat.id, 'Не готово!', reply_markup=hideBoard)
    elif text == 'Выпуклость функции. Точки перегиба...':
        bot.send_chat_action(message.chat.id, 'upload_photo')
        doc_291 = ''
        bot.send_message(message.chat.id, 'Не готово!', reply_markup=hideBoard)

bot.polling()
