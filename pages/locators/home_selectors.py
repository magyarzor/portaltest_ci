class HomeSelectors:
    # Кнопка "Войти"
    LOGIN_BUTTON = 'a:has-text("Войти"), a[href*="passport.yandex.ru"]'
    
    # Вертикали
    HOTELS_TAB = '//span[text()="Отели"]'
    FLIGHTS_TAB = '//span[text()="Авиа"]'
    TRAINS_TAB = '//a[@href="/trains/"]//span[contains(text(), "Поезда") or contains(text(), "Ж/д")]'
    TOURS_TAB = '//span[text()="Туры"]'

    #Заголовок
    EXPECTED_TITLE = "Яндекс Путешествия – бронирование отелей, авиабилеты, билеты на поезд"