import time
from pages.main_page import Pages

"""Тесты для иконок соц.сетей, проверяющие переход на корректные ссылки в футере. """


def test_link_youtube(web_browser):
    page = Pages(web_browser)
    page.scroll_footer()
    page.link_youtube.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    time.sleep(5)

    assert page.get_current_url() == 'https://www.youtube.com/user/labirintruTV'


def test_link_vk(web_browser):
    page = Pages(web_browser)
    page.scroll_footer()
    page.link_VK.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    time.sleep(5)

    assert page.get_current_url() == 'https://vk.com/labirint_ru'


def test_link_vk_kids(web_browser):
    page = Pages(web_browser)
    page.scroll_footer()
    page.link_VK_kids.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    time.sleep(5)

    assert page.get_current_url() == 'https://vk.com/labirintdeti'


def test_link_classmates(web_browser):
    page = Pages(web_browser)
    page.scroll_footer()
    page.link_classmates.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    time.sleep(5)

    assert page.get_current_url() == 'https://ok.ru/labirintru'


def test_link_zen(web_browser):
    page = Pages(web_browser)
    page.scroll_footer()
    page.link_zen.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    time.sleep(5)

    assert page.get_current_url() == 'https://zen.yandex.ru/labirintru'


def test_link_t_me(web_browser):
    page = Pages(web_browser)
    page.scroll_footer()
    page.link_t_me.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    time.sleep(5)

    assert page.get_current_url() == 'https://t.me/labirintru'


def test_link_tiktok(web_browser):
    page = Pages(web_browser)
    page.scroll_footer()
    page.link_tiktok.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    time.sleep(5)

    assert page.get_current_url() == 'https://www.tiktok.com/@labirintru'


def test_link_appstore(web_browser):
    page = Pages(web_browser)
    page.scroll_footer()
    page.link_appstore.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    time.sleep(5)

    assert page.get_current_url() == 'https://apps.apple.com/ru/app/%D0%BB%D0%B0%D0%B1%D0%B8%D1%80%D0%B8%D0%BD%D1%82-%D1%80%D1%83-%D0%BA%D0%BD%D0%B8%D0%B6%D0%BD%D1%8B%D0%B9-%D0%BC%D0%B0%D0%B3%D0%B0%D0%B7%D0%B8%D0%BD/id1008650482'


def test_link_app_gallery(web_browser):
    page = Pages(web_browser)
    page.scroll_footer()
    page.link_appgallery.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    time.sleep(5)

    assert page.get_current_url() == 'https://appgallery.huawei.com/app/C101184737?appId=C101184737&source=appshare&subsource=C101184737'


def test_link_google_play(web_browser):
    page = Pages(web_browser)
    page.scroll_footer()
    page.link_google_play.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    time.sleep(5)

    assert page.get_current_url() == 'https://play.google.com/store/apps/details?id=ru.labirint.android'

