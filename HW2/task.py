# Задание
# Условие: Добавить в наш тестовый проект шаг добавления поста после входа. Должна выполняться проверка на наличие названия поста на странице сразу после его создания.
# Совет: не забудьте добавить небольшие ожидания перед и после нажатия кнопки создания поста.


import yaml
from module import Site
import time

with open("config.yaml") as f:
    testdata = yaml.safe_load(f)
site = Site(testdata["address"])

def test_step1(x_selector1, x_selector2, btn_selector, btn_create_post, enter_title, enter_descr, enter_content,
               btn_save_post, post_name):
    input1 = site.find_element("xpath", x_selector1)
    input1.clear()
    input1.send_keys(testdata['login'])

    input2 = site.find_element("xpath", x_selector2)
    input2.clear()
    input2.send_keys(testdata['passwd'])

    btn = site.find_element("css", btn_selector)
    btn.click()

    time.sleep(3)

    btn_create_posts = site.find_element("css", btn_create_post) # Создание поста
    btn_create_posts.click()

    title = site.find_element("xpath", enter_title) # Ввод заголовка
    title.clear()
    title.send_keys(testdata['title'])

    description = site.find_element("xpath", enter_descr) # Ввод описания
    description.clear()
    description.send_keys(testdata['description'])

    content = site.find_element("xpath", enter_content) # Ввод контента
    content.clear()
    content.send_keys(testdata['content'])

    btn_save_posts = site.find_element("css", btn_save_post) # Сохраняем пост
    btn_save_posts.click()

    time.sleep(3)
    check_post = site.find_element("xpath", post_name) # Проверка на наличие заголовка поста
    assert check_post.text == f"{testdata['title']}"

    site.close()