import pytest
import logging
from pages.home_page import HomePage
from pages.locators.home_selectors import HomeSelectors


def test_home_page_opens(browser):
    logging.info("Запуск теста")
    home = HomePage(browser).open()
    actual_title = home.get_title()
    assert actual_title == HomeSelectors.EXPECTED_TITLE , "Заголовок отличается"
    print(f'✅ Заголовок соответствует')
    assert home.login_button_is_visible(), "Кнопка войти не найдена"
    print(f'✅ Кнопка войти найдена')
    assert home.hotels_tab_is_visible(), "Вертикаль отели не найдена"
    print(f'✅ Вертикаль отели')
    assert home.flights_tab_is_visible(), "Вертикаль авиа не найдена"
    print(f'✅ Вертикаль Авиа')
    assert home.trains_tab_is_visible(), "Вертикаль поезда не найдена"
    print(f'✅ Вертикаль поезда')
    assert home.tours_tab_is_visible(),"Вертикаль туры не найдена"
    print(f'✅ Вертикаль Туры')
    