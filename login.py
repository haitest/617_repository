#_*_ coding:utf-8 _*_ 
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions  as EC
import datetime

driver=webdriver.Firefox()
# driver.implicitly_wait(10)
driver.maximize_window()
driver.get('http://sso.huizhaofang.com/sso/oauth/login/?next=/sso/authorize/%3Fresponse_type%3Dcode%26client_id%3DHO6ENoZq6mT1O0URXVbZTMAGX0BMPecuDNVPC8X6%26redirect_uri%3Dhttp%3A//boss.staging2.hzfapi.com/v2/api/auth/callback/%26state%3DeyJvcmlnaW5fdXJpIjogIi8jL3JlbnRTdGFnaW5nIn0%3D%3Forigin_uri%3D%252F%2523%252FrentStaging')
driver.find_element_by_xpath('//input[@placeholder="请输入账号" and @type="text"]').send_keys('zhanghai@huizhaofang.com')
driver.find_element_by_xpath('//input[@placeholder="输入密码"]').send_keys('19880611zH')
driver.find_element_by_xpath('//button[@class="el-button el-button--primary"]').click()
sleep(1)
driver.find_element_by_css_selector('li.el-submenu:nth-child(9) > div:nth-child(1)').click()
sleep(3)

# WebDriverWait(driver,10).until(EC.visibility_of_element_located(By.CSS_SELECTOR,'li.el-submenu:nth-child(9) > ul:nth-child(2) > li:nth-child(8)'))
driver.find_element_by_css_selector('li.el-submenu:nth-child(9) > ul:nth-child(2) > li:nth-child(8)').click()
# driver.find_element_by_css_selector('button[span="批量生成确认书"]').click()
# ActionChains(driver).move_to_element(By.CSS_SELECTOR,"")
# sleep(3)
WebDriverWait(driver,10,0.5).until(lambda x:x.find_element_by_css_selector('.hfq-list-page-content > div:nth-child(2) > button:nth-child(1)')).click()
sleep(3)
img_name=datetime.datetime.now().strftime('%Y%m%d%H%M%S')+'_qrs.png'
print(img_name)
driver.get_screenshot_as_file(img_name)


driver.quit()