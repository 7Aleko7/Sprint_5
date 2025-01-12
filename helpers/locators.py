from selenium.webdriver.common.by import By

class Locators:
    # Кнопка "Войти в аккаунт"
    login_to_account=(By.XPATH, ".//button[text()='Войти в аккаунт']")

    # Заголовок страницы авторизации "Вход"
    entry_header= (By.XPATH, ".//h2[text()='Вход']")

    # Кнопка "Зарегистрироваться" на странице авторизации
    button_register_on_auth= (By.XPATH, ".//a[text()='Зарегистрироваться']")

    # Кнопка "Зарегистрироваться" на странице регистрации
    button_register= (By.XPATH, ".//button[text()='Зарегистрироваться']")

    # Заголовок страницы регистрации "Регистрация"
    register_header= (By.XPATH, ".//h2[text()='Регистрация']")

    # Инпут "Имя"
    input_name=(By.XPATH, ".//label[text()='Имя']/parent::div/input")

    # Инпут "Email"
    input_mail= (By.XPATH, ".//label[text()='Email']/parent::div/input")

    # Инпут "Пароль"
    input_password= (By.XPATH, ".//label[text()='Пароль']/parent::div/input")

    # ClassName ошибки инпута
    input_error=(By.CLASS_NAME, "input__error")

    # Кнопка "Личный кабинет"
    personal_account= (By.XPATH, ".//p[text()='Личный Кабинет']")

    # Кнопка "Войти" на странице регистрации и восстановления пароля
    button_login= (By.XPATH, ".//a[text()='Войти']")

    # Кнопка "Войти" на странице авторизации
    login=(By.XPATH, ".//button[text()='Войти']")

    # Кнопка "Оформить заказ"
    place_an_order= (By.XPATH, ".//button[text()='Оформить заказ']")

    # Заголовок "Соберите бургер"
    assemble_the_burger= (By.XPATH, ".//h1[text()='Соберите бургер']")

    # Кнопка "Профиль" в ЛК
    profile = (By.XPATH, ".//a[text()='Профиль']")

    # Кнопка "Выход" в ЛК
    logout = (By.XPATH, ".//button[text()='Выход']")

    # Кнопка "Конструктор"
    constructor = (By.XPATH, ".//p[text()='Конструктор']")

    # ClassName логотипа Stellar Burgers
    logo= (By.CLASS_NAME, 'AppHeader_header__logo__2D0X2')

    # Таб "Булки"
    tab_bread = (By.XPATH, ".//span[text()='Булки']")

    # Таб "Соусы"
    tab_sauces = (By.XPATH, ".//span[text()='Соусы']")

    # Таб "Начинки"
    tab_toppings = (By.XPATH, ".//span[text()='Начинки']")

    # Родительский элемент таба "Булки"
    parent_tab_bread = (By.XPATH, ".//span[text()='Булки']/parent::div")

    # Родительский элемент таба "Соусы"
    parent_tab_sauces = (By.XPATH, ".//span[text()='Соусы']/parent::div")

    # Родительский элемент таба "Начинки"
    parent_tab_toppings = (By.XPATH, ".//span[text()='Начинки']/parent::div")