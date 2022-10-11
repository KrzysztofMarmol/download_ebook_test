from src.page.page_ebook_download import PageDownloadEbook
from time import sleep


def download_ebook(driver) -> str:
    website = PageDownloadEbook(driver)
    website.enter_name("Jan Kowalski")
    website.enter_email("jkowalski.benhauer+testrektutacja@selesmanago.com")
    website.enter_website("xyz.pl")
    website.enter_company("xyz")
    website.enter_phone("123456780")
    sleep(1)
    website.click_button_get_for_free()
    sleep(2)
    filename = website.click_button_download_here()
    sleep(2)
    return filename


def chrome_options(options, path):
    options.add_experimental_option('prefs', {
        "download.default_directory": path,  # Changed default directory for download
        #"download.prompt_for_download": False,  # To auto download the file
        "download.directory_upgrade": True,
        #"plugins.always_open_pdf_externally": True,  # It will not show PDF in chrome
        "profile.default_content_setting_values.cookies": 2
    })
    return options
