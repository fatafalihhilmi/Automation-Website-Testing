# Automation Website Testing — Indonesia Indicator

Pengujian otomatis untuk https://indonesiaindicator.com/home menggunakan Python, Selenium, dan Pytest. Fokus utama: navigasi menu, artikel berita, tautan media sosial, filter berita, dan pengecekan fitur search (ditemukan bug redirect ke /news).

## Persiapan Cepat
- Butuh Python 3.x dan Google Chrome terpasang.
- Instal dependensi:
  ```
  pip install -r requirements.txt
  ```

## Cara Menjalankan
- Semua test:
  ```
  pytest tests/
  ```
- Test tertentu (contoh menu):
  ```
  pytest tests/test_menu.py -v
  ```
- Skrip ringkas:
  ```
  python run_tests.py
  ```

## Apa Saja yang Diuji
- `tests/test_menu.py`: menu "Who We Are" (mobile/desktop) membuka halaman tujuan, dan halaman tujuan memiliki judul yang tampil.
- `tests/test_news.py`: membuka halaman `/news`, mengklik salah satu berita, dan memastikan halaman detail menampilkan judul/konten berita.
- `tests/test_social.py`: tautan Instagram, X, dan LinkedIn membuka tab baru dan mengarah ke URL domain yang benar.
- `tests/test_search.py`: ikon search di header diklik tetapi tidak memicu aksi apa pun (test ini diberi `xfail` karena fitur search belum berfungsi di situs).


## Catatan Praktis
- Fixture dan utilitas driver ada di `tests/conftest.py` (termasuk `driver`, `take_screenshot`, dan `switch_to_new_tab`).
- Screenshot disimpan di folder `screenshots/` saat test berjalan (misalnya `menu_who_we_are.png`, `online_news_article.png`, `social_media_instagram.png`, `search_button_no_action.png`).
- Beberapa klik memakai JavaScript (`execute_script`) untuk elemen yang sulit diklik langsung (misalnya link berita dan ikon media sosial).

