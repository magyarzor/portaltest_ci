import pytest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from pages.home_page import HomePage
from pages.flights_page import FlightsPage

@pytest.mark.skipif(os.getenv("CI") == "true", reason="Captcha in CI, run manually")

def test_flights_search_and_redirect(browser):
    """Тест поиска авиабилетов и редиректа на S7"""
    page = browser
    home = HomePage(page).open()
    home.click_flights_tab()
    
    flights = FlightsPage(page)
    flights.search("Казань", "Санкт-Петербург")
    
    flights.wait_for_results()
    assert flights.has_results(), "Нет результатов поиска"
    
    # Главный assert
    assert flights.find_s7_and_buy(), "Чистое S7 не найдено или не кликнулось"
    
    print("✅ Тест пройден: S7 найден, клик выполнен")
