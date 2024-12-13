import sqlite3 as sql_database
from main import bot

# id (INTEGER, PRIMARY KEY, AUTOINCREMENT) name (TEXT) age (INTEGER) grade (TEXT)

class SqlSchool:
    """
    Класс SQL Школа

    Attributes:
        __sql_school: база данных школды с учениками
        __school_cur: курсор базы данных
        __bot: telegram бот

    """
    def __init__(self) -> None:
        self.__sql_school = sql_database.connect('database/school_data.db')
        self.__school_cur = self.__sql_school.cursor()
        self.__bot = bot

    def school_start(self) -> None:
        """
        Активация базы данных школы

        """
        if self.__sql_school:
            print('Соединение с базой данных истории установлено')

        self.sql_base.execute('CREATE TABLE IF NOT EXISTS request(.....)')
        self.sql_base.commit()

        async def sql_add_command(self, state):
        async with state.proxy() as data:
        self.base_cur.execute('INSERT INTO request VALUES (?, ?, ?, ?)', tuple(data.values()))
        self.sql_base.commit()

    async def sql_read(self, message):
        for ret in self.base_cur.execute('SELECT * FROM request').fetchall():
        await self.cricket_bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена: {ret[*1]}')