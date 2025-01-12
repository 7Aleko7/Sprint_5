from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from helpers.locators import Locators
from helpers.data import Data

class TestRegistration:

    def test_successful_registration(self, driver, open_main_page):
        mail=Data.random_email()
        password=Data.random_password()


        #  Нажимаем "Войти в аккаунт" и ждем чтобы прогрузилась страница авторизации(заголовок "Вход")
        driver.find_element(*Locators.login_to_account).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.entry_header))

        #  Нажимаем "Зарегистрироваться" и ждем чтобы прогрузилась страница регистрации(заголовок "Регистрация")
        driver.find_element(*Locators.button_register_on_auth).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.register_header))

        # Вводим имя, почту и пароль
        driver.find_element(*Locators.input_name).send_keys('Cаша')
        driver.find_element(*Locators.input_mail).send_keys(mail)
        driver.find_element(*Locators.input_password).send_keys(password)

        #Нажимаем "Зарегистрироваться" и ожидаем перехода на страницу авторизации
        driver.find_element(*Locators.button_register).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.entry_header))

        # Вводим почту и пароль только что зарегистрированного пользователя
        driver.find_element(*Locators.input_mail).send_keys(mail)
        driver.find_element(*Locators.input_password).send_keys(password)

        # Нажимаем кнопку "Войти" и ждем чтобы прогрузилась главная станица(заголовок "Соберите бургер")
        driver.find_element(*Locators.login).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.assemble_the_burger))

        # Проверяем что произошел вход(появилась кнопка "Оформить заказ")
        assert len(driver.find_elements(*Locators.place_an_order)) == 1

    def test_registration_with_invalid_password(self, driver, open_main_page):

        #  Нажимаем "Войти в аккаунт" и ждем чтобы прогрузилась страница авторизации(заголовок "Вход")
        driver.find_element(*Locators.login_to_account).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.entry_header))

        #  Нажимаем "Зарегистрироваться" и ждем чтобы прогрузилась страница регистрации(заголовок "Регистрация")
        driver.find_element(*Locators.button_register_on_auth).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.register_header))

        # Вводим имя, почту и пароль
        driver.find_element(*Locators.input_name).send_keys('Cаша')
        driver.find_element(*Locators.input_mail).send_keys(Data.random_email())
        driver.find_element(*Locators.input_password).send_keys('12345')

        #Нажимаем "Зарегистрироваться"
        driver.find_element(*Locators.button_register).click()

        # Проверяем что у инпута появилась нотификация об ошибке
        assert driver.find_element(*Locators.input_error).text == 'Некорректный пароль'




