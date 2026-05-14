from playwright.sync_api import Page

class BasePage:
    """Базовый класс для всех страниц"""
    
    def __init__(self, page: Page):
        self.page = page
        self.timeout = 30000  # 30 секунд по умолчанию
    
    def navigate_to(self, url: str):
        """Перейти по URL"""
        self.page.goto(url, timeout=self.timeout)
        print(f"📍 Перешли на: {url}")
    
    def click(self, selector: str):
        """Кликнуть по элементу"""
        self.page.click(selector, timeout=self.timeout)
        print(f"🖱️ Кликнули: {selector}")
    
    def fill(self, selector: str, text: str):
        """Заполнить поле"""
        self.page.fill(selector, text, timeout=self.timeout)
        print(f"✏️ Ввели '{text}' в: {selector}")
    
    def get_title(self) -> str:
        """Получить заголовок страницы"""
        return self.page.title()
    
    def is_visible(self, selector: str) -> bool:
        """Проверить, виден ли элемент"""
        try:
            return self.page.is_visible(selector, timeout=5000)
        except:
            return False
    
    def wait_for_element(self, selector: str, timeout: int = None):
        """Дождаться появления элемента"""
        timeout = timeout or self.timeout
        self.page.wait_for_selector(selector, timeout=timeout)
        print(f"⏳ Дождались элемента: {selector}")