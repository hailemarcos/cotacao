from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# driver =  webdriver.Chrome(executable_path=r'./chromedriver.exe')

#pesquisar cotação dolar
navegador = webdriver.Chrome()

navegador.get("https://www.google.com")

navegador.find_element(By.XPATH ,
'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação dólar")


navegador.find_element(By.XPATH ,
'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

#pegar cotação dolar

cotacao_dolar = navegador.find_element(By.XPATH ,
'//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')




#---------------------------------------------------------------------------------------------------



#pegar cotação euro
navegador.get("https://www.google.com")


#digitar cotação
navegador.find_element(By.XPATH ,
'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação euro")


navegador.find_element(By.XPATH ,
'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

#pegar cotação dolar

cotacao_euro = navegador.find_element(By.XPATH ,
'//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')



#----------------------------------------------------------------------------

#pegar cotação ouro
navegador.get("https://www.melhorcambio.com/ouro-hoje")


#digitar cotação

cotacao_ouro = navegador.find_element(By.XPATH, 
'//*[@id="comercial"]').get_attribute('value')

cotacao_ouro = cotacao_ouro.replace("," , ".")





#pegar cotação ouro

print("a cotação do dolar é ",cotacao_dolar)
print("a cotação do euro é",cotacao_euro)
print("a cotação do ouro é",cotacao_ouro)
