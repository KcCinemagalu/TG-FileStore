# (c) @PredatorHackerzZ || @TeleRoidGroup

import os

class Config(object):
	API_ID = int(os.environ.get("API_ID", "14356452"))
	API_HASH = os.environ.get("API_HASH", "cac21249a0c6373a1b742afb8dbc9cb7")
	BOT_TOKEN = os.environ.get("BOT_TOKEN", "6333028254:AAET_fIthUY8C79uU5nyQGHcXNdbvhI7zZM")
	BOT_USERNAME = os.environ.get("BOT_USERNAME", "Kc_File_Store_Bot")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1001806174534"))
	SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "onepagelink.in")
	SHORTLINK_API = os.environ.get('SHORTLINK_API', "66950884448d68d19c9545a32bbae554e6136cd5")
	BOT_OWNER = int(os.environ.get("BOT_OWNER", "5720092781"))
	DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://Nandesha:alabal18@cluster0.6qjsxnq.mongodb.net/?retryWrites=true&w=majority")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1001825196084")
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "-1002070152377")
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	ABOUT_BOT_TEXT = f"""
This is a Permanent KC FileStore Bot. 
Send Me any Media or File. I can Work In Channel too. Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 

╭────[ **🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅**]────⍟
│
├🔸 **My Name:** [FileStore Bot](https://t.me/{BOT_USERNAME})
│
├🔸 **Language:** [Python 3](https://www.python.org)
│
├🔹 **Library:** [Pyrogram](https://docs.pyrogram.org)
│
├🔹 **Hosted On:** [Heroku](https://heroku.com)
│
├🔸 **Developer:** [𝙼𝙰𝚇](https://t.me/KingKc18) 
│
├🔹 **Bot Support:** [𝙰𝙳𝙼𝙸𝙽 𝚂𝚄𝙿𝙿𝙾𝚁𝚃](https://t.me/KingKc18)
│
├🔸 **Bot Updates:** [𝙼𝙾𝚅𝙸𝙴 𝚄𝙿𝙳𝙴𝚃𝙰𝚂](https://t.me/Kc_Films_2024)
│
╰──────[ 😎 ]───────────⍟
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿:** [𝙼𝙰𝚇](https://t.me/KingKc18)
 
 I am Super noob Please Support My Hard Work.

[Donate Me](https://t.me/KingKc18)
"""
	HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent **KC FileStore Bot**.

How to Use Bot & it's Benefits??

📢 Send me any File & It will be uploaded in My Database & You will Get the File Link.

⚠️ Benefits: If you have a TeleGram Movie Channel or Any Copyright Channel, Then Its Useful for Daily Usage, You can Send Me Your File & I will Send Permanent Link to You & Channel will be Safe from **CopyRight Infringement** Issue. I support Channel Also You Can Check **About Bot**.

❌ **PORNOGRAPHY CONTENTS** are strictly prohibited & get Permanent Ban.
"""
