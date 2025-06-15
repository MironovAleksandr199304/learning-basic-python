def get_user_by_id(user_id):
    """Имитация запроса к API"""
    users = {
        1: {"id": 1, "name": "Alice", "email": "alice@test.com"},
        2: {"id": 2, "name": "Bob", "email": "bob@test.com"},
    }
    return users.get(user_id, None)