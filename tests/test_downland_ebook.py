import os.path
import pytest
from tests.ebooks_list import ebooks_list_from_file
from src.page.page_ebook_download import PageDownloadEbook
from src.page.page_ebook import PageEbook
from time import sleep


def test_all_ebooks_exist(driver, ebooks_list):
    check_list = PageEbook(driver).find_all_ebooks()
    for ebook in ebooks_list:
        assert ebook in check_list


@pytest.mark.parametrize("test_input", ebooks_list_from_file())
def test_download_ebook(driver, temporary_path, test_input):
    website = PageDownloadEbook(driver)
    ebook = PageEbook(driver)
    ebook.click_ebook(test_input)
    driver.switch_to.window(driver.window_handles[1])
    website.enter_name("Jan Kowalski")
    website.enter_email("jkowalski.benhauer+testrektutacja@selesmanago.com")
    website.enter_website("xyz.pl")
    website.enter_company("xyz")
    website.enter_phone("123456780")
    website.click_button_get_for_free()
    sleep(2)
    website.hide_chatbot()
    filename = website.click_button_download_here()
    sleep(6)
    assert os.path.isfile(f"{temporary_path}/{filename}")
