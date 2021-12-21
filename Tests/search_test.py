from selenium import webdriver
import unittest
from PageObjects.page import HomePage



class YandexSearch(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(30)
        cls.test_url = 'https://yandex.ru/'
        cls.test_url_for_check = 'https://tensor.ru/'
        cls.search_text = 'Тензор'

    def test_Yandex_search(self):
        driver = self.driver
        driver.get(self.test_url)
        homepage = HomePage(driver)
        self.assertTrue(homepage.check_text_by_name(), 'Поле поиска не найдено')
        homepage.enter_search_text(self.search_text)
        self.assertTrue(homepage.check_listbox_by_expected_conditions(), "Результатов(Suggest) не видно")
        homepage.press_return_key_search_field()
        self.assertIn(self.test_url_for_check, homepage.get_first_5_links(), str(self.test_url_for_check+" нет в поисковой выдаче"))

    @classmethod
    def tearDown(cls):
        cls.driver.close()


if __name__ == "__main__":
    unittest.main()
