from lib.space import Space
from lib.database_connection import DatabaseConnection

class SpaceRepository:
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute('SELECT * FROM spaces')
        list_to_return = []
        for row in rows:
            space = Space(row['id'], row['name'], row['descr'], row['price'], row['user_id'])
            list_to_return.append(space)
        if len(list_to_return):
            return list_to_return
        return False
        
    def find(self, id_to_find):
        rows = self._connection.execute("SELECT * FROM spaces WHERE id=%s", [id_to_find])
        if rows:
            row = rows[0]
        return Space(row['id'], row['name'], row['descr'], row['price'])
    
    def update(self, space: Space):
        self._connection.execute("UPDATE spaces SET name=%s, descr=%s, price=%s WHERE id=%s", [space.name, space.desc, space.price, space.id])