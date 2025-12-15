import time
from selenium.webdriver.common.by import By
from conftest import BASE_URL, take_screenshot

def js_click(driver, element):
    driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});",
        element
    )
    driver.execute_script("arguments[0].click();", element)

def test_online_news_open_article(driver):
    # 1. Buka langsung halaman news
    driver.get("https://indonesiaindicator.com/news")

    # 2. Cari link berita di halaman /news
    news_links = driver.find_elements(By.CSS_SELECTOR, 'a[href*="news"]')
    assert news_links, "Tidak menemukan link berita di halaman /news"

    # 3. Klik link berita pertama
    first_news_link = news_links[0]
    js_click(driver, first_news_link)
    time.sleep(3)

    # 4. Verifikasi: ada judul/konten berita di halaman detail
    heading_candidates = driver.find_elements(By.CSS_SELECTOR, "h1, h2, h3")
    visible_titles = [h.text.strip() for h in heading_candidates if h.text.strip()]
    assert visible_titles, "Tidak menemukan judul/konten berita setelah link diklik"

    # 5. Screenshot bukti
    take_screenshot(driver, "online_news_article")
