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
  await event.reply("**𝐄𝐱𝐭𝐫𝐚𝐓𝐚𝐆𝐆𝐞𝐑**, 𝙶𝚛𝚞𝚙 𝚟𝚎𝚢𝚊 𝚔𝚊𝚗𝚊𝚕𝚍𝚊𝚔𝚒 𝚗𝚎𝚛𝚎𝚍𝚎𝚢𝚜𝚎 𝚝ü𝚖 ü𝚢𝚎𝚕𝚎𝚛𝚍𝚎𝚗 𝚋𝚊𝚑𝚜𝚎𝚍𝚎𝚋𝚒𝚕𝚒𝚛𝚒𝚖 ★\𝚗𝙳𝚊𝚑𝚊 𝚏𝚊𝚣𝚕𝚊 𝚋𝚒𝚕𝚐𝚒 𝚒ç𝚒𝚗 **/𝚑𝚎𝚕𝚙**'𝚒 𝚝ı𝚔𝚕𝚊𝚢ı𝚗.",
                    buttons=(
                      [Button.url('🌟 𝙱𝚎𝚗𝚒 𝙱𝚒𝚛 𝙶𝚛𝚞𝚋𝚊 𝙴𝚔𝚕𝚎', 'https://t.me/ExtraTaGGerbot?startgroup=a'),
                      Button.url('📣 𝙺𝚊𝚗𝚊𝚕', 'https://t.me/Extremekanallar'),
                      Button.url('🚀 𝚂𝚊𝚑𝚒𝚋𝚒𝚖', 'https://t.me/OrmanCocuklariylaMucadele')]
                    ),
                    link_preview=False
                   )
@client.on(events.NewMessage(pattern="^/help$"))
async def help(event):
  helptext = "**𝐄𝐱𝐭𝐫𝐚𝐓𝐚𝐆𝐆𝐞𝐑 𝚋𝚘𝚝'𝚞𝚗 𝚈𝚊𝚛𝚍ı𝚖 𝙼𝚎𝚗ü𝚜ü**\𝚗\𝚗𝙺𝚘𝚖𝚞𝚝: /𝚊𝚕𝚕 \𝚗 𝙱𝚞 𝚔𝚘𝚖𝚞𝚝𝚞, 𝚋𝚊ş𝚔𝚊𝚕𝚊𝚛ı𝚗𝚊 𝚋𝚊𝚑𝚜𝚎𝚝𝚖𝚎𝚔 𝚒𝚜𝚝𝚎𝚍𝚒ğ𝚒𝚗𝚒𝚣 𝚖𝚎𝚝𝚒𝚗𝚕𝚎 𝚋𝚒𝚛𝚕𝚒𝚔𝚝𝚎 𝚔𝚞𝚕𝚕𝚊𝚗𝚊𝚋𝚒𝚕𝚒𝚛𝚜𝚒𝚗𝚒𝚣. \𝚗`Ö𝚛𝚗𝚎𝚔: /𝚊𝚕𝚕 𝙶ü𝚗𝚊𝚢𝚍ı𝚗!` \𝚗𝙱𝚞 𝚔𝚘𝚖𝚞𝚝𝚞 𝚢𝚊𝚗ı𝚝 𝚘𝚕𝚊𝚛𝚊𝚔 𝚔𝚞𝚕𝚕𝚊𝚗𝚊𝚋𝚒𝚕𝚒𝚛𝚜𝚒𝚗𝚒𝚣. 𝚑𝚎𝚛𝚑𝚊𝚗𝚐𝚒 𝚋𝚒𝚛 𝚖𝚎𝚜𝚊𝚓 𝙱𝚘𝚝, 𝚢𝚊𝚗ı𝚝𝚕𝚊𝚗𝚊𝚗 𝚒𝚕𝚎𝚝𝚒𝚢𝚎 𝚔𝚞𝚕𝚕𝚊𝚗ı𝚌ı𝚕𝚊𝚛ı 𝚎𝚝𝚒𝚔𝚎𝚝𝚕𝚎𝚢𝚎𝚌𝚎𝚔"
  await event.reply(helptext,
                    buttons=(
                      [Button.url('🌟 𝙱𝚎𝚗𝚒 𝙱𝚒𝚛 𝙶𝚛𝚞𝚋𝚊 𝙴𝚔𝚕𝚎', 'https://t.me/ExtraTaGGerbot?startgroup=a'),
                      Button.url('📣 𝙺𝚊𝚗𝚊𝚕', 'https://t.me/Extremekanallar'),
                      Button.url('🚀 𝚂𝚊𝚑𝚒𝚋𝚒𝚖', 'https://t.me/OrmanCocuklariylaMucadele')]
                    ),
                    link_preview=False
                   )


@client.on(events.NewMessage(pattern="^/all ?(.*)"))
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
