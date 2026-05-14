from pages.base_page import BasePage
from pages.locators.flights_selectors import FlightsSelectors
from datetime import datetime, timedelta
import time


class FlightsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
    
    def _select_date(self, days_ahead: int = 10):
        target_date = datetime.now() + timedelta(days=days_ahead)
        target_day = target_date.day
        target_month = target_date.strftime("%B")
        current_month = datetime.now().strftime("%B")

        if target_month != current_month:
            self.click(f'[data-qa="calendar-month-text"]:has-text("{target_month}")')
            self.page.wait_for_timeout(300)
        
        self.click(f'//span[text()="{target_day}"]')

    def search(self, from_city: str, to_city: str):
        """Поиск авиабилетов"""
        self.click(FlightsSelectors.FROM_INPUT)
        time.sleep(1.3)
        self.page.keyboard.press("Backspace")  # удалить
        self.fill(FlightsSelectors.FROM_INPUT, from_city)
        time.sleep(1.3)
        self.page.keyboard.press("Tab")
        self.click(FlightsSelectors.TO_INPUT)
        time.sleep(1.3)
        self.fill(FlightsSelectors.TO_INPUT, to_city)
        time.sleep(0.3)
        self.page.keyboard.press("Tab")
        #self.click(FlightsSelectors.DATE_PICKER_START)
        self._select_date(days_ahead=10)  # 👈 ЗДЕСЬ ВЫЗЫВАЕТСЯ
        self.click(FlightsSelectors.SEARCH_BUTTON)
        return self
    
    def wait_for_results(self, timeout: int = 30000):
        """Дождаться загрузки результатов поиска"""
        self.page.wait_for_selector('.Kw61r.vOWh4.ckU2e.WwWk2', timeout=timeout)
        self.page.wait_for_timeout(6000)
        return self

    def has_results(self) -> bool:
        """Проверить, есть ли результаты поиска"""
        return self.page.locator('.Kw61r.vOWh4.ckU2e.WwWk2').count() > 0

    def find_s7_and_buy(self):
        """Найти чистое S7, открыть карточку, нажать кнопку с ценой"""
        
        # 1. Находим ссылку на чистое S7
        all_links = self.page.locator('a[href*="forward=S7"]')
        
        for i in range(all_links.count()):
            href = all_links.nth(i).get_attribute('href') or ""
            if 'forward=' in href:
                forward_part = href.split('forward=')[1].split('&')[0]
                forward_clean = forward_part.replace('%20', ' ')
                
                if forward_clean.startswith('S7') and ',' not in forward_clean:
                    print(f"✅ Чистое S7: {forward_clean}")
                    
                    # Кликаем по ссылке (открывается карточка)
                    all_links.nth(i).click()
                    self.page.wait_for_timeout(2000)
                    
                    # 2. В карточке нажимаем кнопку с ценой (локатор из твоего HTML)
                    buy_button = self.page.locator('a[href*="/avia/redirect/"][href*="partner=s_seven"]')
                    
                    if buy_button.count() > 0:
                        buy_button.first.click()
                        print("✅ Кнопка с ценой нажата")
                        return True
                    else:
                        print("❌ Кнопка с ценой не найдена")
                        return False
        
        print("❌ Чистое S7 не найдено")
        return False
    
    # Проверка редиректа на партнера
    def check_s7_redirect(self, context):
        """Проверить, что открылась новая вкладка с s7.ru (без каптчи и проверок)"""
        
        # Ждём 3 секунды появления новой вкладки
        self.page.wait_for_timeout(3000)
        
        # Проверяем, открылась ли новая вкладка
        if len(context.pages) < 2:
            print("❌ Новая вкладка не открылась")
            return False
        
        # Проверяем URL новой вкладки
        new_page = context.pages[-1]
        new_url = new_page.url
        
        if "s7.ru" in new_url:
            print(f"✅ Редирект на S7 выполнен: {new_url[:80]}...")
            # Закрываем вкладку с S7
            new_page.close()
            print("✅ Вкладка с S7 закрыта")
            
            # Возвращаемся к основной вкладке
            main_page = context.pages[0]
            main_page.bring_to_front()
            return True
        else:
            print(f"❌ Редирект не на S7: {new_url[:80]}...")
            return False