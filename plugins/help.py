from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"දැනට සහය දක්වන්නේ යූටියුබ් සිංගල් සඳහා පමණි (ධාවන ලැයිස්තුවක් නොමැත) යූටියුබ් යූආර්එල් යවන්න \nසම්බන්ධ කරගන්න @kavinduaj🤗️"
    await message.reply_text(helptxt)
