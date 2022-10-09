from selenium.webdriver.common.by import By
from time import sleep


class PageDownloadEbook:

    def __init__(self, driver):
        self.driver = driver
        self._ebook_filename = None

    @property
    def ebook_filename(self):
        return self._ebook_filename

    def enter_name(self, name: str) -> None:
        """ Enters name and surname in the "Name and Surname" label

        Args:
            name (str): Username and surname as one string.

        """
        try:
            self.driver.find_element(By.XPATH, '//*[@id="uspForm"]/div[1]/div[1]/div/input').send_keys(name)
        except Exception:
            raise

    def enter_email(self, email: str) -> None:
        """ Enters email in the "Business email" label

        Args:
            email (str): User email.

        """
        try:
            self.driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(email)
        except Exception:
            raise

    def enter_company(self, company: str) -> None:
        """ Enters company name in the "Company" label

        Args:
            company (str): Name of the user's company.

        """
        try:
            self.driver.find_element(By.XPATH, '//*[@id="company"]/div/input').send_keys(company)
        except Exception:
            raise

    def enter_website(self, website: str) -> None:
        """ Enters website url in the "Website URL" label

        Args:
            website(str): User's website address.

        """
        try:
            self.driver.find_element(By.XPATH, '//*[@id="uspForm"]/div[1]/div[5]/div/input').send_keys(website)
        except Exception:
            raise

    def enter_phone(self, phone: str) -> None:
        """ Enters phone number in the "Phone number" label

        Args:
            phone(str): User's telephone number.

        """
        try:
            self.driver.find_element(By.XPATH, '//*[@id="phoneNumber"]').send_keys(phone)
        except Exception:
            raise

    def click_button_download(self) -> None:
        """ Clicks the download button

        """
        try:
            self.driver.find_element(By.XPATH, '//*[@id="uspForm"]/div[2]/div/button').click()
        except Exception:
            raise

    def click_button_download_here(self) -> None:
        """ Clicks the download here button

        """
        try:
            element = self.driver.find_element(By.XPATH, '/html/body/main/div[2]/div/div[2]/div[2]/div/div/a[1]')

            self.driver.implicitly_wait(5)
            self._ebook_filename = self.extract_filename(element.get_attribute('href'))  # set ebook filename

            # element it is hide under chatbot, selenium can not click on it
            self.driver.execute_script("arguments[0].click();", element)

        except Exception:
            raise

    @staticmethod
    def sleep_some_time(sec):
        sleep(sec)

    @staticmethod
    def extract_filename(link: str) -> str:
        name = link.split('/')[-1]
        return name
