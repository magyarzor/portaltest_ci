from pages.base_page import BasePage
from pages.locators.home_selectors import HomeSelectors

class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = "https://travel.yandex.ru/"
    
    def open(self):
        self.navigate_to(self.url)
        return self
    
    def login_button_is_visible(self) -> bool:
        return self.is_visible(HomeSelectors.LOGIN_BUTTON)
    
    def hotels_tab_is_visible(self) -> bool:
        return self.is_visible(HomeSelectors.HOTELS_TAB)
    
    def flights_tab_is_visible(self) -> bool:
        return self.is_visible(HomeSelectors.FLIGHTS_TAB)
    
    def trains_tab_is_visible(self) -> bool:
        return self.is_visible(HomeSelectors.TRAINS_TAB)
    
    def tours_tab_is_visible(self) -> bool:
        return self.is_visible(HomeSelectors.TOURS_TAB)
    
    def click_flights_tab(self):
        self.click(HomeSelectors.FLIGHTS_TAB)
        return self