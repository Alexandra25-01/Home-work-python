@echo off
REM Очистка старых результатов
rmdir /s /q allure-results

REM Запуск тестов с генерацией Allure-результатов
pytest shop_test_allure.py --alluredir=./allure-results

REM Просмотр отчета в браузере
allure serve allure-results
pause