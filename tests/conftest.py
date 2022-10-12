import pytest
from src.driver import chrome_driver
import os.path
from pathlib import Path
from tests.ebooks_list import ebooks_list_from_file


@pytest.fixture()
def ebooks_list():
    return ebooks_list_from_file()


@pytest.fixture()
def temporary_path():
    dir = os.path.dirname(os.getcwd()) + "/tmp"
    yield dir
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))


@pytest.fixture()
def website():
    return "https://www.salesmanago.com/info/knowledgecenter.htm"


@pytest.fixture()
def driver(temporary_path, website):
    driver = chrome_driver(temporary_path)
    driver.get(website)
    yield driver
    driver.quit()
