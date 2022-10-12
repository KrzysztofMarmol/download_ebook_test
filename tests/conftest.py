import pytest
from selenium import webdriver
from src.download_ebook import download_ebook, chrome_options
import os.path
from pathlib import Path


@pytest.fixture()
def ebooks_list():
    path = Path(__file__).parent / "Ebook_list.txt"
    f = open(path, 'r')
    list_ebooks = [line.rstrip() for line in f.readlines()]
    f.close()
    return list_ebooks


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
def driver(website, options):
    driver = webdriver.Chrome(options=options)
    driver.get(website)
    yield driver
    driver.quit()


@pytest.fixture()
def options(file_directories):
    options = chrome_options(webdriver.ChromeOptions(), file_directories)
    return options