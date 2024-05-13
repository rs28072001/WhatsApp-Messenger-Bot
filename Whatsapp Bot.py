    # Code For Bot Is here  
import time,subprocess,csv,os,pyautogui
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin

# web = webdriver.Chrome(ChromeDriverManager().install(),options= option)
base_url = 'https://web.whatsapp.com'

yessing = input("=> If you wanna Open Browser Type 'Yes' if 'No' then skip it\n")


def loading(yourword,rest):
    from sys import stdout
    loading_speed = 10
    loading_string = f"{yourword}......" * 1
    for i in range(rest):  
        for index, char in enumerate(loading_string):
            stdout.write(char)
            stdout.flush()  
            time.sleep(1.0 / loading_speed) 
        index += 1  
        stdout.write("\b" * index + " " * index + "\b" * index)
        stdout.flush() 

def get_br_path():
    from os.path import join as OsJoin
    from os.path import expanduser
    from os import environ
    possible_paths = [OsJoin(environ["PROGRAMFILES(X86)"], "Google", "Chrome", "Application", "chrome.exe"),
    OsJoin(environ["PROGRAMFILES"], "Google", "Chrome", "Application", "chrome.exe"),
    OsJoin(expanduser("~"), "AppData", "Local", "Google", "Chrome", "Application", "chrome.exe"),]
    chrome_paths = [path for path in possible_paths if os.path.exists(path)]
    if chrome_paths:
        for path in chrome_paths:
            browserpath =  (path)
    return path
         
def loginprocess():
    cmd = f'"{get_br_path()}" --remote-debugging-port=9765 --user-data-dir="C:\ChromeProfiles\9765"'
    subprocess.Popen(cmd, shell=True)

if yessing.lower() == 'yes': 
    loginprocess()
    option = webdriver.ChromeOptions()
    option.add_experimental_option("debuggerAddress","localhost:9765")
    time.sleep(1)
    web = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=option)
    web.get(base_url)
    loading('Webpage is Opening....',5)
else:
    try:                
        option = webdriver.ChromeOptions()
        option.add_experimental_option("debuggerAddress","localhost:9765")
        web = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=option)
    except:
        input('\n\n=> Browser Connection Failed, Please Make Sure Browser is Opened')
        exit()


def active_content(sent_message,sent_img):
   loading('Sending message....',1)
   if sent_img == "":
        WebDriverWait(web, 20).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div[2]/div[1]'))).send_keys(sent_message)
   else:
        WebDriverWait(web, 20).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[1]'))).send_keys(sent_message)
   cont =  web.switch_to.active_element
   loading('Submitting message....',1)
   cont.send_keys(Keys.RETURN)
   loading('Message Sent Successfully....',1)

def auto_messaging(phonenum,sent_message,sent_img):
    doit =  base_url + "/send?phone=" + str(phonenum)
    web.get(doit)
    loading('Opening the Chat....',5)
    if sent_img == "":
        active_content(sent_message,sent_img)
    else:    
        WebDriverWait(web, 20).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]')))
        web.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/div/span').click()
        web.implicitly_wait(3)
        WebDriverWait(web, 20).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div/div/span/div/ul/div/div[2]/li/div/input')))
        img = web.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div/div/span/div/ul/div/div[2]/li/div/input')
        web.implicitly_wait(3)
        img.send_keys(sent_img)
        loading('Uploading Image....',5)
        active_content(sent_message,sent_img)


def one_screen(phonenum,sent_message,sent_img):
    WebDriverWait(web, 20).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div[3]/header/div[2]/div/span/div[5]'))).click()
    search_bar = WebDriverWait(web, 20).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div[1]/span/div/span/div/div[1]/div[2]/div[2]/div/div[1]/p'))).send_keys(phonenum)
    loading(f'Initiating the Chat with {phonenum}....',1)
    user_chat = WebDriverWait(web, 20).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div[1]/span/div/span/div/div[2]/div/div/div/div[2]/div/div/div[2]'))).click()
    if sent_img == "":
        active_content(sent_message,sent_img)
    else:    
        loading(f'Fetching The Image/Video....',1)
        web.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/div/span').click()
        img = web.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div/div/span/div/ul/div/div[2]/li/div/input')
        img.send_keys(sent_img)
        loading(f'Image is Ready to Send to this => {phonenum}....',2)
        active_content(sent_message,sent_img)

def read_csv():
    try:
        with open('numbers.csv', newline='') as csvfile:
            csvreader = csv.DictReader(csvfile)
            for row in csvreader:
                phonenum = (row['Numbers'])
                sent_message = (row['Messages'])
                sent_img = (row['File'])
                if workfunc == '1':
                    auto_messaging(phonenum,sent_message,sent_img)
                else:
                    one_screen(phonenum,sent_message,sent_img)

    except Exception as e:
        input(f"\n\n => Error :- {e}\n=> Solution:- Create 'numbers.csv' file in which 'Numbers','Messages','File' respective column names")
        return()
            
def refine_number(group_name,groupHeading):
    all_numbers = str(groupHeading).split(',')
    with open(f'{group_name}.txt', 'w') as f:
        for line in all_numbers:
            f.write(line + '\n')
    print(f"\n\nSuccessfully all Numbers Extracted in :- {group_name}")

def extract_number():
    group_name = input("\n\n=> Enter the Group Name\n")
    search_bar = web.find_element(By.XPATH,'//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]')
    search_bar.send_keys(group_name)
    WebDriverWait(web, 20).until(EC.visibility_of_element_located((By.CLASS_NAME,'_ak8q')))
    loading('Searching Group ....',1)
    find_number = web.find_elements(By.CLASS_NAME,'_ak8q')
    find_number[-1].click()           
    loading('Opening Chat of Group....',2)
    if workfunc == 5:
        return
    groupHeading = WebDriverWait(web, 20).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="main"]/header/div[2]/div[2]/span'))).get_attribute("innerHTML")
    if groupHeading == "click here for group info":
        loading('Wait for Load Numbers....',2)
    groupHeading = WebDriverWait(web, 20).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="main"]/header/div[2]/div[2]/span'))).get_attribute("innerHTML")
    refine_number(group_name,groupHeading)

def rapid_group():
    group_name = WebDriverWait(web, 20).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="main"]/header/div[2]/div[1]/div/span'))).get_attribute("innerHTML")
    name_consent = input(f"\n\n=> {group_name}<-- This is the Group Name if You wanna change file name Press:- No\n")
    if name_consent.lower() == 'no':
        group_name = input("\n\n=> Enter Group Name \n")
    groupHeading = WebDriverWait(web, 20).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="main"]/header/div[2]/div[2]/span'))).get_attribute("innerHTML")
    refine_number(group_name,groupHeading)

number_list = []
check_length = []

def put_number(num,group_name):
    global count
    if num not in number_list:
        count = 0
        print('=> Scraped Number :-',num)
        number_list.append(num)
        with open (f'{group_name}.txt','a') as txt:
            txt.write((num))
            txt.write('\n')

def extract_all_number():
    global count
    group_name = input('\n\n=> Open the Group and Click on View All Members and Enter the File Name\n\n')
    count = 0
    while count <= 9:
        try:
            snum = web.find_elements(By.CSS_SELECTOR, '.x10l6tqk.xh8yej3.x1g42fcv[role="listitem"]')
            for sn in snum:
                headtext = str(sn.text)
                if '+' in headtext:
                    # print(headtext,'lenght=>',len(headtext),'\n')
                    num="+"
                    for n in headtext.split('+')[-1]:
                        if n == ' ':
                            num += ' '
                        else:
                            try :
                                int(n)
                                num += str(n)
                            except Exception as e:
                                break
                    if '+91' in num:
                        num = num.replace(' ','')[:13]
                # num = (headtext.split('+91 ')[-1][:11]).replace(' ','')
                    check_length.append(len(number_list))
                    put_number((num),group_name)
            print('The Checking System',len(number_list),' ==', check_length[-1])
        
        except Exception as e:
            print('WE GOT ERROR :',e)
            pass
        count += 1
        print('\n\n',count,'<= Finishes value becomes 10',number_list,'\n\n')
        pyautogui.FAILSAFE
        pyautogui.press('pagedown',interval=3)
    
    input("\n\n=> Program Completed :)\n\n")


while True:
    workfunc = input("\n\n=> Press:- 1 for sending messages with Number Link Technique Crash Rate 2%\n\n=> Press:- 2 for sending messages with New Chat Technique Crash Rate 5%\n\n=> Press:- 3 for scrape numbers from group (crash rate:-10%) you have to just enter the group name and it's automatically search and Scrape \n\n=> Press:- 4 for scrape number from group (crash rate:-0%) you have mannually open the group chat for scraping the numbers\n\n=> Press:- 5 for extract numbers if group contains more than 500+ members\n\n")

    if workfunc == '1':
        read_csv()
    elif workfunc == '2':
        read_csv()
    elif workfunc == '3':
        extract_number()
    elif workfunc == '4':
        rapid_group()
    elif workfunc == '5':
        extract_all_number()
    else:
        input(f"\n\nInvalid User Input ! {workfunc}")

    if input("\n\n=> If You wanna start Again Press 'Enter' if No then Type 'No'").lower() == 'no':
        exit()

    
        




