from selenium import webdriver
from time import sleep
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import threading
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

'''
███████╗██████╗ ███████╗███████╗██████╗ ██████╗  ██████╗ ████████╗    ██╗   ██╗██████╗ 
██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗██╔═══██╗╚══██╔══╝    ██║   ██║╚════██╗
█████╗  ██████╔╝█████╗  █████╗  ██████╔╝██████╔╝██║   ██║   ██║       ██║   ██║ █████╔╝
██╔══╝  ██╔══██╗██╔══╝  ██╔══╝  ██╔══██╗██╔══██╗██║   ██║   ██║       ╚██╗ ██╔╝██╔═══╝ 
██║     ██║  ██║███████╗███████╗██║  ██║██████╔╝╚██████╔╝   ██║        ╚████╔╝ ███████╗
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚═════╝  ╚═════╝    ╚═╝         ╚═══╝  ╚══════╝

Credits to Github: @xtekky

How freer.es works:
captcha > tiktok > input link > search > select views > close popup > 10 min timer > refresh > ...
'''


username = input('Link: ')

def main():
    global wait
    global driver
    global username

    # chrome_options.add_argument("--headless")
    print('[*] Loading Site')
    driver.get('https://homedecoratione.com')
    print('[*] Site Loaded')
    try:

        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="msg"]/div/div[1]/div[3]/div/div/button'))).click()
        print('[*] TikTok selected')
        methodFollowers()
    except:
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="bootstrap-show-modal-0"]/div/div/div[1]/button/ span'))).click()
            print('')
        except:


            print("[x] Make sure that captcha is solved")
            sleep(10)
            main()


def methodFollowers():
    try:
        print("[N] Getting TikTok link")
        # sleep(1)


        wait.until(EC.element_to_be_clickable((By.ID, "searchinput"))).clear()  # clear link input
        wait.until(EC.element_to_be_clickable((By.ID, "searchinput"))).send_keys(username)  # input url
        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"form1\"]/div/div/button"))).click()  # search url
        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"msg\"]/div/div/div[1]/h5/button[2]"))).click()  # select views
        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"bootstrap-show-modal-0\"]/div/div/div[1]/button"))).click()  # close popup button
        print("[+] Views Sent!")
        print('[-] Sleeping 10 min')
        sleep(600) #sleep 10 min
        methodFollowers()

    except:
        print('[-] An error occurred')
        main()


if __name__ == "__main__":
    opt = webdriver.ChromeOptions()
    opt.add_argument("--disable-popup-blocking")
    opt.add_argument("user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B179 Safari/7534.48.3")
    driver = uc.Chrome(use_subprocess=True, options=opt)
    wait = WebDriverWait(driver, 15)
    driver.set_window_size(1024, 480)
    driver.delete_all_cookies()
#so this is an user agent but idk, i have to find some usable agents, this is an iphone for example, lets start the script
    a = threading.Thread(target=main)

    a.start()
'''captcha image not loading because of the user agen pro
yeees idk , sometimes there is sometimes npt
can you reoeat
ok lets try without '''
#https://www.tiktok.com/@repl1c4.world/video/7078355419445366022?is_from_webapp=1&sender_device=pc&web_id=7062836892223768069*

#ok wait

