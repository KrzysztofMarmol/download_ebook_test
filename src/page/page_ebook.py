from selenium.webdriver.common.by import By
# from src.extract_element_from_url import extract_filename


class PageEbook:

    def __init__(self, driver):
        self.driver = driver

    def click_ebook(self, href: str) -> None:
        """ Clicks the ebook containing the link

        Args:
            href (str): Ebook's link.

        """
        self.driver.find_element(By.XPATH, f"//a[@href='{href}']").click()

    def find_all_ebooks(self) -> list:
        """ Find existing ebooks

            Return:
                hrefs (list): Ebook link list

        """
        elements = self.driver.find_elements(By.XPATH, "//*[@class='col-lg-3 ebook__text']//a[@href]")
        hrefs = []
        for element in elements:
            hrefs.append(element.get_attribute('href'))

        return hrefs
