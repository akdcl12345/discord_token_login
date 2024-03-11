import os, sys, ctypes, time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
os.system('cls')
print("")
print("")
print(
    "\x1b[31m" + "██╗  ██╗ █████╗ ███╗   ███╗███╗   ███╗███████╗██████╗     ██╗      ██████╗  ██████╗ ██╗███╗   ██╗" + "\x1b[0m")
print(
    "\x1b[33m" + "██║  ██║██╔══██╗████╗ ████║████╗ ████║██╔════╝██╔══██╗    ██║     ██╔═══██╗██╔════╝ ██║████╗  ██║" + "\x1b[0m")
print(
    "\x1b[32m" + "███████║███████║██╔████╔██║██╔████╔██║█████╗  ██████╔╝    ██║     ██║   ██║██║  ███╗██║██╔██╗ ██║" + "\x1b[0m")
print(
    "\x1b[36m" + "██╔══██║██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝  ██╔══██╗    ██║     ██║   ██║██║   ██║██║██║╚██╗██║" + "\x1b[0m")
print(
    "\x1b[34m" + "██║  ██║██║  ██║██║ ╚═╝ ██║██║ ╚═╝ ██║███████╗██║  ██║    ███████╗╚██████╔╝╚██████╔╝██║██║ ╚████║" + "\x1b[0m")
print(
    "\x1b[35m" + "╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝    ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝╚═╝  ╚═══╝" + "\x1b[0m")
print("\nSupport By 망치\n")
print("Support Server : https://guildslink.com\n ")
token = input('로그인할 토큰을 입력 : ')
ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
options=Options()
driver = webdriver.Chrome(options=options)
driver.get('https://discord.com/login')
js = 'function login(token) {setInterval(() => {document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`}, 50);setTimeout(() => {location.reload();}, 500);}'
time.sleep(3)
driver.execute_script(js + f'login("{token}")')
time.sleep(100000)