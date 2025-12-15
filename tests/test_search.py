import pytest
from selenium.webdriver.common.by import By
from conftest import BASE_URL, take_screenshot


@pytest.mark.xfail(reason="Search button does not trigger any search action")
def test_search_button_does_nothing(driver):
    # 1. Buka halaman home
    driver.get(BASE_URL)

    # 2. Temukan ikon search dan klik
    search_button = driver.find_element(
        By.CSS_SELECTOR,
        'button.btn.me-3.bg-transparent'
    )
    before_url = driver.current_url
    search_button.click()
    after_url = driver.current_url

    # 3. Simpan screenshot sebagai bukti
    take_screenshot(driver, "search_button_no_action")

    # 4. Ekspektasi: seharusnya URL berubah / ada aksi search
    assert after_url != before_url, "Search button tidak melakukan aksi apa pun"
