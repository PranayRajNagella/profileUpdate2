from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

def update_naukri_profile(username,password):
        print("hello")
        service = Service(ChromeDriverManager().install())
        chrome_options = Options()
        # chrome_options.add_argument("--headless")  # Enable headless mode
        # chrome_options.add_argument("--disable-gpu")
        # chrome_options.add_argument("--window-size==1920,1080")
        # chrome_options.add_argument("--no-sandbox")
        # chrome_options.add_argument("--disable-dev-shm-usage")
        # chrome_options.add_argument(
        #     "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36")
        driver = webdriver.Chrome(service=service,options=chrome_options)
        driver.maximize_window()
        driver.get("https://www.naukri.com")

        # Login
        login_btn = WebDriverWait(driver, 120).until(
            EC.presence_of_element_located((By.XPATH, "// a[@ title = 'Jobseeker Login']"))
        )
        login_btn.click()

        usr_btn= WebDriverWait(driver, 120).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter your active Email ID / Username']"))
        )
        usr_btn.send_keys(username)
        password_field = driver.find_element(By.XPATH, "//input[@placeholder='Enter your password']")
        password_field.send_keys(password)
        driver.find_element(By.XPATH, '//button[@type="submit"]').click()

        # Navigate to profile editing
        driver.get("https://www.naukri.com/mnjuser/profile")  # or a specific profile edit link

        try:
            cross_button = WebDriverWait(driver, 120).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//div[@class='crossIcon chatBot chatBot-ic-cross']")))
            cross_button.click()
        except TimeoutException:
            print("Exeption in cross button either not there")
        except Exception as e:
            print("Failed here on the cross button")
            e.with_traceback()

        try:
           edit_summary_button = WebDriverWait(driver, 120).until(
               EC.presence_of_element_located(
                   (By.XPATH, "//div[@class='resumeHeadline']//div//span[@class='edit icon']"))
           )

           edit_summary_button.click()

           print("Here Clicked")
           summary_textarea = WebDriverWait(driver, 120).until(
               EC.element_to_be_clickable((By.XPATH, "//textarea[@id='resumeHeadlineTxt']"))
           )
           current_summary_text = summary_textarea.text
           print(current_summary_text)
           summary_textarea.clear()
           if '...' in current_summary_text:
               summary_textarea.send_keys(current_summary_text.replace("...", ""))
           else:
               summary_textarea.send_keys(current_summary_text + "...")
           save_button = driver.find_element(By.XPATH, "//form[@name='resumeHeadlineForm']//button[contains(text(), 'Save')]")
           save_button.click()
           print(f"Profile summary updated successfully! for user {username}")
        except Exception as e:
            print("Error while updating resume headline")
            print(e.with_traceback())


# update_naukri_profile("nagellapranayraj@gmail.com","Dhanush$$14")
# update_naukri_profile("monikalakshmi2000@gmail.com","Pranay$12")
update_naukri_profile("nagelladhanush@gmail.com","Dhanush$$14")