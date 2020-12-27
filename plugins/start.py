from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("නාළිකාව❤️", url="https://t.me/lkhitech")],
        [InlineKeyboardButton(
            "බලන්න 😊", url="https://visi.tk/kavinduaj")]
    ])
    welcomed = f"ආයුබෝවාන්🙏 <b>{message.from_user.first_name}</b>\nමෙය යූ ටියුබ් වීඩියෝ බාගත කිරීමේ බොට් එකකි🔥\nඒකතුවෙන්න @kavinduaj එය භාවිතා කිරීම ආරම්භ කිරීමට❣️\nවැඩි විස්තර දැන ගැනීමට  /Help "
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
