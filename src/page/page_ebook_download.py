from selenium.webdriver.common.by import By
from src.extract_element_from_url import extract_filename
from urllib.parse import unquote
from selenium.common.exceptions import NoSuchElementException
from src.page.page import Page


class PageDownloadEbook(Page):
    def enter_name(self, name: str) -> None:
        """ Enters name and surname in the "Name and Surname" label

        Args:
            name (str): Username and surname as one string.

        """
        self.driver.find_element(By.XPATH, '//*[@id="uspForm"]//input[@name="name"]').send_keys(name)

    def enter_email(self, email: str) -> None:
        """ Enters email in the "Business email" label

        Args:
            email (str): User email.

        """
        self.driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(email)

    def enter_company(self, company: str) -> None:
        """ Enters company name in the "Company" label

        Args:
            company (str): Name of the user's company.

        """
        try:
            element = self.driver.find_element(By.XPATH, '//*[@id="company"]//input')
        except NoSuchElementException:
            element = self.driver.find_element(By.XPATH, '//*[@id="company"]')

        element.send_keys(company)

    def enter_website(self, website: str) -> None:
        """ Enters website url in the "Website URL" label

        Args:
            website(str): User's website address.

        """
        self.driver.find_element(By.XPATH, '//*[@id="uspForm"]//input[@name="url"]').send_keys(website)

    def enter_phone(self, phone: str) -> None:
        """ Enters phone number in the "Phone number" label

        Args:
            phone(str): User's telephone number.

        """
        self.driver.find_element(By.XPATH, '//*[@id="phoneNumber"]').send_keys(phone)

    def click_button_get_for_free(self) -> None:
        """ Clicks the download button

        """
        self.driver.find_element(By.XPATH, '//*[@id="uspForm"]//button').click()

    def click_button_download_here(self) -> str:
        """ Clicks the download here button

        Return:
            filename(str): Download filename
        """
        try:
            element = self.driver.find_element(By.XPATH, '//*[@class="thanks-message"]//a[1]')
        except NoSuchElementException:
            element = self.driver.find_element(By.XPATH, '//*[@class="ebookcontainer__img--buttoncontainer"]//a[@href]')

        self.driver.execute_script("arguments[0].scrollIntoViewIfNeeded(true);", element)
        element.click()
        return unquote(extract_filename(element.get_attribute('href')))

    def hide_chatbot(self) -> None:
        element = self.driver.find_element(By.XPATH, '//*[@id="hubspot-messages-iframe-container"]')
        self.driver.execute_script("arguments[0].style.visibility='collapse';", element)
