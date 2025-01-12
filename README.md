# Sprint_5 - тестирование сервиса Stellar Burger
# В файле locators описаны все локаторы используемые в тестах
# В файле data созданы генераторы пароля и почты, а так же указаны авторизационные данные уже зарегистрированного пользователя
# В файле test_login_in_account созданы тесты на вход в аккаунт:
## В тесте test_login_in_account_by_button_sign_in_account проверяется вход через кнопку "Войти в личный кабинет"
## В тесте test_login_in_account_by_button_personal_account проверяется вход через кнопку "Личный кабинет"
## В тесте test__login_in_account_by_registration_form проверяется вход через форму регистрации
## В тесте test__login_in_account_by_forgot_password_form проверяется вход через форму восстановления пароля
# В файле test_logout_of_account созданы тесты на выход из аккаунта:
## В тесте test_logout_of_account проверяется выход из аккаунта через личный кабинет
# В файле test_registration созданы тесты на регистрацию аккаунта:
## В тесте test_successful_registration проверяется регистрация аккаунта с валидными данными, с последующей авторизацией только созданного пользователя
## В тесте test_registration_with_invalid_password проверяется регистрация аккаунта с некорректным паролем
# В файле test_page_navigation созданы тесты на переход по страницам:
## В тесте test_going_to_personal_account проверяется переход в личный кабинет
## В тесте test_going_from_personal_account_to_constructor_by_button_constructor проверяется переход к конструктору из личного кабинета, по кнопке "Конструктор"
## В тесте test_going_from_personal_account_to_constructor_by_click_on_logo проверяется переход к конструктору из личного кабинета, по клику по логотипу
## В тесте test_when_opening_main_page_selected_tab_bread проверяется что при открытие конструктора выбран раздел "Булки"
## В тесте test_going_to_the_tab_sauces проверяется переход к разделу "Соусы"
## В тесте test_going_to_the_tab_toppings проверяется переход к разделу "Начинки"
## В тесте test_going_to_the_tab_bread_after_going_another_teb проверяется переход к разделу "Булки", после предварительного перехода к другому разделу.
