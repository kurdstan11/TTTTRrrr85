from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("API_ID", "13980703")) #لا تغير هاذة القيمة
API_HASH = getenv("API_HASH", "8739dceb2d5ee894b67b106efc50d52c")#لا تغير هاذة القيمة
BOT_TOKEN = getenv("BOT_TOKEN", "5861877575:AAFC0i9Tgwcuqadnbq3fTE0EwoXYATSbvFU")
SESSION_NAME = getenv("SESSION_NAME", "1ApWapzMBu24oS_bBbNqASrCOCXvF572VjiLr0Pfuej2T-uTRMb9usoTafL4xO25RET_x4iWqY4KwJ51leHECMrerKUYxSekPn4YdPcXd7A2rlSvCIbPlmgofw9PXf-rrrToaC0MSxEFX0wBD6l4X0uv5inyFjdX93CzJzkSVfa1fIMm36VUNUJuSlI_sO0O0Zn8Qxqbjr-j_uiCKRJkKjhAfmjrSgjmOULCWG2ICXMA5fCSNCMgTE3TUSqdVn-OJGefN3ipDZkaalgu0NQ7TaEyXGyCyOA89iprTOMifhu4aYwXHJT0bqMqHgdNucZog0kTebhdP6XRR_qwyGch0MeBS8ogNAMo=")

# mandatory vars
OWNER_USERNAME = getenv("OWNER_USERNAME", "kurdi_sport") # @ هنا ضع يوزر حسابك بدون 
ALIVE_NAME = getenv("ALIVE_NAME", "BEZARM") # هنا ضع اسم حسابك
BOT_USERNAME = getenv("BOT_USERNAME", "kurdi_sport_BOT") # @ هنا ضع يوزر البوت بدون 
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/kurdstan11/TTTTRrrr85") 
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main") #لا تغير هاذة القيمة
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60")) #لا تغير هاذة القيمة
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "Reklam_jat") # @ هنا ضغ يوزر كروبك بدون 
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Hzrvany_savy") # @ هنا ضغ يوزر قناتك بدون

# database, decorators, handlers mandatory vars
MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . $").split())
OWNER_ID = list(map(int, getenv("OWNER_ID", "5799939262").split()))
                                             #هنا ضع ايدي المطور فوق و الاعلئ
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5799939262").split()))

# image resources vars
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.png")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.png")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/d70bb6fa92728763c671f.png")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/430dcf25456f2bb38109f.png")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/cd5c96a3c7e8ae1913ef3.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
