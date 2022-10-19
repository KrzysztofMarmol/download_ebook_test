import os.path
import pytest
from src.page.page_ebook_download import PageDownloadEbook
from src.page.page_ebook import PageEbook
from time import sleep
from pathlib import Path


def ebooks_list_from_file():
    path = Path(__file__).parent / "Ebook_list.txt"
    with open(path, 'r') as file:
        return [line.rstrip() for line in file.readlines()]


def test_all_ebooks_exist(driver):
    website = PageEbook(driver)
    website.open_website()
    check_list = website.find_all_ebooks()
    for ebook in ebooks_list_from_file():
        assert ebook in check_list


@pytest.mark.parametrize("test_input", ebooks_list_from_file())
def test_download_ebook(driver, temporary_path, test_input):
    website_ebook = PageEbook(driver)
    website_ebook_download = PageDownloadEbook(driver)
    website_ebook.open_website()
    website_ebook.click_ebook(test_input)
    driver.switch_to.window(driver.window_handles[1])
    website_ebook_download.enter_name("Jan Kowalski")
    website_ebook_download.enter_email("jkowalski.benhauer+testrekrutacja@salesmanago.com")
    website_ebook_download.enter_website("xyz.pl")
    website_ebook_download.enter_company("xyz")
    website_ebook_download.enter_phone("123456780")
    website_ebook_download.click_button_get_for_free()
    sleep(2)
    website_ebook_download.hide_chatbot()
    filename = website_ebook_download.click_button_download_here()
    sleep(6)
    assert os.path.isfile(f"{temporary_path}/{filename}")
