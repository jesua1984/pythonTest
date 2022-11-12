from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import unittest


#############################################################
#negativo
#given
driver = webdriver.Chrome(executable_path= "chromedriver.exe")
driver.get("http://www.python.org")
#assert "Python" in driver.title

#When
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("varible")
boton = driver.find_element(By.NAME, "submit")
boton.click
time.sleep(5)

#then
#resultado = driver.find_elements_By_Xpath("//" )

#############################################################
#positivo
#given
driver = webdriver.Chrome(executable_path= "chromedriver.exe")
driver.get("http://www.python.org")
#assert "Python" in driver.title

#When
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("variable")
boton = driver.find_element(By.NAME, "submit")
boton.click
time.sleep(5)

#then
#resultado = driver.find_elements_By_Xpath("//" )
driver.close()
