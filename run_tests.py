import pytest

if __name__ == "__main__":
    # Jalankan test yang stabil dulu
    pytest.main(["-v", "tests/test_news.py"])
    pytest.main(["-v", "tests/test_social.py"])
    pytest.main(["-v", "tests/test_search.py"])

    # Terakhir jalankan test_menu
    pytest.main(["-v", "tests/test_menu.py"])
