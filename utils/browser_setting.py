import os
from playwright.sync_api import sync_playwright

PROFILE_DIR = os.path.expanduser("~/playwright-profile")
HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"

def start_browser():
    playwright = sync_playwright().start()
    context = playwright.chromium.launch_persistent_context(
        user_data_dir=PROFILE_DIR,
        headless=HEADLESS,  # 👈 теперь управляется через переменную
        channel="chrome",
        ignore_default_args=["--enable-automation"],
        args=[
            "--disable-blink-features=AutomationControlled",
            "--disable-infobars",
            "--no-sandbox",
            "--disable-dev-shm-usage"
        ]
    )
    
    # Маскировка бота
    context.add_init_script("""
        Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
        window.chrome = window.chrome || {};
        Object.defineProperty(navigator, 'languages', { get: () => ['ru-RU', 'ru'] });
        Object.defineProperty(navigator, 'plugins', { get: () => [1, 2, 3, 4, 5] });
    """)
    
    page = context.pages[0] if context.pages else context.new_page()
    return playwright, context, page

def close_browser(playwright, context):
    context.close()
    playwright.stop()
