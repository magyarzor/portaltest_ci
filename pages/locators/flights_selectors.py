class FlightsSelectors:
    # Вкладка Авиабилеты (уже есть в home_selectors)
    
    # Поля ввода
    FROM_INPUT = 'input.urSya' 
    TO_INPUT = 'input.urSya.input_center'

    # Календарь
    DATE_PICKER_START = '[data-qa="search-form-date-picker-start-trigger"]'
    DATE_PICKER_END = '[data-qa="search-form-date-picker-end-trigger"]'

    
    # Кнопки
    SEARCH_BUTTON = 'button:has-text("Найти")'
    BUY_BUTTON = 'button:has-text("Купить")'
    PARTNER_BUTTON = 'a:has-text("Перейти на сайт")'  # или data-qa