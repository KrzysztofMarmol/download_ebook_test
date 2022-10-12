from src.download_ebook import download_ebook, chrome_options
import os.path
from src.page.page_ebook import PageEbook


def test_all_ebooks_exist(driver, ebooks_list):
    check_list = PageEbook(driver).find_all_ebooks()
    for ebook in ebooks_list:
        assert ebook in check_list


def test_download_ebook(driver, file_directories):
    filename = download_ebook(driver, "https://www.salesmanago.com/info/recession-survival.htm")
    assert os.path.isfile(f"{file_directories}/{filename}")
