import os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)

api_id = int(os.environ.get("APP_ID"))
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("TOKEN")
client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)

anlik_calisan = []

@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)


@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  await event.reply("[ᴇxᴛʀᴇᴍᴇ & ʜüᴋüᴍꜱüᴢʟᴇʀ ʙᴏᴛ], **Federasyonlarının Kanal Grup Bot Bilgilendirme Botudur.** /grup /kanal /bot **Komutlarını Kullanabilirsiniz.**",
                    buttons=(
                      [Button.url('😎 ᴇxᴛʀᴇᴍᴇ ꜱᴀʜɪᴘ', 'https://t.me/Pukele_ka'),
                      Button.url('😎 ʜüᴋüᴍꜱüᴢʟᴇʀ ꜱᴀʜɪᴘ', 'https://t.me/Hukumsuzlersahibi')],
                      [Button.url('💻 ɢɪᴛʜᴜʙ', 'https://github.com/Iregullar'),
                       Button.url('📍ɪɴꜱᴛᴀɢʀᴀᴍ', 'https://instagram.com/antolojiedebiyat?utm_medium=copy_link')]
                    ),
                    link_preview=False
                   )
@client.on(events.NewMessage(pattern="^/kanal$"))
async def help(event):
  helptext = "[ᴇxᴛʀᴇᴍᴇ & ʜüᴋüᴍꜱüᴢʟᴇʀ ʙᴏᴛ], **Federasyonlarının Kanallarıdır.**"
  await event.reply(helptext,
                    buttons=(
                      [Button.url('🔥 ᴇxᴛʀᴇᴍᴇ ꜰᴇᴅ', 'https://t.me/Extremekanallar'),
                      Button.url('⚔️ ᴇxᴛʀᴇᴍᴇ ʟɪɴᴋ ', 'https://t.me/ExtremeUcretliLink'),
                      Button.url('💪 ᴇxᴛʀᴇᴍᴇ İᴄʀᴀᴀᴛ', 'https://t.me/OrmanCocuklariylaMucadele')],
                      [Button.url('💠 ʀᴇᴋʟᴀᴍ ᴋᴀɴᴀʟı', 'https://t.me/Platformreklam'),
                      Button.url('🎭 ʀᴇꜱɪᴍ ᴋᴀɴᴀʟı ', 'https://t.me/picttureprofil'),
                      Button.url('🛡 ʙᴏᴛ ᴋᴀɴᴀʟı', 'https://t.me/sohbetdestek')]
                    ),
                    link_preview=False
                   )
@client.on(events.NewMessage(pattern="^/grup$"))
async def help(event):
  helptext = "[ᴇxᴛʀᴇᴍᴇ & ʜüᴋüᴍꜱüᴢʟᴇʀ ʙᴏᴛ], **Federasyonlarının Gruplarıdır.**"
  await event.reply(helptext,
                    buttons=(
                      [Button.url('🔥 ᴇxᴛʀᴇᴍᴇ ꜱᴏʜʙᴇᴛ', 'https://t.me/ExtremeSohbett'),
                      Button.url('📣 𝙺𝚊𝚗𝚊𝚕', 'https://t.me/Extremekanallar'),
                      Button.url('🚀 𝚂𝚊𝚑𝚒𝚋𝚒𝚖', 'https://t.me/OrmanCocuklariylaMucadele')]
                    ),
                    link_preview=False
                   )
@client.on(events.NewMessage(pattern="^/bot$"))
async def help(event):
  helptext = "[ᴇxᴛʀᴇᴍᴇ & ʜüᴋüᴍꜱüᴢʟᴇʀ ʙᴏᴛ], **Federasyonlarının Botlarıdır.**"
  await event.reply(helptext,
                    buttons=(
                      [Button.url('🎶 ᴍüᴢɪᴋ + ꜰɪʟᴍ ʙᴏᴛ', 'https://t.me/Winampmuzikbot'),
                      Button.url('⚙️ ꜱᴇꜱꜱɪᴏɴ ʙᴏᴛ', 'https://t.me/Session_TR_bot'),
                      Button.url('🎭 ᴇᴛɪᴋᴇᴛ ʙᴏᴛ', 'https://t.me/UserEtiketBot')],
                      [Button.url('🎶 ᴍüᴢɪᴋ + ꜰɪʟᴍ 2', 'https://t.me/Movingmusicbot'),
                      Button.url('🛡 ғᴇᴅ ʙɪʟɢɪ ʙᴏᴛ', 'https://t.me/ExtremeHukumsuzlerFedBot'),
                      Button.url('🎭 ᴇᴛɪᴋᴇᴛ ʙᴏᴛ', 'https://t.me/LinaTagBot')]
                    ),
                    link_preview=False
                   )


@client.on(events.NewMessage(pattern="^/allllllllllll ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("__𝙱𝚞 𝚔𝚘𝚖𝚞𝚝 𝚐𝚛𝚞𝚙𝚕𝚊𝚛𝚍𝚊 𝚟𝚎 𝚔𝚊𝚗𝚊𝚕𝚕𝚊𝚛𝚍𝚊 𝚔𝚞𝚕𝚕𝚊𝚗ı𝚕𝚊𝚋𝚒𝚕𝚒𝚛.!__")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("__𝚈𝚊𝚕𝚗ı𝚣𝚌𝚊 𝚢ö𝚗𝚎𝚝𝚒𝚌𝚒𝚕𝚎𝚛 𝚑𝚎𝚙𝚜𝚒𝚗𝚍𝚎𝚗 𝚋𝚊𝚑𝚜𝚎𝚍𝚎𝚋𝚒𝚕𝚒𝚛!__")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("__𝙴𝚜𝚔𝚒 𝚖𝚎𝚜𝚊𝚓𝚕𝚊𝚛 𝚒ç𝚒𝚗 ü𝚢𝚎𝚕𝚎𝚛𝚍𝚎𝚗 𝚋𝚊𝚑𝚜𝚎𝚍𝚎𝚖𝚎𝚖! (𝚐𝚛𝚞𝚋𝚊 𝚎𝚔𝚕𝚎𝚖𝚎𝚍𝚎𝚗 ö𝚗𝚌𝚎 𝚐ö𝚗𝚍𝚎𝚛𝚒𝚕𝚎𝚗 𝚖𝚎𝚜𝚊𝚓𝚕𝚊𝚛)__")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("__𝙱𝚊𝚗𝚊 𝚋𝚒𝚛 𝚊𝚛𝚐ü𝚖𝚊𝚗 𝚟𝚎𝚛!__")
  else:
    return await event.respond("__𝙱𝚒𝚛 𝚖𝚎𝚜𝚊𝚓ı 𝚢𝚊𝚗ı𝚝𝚕𝚊𝚢ı𝚗 𝚟𝚎𝚢𝚊 𝚋𝚊ş𝚔𝚊𝚕𝚊𝚛ı𝚗𝚍𝚊𝚗 𝚋𝚊𝚑𝚜𝚎𝚝𝚖𝚎𝚖 𝚒ç𝚒𝚗 𝚋𝚊𝚗𝚊 𝚋𝚒𝚛 𝚖𝚎𝚝𝚒𝚗 𝚟𝚎𝚛𝚒𝚗!__")
    
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("İş𝚕𝚎𝚖 𝙱𝚊ş𝚊𝚛ı𝚕ı 𝙱𝚒𝚛 Ş𝚎𝚔𝚒𝚕𝚍𝚎 𝙳𝚞𝚛𝚍𝚞𝚛𝚞𝚕𝚍𝚞 ❌")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("İş𝚕𝚎𝚖 𝙱𝚊ş𝚊𝚛ı𝚕ı 𝙱𝚒𝚛 Ş𝚎𝚔𝚒𝚕𝚍𝚎 𝙳𝚞𝚛𝚍𝚞𝚛𝚞𝚕𝚍𝚞 ❌")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""


print(">> 𝙱𝚘𝚝 ç𝚊𝚕ı𝚢𝚘𝚛 𝚖𝚎𝚛𝚊𝚔 𝚎𝚝𝚖𝚎 🚀 @OrmanCocuklariylaMucadele 𝚋𝚒𝚕𝚐𝚒 𝚊𝚕𝚊𝚋𝚒𝚕𝚒𝚛𝚜𝚒𝚗 <<")
client.run_until_disconnected()
