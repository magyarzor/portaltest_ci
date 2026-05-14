from playwright.sync_api import sync_playwright
import os

PROFILE_DIR = os.path.expanduser("~/playwright-profile")
HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"

def start_browser():
    """Запускает браузер с сохранением профиля"""
    playwright = sync_playwright().start()
    context = playwright.chromium.launch_persistent_context(
        user_data_dir=PROFILE_DIR,
        headless=HEADLESS,
        channel="chrome",
        ignore_default_args=["--enable-automation"],
        args=[
            "--disable-blink-features=AutomationControlled",
            "--disable-infobars"                              
        ]
    )
    # 👇 МАСКИРУЕМ БОТА
    context.add_init_script("""
        // Убираем webdriver
        Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined
        });
        
        // Добавляем chrome (если нет)
        window.chrome = window.chrome || {};
        
        // Маскируем languages
        Object.defineProperty(navigator, 'languages', {
            get: () => ['ru-RU', 'ru', 'en-US', 'en']
        });
        
        // Маскируем plugins
        Object.defineProperty(navigator, 'plugins', {
            get: () => [1, 2, 3, 4, 5]
        });
    """)
    page = context.pages[0] if context.pages else context.new_page()
    return playwright, context, page

def close_browser(playwright, context):
    """Закрывает браузер"""
    context.close()
    playwright.stop()