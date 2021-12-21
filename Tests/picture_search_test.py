from selenium import webdriver
import unittest
from PageObjects.page import HomePage
from PageObjects.page import PicturePage



class YandexPictureSearch(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(30)
        cls.test_url = 'https://yandex.ru/'
        cls.test_url_picture = 'https://yandex.ru/images/'

    def test_Yandex_search(self):
        driver = self.driver
        driver.get(self.test_url)
        picturepage = PicturePage(driver)

        self.assertTrue(picturepage.check_yandex_picture_link_by_css_selector(), 'Ссылка на "Картинки" не найдена')
        picturepage.click_on_yeandex_pictures()
        picturepage.switch_window()
        self.assertIn(self.test_url_picture, picturepage.get_current_url(), str("Ссылка ведет не на " + self.test_url_picture + "!"))
        picturepage.click_on_first_category()
        self.assertEqual(picturepage.get_first_category_href(), picturepage.get_current_url(), "Ссылка ведёт не туда")
        self.assertEqual(picturepage.get_first_category_text(), picturepage.get_picture_search_box_text(), "Название категории и поле поиска отличаются")
        scr_1 = picturepage.get_screenshot('screen1.png')

        picturepage.click_on_first_preview()
        scr_2 = picturepage.get_screenshot('screen2.png')
        self.assertFalse(picturepage.check_equal_pics(scr_1, scr_2), "Скриншоты одинаковые, картинка не открылась")
        image_1 = picturepage.save_pic("Image_1.png")
        picturepage.click_next_button()
        image_2 = picturepage.save_pic("Image_2.png")
        picturepage.click_prev_button()
        self.assertFalse(picturepage.check_equal_pics(image_1, image_2), "Картинки одинаковые, кнопка не сработала")
        image_3 = picturepage.save_pic("Image_3.png")
        self.assertTrue(picturepage.check_equal_pics(image_1, image_3), "Предыдущая картинка была другой")

    @classmethod
    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()