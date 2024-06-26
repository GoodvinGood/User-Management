import tkinter as tk
from tkinter import messagebox

# Класс Пользователь
class Пользователь:
    def __init__(self, id_пользователя, имя, уровень_доступа='пользователь'):
        self.__id_пользователя = int(id_пользователя)  # Убедимся, что ID является целым числом
        self.__имя = имя
        self.__уровень_доступа = уровень_доступа

    def получить_id(self):
        return self.__id_пользователя

    def получить_имя(self):
        return self.__имя

    def получить_уровень_доступа(self):
        return self.__уровень_доступа

    def установить_имя(self, имя):
        self.__имя = имя

    def установить_уровень_доступа(self, уровень_доступа):
        self.__уровень_доступа = уровень_доступа

# Класс Администратор
class Администратор(Пользователь):
    def __init__(self, id_пользователя, имя, уровень_админа='админ'):
        super().__init__(id_пользователя, имя, уровень_админа)
        self.__список_пользователей = []

    def добавить_пользователя(self, пользователь):
        if isinstance(пользователь, Пользователь):
            self.__список_пользователей.append(пользователь)
            print(f"Пользователь {пользователь.получить_имя()} добавлен.")
        else:
            print("Добавлять можно только экземпляры класса Пользователь.")

    def удалить_пользователя(self, id_пользователя):
        id_пользователя = int(id_пользователя)  # Убедимся, что ID является целым числом
        for пользователь in self.__список_пользователей:
            if пользователь.получить_id() == id_пользователя:
                self.__список_пользователей.remove(пользователь)
                print(f"Пользователь {пользователь.получить_имя()} удален.")
                return True
        print(f"Пользователь с ID {id_пользователя} не найден.")
        return False

    def получить_список_пользователей(self):
        return self.__список_пользователей

# Класс приложения на Tkinter
class Приложение(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Система управления пользователями")
        self.geometry("500x500")
        self.resizable(True, True)  # Разрешаем изменение размера окна

        self.админ = Администратор(0, "Главный Админ")

        # Добавление тестовых пользователей в базу
        self.админ.добавить_пользователя(Пользователь(1, "Алиса"))
        self.админ.добавить_пользователя(Пользователь(2, "Боб"))
        self.админ.добавить_пользователя(Пользователь(3, "Чарли"))
        self.админ.добавить_пользователя(Пользователь(4, "Дэйв"))
        self.админ.добавить_пользователя(Администратор(5, "Администратор"))

        self.создать_виджеты()

    def создать_виджеты(self):
        # Метка и поле для ввода ID пользователя
        self.label_id = tk.Label(self, text="ID пользователя")
        self.label_id.grid(row=0, column=0, padx=10, pady=10)

        self.entry_id = tk.Entry(self)
        self.entry_id.grid(row=0, column=1, padx=10, pady=10)

        # Метка и поле для ввода имени пользователя
        self.label_имя = tk.Label(self, text="Имя пользователя")
        self.label_имя.grid(row=1, column=0, padx=10, pady=10)

        self.entry_имя = tk.Entry(self)
        self.entry_имя.grid(row=1, column=1, padx=10, pady=10)

        # Метка и поле для ввода уровня доступа
        self.label_уровень = tk.Label(self, text="Уровень доступа")
        self.label_уровень.grid(row=2, column=0, padx=10, pady=10)

        self.entry_уровень = tk.Entry(self)
        self.entry_уровень.grid(row=2, column=1, padx=10, pady=10)

        # Кнопка для добавления пользователя
        self.button_добавить = tk.Button(self, text="Добавить пользователя", command=self.добавить_пользователя)
        self.button_добавить.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        # Кнопка для удаления пользователя
        self.button_удалить = tk.Button(self, text="Удалить пользователя", command=self.удалить_пользователя)
        self.button_удалить.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        # Кнопка для показа списка пользователей
        self.button_показать = tk.Button(self, text="Показать пользователей", command=self.показать_пользователей)
        self.button_показать.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        # Текстовое поле для отображения списка пользователей
        self.text_список = tk.Text(self, height=15, width=60)
        self.text_список.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

    def добавить_пользователя(self):
        # Получение ID, имени и уровня доступа пользователя из полей ввода
        id_пользователя = self.entry_id.get()
        имя = self.entry_имя.get()
        уровень_доступа = self.entry_уровень.get() or 'пользователь'  # По умолчанию уровень 'пользователь'

        # Проверка, что поля не пустые
        if id_пользователя and имя:
            try:
                id_пользователя = int(id_пользователя)
                if уровень_доступа.lower() == 'админ':
                    пользователь = Администратор(id_пользователя, имя)
                else:
                    пользователь = Пользователь(id_пользователя, имя, уровень_доступа)
                self.админ.добавить_пользователя(пользователь)
                messagebox.showinfo("Успех", f"Пользователь {имя} добавлен.")
                # Очистка полей ввода
                self.entry_id.delete(0, tk.END)
                self.entry_имя.delete(0, tk.END)
                self.entry_уровень.delete(0, tk.END)
            except ValueError:
                messagebox.showwarning("Ошибка ввода", "ID пользователя должен быть числом.")
        else:
            messagebox.showwarning("Ошибка ввода", "Пожалуйста, введите ID и имя пользователя.")

    def удалить_пользователя(self):
        # Получение ID пользователя из поля ввода
        id_пользователя = self.entry_id.get()
        if id_пользователя:
            try:
                id_пользователя = int(id_пользователя)
                if self.админ.удалить_пользователя(id_пользователя):
                    messagebox.showinfo("Успех", f"Пользователь с ID {id_пользователя} удален.")
                else:
                    messagebox.showwarning("Ошибка", f"Пользователь с ID {id_пользователя} не найден.")
                # Очистка поля ввода
                self.entry_id.delete(0, tk.END)
            except ValueError:
                messagebox.showwarning("Ошибка ввода", "ID пользователя должен быть числом.")
        else:
            messagebox.showwarning("Ошибка ввода", "Пожалуйста, введите ID пользователя.")

    def показать_пользователей(self):
        # Очистка текстового поля
        self.text_список.delete(1.0, tk.END)
        # Получение списка пользователей
        список_пользователей = self.админ.получить_список_пользователей()
        # Вывод каждого пользователя в текстовое поле
        for пользователь in список_пользователей:
            self.text_список.insert(tk.END, f"ID: {пользователь.получить_id()}, Имя: {пользователь.получить_имя()}, Уровень доступа: {пользователь.получить_уровень_доступа()}\n")

# Запуск приложения
if __name__ == "__main__":
    приложение = Приложение()
    приложение.mainloop()
