from selenium import webdriver

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.implicitly_wait(15)

driver.get('http://ynet.co.il')
main_paragraph = driver.find_element_by_xpath('/html/body/div[7]/div/div/div[1]/div[4]/div[1]/span/div/div/div[2]/div/div/div/div[1]/div[3]/a/span')
print(main_paragraph.text)

driver.close()

