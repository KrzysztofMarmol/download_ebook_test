import pytest
from src.driver import create_chrome_driver
import os.path


@pytest.fixture()
def temporary_path():
    dir = os.path.dirname(os.getcwd()) + "/tmp"
    yield dir
    for f in os.listdir(dir):
        #os.remove(os.path.join(dir, f))
        pass

@pytest.fixture()
def driver(temporary_path):
    driver = create_chrome_driver(temporary_path)
    yield driver
    driver.quit()
