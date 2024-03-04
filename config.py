import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7056418695:AAGeFA1ZTEP3SzZNZ7SSHZSofZuvTBzYmrI")
    API_ID = int(os.environ.get("API_ID", 24100993))
    API_HASH = os.environ.get("API_HASH", "22e7ddd8edc0dc58ffa67a57b06a8712")
    DB_URL = os.environ.get("DATABASE_URL", "mongodb+srv://<Abdul2024>:<abdul54321>@cluster0.6xep2fb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
