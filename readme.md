Финальное тестовое задание для студентов курса. Написание автоматизированных тестов с использованием PyTest и Selenium для интернет-магазина, 
в котором есть большое количество товаров, а также функционал поиска и сортировки / фильтрации товаров.

Автоматизированное тестирование UI сайта: https://labirint.ru/ с использованием PyTest и Selenium.

в папке Pages: base.py содержит библиотеку Smart Page Object
elements.py содержит класс для определения элементов на веб-страницах

запуск тестов командой: python -m pytest -v --driver Chrome --driver-path <chromedriver_directory>/<chromedriver_file> Tests/tests.py 
                        python -m pytest -v --driver Chrome --driver-path <chromedriver_directory>/<chromedriver_file> Tests/tests_social.py
                        
файл chromdriver.exe добавляю в корневую папку проекта
