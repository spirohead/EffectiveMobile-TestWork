import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class SauceTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('https://saucedemo.com')

    def test_purchase(self):
        driver = self.driver

        # Авторизация
        driver.find_element('id', 'user-name').send_keys('standard_user')
        driver.find_element('id', 'password').send_keys('secret_sauce')
        driver.find_element('id', 'login-button').click()

        # Выбор товара
        driver.find_element('xpath', '//div[text()=\'Sauce Labs Backpack\']'
                                     '/ancestor::div[@class=\'inventory_item\']//button').click()

        # Переход в корзину
        driver.find_element('class name', 'shopping_cart_link').click()

        # Проверка, что товар добавлен в корзину
        cart_item = driver.find_element('class name', 'cart_item')
        self.assertIn('Sauce Labs Backpack', cart_item.text)

        # Оформление покупки
        driver.find_element('id', 'checkout').click()

        # Заполнение полей
        driver.find_element('id', 'first-name').send_keys('John')
        driver.find_element('id', 'last-name').send_keys('Doe')
        driver.find_element('id', 'postal-code').send_keys('12345')

        driver.find_element('id', 'continue').click()

        # Завершение покупки
        driver.find_element('id', 'finish').click()

        # Проверка успешного завершения покупки
        message = driver.find_element('class name', 'complete-header')
        self.assertEqual(message.text, 'Thank you for your order!')

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
