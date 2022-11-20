import datetime
import uuid
from random import randint
from aiogram import Dispatcher, Bot, types
from aiogram.dispatcher import FSMContext
from aiogram.types import ParseMode
from admin.keyboards import *
from admin.reports.states import ReportStates
from admin.сallbacks import current_dispute
from db.models import RoundVideo, Users
from initialize import bot as mainbot



async def test_videos(call: types.CallbackQuery, state: FSMContext):
    new_videos = RoundVideo.objects.filter(status="", type_video="test").first()

    if new_videos is None:
        await call.message.answer("Нет новых видео")
    else:
        user = Users.objects.filter(user_id=new_videos.user_tg_id).first()
        id_dispute = str(new_videos.id_video)
        purpose = current_dispute(user.action, user.additional_action)

        code = " ".join(list(new_videos.code_in_video))

        tmp_msg = (f"Диспут #D{id_dispute}\n"
                   f"*День 0*\n\n"
                   f"🔒 {code}\n"
                   f"{purpose}")
        # print(new_videos.tg_id, "ADMIN BOT")

        await state.update_data(video_user_id=new_videos.tg_id, user_id=call.from_user.id, id_video=new_videos.id_video)
        await call.message.answer(text=tmp_msg, parse_mode=ParseMode.MARKDOWN)
        if user.action == "money":
            await call.message.answer_video(video=new_videos.tg_id,
                                            reply_markup=test_keyboard)
        else:
            await call.message.answer_video_note(video_note=new_videos.tg_id,
                                                 reply_markup=test_keyboard)


async def access_video(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    RoundVideo.objects.filter(tg_id=data['video_user_id']).update(status="good")

    await call.message.answer(text="Готово!")

    user = RoundVideo.objects.get(tg_id=data['video_user_id'])
    current_user = Users.objects.filter(user_id=user.user_tg_id).first()
    start = ""

    if current_user.start_disput == "tomorrow":
        start = "послезавтра"
    elif current_user.start_disput == "monday":
        start = "в понедельник"
    success_keyboard = types.InlineKeyboardMarkup()
    success_keyboard.add(types.InlineKeyboardButton(text='👍 Хорошо', callback_data='good'))

    await mainbot.send_message(text="Отлично 🔥 У тебя всё получилось", chat_id=user.chat_tg_id)
    await mainbot.send_message(text=f"Твой новый код придёт сюда {start}.", chat_id=user.chat_tg_id,
                               reply_markup=success_keyboard)
    date_now = call.message.date + datetime.timedelta(seconds=30)
    #scheduler.start()
    #scheduler.add_job(new_code, "date", run_date=date_now, args=(user.chat_tg_id, state,))
    #scheduler.print_jobs()
    await test_videos(call, state)


async def refused_video(call: types.CallbackQuery, state: FSMContext):

    await call.message.edit_reply_markup(reply_markup=refused_keyboard)


async def new_code(chat_id: int, state: FSMContext):
    new_code = str(randint(1000, 9999))
    code = " ".join(list(new_code))
    msg = f"Твой новый код: {code}"
    data = await state.get_data()
    await RoundVideo.objects.acreate(user_tg_id=data['user_id'],
                                     chat_tg_id=chat_id,
                                     code_in_video=new_code,
                                     id_video=data['id_video'],
                                     type_video=RoundVideo.TypeVideo.dispute,
                                     n_day=1)

    await mainbot.send_message(text=msg, chat_id=chat_id, reply_markup=types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton(text="Отправить репорт", callback_data="send_dispute_report")))


async def thirty_days_videos(call: types.CallbackQuery):
    tmp_msg = "Сюда попадают новые репорты из 30 дневной игры \"Испытания воли\""

    await call.message.edit_text(text=tmp_msg, reply_markup=types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton(text='🔥 Начать', callback_data='lets_go'),
        types.InlineKeyboardButton(text='Назад', callback_data='back_reports')))


async def back_to_menu(call: types.CallbackQuery):
    await call.message.edit_text(text="Меню репортов", reply_markup=reports_menu_keyboard)


async def back_to_video(call: types.CallbackQuery):
    await call.bot.delete_message(message_id=call.message.message_id, chat_id=call.message.chat.id)


async def confirm_video(call: types.CallbackQuery):
    await call.message.answer(text='Пользователь успешно прошел подготовку и готов к игре?',
                              reply_markup=access_keyboard)


async def refused1_video(call: types.CallbackQuery, state: FSMContext):
    v = await state.get_data()
    RoundVideo.objects.filter(tg_id=v['video_user_id']).update(status="bad")
    user = RoundVideo.objects.get(tg_id=v['video_user_id'])

    await mainbot.send_message(text=" Не видно лица / результатов. Пожалуйста, попробуй ещё раз",
                               chat_id=user.chat_tg_id,
                               reply_markup=types.InlineKeyboardMarkup().add(
                                   types.InlineKeyboardButton(text='Отправить репорт', callback_data="send_new1")
                               ))

    await call.message.answer('Готово!')
    await test_videos(call, state)

async def refused2_video(call: types.CallbackQuery, state: FSMContext):
    v = await state.get_data()
    RoundVideo.objects.filter(tg_id=v['video_user_id']).update(status="bad")
    user = RoundVideo.objects.get(tg_id=v['video_user_id'])

    await mainbot.send_message(text="На видео не слышно кода. Пожалуйста, попробуй ещё раз",
                               chat_id=user.chat_tg_id,
                               reply_markup=types.InlineKeyboardMarkup().add(
                                   types.InlineKeyboardButton(text='Отправить репорт', callback_data="send_new1")
                               ))

    await call.message.answer('Готово!')
    await test_videos(call, state)


async def refused3_video(call: types.CallbackQuery, state: FSMContext):
    await ReportStates.input_message.set()

    await call.message.answer("Введите сообщение:")


def register_callback(dp: Dispatcher, bot: Bot):
    dp.register_callback_query_handler(test_videos, text='test_videos', state="*")
    dp.register_callback_query_handler(access_video, text='confirm_video', state="*")
    dp.register_callback_query_handler(confirm_video, text='good', state="*")
    dp.register_callback_query_handler(refused_video, text='bad', state="*")
    dp.register_callback_query_handler(thirty_days_videos, text='every_day', state="*")
    dp.register_callback_query_handler(back_to_menu, text='back_reports', state="*")
    dp.register_callback_query_handler(back_to_video, text="back_to_video", state="*")
    dp.register_callback_query_handler(refused1_video, text="face_result", state="*")
    dp.register_callback_query_handler(refused3_video, text="send_message", state="*")
    dp.register_callback_query_handler(refused2_video, text="incorrect_code", state="*")