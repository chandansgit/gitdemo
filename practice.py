#find the first and last occurance of a
from selenium import webdriver

s1 = 'amazonnaanazz'

print(s1.find('a'))
print(s1.rfind('a'))
print(s1.rindex('a'))


t1 = (*(x for x in 'pytho2n' if x.isalpha()),)
print(t1)

driver = webdriver.Chrome()
driver.get("https://www.udemy.com/")
#driver.back()
print(driver.title)