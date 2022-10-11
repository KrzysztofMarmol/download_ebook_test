import pytest
from selenium import webdriver
from src.download_ebook import download_ebook, chrome_options
import os.path


# folder w projekcie
@pytest.fixture()
def file_directories():
    dir = os.path.dirname(os.getcwd()) + "/tmp"
    yield dir
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))


@pytest.fixture()
def website():
    return "https://www.salesmanago.com/info/recession-survival.htm"


@pytest.fixture()
def options(file_directories):
    options = chrome_options(webdriver.ChromeOptions(), file_directories)
    return options


@pytest.fixture()
def driver(website, options):
    driver = webdriver.Chrome(options=options)
    driver.get(website)
    yield driver
    driver.close()


def test_download_ebook(driver, file_directories):
    filename = download_ebook(driver)
    print(filename)
    assert os.path.isfile(f"{file_directories}/{filename}")
