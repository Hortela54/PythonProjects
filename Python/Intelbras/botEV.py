from selenium import webdriver
import pyautogui
import time

cont = 1

navegador = webdriver.Chrome()
navegador.set_window_size(1000,1000) #tamanho da tela
navegador.get('https://intelbras.umov.me/CenterWeb/#__main__') #url site
navegador.find_element_by_xpath('//*[@id="username"]').send_keys("samuel.silva@intelbras.com.br") #login
navegador.find_element_by_xpath('//*[@id="password"]').send_keys("S!A@055861") #senha
navegador.find_element_by_xpath('//*[@id="submit_button"]').click() #botão entrar
time.sleep(3)
pyautogui.click(x=905, y=160) #engrenagem
pyautogui.click(x=872, y=223) #exportar
time.sleep(1)
pyautogui.click(x=428, y=335) #tipo de exportação
pyautogui.click(x=394, y=376) #exportação de execução
time.sleep(0.5)
pyautogui.click(x=646, y=339) #modelo
time.sleep(0.5)
pyautogui.click(x=641, y=417) #Conqusitadores do olimpo outubro EV
time.sleep(0.5)
pyautogui.click(x=297, y=442) #pedir exportação
time.sleep(15) 
pyautogui.click(x=947, y=500) #atualizar lista
time.sleep(1) 
pyautogui.click(x=852, y=594) #download
navegador.close()

mouse = pyautogui.position
print(mouse)