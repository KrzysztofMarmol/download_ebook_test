from selenium.webdriver.common.by import By
from src.page.page import Page


class PageEbook(Page):
    PAGE_URL = "https://www.salesmanago.com/info/knowledgecenter.htm"

    def open_website(self):
        self.driver.get(self.PAGE_URL)

    def click_ebook(self, href: str) -> None:
        """ Clicks the ebook containing the link

        Args:
            href (str): Ebook's link.

        """
        self.driver.find_element(By.XPATH, f"//a[@href='{href}']").click()

    def find_all_ebooks(self) -> list:
        """ Find existing ebooks

            Return:
                (list): Ebooks link list

        """
        elements = self.driver.find_elements(By.XPATH, "//*[@class='col-lg-3 ebook__text']//a[@href]")
        return [element.get_attribute('href') for element in elements]
