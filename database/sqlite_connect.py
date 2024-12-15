import sqlite3 as sql_database
from loader import logger


class SqlSchool:
    """
    Класс SQL Школа

    Attributes:
        __school: база данных школы с учениками
        __cursor: курсор базы данных

    """
    def __init__(self) -> None:
        self.__school = sql_database.connect('database/school_data.db')
        self.__cursor = self.__school.cursor()

    def school_start(self) -> None:
        """
        Активация базы данных школы, создание таблицы учеников(pupils)

        """
        if self.__school:
            logger.info('Соединение с базой данных установлено')

        self.__cursor.execute(
            'CREATE TABLE IF NOT EXISTS pupils('
            'id INTEGER PRIMARY KEY AUTOINCREMENT, '
            'name TEXT NOT NULL, '
            'age INTEGER NOT NULL, '
            'grade TEXT NOT NULL)'
        )
        self.__school.commit()

    def add_pupil(self, name: str, age: int | str, grade: str) -> None:
        """
        Добавление ученика в базу данных

        """
        self.__cursor.execute(
            'INSERT INTO pupils(name, age, grade) VALUES(?, ?, ?)', (name, age, grade)
        )
        self.__school.commit()
        self.__school.close()