from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
#from secrets import pw
PATH = "/Users/edwinkam/Documents/Code/Auto_Robot/chromedriver"


class InstaBot:
    def __init__(self):
        self.driver= webdriver.Chrome(PATH)
        self.driver.get("https://www.nike.com/launch/t/womens-air-force-1-pixel-leopard?cp=65052578087_search_%7Csnkrs%7Cg%7C11856077755%7C115377939556%7Ce%7Cc")
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div[1]/div/div[2]/div[2]/div/section[1]/div[2]/aside/div/div[2]/div/div[2]/ul/li[13]').click()
        self.driver.find_element_by_xpath('//button[contains(text(), "Add to Cart")]').click()
        
#        self.driver.find_element_by_xpath("//a[contains(text(), 'Sign up')]").click()
#        sleep(2)
#        self.driver.find_element_by_name("username").send_keys(un)
#        self.driver.find_element_by_name("password").send_keys(pw)
#        self.driver.find_element_by_name("password").send_keys(Keys.RETURN)
#        sleep(5)
#        self.driver.find_element_by_xpath('//button[contains(text(), "Not Now")]').click()
        sleep(10)
#        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/span").send_keys('_.0506bh._')
#        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input").send_keys('Cat39170826')
#        self.driver.find_element_by_xpath("//button[@type='Submit']").click()
        

#driver = webdriver.Chrome(P)
InstaBot()
