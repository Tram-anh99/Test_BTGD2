import os
import time
import json
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

# Setup screenshot directory 
ARTIFACT_DIR = r"C:\Users\Admin\.gemini\antigravity-ide\brain\eb44a9f1-0ed0-4823-8286-0b39cb7feced"
SCREENSHOT_DIR = os.path.join(ARTIFACT_DIR, "screenshots")
if not os.path.exists(SCREENSHOT_DIR):
    os.makedirs(SCREENSHOT_DIR)

def save_screenshot(driver, name):
    path = os.path.join(SCREENSHOT_DIR, f"{name}.png")
    driver.save_screenshot(path)
    print(f"Captured screenshot: {path}")
    return path

def log_console(driver, step_name):
    try:
        logs = driver.get_log('browser')
        log_path = os.path.join(SCREENSHOT_DIR, f"{step_name}_console.json")
        with open(log_path, 'w', encoding='utf-8') as f:
            json.dump(logs, f, indent=4, ensure_ascii=False)
        print(f"Logged console for {step_name}: {len(logs)} logs saved.")
    except Exception as e:
        print(f"Failed to get console logs for {step_name}: {str(e)}")

def run_testing():
    options = Options()
    options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    # Enable console logs collection
    options.set_capability('goog:loggingPrefs', {'browser': 'ALL'})

    print("Initializing WebDriver...")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)

    try:
        # Step 1: Open Login Page
        print("Navigating to https://thuyloi.opengis.vn/map ...")
        driver.get("https://thuyloi.opengis.vn/map")
        time.sleep(5)
        
        # Log current URL and page source summary
        print(f"Current URL: {driver.current_url}")
        save_screenshot(driver, "01_login_page")
        
        # Dump page elements to identify inputs
        inputs = driver.find_elements(By.TAG_NAME, "input")
        print(f"Found {len(inputs)} input fields:")
        for idx, inp in enumerate(inputs):
            print(f"  Input {idx}: id='{inp.get_attribute('id')}', name='{inp.get_attribute('name')}', type='{inp.get_attribute('type')}', placeholder='{inp.get_attribute('placeholder')}', class='{inp.get_attribute('class')}'")

        # Step 2: Login
        # Try to find username and password by placeholder, id or name
        username_field = None
        password_field = None
        
        for inp in inputs:
            itype = inp.get_attribute('type')
            iname = inp.get_attribute('name') or ''
            iid = inp.get_attribute('id') or ''
            iplace = inp.get_attribute('placeholder') or ''
            
            if 'email' in itype or 'text' in itype or 'username' in iname or 'email' in iname or 'user' in iid or 'email' in iid or 'nhập' in iplace.lower() or 'tên' in iplace.lower():
                if not username_field and itype != 'password':
                    username_field = inp
            if 'password' in itype or 'pass' in iname or 'pass' in iid or 'mật khẩu' in iplace.lower():
                if not password_field:
                    password_field = inp

        if not username_field or not password_field:
            # Fallback to general input selection if needed
            print("Could not automatically identify username/password field, falling back to index...")
            if len(inputs) >= 2:
                username_field = inputs[0]
                password_field = inputs[1]

        if username_field and password_field:
            print(f"Using username field: id={username_field.get_attribute('id')}, name={username_field.get_attribute('name')}")
            print(f"Using password field: id={password_field.get_attribute('id')}, name={password_field.get_attribute('name')}")
            
            username_field.clear()
            username_field.send_keys("dtlong@vnsc.org.vn")
            password_field.clear()
            password_field.send_keys("dtlong")
            
            save_screenshot(driver, "02_login_credentials_filled")
            
            # Find submit button
            submit_btn = None
            buttons = driver.find_elements(By.TAG_NAME, "button")
            print(f"Found {len(buttons)} buttons:")
            for idx, btn in enumerate(buttons):
                btn_text = btn.text or btn.get_attribute('value') or ''
                btn_type = btn.get_attribute('type') or ''
                print(f"  Button {idx}: text='{btn_text}', type='{btn_type}', class='{btn_class := btn.get_attribute('class')}'")
                if 'submit' in btn_type or 'đăng nhập' in btn_text.lower() or 'login' in btn_text.lower() or 'enter' in btn_text.lower():
                    submit_btn = btn
            
            if not submit_btn:
                # Try finding input[type='submit'] or input[type='button']
                input_buttons = driver.find_elements(By.XPATH, "//input[@type='submit'] | //input[@type='button']")
                if input_buttons:
                    submit_btn = input_buttons[0]
            
            if not submit_btn and len(buttons) > 0:
                submit_btn = buttons[0] # fallback

            if submit_btn:
                print(f"Clicking submit button: text='{submit_btn.text}'")
                submit_btn.click()
            else:
                print("No submit button found! Submitting form via password field.")
                password_field.submit()
                
            time.sleep(8)
            print(f"Redirection URL: {driver.current_url}")
            save_screenshot(driver, "03_after_login_attempt")
            log_console(driver, "after_login")
        else:
            print("ERROR: Username or password fields not found.")
            save_screenshot(driver, "error_no_fields")
            return

        # Step 3: Explore and interact with the platform
        # Let's inspect the page menus/navigation to test further
        print("Exploring pages...")
        # Check for sidebar elements or navigation bar
        menu_items = driver.find_elements(By.XPATH, "//a | //button | //li[contains(@class, 'menu')]")
        print(f"Found {len(menu_items)} potential menu/link items.")
        
        # Let's see if we are logged in successfully.
        if "login" in driver.current_url.lower() or "sso" in driver.current_url.lower():
            print("WARNING: It seems login failed or redirecting back to login page.")
        else:
            print("SUCCESS: Login seems successful. Navigating different sections.")
            # Take screenshot of main map and check for console errors
            save_screenshot(driver, "04_dashboard_main_map")
            
            # Let's try to find specific tabs/navigation items to click.
            # We can find menu items with text like "Giám sát", "Bản đồ", "Quản lý", "Báo cáo", "Hệ thống"
            nav_keywords = ["Bản đồ", "Giám sát", "Báo cáo", "Quản lý", "Hệ thống", "Lịch sử", "Trạm", "Thiết bị", "Cảnh báo"]
            clicked_count = 0
            
            for keyword in nav_keywords:
                try:
                    # Find elements containing keyword
                    elements = driver.find_elements(By.XPATH, f"//*[contains(text(), '{keyword}')]")
                    for el in elements:
                        if el.is_displayed() and el.is_enabled():
                            tag = el.tag_name
                            text = el.text.strip()
                            if len(text) < 30 and tag in ['a', 'button', 'span', 'div', 'li']:
                                print(f"Clicking navigation item '{text}' ({tag})...")
                                # Click using Javascript to avoid click intercepted exceptions
                                driver.execute_script("arguments[0].click();", el)
                                time.sleep(5)
                                clicked_count += 1
                                save_screenshot(driver, f"05_nav_{clicked_count}_{keyword.lower()}")
                                log_console(driver, f"nav_{clicked_count}_{keyword.lower()}")
                                break # move to next keyword
                except Exception as ex:
                    print(f"Error navigating keyword {keyword}: {str(ex)}")
                    
            print(f"Navigation completed. Clicked {clicked_count} items.")

    except Exception as e:
        print(f"An error occurred during test execution: {str(e)}")
        save_screenshot(driver, "exception_error")
    finally:
        print("Closing browser...")
        driver.quit()

if __name__ == "__main__":
    run_testing()
