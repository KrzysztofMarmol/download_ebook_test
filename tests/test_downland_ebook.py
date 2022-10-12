import pytest
from selenium import webdriver
from src.download_ebook import download_ebook, chrome_options
import os.path
from pathlib import Path
from src.page.page_ebook import PageEbook


# folder w projekcie
@pytest.fixture()
def file_directories():
    dir = os.path.dirname(os.getcwd()) + "/tmp"
    yield dir
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))


@pytest.fixture()
def website():
    return "https://www.salesmanago.com/info/knowledgecenter.htm"


@pytest.fixture()
def options(file_directories):
    options = chrome_options(webdriver.ChromeOptions(), file_directories)
    return options


@pytest.fixture()
def driver(website, options):
    driver = webdriver.Chrome(options=options)
    driver.get(website)
    yield driver
    driver.quit()


@pytest.fixture()
def ebooks_list():
    path = Path(__file__).parent / "Ebook_list.txt"
    f = open(path, 'r')
    list_ebooks = [line.rstrip() for line in f.readlines()]
    f.close()
    return list_ebooks


def test_all_ebooks_exist(driver, ebooks_list):
    check_list = PageEbook(driver).find_all_ebooks()
    for ebook in ebooks_list:
        assert ebook in check_list


def test_download_ebook(driver, file_directories):
    filename = download_ebook(driver, "https://www.salesmanago.com/info/recession-survival.htm")
    assert os.path.isfile(f"{file_directories}/{filename}")
