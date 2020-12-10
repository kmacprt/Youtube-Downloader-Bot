from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Channel❤️", url="https://t.me/AyushBots")],
        [InlineKeyboardButton(
            "Report Bugs 😊", url="https://t.me/CyberBoyAyushBot")]
    ])
    welcomed = f"Hey <b>{message.from_user.first_name}</b>\nThis Is A Youtube Video Downloader Bot🔥\nJoin @AyushBots To Start Using It❣️\nHit /Help For Any More Info"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
