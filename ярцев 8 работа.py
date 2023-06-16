class CustomExceptionOne(BaseException):
    pass

class CustomExceptionTwo(BaseException):
    pass

class CustomExceptionThree(BaseException):
    pass

class UserFinder:
    def __init__(self, user_db):
        self.user_db = user_db
    
    def get_user_by_id(self, user_id):
        if not isinstance(user_id, int):
            raise TypeError("Идентификатор пользователя должен быть целым числом")
        
        user = self.user_db.get(user_id)
        if user is None:
            raise ValueError(f"Не найден пользователь с идентификатором {user_id}")
        
        return user
    
    def get_users_by_name(self, name):
        if not isinstance(name, str):
            raise TypeError("Имя должно быть строкой")
        
        users = [u for u in self.user_db if u.name == name]
        if not users:
            raise ValueError(f"Не найдено пользователей с именем {name}")
        
        return users
    
    def delete_user(self, user):
        if not isinstance(user, User):
            raise TypeError("Пользователь должен быть экземпляром класса User")
        
        self.user_db.delete(user.id)

class UserHandler:
    def __init__(self, user_finder):
        self.user_finder = user_finder
    
    def find_user(self, user_id):
        try:
            user = self.user_finder.get_user_by_id(user_id)
        except (TypeError, ValueError) as e:
            print(f"Не удалось найти пользователя: {str(e)}")
            return None
        
        return user
    
    def find_users_by_name(self, name):
        try:
            users = self.user_finder.get_users_by_name(name)
        except (TypeError, ValueError) as e:
            print(f"Не удалось найти пользователей: {str(e)}")
            return []
        
        return users
    
    def remove_user(self, user):
        try:
            self.user_finder.delete_user(user)
        except TypeError as e:
            print(f"Не удалось удалить пользователя: {str(e)}")
            return False
        
        return True