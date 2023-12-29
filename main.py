import time
from colorama import init, Fore, Style

def main():
    init(autoreset=True)  # Инициализация colorama с авто-сбросом цвета

    try:
        while True:
            # Получение текущего времени
            current_time = time.strftime("%H:%M:%S", time.localtime())

            # Форматирование строки с увеличенным размером шрифта и красным цветом
            formatted_time = f"{Fore.RED}{Style.BRIGHT}{current_time}{Style.RESET_ALL}"
            # Добавление символа новой строки
            #formatted_time += '\n'

            # Вывод текущего времени на экран
            print(formatted_time, end='\r', flush=True)
            #print('11111')


            # Ожидание 1 секунды
            time.sleep(1)


    except KeyboardInterrupt:
        pass  # Обработка прерывания клавиатуры (например, нажатие Ctrl+C)

    print("\nПрограмма завершена.")


if __name__ == "__main__":
    main()


