import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import csv
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# ""안에 드라이버 폴더 경로를 넣어주세요
service = ChromeService(executable_path="")
driver = webdriver.Chrome(service = service)
f = open(r"C:/Users/user/Desktop/pay/test.csv", 'a', encoding= 'UTF-8', newline = '')
writer = csv.writer(f)

# ""안에 접속하고 싶은 url을 넣어주세요
driver.get("")

# 페이지 끝까지 스크롤 하기
while(True):
    h = driver.execute_script('return window.scrollY')
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
    if(h == driver.execute_script('return window.scrollY')):
        break

# ""안에 찾고 싶은 요소의 해당 값을 넣어주세요
driver.find_elements(By.XPATH, "")
driver.find_elements(By.CLASS_NAME, "")
driver.find_elements(By.CSS_SELECTOR, "")
driver.find_elements(By.ID, "")
driver.find_elements(By.TAG_NAME, "")

# 키 입력, 텍스트 추출 예시
driver.find_elements(By.XPATH, "").send_keys(Keys.ENTER)
driver.find_elements(By.XPATH, "").text

# 원하는 시간만큼 작업중단
time.sleep(5)

# 요청을 지정한 시간까지 대기, 완료시 즉시 다음코드 실행
driver.implicitly_wait(5)

# 열 추가 예시
for i in range(len(titles)):
    row = [titles[i].text, prices[i].text]
    print(row)
    writer.writerow(row) #열 추가 예시 
