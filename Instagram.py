import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

driver = webdriver.Chrome('./chromedriver')

driver.get('https://www.instagram.com')
driver.maximize_window()
time.sleep(10)
userinput = driver.find_elements_by_xpath("//input[@name='username']")

time.sleep(5)
userinput[0].send_keys("ansari.rizwan.007")#userName

password = driver.find_elements_by_xpath("//input[@name='password']")
password[0].send_keys("")#Password
time.sleep(5)

login_button = driver.find_elements_by_xpath("//div[contains(text(),'Log In')]")
login_button[0].click()
time.sleep(5)
try:
    not_now = driver.find_elements_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")
    time.sleep(5)
    not_now[0].click()
except:
    pass
window_before = driver.window_handles[0]
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])
time.sleep(10)
driver.get("https://www.instagram.com/katrinakaif")
print("Current Page Title is : %s" % driver.current_url)
followers = driver.find_element_by_xpath("/html/body/div[1]/div/div/section/main/div/header/section/ul/li[2]/a")
nofollowers = driver.find_element_by_class_name("g47SY")
nofollowers = nofollowers.text
nofollowers = nofollowers.replace(" ", "")
try:
    nofollowers = int(nofollowers)
except:
    nofollowers=1
nofollowers = nofollowers + 2
followers.click()
driver.implicitly_wait(30)
totalPeople = []
c = 0
followersListData = []
while c <= 50:
    time.sleep(2)
    scr = driver.find_elements_by_xpath("//div[@class='isgrP']")

    driver.execute_script("arguments[0].scrollTop=arguments[0].scrollHeight", scr[0])
    followersList = driver.find_elements(By.CLASS_NAME, "isgrP")
    flage = False
    for follower in followersList:
        check = follower.find_elements_by_tag_name("li")

        driver.implicitly_wait(10)

        checklen = len(check)


        if checklen >= 500:

            d = 0
            for user in check:

                if d == 0 or d == 1 or d == 2 or d==3 or d==4:
                    pass
                else:
                    flage = True

                    try:
                        url = user.find_element_by_tag_name("a")

                        usrurl = url.get_attribute("href")
                    except:
                        usrurl=''
                    totalPeople.append(usrurl)

                    user = user.text
                    user = user.split("\n")

                    userInf = []
                    username = user[0]
                    fullname = user[1]
                    userInf.append(str(fullname))
                    userInf.append(str(username))
                    userInf.append(str(usrurl))
                    followersListData.append(userInf)

                d = d + 1

            break
        else:
            pass
    if flage:
        break
    else:
        pass


    c = c + 1
fields = ["Full Name", "User Name", "User Profile Link"]
with open('Followers.csv', 'w', newline='') as file:
    csvwriter = csv.writer(file)

    # writing the fields
    csvwriter.writerow(fields)

    # writing the data rows
    csvwriter.writerows(followersListData)

