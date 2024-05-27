from selenium import webdriver
driver= webdriver.Chrome()
driver.get("file:///html_code_02.html")
username = driver.find_element(by='name', value='username')
print("My input element is:")
print(username)
driver.close()
