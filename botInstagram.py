from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(executable_path=r'C:\Users\joaov\Desktop\geckodriver\geckodriver.exe')

    # //a[@href='/accounts/login/?source=auth_switcher']
    # //input[@name='username']
    # //input[@name='password']

    def login(self):
        driver = self.driver
        driver.get('https://www.instagram.com/') #Abre o link do Instagram

        time.sleep(2) #Para a execução por 2 segundos, para parecer mais como uma atividade humana

        # login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']") #Encontra o link com o href especificado
        # login_button.click() ////Caso a primeira página que abra no seu navegador seja a de cadastro

        user_element = driver.find_element_by_xpath("//input[@name='username']") #Encontra o input com o name especificado
        user_element.clear()#zerar qualquer histórico no campo
        user_element.send_keys(self.username)#Digita o username no input informado

        password_element = driver.find_element_by_xpath("//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.password)
        password_element.send_keys(Keys.RETURN)#Aciona o botão enter para fazer login

        time.sleep(5)

        self.curtir_fotos("memesBR")

    def curtir_fotos(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(5)
        for i in range(1, 3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
        hrefs = driver.find_elements_by_tag_name('a')
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
        for pic_href in pic_hrefs:
            if 'tags' in pic_href:
                pass
            else:
                driver.get(pic_href)
                #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                try:
                    botao_curtir = driver.find_element_by_class_name('//button[@class="wpO6b"]')
                    print(botao_curtir)
                    botao_curtir.click()
                    time.sleep(19)
                except Exception as e:
                    time.sleep(5)



joaoBot = InstagramBot('myUser', 'myPassword')
joaoBot.login()
