import time
from selenium.webdriver.common.by import By
from conftest import BASE_URL, take_screenshot


def test_menu_to_news(driver):
    driver.set_window_size(980, 641)
    driver.get(BASE_URL)

    # Klik hamburger menu
    hamburger = driver.find_element(By.CSS_SELECTOR, 'button.nav-toggle[aria-label="Toggle navigation"]')
    driver.execute_script("arguments[0].click();", hamburger)
    time.sleep(1)

    # Klik item menu "Who-we-are" di mobile menu (berdasarkan atribut navigate)
    who_we_are_menu = driver.find_element(By.CSS_SELECTOR, 'a.nav-link[navigate="who-we-are"]')
    driver.execute_script("arguments[0].click();", who_we_are_menu)
    time.sleep(3)

    # Verifikasi: URL atau state berubah dari home
    assert driver.current_url != BASE_URL, "URL tidak berubah setelah klik menu Who We Are"

    headings = driver.find_elements(By.CSS_SELECTOR, "h1, h2")
    visible_titles = [h.text.strip() for h in headings if h.text.strip()]
    assert visible_titles, "Tidak menemukan judul di halaman tujuan menu Who We Are"
    
    take_screenshot(driver, "menu_news")
