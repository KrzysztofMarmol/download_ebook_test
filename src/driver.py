from selenium import webdriver


def create_chrome_driver(path=None):
    """ Creates a webdriver with experimental_option

    Args:
        path(str): Driver's download directory

    Return:
        webdriver.Chrome()
    """

    chrome_options = {
        "download.prompt_for_download": False,  # To auto download the file
        "download.directory_upgrade": True,
        "plugins.always_open_pdf_externally": True,  # It will not show PDF in chrome
        "profile.default_content_setting_values.cookies": 2
    }

    if path is not None:
        chrome_options["download.default_directory"] = path
        # Changed default directory for download

    options = webdriver.ChromeOptions()
    options.add_experimental_option('prefs', chrome_options)
    return webdriver.Chrome(options=options)
