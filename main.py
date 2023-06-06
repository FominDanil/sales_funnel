import os
from datetime import datetime, timedelta

from aiogram import executor, Dispatcher, Bot, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from asyncio import sleep
from PIL import Image, ImageDraw, ImageOps, ImageFont

from apscheduler.schedulers.asyncio import AsyncIOScheduler

from dotenv import load_dotenv

load_dotenv()

token = os.getenv('BOT_TOKEN')


bot = Bot(token)

dp = Dispatcher(bot, storage=MemoryStorage())

scheduler = AsyncIOScheduler(timezone='Europe/Moscow', job_defaults={'misfire_grace_time': 600})

delay_sec = 300
jobs = {}

class States(StatesGroup):
    first = State()
    second = State()
    third = State()
    fin = State()

async def reminder(user_id):

    if jobs.get(user_id):
        jobs[user_id] = ''

    with open('8.jpg', 'rb') as f:
        await bot.send_photo(user_id, f, caption='👋 Мы почти рассчитали твой потенциал! Давай доведем дело до конца?\nОтветь на предыдущий вопрос👆🏻')


@dp.message_handler(commands=['start'], state='*')
async def send_welcome(message: types.Message):
    job = jobs.get(message.from_user.id)
    if job:
        try:
            job.remove()
        except Exception as e:
            print(e)

    jobs[message.from_user.id] = scheduler.add_job(reminder, trigger='date', run_date=datetime.now() + timedelta(seconds=delay_sec), kwargs=dict(user_id=message.from_user.id))

    markup = types.InlineKeyboardMarkup()
    itembtn1 = types.InlineKeyboardButton(text='Погнали!', callback_data='button0_pressed')
    markup.add(itembtn1)

    with open('1.jpg', 'rb') as privetstvie_photo:
        await message.answer_photo(privetstvie_photo, caption="Привет! 🥰\n \nОчень рада, что ты решил пополнить наши ряды успешных агентов!\n \nСкорей жми «Старт», чтобы узнать секретную разработку и посчитать сколько ты сможешь заработать со своего блога УЖЕ СЕЙЧАС 🤫",reply_markup=markup)


@dp.callback_query_handler(text='button0_pressed')
async def handle_callback_query(call: types.CallbackQuery):
    job = jobs.get(call.from_user.id)
    if job:
        job.remove()
    jobs[call.from_user.id] = scheduler.add_job(reminder, trigger='date',
                                                   run_date=datetime.now() + timedelta(seconds=delay_sec),
                                                   kwargs=dict(user_id=call.from_user.id))

    await call.message.answer('🤑 Для того, чтобы узнать какие результаты ты сможешь получить. Нам нужно понять, чем ты занимаешься.\n \nИнформация конфиденциальна, поэтому можешь не стесняться и говорить правду!')

    keyboard = [[types.InlineKeyboardButton("Бьюти", callback_data='button10_pressed')],
                [types.InlineKeyboardButton("Эксперт", callback_data='button11_pressed')],
                [types.InlineKeyboardButton("Фриланс", callback_data='button12_pressed')],
                [types.InlineKeyboardButton("Хендмейд", callback_data='button13_pressed')]]

    reply_markup = types.InlineKeyboardMarkup(row_width=1, inline_keyboard=keyboard)

    with open('2.jpg', 'rb') as photo_nisha:
        await call.message.answer_photo(photo_nisha, caption='Выбери свою нишу.', reply_markup=reply_markup)

    await call.answer()

@dp.callback_query_handler(text=['button10_pressed', 'button11_pressed', 'button12_pressed', 'button13_pressed'])
async def btq023(call: types.CallbackQuery, state: FSMContext):
    job = jobs.get(call.from_user.id)
    if job:
        job.remove()
    jobs[call.from_user.id] = scheduler.add_job(reminder, trigger='date',
                                                run_date=datetime.now() + timedelta(seconds=delay_sec),
                                                kwargs=dict(user_id=call.from_user.id))

    await call.message.answer('Отлично, мы внесли в секретную базу эту информацию. 👩‍💻')  # , reply_markup=reply_markup45)
    await sleep(2)
    await call.message.answer('🔥 Чтобы более точно рассчитать твой РЕАЛЬНО ВОЗМОЖНЫЙ ДОХОД. Ответь на следующие вопросы.')
    await sleep(3)
    with open('3.jpg', 'rb') as photo_followers:
        await call.message.answer_photo(photo_followers, caption="Какое у тебя количество подписчиков?\n \n❗️Введи точную цифру СЛИТНО. Пример: 3891")
    await States.first.set()
    await call.answer()


@dp.callback_query_handler(text=['button20_pressed', 'button22_pressed', 'button23_pressed'])
async def btn202223(call: types.CallbackQuery, state: FSMContext):
    job = jobs.get(call.from_user.id)
    if job:
        job.remove()
    jobs[call.from_user.id] = scheduler.add_job(reminder, trigger='date',
                                                run_date=datetime.now() + timedelta(seconds=delay_sec),
                                                kwargs=dict(user_id=call.from_user.id))
    await state.update_data(count=0.1)
    with open('3.jpg', 'rb') as photo3:
        await call.message.answer_photo(photo3, caption='🤔 Укажи какой у тебя охват в сторис? (Количество просмотров в сторис. Возьми цифру первой сторис)')
    await States.second.set()
    await call.answer()

@dp.callback_query_handler(text='button21_pressed')
async def btn21(call: types.CallbackQuery, state: FSMContext):
    job = jobs.get(call.from_user.id)
    if job:
        job.remove()
    jobs[call.from_user.id] = scheduler.add_job(reminder, trigger='date',
                                                run_date=datetime.now() + timedelta(seconds=delay_sec),
                                                kwargs=dict(user_id=call.from_user.id))
    await state.update_data(count=0.05)
    with open('3.jpg', 'rb') as photo3:
        await call.message.answer(photo3, caption='🤔 Укажи какой у тебя охват в сторис? (Количество просмотров в сторис. Возьми цифру первой сторис)')
    await States.second.set()
    await call.answer()


@dp.callback_query_handler(text=['button40_pressed', 'button41_pressed'], state='*')
async def btn4041(call: types.CallbackQuery, state: FSMContext):
    job = jobs.get(call.from_user.id)
    if job:
        job.remove()
    jobs[call.from_user.id] = scheduler.add_job(reminder, trigger='date',
                                                run_date=datetime.now() + timedelta(seconds=delay_sec),
                                                kwargs=dict(user_id=call.from_user.id))
    with open('7.jpg', 'rb') as photo7:
        await call.message.answer_photo(photo7, caption='🔥 Спасибо, за предоставленную информацию!\n \n💎 Делаем расчет…')
    await sleep(5)

    state_data = await state.get_data()
    vovlechonost1 = int(0.3 * state_data['user_input_count_followers'] * 0.15 * state_data['user_input_check'])
    vovlechonost2 = int(0.1 * state_data['user_input_count_followers'] * 0.1 * state_data['user_input_check'])

    await call.message.answer('Твой потенциал дохода (СКОЛЬКО ТЫ РЕАЛЬНО МОЖЕШЬ ЗАРАБОТАТЬ С БЛОГА) сейчас равен {:,}'.format(
                         vovlechonost1) + '\n \n😏 Неплохо, не правда ли?')

    await sleep(3)

    result = (abs(vovlechonost2 - vovlechonost1)) * 12
    with open('666.jpg', 'rb') as photo666:
        await call.message.answer_photo(photo666, caption= 'В большинстве случаев, при таких данных, многие зарабатывают не больше -> {:,} рублей'.format(vovlechonost2) + '\nТаким образом, ты теряешь около {:,}'.format(result) + ' рублей В ГОД😱!!!')

    await sleep(5)

    markup101 = types.InlineKeyboardMarkup(row_width=1)
    button101 = types.InlineKeyboardButton(text="ДА!!!", callback_data='button123_pressed')
    markup101.add(button101)

    await call.message.answer('🥳 Выйти на сумму в {:,}'.format(vovlechonost1) +' рублей можно легко уже в следующем месяце, если знать какие инструменты применять и понимать систему продаж в блоге!\n \nХочешь узнать как?',reply_markup= markup101)
    await call.answer()

@dp.callback_query_handler(text='button123_pressed', state='*')
async def btn123(call: types.CallbackQuery, state: FSMContext):
    job = jobs.get(call.from_user.id)
    if job:
        job.remove()

    with open('9.jpg', 'rb') as photo9:
        await call.message.answer_photo(photo9, caption='😎 Как увеличить количество вовлечённости аудитории и продажи БЕЗ ПРИВЛЕЧЕНИЯ НОВОЙ АУДИТОРИИ, секретный агент и расскажет тебе на вебинаре!\n \nПриходи 3 апреля в 10.00 по Мск.\n \nНе забудь!💸')
        #bot.send_message(call.message.chat.id, "😎 Как увеличить количество вовлечённости аудитории и продажи БЕЗ ПРИВЛЕЧЕНИЯ НОВОЙ АУДИТОРИИ, секретный агент и расскажет тебе на вебинаре!\nПриходи такого то числа, во столько.\n \nНе забудь!💸")
    await sleep(8)

    await call.message.answer('🎁 У меня есть для тебя подарок!\nВыставляй свой результат в сторис с отметкой меня и участвуй в розыгрыше разбора ТВОЕГО АККАУНТА. Мы выберем несколько человек и ПОДСВЕТИМ ВАШИ ТОЧКИ РОСТА прямо на вебинаре!\n \nДержи макет👇🏻')

    user_id = call.from_user.id
    user_info = await bot.get_user_profile_photos(user_id)

    if user_info.photos:
        state_data = await state.get_data()

        vovlechonost = int(0.3 * state_data['user_input_count_followers'] * 0.15 * state_data['user_input_check'])

        file_id = user_info.photos[0][-1].file_id
        file_info = await bot.get_file(file_id)
        downloaded_file = await bot.download_file(file_info.file_path)

        # загружаем другую фотографию
        other_image = Image.open("final.jpg")

        # загружаем аватар пользователя и создаем объект Image
        avatar_image = Image.open(downloaded_file)

        avatar_image = avatar_image.resize((int(avatar_image.width * 0.70), int(avatar_image.height * 0.70)))
        # создание маски круга
        mask = Image.new('L', avatar_image.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + avatar_image.size, fill=255)

        # обрезание аватарки пользователя в форме круга
        avatar_image = ImageOps.fit(avatar_image, mask.size, centering=(0.5, 0.5))
        avatar_image.putalpha(mask)

        # наложение аватарки пользователя на другую фотографию
        other_image.paste(avatar_image, (350, 800), avatar_image)

        draw = ImageDraw.Draw(other_image)
        font_size = 100
        font = ImageFont.truetype('CascadiaMono.ttf', font_size)

        #text = "{:,}".format(vovlechonost2)
        #text_width, text_height = draw.textsize(text, font)
        #x = other_image.width - text_width - 400
        #y = other_image.height - text_height - 1489
        #draw.text((x, y), text, font=font, fill=(255, 255, 255))
        text = "{:,}".format(vovlechonost)
        text_bbox = font.getbbox(text)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]
        x = other_image.width - text_width - 390
        y = other_image.height - text_height - 1498
        draw.text((x, y), text, font=font, fill=(255, 255, 255))

        # сохранение результата
        other_image.save(f"porosonok-{user_id}.jpg")
        await sleep(4)
        with open(f'porosonok-{user_id}.jpg', 'rb') as photo101:
            await call.message.answer_photo(photo101)


        other_image.close()
        avatar_image.close()
        try:
            os.remove(f'porosonok-{user_id}.jpg')
            print(f'Файл porosonok-{user_id}.jpg успешно удален.')
        except OSError as e:
            print(f'Ошибка при удалении файла porosonok-{user_id}.jpg: {e.strerror}')
        await sleep(180)
        with open('guide_po_progrevu.pdf', 'rb') as pdf_file:
            await call.message.answer_document(pdf_file, caption='👋Пока есть несколько дней до вебинара даю тебе небольшую пользу. Ты сможешь изучить материал и уже начать делать первые шаги в сторону своего успеха. Забирай гайд «Универсальный прогрев для любого эксперта»')
        await state.finish()
        await call.answer()


@dp.message_handler(state=States.first)
async def podpis(message: types.Message, state: FSMContext):
    job = jobs.get(message.from_user.id)
    if job:
        job.remove()
    jobs[message.from_user.id] = scheduler.add_job(reminder, trigger='date',
                                                   run_date=datetime.now() + timedelta(seconds=delay_sec),
                                                   kwargs=dict(user_id=message.from_user.id))

    try:
        user_input_count_followers = int(message.text)
        if user_input_count_followers >= 10:
            with open('4.jpg', 'rb') as photo4:
                await message.answer_photo(photo4,
                           caption='🤔 Укажи какой у тебя охват в сторис? (Количество просмотров в сторис. Возьми цифру первой сторис)\n \n❗️Введи точную цифру СЛИТНО. Пример: 380')

            await States.second.set()
            await state.update_data({'user_input_count_followers': user_input_count_followers})
        else:
            await message.reply('Вы ввели число за пределами диапазона от 10 до 100000')
    except ValueError:
        await message.reply('Пожалуйста, введите целое число')


@dp.message_handler(state=States.second)
async def ohvat(message: types.Message, state: FSMContext):
    job = jobs.get(message.from_user.id)
    if job:
        job.remove()
    jobs[message.from_user.id] = scheduler.add_job(reminder, trigger='date',
                                                   run_date=datetime.now() + timedelta(seconds=delay_sec),
                                                   kwargs=dict(user_id=message.from_user.id))

    try:
        user_input_ohvati = int(message.text)
        await message.answer('🥳 Формула почти готова и у тебя в руках!\n \nНо для итога ответь еще на пару вопросов…')
        await States.third.set()
        await state.update_data({'user_input_ohvati': user_input_ohvati})
        await sleep(3)
        with open('5.jpg', 'rb') as photo5:
            await message.answer_photo(photo5,
                           caption='💵 Какой у тебя средний чек?\n \n❗️Введи цифру СЛИТНО. Пример: 20000')

    except ValueError:
        await message.reply('Пожалуйста, введите целое число')


@dp.message_handler(state=States.third)
async def avg(message: types.Message, state: FSMContext):
    job = jobs.get(message.from_user.id)
    if job:
        job.remove()
    jobs[message.from_user.id] = scheduler.add_job(reminder, trigger='date',
                                                   run_date=datetime.now() + timedelta(seconds=delay_sec),
                                                   kwargs=dict(user_id=message.from_user.id))

    try:
        user_input_check = int(message.text)
        keyboard8 = [[types.InlineKeyboardButton("Да", callback_data='button40_pressed'),
                      types.InlineKeyboardButton("Нет", callback_data='button41_pressed')]]
        reply_markupQ = types.InlineKeyboardMarkup(row_width=1, inline_keyboard=keyboard8)
        with open('6.jpg', 'rb') as photo6:
            await message.answer_photo(photo6, caption='🤔 Расскажи, ты продавал в блоге раньше или нет?',
                       reply_markup=reply_markupQ)
        await state.update_data({'user_input_check':user_input_check})
        await States.fin.set()

    except ValueError:
        await message.reply('Пожалуйста, введите целое число')


async def start_up(dp):
    scheduler.start()


executor.start_polling(dp, skip_updates=True, on_startup=start_up)