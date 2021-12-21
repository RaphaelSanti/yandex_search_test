from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from PIL import Image
from PIL import ImageChops
import urllib.request


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def check_text_by_name(self):
        "Проверка наличия поля поиска"
        try:
            self.driver.find_element(By.NAME, "text")
        except NoSuchElementException:
            return False
        return True

    def enter_search_text(self, input_text):
        "Ввод текста в поле поиска"
        return self.driver.find_element(By.XPATH, '//input[@id="text"]').send_keys(input_text)

    def press_return_key_search_field(self):
        "Ввод ENTER в поле поиска"
        return self.driver.find_element(By.XPATH, '//input[@id="text"]').send_keys(Keys.ENTER)



    def check_listbox_by_expected_conditions(self):
        "Проверка наличия ListBox с результатами поиска"
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, '//ul[@role="listbox"]//li[@role="option"]')))
        except NoSuchElementException:
            return False
        return True

    def get_first_5_links(self):
        "Получает первый 5(6) ссылок из резульата поиска"
        items = self.driver.find_elements(By.CSS_SELECTOR, "li[data-cid] a[class*='Link'][href][role='text'")
        links = [item.get_attribute('href') for item in items[:6]]  # Первая ссылка - реклама, хз пропускать ли
        return links


class PicturePage:

    def __init__(self, driver):
        self.driver = driver

    def check_yandex_picture_link_by_css_selector(self):
        "Проверка ссылки на Яндекс картинки"
        try:
            self.driver.find_element(By.CSS_SELECTOR, "nav[class*='services'] a[href][data-id='images'")
        except NoSuchElementException:
            return False
        return True

    def get_link_from_pictur_button(self):
        "Получает сслыку из кнопки яндекс картинок"
        link = self.driver.find_element(By.CSS_SELECTOR, "nav[class*='services'] a[href][data-id='images'").get_attribute('href')
        return link

    def click_on_yeandex_pictures(self):
        "Кликает на яндекс картинки"
        return self.driver.find_element(By.CSS_SELECTOR, "nav[class*='services'] a[href][data-id='images'").click()

    def switch_window(self):
        "Переключает на второе окно"
        return self.driver.switch_to.window(self.driver.window_handles[1])

    def get_first_category_text(self):
        "Получает название первой категории"
        return self.driver.find_element(By.CSS_SELECTOR, "div[class='PopularRequestList-SearchText'").get_attribute('innerHTML')

    def get_first_category_href(self):
        "Получает ссылку на первую категорию"
        return self.driver.find_element(By.CSS_SELECTOR, "div[class='PopularRequestList'] div[class*='PopularRequestList-Item'] a[href]").get_attribute('href')

    def get_current_url(self):
        "Получает текущий адрес"
        return self.driver.current_url

    def click_on_first_category(self):
        "Клик на первую категорию"
        return self.driver.find_element(By.CSS_SELECTOR, "div[class*='PopularRequestList-Item']>a[href][class='Link PopularRequestList-Preview']").click()

    def get_picture_search_box_text(self):
        "Получает текст в строке поиска"
        return self.driver.find_element(By.CSS_SELECTOR, "input[class*='input__control'][value]").get_attribute('value')

    def get_screenshot(self, screen_name):
        "Делает скриншот"
        self.driver.save_screenshot(screen_name)
        screenshot = Image.open(screen_name).convert('RGB')
        return screenshot

    def click_on_first_preview(self):
        "Клик на первую картинку в категории"
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[class='serp-item__link']"))).click()

    def check_equal_pics(self, a, b):
        "Определяет одинаковые ли картинки"
        a.load()
        b.load()
        matches = ImageChops.difference(a, b).getbbox()
        if matches is None:
            return True
        else:
            return False

    def save_pic(self, pic_name):
        "Получает картинку по URL"
        img_url_full = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "img[class='MMImage-Origin'][src]"))).get_attribute('src')
        urllib.request.urlretrieve(img_url_full, pic_name)
        img = Image.open(pic_name).convert('RGB')
        return img

    def click_next_button(self):
        "Кликает на кнопку вперед"
        return WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[class*='CircleButton_type_next']"))).click()

    def click_prev_button(self):
        "Кликает на кнопку назад"
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class*='CircleButton_type_prev']"))).click()

    def wait_for_url_update_from_Homepage(self, homepage):
        WebDriverWait(self.driver, 30).until(EC.url_to_be(homepage))