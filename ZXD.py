#_*_ coding:utf-8 _*_ 
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('http://fang.staging2.hzfapi.com/login.html')
driver.find_element_by_xpath('//input[@placeholder="输入手机号"]').send_keys('18515898084')
driver.find_element_by_xpath('//input[@placeholder="输入密码"]').send_keys('qK2NG1Wn')
driver.find_element_by_xpath('//div[@id="js-login"]').click()#点击登录
# enter=driver.find_element_by_xpath('//span[@class="guidance-btn js-cls"]') # 点击进入系统
WebDriverWait(driver,20).until(lambda x:x.find_element_by_xpath('//span[@class="guidance-btn js-cls"]')).click()
WebDriverWait(driver,20).until(lambda x:x.find_element_by_xpath('//div[@class="mine-modal-header"]/span')).click()
# driver.find_element_by_xpath('//div[@class="mine-modal-header"]/span').click()#关闭消息通知
print('++++++++++++++++++++++++++++++++++++++++++')
driver.find_element_by_xpath('//div[@class="hfq-modal-body"]/div/div[1]/div/div[2]/a[2]').click()
zxfq=driver.find_element_by_xpath('//div[@class="nav-section nav-section-rnl"]')#装修分期
ActionChains(driver).move_to_element(zxfq).perform()
driver.find_element_by_xpath('//a[contains(@href,"/decoration/contracts/list")]').click()#点击装修分期合同
driver.find_element_by_css_selector('span[class="borrowing-btn js-application"]').click()#点击申请借款
driver.find_element_by_css_selector('.loan_amount').send_keys('1000')#借款金额输入1000
# driver.find_element_by_css_selector('[data-cycle="9"]').click()#选择分期期数  该方法不知为何定位到却不执行操作
driver.find_element_by_xpath('//dd[@data-cycle="9"]').click()
try:
    WebDriverWait(driver,10).until(EC.element_located_to_be_selected(By.XPATH,'//dd[@data-cycle="9"]'))
    # EC.element_to_be_clickable(By.XPATH,'//dd[@data-cycle="9"]')
    print('期数可被点击')
    print('已经选中了')
except:
    print('未选中期数')
finally:
    driver.find_element_by_css_selector('dl.radio-panel>dd:nth-child(3)').click()
print('====================================')
driver.find_element_by_css_selector('span[class="hfq-normal-btn-l hfq-bgc-btn-color next"]').click()#点击下一步
print('+++++++++++++填写申请信息+++++++++++')
driver.find_element_by_css_selector('div.js-floor>input').send_keys('5')#楼层
driver.find_element_by_css_selector('div.js-total-floor>input').send_keys('10')#总楼层