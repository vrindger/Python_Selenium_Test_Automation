from selenium import webdriver
driver= webdriver.Chrome()
driver.get("file:///html_code_02.html")
login_form = driver.find_element( value='loginForm')
print("My login form element is:")
print(login_form)
driver.close()
