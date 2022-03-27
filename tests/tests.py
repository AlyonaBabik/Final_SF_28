from pages.main_page import Pages


def test_field_search(web_browser):
    """1.Тестирование поле поиска. Поиск книги"""
    page = Pages(web_browser)
    page.search.send_keys('Алиса')
    page.search_run_button.click()

    assert page.message_search


def test_book_button(web_browser):
    """2.Тестируем кнопку "Книги", с переходом на соответствующую страницу"""
    page = Pages(web_browser)
    page.book_button.click()

    assert page.get_current_url() == 'https://www.labirint.ru/books/'


def test_best_button(web_browser):
    """3.Тестируем кнопку "Главное 2022", с переходом на соответствующую страницу"""
    page = Pages(web_browser)
    page.best_button.click()

    assert page.get_current_url() == 'https://www.labirint.ru/best/'


def test_school_button(web_browser):
    """4.Тестируем кнопку "Школа", с переходом на соответствующую страницу"""
    page = Pages(web_browser)
    page.school_button.click()

    assert page.get_current_url() == 'https://www.labirint.ru/school/'


def test_toys_button(web_browser):
    """5.Тестируем кнопку "Игрушки", с переходом на соответствующую страницу"""
    page = Pages(web_browser)
    page.toys_button.click()

    assert page.get_current_url() == 'https://www.labirint.ru/games/'


def test_button_office(web_browser):
    """6.Тестируем кнопку "Канцелярские товары", с переходом на соответствующую страницу """
    page = Pages(web_browser)
    page.office_supplies_button.click()

    assert page.get_current_url() == 'https://www.labirint.ru/office/'


def test_delivery_button(web_browser):
    """7. Тестируем кнопку "Доставка и оплата", с переходом на соответствующую страницу """
    page = Pages(web_browser)
    page.delivery_button.click()

    assert page.get_current_url() == 'https://www.labirint.ru/help/'


def test_certificate_button(web_browser):
    """8. Тестируем кнопку "Сертификаты", с переходом на соответствующую страницу """
    page = Pages(web_browser)
    page.certificate_button.click()

    assert page.get_current_url() == 'https://www.labirint.ru/top/certificates/'


def test_rating_button(web_browser):
    """9.Тестируем кнопку "Рейтинги", с переходом на соответствующую страницу """
    page = Pages(web_browser)
    page.rating_button.click()

    assert page.get_current_url() == 'https://www.labirint.ru/rating/?id_genre=-1'


def test_novelty_button(web_browser):
    """10.Тестируем кнопку "Новинки", с переходом на соответствующую страницу """
    page = Pages(web_browser)
    page.novelty_button.click()

    assert page.get_current_url() == 'https://www.labirint.ru/novelty/'


def test_sale_button(web_browser):
    """11.Тестируем кнопку " Скидки",  с переходом на соответствующую страницу """
    page = Pages(web_browser)
    page.sale_button.click()

    assert page.get_current_url() == 'https://www.labirint.ru/search/?discount=1&available=1&order=actd&way=back&paperbooks=1&ebooks=1&otherbooks=1'


def test_contact_button(web_browser):
    """12.Тестируем кнопку "Контакты",с переходом на соответствующую страницу """
    page = Pages(web_browser)
    page.sale_button.click()

    assert page.get_current_url() == 'https://www.labirint.ru/contact/'


def test_support_button(web_browser):
    """13.Тестируем кнопку "Поддержка",с переходом на соответствующую страницу """
    page = Pages(web_browser)
    page.sale_button.click()

    assert page.get_current_url() == 'https://www.labirint.ru/support/'


def test_change_region(web_browser):
    """14.Тестируем кнопку 'Регион'"""
    page = Pages(web_browser)
    page.region_button.click()
    page.region_button.delete()
    page.field_region_button.send_keys("Красноярск")
    page.click_region.click()

    assert page.message_region


def test_button_maps(web_browser):
    """15.Тестируем кнопку "Доставим... (доступная дата)"""
    page = Pages(web_browser)
    page.maps_button.click()

    assert page.get_current_url() == 'https://www.labirint.ru/maps/'


def test_button_what_to_reed(web_browser):
    page = Pages(web_browser)
    page.what_reed_button.click()

    assert page.get_current_url() == 'https://www.labirint.ru/top/toread/'


def test_topic_month(web_browser):
    page = Pages(web_browser)
    page.what_reed_recommend.click()

    assert page.get_current_url() == 'https://www.labirint.ru/now/'


def test_child_now(web_browser):
    page = Pages(web_browser)
    page.what_reed_recommend.click()
    page.child_nav_button.click()

    assert page.get_current_url() == 'https://www.labirint.ru/child-now/'


def test_journals(web_browser):
    page = Pages(web_browser)
    page.what_reed_recommend.click()
    page.button_journals.click()

    assert page.get_current_url() == 'https://www.labirint.ru/journals/'


def test_book_review(web_browser):
    page = Pages(web_browser)
    page.what_reed_recommend.click()
    page.button_review.click()

    assert page.get_current_url() == 'https://www.labirint.ru/news/books/'


def test_reader_review(web_browser):
    page = Pages(web_browser)
    page.what_reed_recommend.click()
    page.button_review.click()

    assert page.get_current_url() == 'https://www.labirint.ru/reviews/'


def test_reader_recommendation(web_browser):
    page = Pages(web_browser)
    page.what_reed_recommend.click()
    page.button_recommendations.click()

    assert page.get_current_url() == 'https://www.labirint.ru/recommendations/'


def test_littest(web_browser):
    page = Pages(web_browser)
    page.what_reed_recommend.click()
    page.button_littest.click()

    assert page.get_current_url() == 'https://www.labirint.ru/littest/'


def test_contests(web_browser):
    page = Pages(web_browser)
    page.what_reed_recommend.click()
    page.button_contests.click()

    assert page.get_current_url() == 'https://www.labirint.ru/contests/'


def test_multimedia(web_browser):
    page = Pages(web_browser)
    page.scroll_footer()
    page.button_multimedia.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    time.sleep(5)

    assert page.get_current_url() == 'https://www.labirint.ru/multimedia/'


def test_souvenir(web_browser):
    page = Pages(web_browser)
    page.scroll_footer()
    page.button_souvenir.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    time.sleep(5)

    assert page.get_current_url() == 'https://www.labirint.ru/souvenir/'


def test_goods_for_home(web_browser):
    page = Pages(web_browser)
    page.scroll_footer()
    page.button_home_goods.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    time.sleep(5)

    assert page.get_current_url() == 'https://www.labirint.ru/household/'


def test_soap_category(web_browser):
    page = Pages(web_browser)
    page.scroll_footer()
    page.button_home_goods.click()
    page.button_soap.click()

    assert page.get_current_url() == 'https://www.labirint.ru/genres/3238/'


def test_toothpaste_category(web_browser):
    page = Pages(web_browser)
    page.scroll_footer()
    page.button_home_goods.click()
    page.button_toothpaste.click()

    assert page.get_current_url() == 'https://www.labirint.ru/genres/3237/'


def test_wet_wipes_category(web_browser):
    page = Pages(web_browser)
    page.scroll_footer()
    page.button_home_goods.click()
    page.button_wipes.click()

    assert page.get_current_url() == 'https://www.labirint.ru/genres/3239/'


def test_calendars(web_browser):
    page = Pages(web_browser)
    page.scroll_footer()
    page.button_souvenir.click()
    page.button_calendars.click()

    assert page.get_current_url() == 'https://www.labirint.ru/genres/179/'


def test_advent_calendars(web_browser):
    page = Pages(web_browser)
    page.scroll_footer()
    page.button_souvenir.click()
    page.button_cal_advent.click()

    assert page.get_current_url() == 'https://www.labirint.ru/genres/3330/'


def test_magnet_calendars(web_browser):
    page = Pages(web_browser)
    page.scroll_footer()
    page.button_souvenir.click()
    page.button_cal_magnet.click()

    assert page.get_current_url() == 'https://www.labirint.ru/genres/718/'


def test_quarter_calendars(web_browser):
    page = Pages(web_browser)
    page.scroll_footer()
    page.button_souvenir.click()
    page.button_kvartal_cal.click()

    assert page.get_current_url() == 'https://www.labirint.ru/genres/2753/'


def test_wall_calendars(web_browser):
    page = Pages(web_browser)
    page.scroll_footer()
    page.button_souvenir.click()
    page.button_wall_cal.click()

    assert page.get_current_url() == 'https://www.labirint.ru/genres/716/'


def test_small_calendars(web_browser):
    page = Pages(web_browser)
    page.scroll_footer()
    page.button_souvenir.click()
    page.button_small_cal.click()

    assert page.get_current_url() == 'https://www.labirint.ru/genres/717/'


def test_multimedia_audio(web_browser):
    page = Pages(web_browser)
    page.scroll_footer()
    page.button_multimedia.click()
    page.button_audio.click()

    assert page.get_current_url() == 'https://www.labirint.ru/multimedia/audio'


def test_multimedia_video(web_browser):
    page = Pages(web_browser)
    page.scroll_footer()
    page.button_multimedia.click()
    page.button_video.click()

    assert page.get_current_url() == 'https://www.labirint.ru/multimedia/video'


def test_multimedia_soft(web_browser):
    page = Pages(web_browser)
    page.scroll_footer()
    page.button_multimedia.click()
    page.button_soft.click()

    assert page.get_current_url() == 'https://www.labirint.ru/multimedia/software'


def test_special_offer(web_browser):
    page = Pages(web_browser)
    page.scroll_footer()
    page.button_action.click()

    assert page.get_current_url() == 'https://www.labirint.ru/actions/'
