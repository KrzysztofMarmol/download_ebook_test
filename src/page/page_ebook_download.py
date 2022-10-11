from selenium.webdriver.common.by import By
from src.extract_element_from_url import extract_filename
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains


class PageDownloadEbook:

    def __init__(self, driver):
        self.driver = driver

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
        self.driver.find_element(By.XPATH, '//*[@id="company"]//input').send_keys(company)

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
        element = self.driver.find_element(By.XPATH, '//*[@id="thanks-message"]//a[1]')
        self.driver.execute_script("arguments[0].scrollIntoViewIfNeeded(true);", element)
        element.click()

        return extract_filename(element.get_attribute('href'))

    def hide_chatbot(self) -> None:
        element = self.driver.find_element(By.XPATH, '//*[@id="hubspot-messages-iframe-container"]')
        self.driver.execute_script("arguments[0].style.visibility='collapse';", element)
