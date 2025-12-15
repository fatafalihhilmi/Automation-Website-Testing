import time
from selenium.webdriver.common.by import By
from conftest import BASE_URL, take_screenshot, switch_to_new_tab

def js_click(driver, element):
    # Helper: klik elemen dengan JavaScript
    driver.execute_script("arguments[0].click();", element)

def test_social_media_instagram(driver):
    # 1. Buka halaman home
    driver.get(BASE_URL)

    # 2. Klik ikon Instagram
    instagram_icon = driver.find_element(
        By.CSS_SELECTOR,
        'a[href="https://www.instagram.com/indonesia.indicator/"]'
    )
    original_window = driver.current_window_handle
    js_click(driver, instagram_icon)
    time.sleep(3)

    # 3. Pindah ke tab baru dan verifikasi domain
    original = switch_to_new_tab(driver)
    current_url = driver.current_url.lower()
    assert "instagram.com" in current_url, "URL social media bukan Instagram"
    take_screenshot(driver, "social_media_instagram")

    # 4. Tutup tab sosmed dan kembali ke tab awal
    driver.close()
    driver.switch_to.window(original_window or original)

def test_social_media_x(driver):
    driver.get(BASE_URL)

    x_icon = driver.find_element(
        By.CSS_SELECTOR,
        'a[href="https://x.com/id_indicator"]'
    )
    original_window = driver.current_window_handle
    js_click(driver, x_icon)
    time.sleep(3)

    original = switch_to_new_tab(driver)
    current_url = driver.current_url.lower()
    assert "x.com" in current_url or "twitter.com" in current_url, \
        "URL social media bukan X/Twitter"
    take_screenshot(driver, "social_media_x")

    driver.close()
    driver.switch_to.window(original_window or original)

def test_social_media_linkedin(driver):
    driver.get(BASE_URL)

    linkedin_icon = driver.find_element(
        By.CSS_SELECTOR,
        'a[href="https://www.linkedin.com/company/indonesia-indicator/"]'
    )
    original_window = driver.current_window_handle
    js_click(driver, linkedin_icon)
    time.sleep(3)

    original = switch_to_new_tab(driver)
    current_url = driver.current_url.lower()
    assert "linkedin.com" in current_url, "URL social media bukan LinkedIn"
    take_screenshot(driver, "social_media_linkedin")

    driver.close()
    driver.switch_to.window(original_window or original)
