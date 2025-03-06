from sqlalchemy import create_engine, text


class Subject:
    __scripts = {
        'select': text(
            'select * from subject'),
        'max_id': text(
            'select max(subject_id) from subject'),
        'insert': text(
            'insert into subject(subject_id, subject_title) '
            'values(:new_id, :new_title)'),
        'delete': text(
            'delete from subject where subject_id = :sub_id'),
        'update': text(
            'update subject set subject_title = :new_title '
            'where subject_id = :sub_id')
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    def get_all(self):
        with self.__db.connect() as connection:
            result = connection.execute(self.__scripts['select'])
            return result.mappings().all()

    def get_new_id(self):
        with self.__db.connect() as connection:
            result = connection.execute(self.__scripts['max_id'])
            return result.mappings().all()[0]['max']+1

    def create(self, id, title):
        with self.__db.connect() as connection:
            transaction = connection.begin()
            connection.execute(
                self.__scripts['insert'], {"new_id": id, "new_title": title})
            transaction.commit()

    def delete(self, id):
        with self.__db.connect() as connection:
            transaction = connection.begin()
            connection.execute(self.__scripts['delete'], {'sub_id': id})
            transaction.commit()

    def update(self, title, id):
        with self.__db.connect() as connection:
            transaction = connection.begin()
            connection.execute(
                self.__scripts['update'], {'new_title': title, 'sub_id': id})
            transaction.commit()
