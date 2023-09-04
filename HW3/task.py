"""
Условие: Добавить в проект тест по проверке механики работы формы Contact Us
на главной странице личного кабинета. Должно проверятся открытие формы, ввод
данных в поля, клик по кнопке и появление всплывающего alert.
"""

import time
from TPage import OperationHelper

username = "nasty2008"
password = "bbabab5544bb"

def test_step(browser):
    test_page1 = OperationHelper(browser)
    test_page1.go_to_site()
    test_page1.enter_login(username)
    test_page1.enter_pswd(password)
    test_page1.click_button()

    time.sleep(3)

    test_page1.click_contact()

    time.sleep(3)

    test_page1.enter_cont_name("field_name")
    test_page1.enter_cont_email("email@gmail.ru")
    test_page1.enter_cont_text("field_text")

    time.sleep(1)

    test_page1.click_button()

    time.sleep(1)

    assert test_page1.get_alert_text() == "Form successfully submitted"