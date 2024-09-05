from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
import time
import pyautogui

def instaH() -> None:
    mobile_emulation = { "deviceName": "iPhone X" }
    chrome_options = Options()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

    driver = webdriver.Chrome(options = chrome_options)

    try:
        driver.set_window_size(500, 900)
        driver.get('https://www.instagram.com/accounts/login/')
        time.sleep(10)
        text_input = driver.find_element(By.NAME, "username")
        text_input.send_keys('') #Ingresa tu usuario
        text_input = driver.find_element(By.NAME, "password")
        text_input.send_keys('') #Ingresa tu contraseña
        time.sleep(1)
        button = driver.find_element(By.XPATH, "//div[contains(text(),'Entrar')]")
        button.click()
        time.sleep(15)
        button = driver.find_element(By.XPATH, "//div[contains(text(),'Ahora no')]")
        button.click()
        time.sleep(10)
        try:
            button = driver.find_element(By.XPATH, "//button[contains(text(),'Cancelar')]")
            button.click()
        except:
            pass
        time.sleep(2)
        action = ActionChains(driver)
        action.move_by_offset(312, 20).click().perform()
        time.sleep(2)
        action2 = ActionChains(driver)
        action2.move_by_offset(0, 80).click().perform()

        time.sleep(300)
        
        time.sleep(10)

    # Sigue en desarrollo

    finally:
        driver.quit()

if __name__ == "__main__":
    instaH()