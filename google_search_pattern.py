from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options


service = Service("chromedriver.exe")
chrome_options = Options()
# chrome_options.add_argument("--user-data-dir=C:/Users/mohd.saad/AppData/Local/Google/Chrome/User Data")
# chrome_options.add_argument("--profile-directory=Default")
driver = webdriver.Chrome(webdriver.,options=chrome_options)

def google_search_data(companyname):
    #google_url=f'https://www.google.com/search?q={companyname}+linkedin'
    search_company=f'{companyname} linkedin'
    driver.get('https://www.google.co.in')
    time.sleep(5)
    driver.find_element(By.ID,'APjFqb').send_keys(search_company)
    driver.find_element(By.ID,'APjFqb').submit()

    time.sleep(3)
    driver.find_element(By.XPATH,'//a[@jsname="UWckNb"]').click()

    try:
        driver.find_element(By.XPATH,'//a[@class="ember-view active pv3 ph4 t-16 t-bold t-black--light org-page-navigation__item-anchor "]').click()
    except NoSuchElementException:
        pass
    try:
        if driver.find_element(By.XPATH,'//div[@class="modal__overlay flex items-center bg-color-background-scrim justify-center fixed bottom-0 left-0 right-0 top-0 opacity-0 invisible pointer-events-none z-[1000] transition-[opacity] ease-[cubic-bezier(0.25,0.1,0.25,1.0)] duration-[0.17s] py-4 modal__overlay--visible"]'):
            driver.execute_script("""document.getElementsByClassName("modal__overlay flex items-center bg-color-background-scrim justify-center fixed bottom-0 left-0 right-0 top-0 opacity-0 invisible pointer-events-none z-[1000] transition-[opacity] ease-[cubic-bezier(0.25,0.1,0.25,1.0)] duration-[0.17s] py-4 modal__overlay--visible")[0].style.display='none'""")
            driver.execute_script("document.body.style.overflow='auto'")
    except NoSuchElementException:
        pass
    time.sleep(2)
    try:
        if driver.find_element(By.XPATH,'//h1[@class="top-card-layout__title font-sans text-lg papabear:text-xl font-bold leading-open text-color-text mb-0"]'):
            company_name = driver.find_element(By.XPATH,'//h1[@class="top-card-layout__title font-sans text-lg papabear:text-xl font-bold leading-open text-color-text mb-0"]').text
    except NoSuchElementException:
        company_name = companyname
    time.sleep(2)
    try:
        if driver.find_element(By.XPATH, """//p[@class="break-words white-space-pre-wrap t-black--light text-body-medium"]"""):
            company_desc=driver.find_element(By.XPATH, """//p[@class="break-words white-space-pre-wrap t-black--light text-body-medium"]""").text
        else:
            pass
    except NoSuchElementException:
        company_desc='no description'
    try:
        if driver.find_element(By.XPATH,'//div[@data-test-id="about-us__industry"]/dd'):
            industry_type=driver.find_element(By.XPATH,'//div[@data-test-id="about-us__industry"]/dd').text
    except NoSuchElementException:
        industry_type='No Industry Type'
    # try:
    #     element=driver.find_element(By.PATH,'//div[@data-test-modal-id="org-page-viewing-setting-modal"]')
    #     if element:
    #          driver.execute_script("""document.getElementsByClassName("artdeco-modal-overlay artdeco-modal-overlay--layer-default artdeco-modal-overlay--is-top-layer  ember-view")[0].style.display='none'""")
    #     else:
    #         pass
    # except NoSuchElementException:
    #     return None

    company_data = {
        'company_name': company_name,
        'company_description': company_desc,
        'industry_type': industry_type,
    }
    return company_data

