from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def cobretad(args: list[str]) -> str: 
	driver = webdriver.Chrome()
	try:
		driver.set_window_size(700, 600)
		driver.get('https://www.cobremex.com/clientes/clientesreg/Login')
		time.sleep(10)
		text_input = driver.find_element(By.NAME, "Documento")
		text_input.send_keys(args[0])
		text_input = driver.find_element(By.NAME, "Clave")
		text_input.send_keys(args[1])
		time.sleep(1)
		button = driver.find_element(By.XPATH, "//button[contains(text(),'Ingresar')]")
		button.click()
		time.sleep(7)
		element = driver.find_element(By.XPATH, "//h4[@class='text-center text-white font-italic']")
		text = element.text
		return text
	finally:
		driver.quit()
if __name__ == "__main__":
	cobretad()