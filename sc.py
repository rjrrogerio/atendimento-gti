from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait


# Credentials
username = "rogerio.junior"
password = "68931520@Rr*"

# initialize the Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://intrasesc.sescsp.org.br/web/guest/login")
# find username/email field and send the username itself to the input field
driver.find_element("id", "_br_org_sescsp_intrasesc_customlogin_CustomLoginPortlet_login").send_keys(username)
# find password input field and insert password as well
driver.find_element("id", "_br_org_sescsp_intrasesc_customlogin_CustomLoginPortlet_password").send_keys(password)
# click login button
driver.find_element("id", "_br_org_sescsp_intrasesc_customlogin_CustomLoginPortlet_kbge").click()

# wait the ready state to be complete
WebDriverWait(driver=driver, timeout=10).until(
    lambda x: x.execute_script("return document.readyState === 'complete'")
)

error_message = "Incorrect username or password."
# get the errors (if there are)
errors = driver.find_elements("css selector", ".flash-error")
# print the errors optionally
# for e in errors:
#     print(e.text)
# if we find that error message within errors, then login is failed
if any(error_message in e.text for e in errors):
    print("[!] Login failed")
else:
    print("[+] Login successful")

driver.close()

