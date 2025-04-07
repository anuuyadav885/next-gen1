import os

API_ID = os.environ.get("API_ID", "24509126")

API_HASH = os.environ.get("API_HASH", "2c1e3e02b9e1b0a3f9c7955d5d55a1d5")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7486654677:AAEMctqP4RTuYbJ8PssgLvYsyS7HmgRoxdU")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6127347210))

LOG = -1002684777603,

# UPDATE_GRP = , # bot sat group

# auth_chats = []

try:
    ADMINS=[6127347210]
    for x in (os.environ.get("ADMINS", "7827463899").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)
