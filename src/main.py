from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time, random, urllib.request, config, requests, os

chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
url = "https://account.mail.ru/signup?back=https%3A%2F%2Faccount.mail.ru%2Fregister%3Fauthid%3Dlc7psg5f.6h7%26dwhsplit%3Ds10273.b1ss12743s%26from%3Dlogin&dwhsplit=s10273.b1ss12743s&from=login"


puth = os.path.dirname(os.path.abspath(__file__)) + '\\'

def getRand(ln):
    password = ''
    for i in range(ln):
        password += random.choice(chars)
    return password


def check_capcha(img):

    r = requests.post('http://rucaptcha.com/in.php', data={'key': config.token, 'method': 'base64', 'body': img, 'phrase': 0, 'regsense': 0, 'lang': 'en'}).text

    print(f'request - {r}')
    capcha_id = ''

    if(r[:2] == 'OK'):
        capcha_id = r[3:]
    else:
        return False

    for i in range(8):
        time.sleep(5)
        result = requests.get(f'http://rucaptcha.com/res.php?key={config.token}&action=get&id={capcha_id}').text
        print(result)
        if(result[:2] == 'OK'):
            return result[3:]
    return False


def reg_mail():
    browser = webdriver.Chrome()
    browser.get(url)

    browser.find_element(by=By.NAME, value='fname').send_keys(getRand(6))
    browser.find_element(by=By.NAME, value='lname').send_keys(getRand(6))
    username = getRand(8)
    browser.find_element(by=By.NAME, value='username').send_keys(username)

    browser.find_element(by=By.CLASS_NAME, value='label-0-2-145').click()
    password = getRand(12)

    browser.find_element(by=By.LINK_TEXT, value='Указать резервную почту').click()
    browser.find_element(by=By.LINK_TEXT, value='Сгенерировать надёжный пароль').click()
    password = browser.find_element(by=By.NAME, value='password').get_attribute("value")
    browser.find_elements(by=By.CLASS_NAME, value='Select__value-container')[0].click()
    browser.find_elements(by=By.CLASS_NAME, value='Select__option')[7].click()
    browser.find_elements(by=By.CLASS_NAME, value='Select__value-container')[1].click()
    browser.find_elements(by=By.CLASS_NAME, value='Select__option')[2].click()
    browser.find_elements(by=By.CLASS_NAME, value='Select__value-container')[2].click()
    browser.find_elements(by=By.CLASS_NAME, value='Select__option')[30].click()

    print(f'{username}@mail.ru:{password}')
    browser.find_element(by=By.NAME, value='email').send_keys(f'{getRand(6)}@rambler.ru')

    browser.find_elements(by=By.XPATH, value="//button[@type='submit']")[1].click()
    time.sleep(3)

    img = browser.find_elements(by=By.TAG_NAME, value="img")[1].screenshot_as_base64


    if(len(img) < 1000):
        return False

    result = check_capcha(img)

    if(result == False):
        return False

    browser.find_element(by=By.CLASS_NAME, value='input-0-2-112').send_keys(result)
    browser.find_elements(by=By.XPATH, value="//button[@type='submit']")[0].click()

    time.sleep(5)

    if(browser.current_url == url):
        return False

    return f'{username}@mail.ru:{password}'


if __name__ == "__main__":
    count = int(input('Quantity autoreg: '))
    file = open(f"{puth}autoreg[{getRand(5)}].txt", "w")

    for i in range(count):
        reg = reg_mail()
        if(reg == False):
            print("Error!")
            break
        else:
            file.write(reg + '\n')

    file.close()