class User:
    def __init__(self, user_id, name, access_level='user'):
        self.__user_id = user_id
        self.__name = name
        self.__access_level = access_level

    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level

    def set_name(self, name):
        self.__name = name


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name, access_level='admin')

    def add_user(self, user_list, user):
        user_list.append(user)

    def remove_user(self, user_list, user_id):
        for index, user in enumerate(user_list):
            if user.get_user_id() == user_id:
                del user_list[index]
                break


if __name__ == "__main__":
    # Создание администратора

    admin = Admin(1, "Стас")

    # Создаем обычных пользователей
    user_boris = User(2, "Борис")
    user_maria = User(3, "Мария")
    user_anton = User(4, "Антон")
    user_olga = User(5, "Ольга")

    company_users = []

    # Администратор добавляет всех пользователей
    admin.add_user(company_users, user_boris)
    admin.add_user(company_users, user_maria)
    admin.add_user(company_users, user_anton)
    admin.add_user(company_users, user_olga)

    print(f"Пользователи после добавления:")
    for user in company_users:
        print(f"ID: {user.get_user_id()}, Имя: {user.get_name()}, Уровень доступа: {user.get_access_level()}")

    # Администратор удаляет Антона (ID=4)
    admin.remove_user(company_users, 4)

    print("\nПользователи после удаления Антона:")
    for user in company_users:
        print(f"ID: {user.get_user_id()}, Имя: {user.get_name()}")
