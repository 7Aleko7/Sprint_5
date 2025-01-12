from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from helpers.locators import Locators
from helpers.data import Data

class TestPageNavigation:
    def test_going_to_personal_account(self, driver, open_main_page):
        #  Нажимаем "Войти в аккаунт" и ждем чтобы прогрузилась страница авторизации(заголовок "Вход")
        driver.find_element(*Locators.login_to_account).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.entry_header))

        # Вводим почту и пароль зарегистрированного пользователя
        driver.find_element(*Locators.input_mail).send_keys(Data.test_user_mail)
        driver.find_element(*Locators.input_password).send_keys(Data.test_user_password)

        # Нажимаем кнопку "Войти" и ждем чтобы прогрузилась главная станица(заголовок "Соберите бургер")
        driver.find_element(*Locators.login).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.assemble_the_burger))

        # Нажимаем кнопку "Личный кабинет" и ожидаем чтобы прогрузилась страница ЛК(кнопка "Профиль")
        driver.find_element(*Locators.personal_account).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.profile))

        # Проверяем что произошел переход в ЛК
        current_url = driver.current_url
        assert current_url =='https://stellarburgers.nomoreparties.site/account/profile'

    def test_going_from_personal_account_to_constructor_by_button_constructor(self, driver, open_main_page):
        #  Нажимаем "Войти в аккаунт" и ждем чтобы прогрузилась страница авторизации(заголовок "Вход")
        driver.find_element(*Locators.login_to_account).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.entry_header))

        # Вводим почту и пароль зарегистрированного пользователя
        driver.find_element(*Locators.input_mail).send_keys(Data.test_user_mail)
        driver.find_element(*Locators.input_password).send_keys(Data.test_user_password)

        # Нажимаем кнопку "Войти" и ждем чтобы прогрузилась главная станица(заголовок "Соберите бургер")
        driver.find_element(*Locators.login).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.assemble_the_burger))

        # Нажимаем кнопку "Личный кабинет" и ожидаем чтобы прогрузилась страница ЛК(кнопка "Профиль")
        driver.find_element(*Locators.personal_account).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.profile))

        # Нажимаем кнопку "Конструктор" и ждем чтобы прогрузилась главная станица(заголовок "Соберите бургер")
        driver.find_element(*Locators.constructor).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.assemble_the_burger))


        # Проверяем что произошел переход к главной странице
        current_url = driver.current_url
        assert current_url =='https://stellarburgers.nomoreparties.site/'

    def test_going_from_personal_account_to_constructor_by_click_on_logo(self, driver, open_main_page):
        #  Нажимаем "Войти в аккаунт" и ждем чтобы прогрузилась страница авторизации(заголовок "Вход")
        driver.find_element(*Locators.login_to_account).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.entry_header))

        # Вводим почту и пароль зарегистрированного пользователя
        driver.find_element(*Locators.input_mail).send_keys(Data.test_user_mail)
        driver.find_element(*Locators.input_password).send_keys(Data.test_user_password)

        # Нажимаем кнопку "Войти" и ждем чтобы прогрузилась главная станица(заголовок "Соберите бургер")
        driver.find_element(*Locators.login).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.assemble_the_burger))

        # Нажимаем кнопку "Личный кабинет" и ожидаем чтобы прогрузилась страница ЛК(кнопка "Профиль")
        driver.find_element(*Locators.personal_account).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.profile))

        # Нажимаем кнопку "Конструктор" и ждем чтобы прогрузилась главная станица(заголовок "Соберите бургер")
        driver.find_element(*Locators.logo).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.assemble_the_burger))


        # Проверяем что произошел переход к главной странице
        current_url = driver.current_url
        assert current_url =='https://stellarburgers.nomoreparties.site/'

    def test_when_opening_main_page_selected_tab_bread(self, driver, open_main_page):
        element = driver.find_element(*Locators.parent_tab_bread)

        # Проверяем что выбран таб "Булки"
        assert 'tab_tab_type_current' in element.get_attribute('class')


    def test_going_to_the_tab_sauces(self, driver, open_main_page):
        #  Нажимаем на таб "Соусы"
        driver.find_element(*Locators.tab_sauces).click()

        element = driver.find_element(*Locators.parent_tab_sauces)

        # Проверяем что выбран таб "Соусы"
        assert 'tab_tab_type_current' in element.get_attribute('class')

    def test_going_to_the_tab_toppings(self, driver, open_main_page):
        #  Нажимаем на таб "Начинки"
        driver.find_element(*Locators.tab_toppings).click()

        element = driver.find_element(*Locators.parent_tab_toppings)

        # Проверяем что выбран таб "Начинки"
        assert 'tab_tab_type_current' in element.get_attribute('class')

    def test_going_to_the_tab_bread_after_going_another_teb(self, driver, open_main_page):
        #  Нажимаем на таб "Начинки"
        driver.find_element(*Locators.tab_toppings).click()

        #  Нажимаем на таб "Булки"
        driver.find_element(*Locators.tab_bread).click()

        element = driver.find_element(*Locators.parent_tab_bread)

        # Проверяем что выбран таб "Булки"
        assert 'tab_tab_type_current' in element.get_attribute('class')




