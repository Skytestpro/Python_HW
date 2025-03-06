from Class_Subject_DB import Subject
from faker import Faker
fake = Faker()
db = Subject('postgresql://postgres:123@localhost:5432/postgres')


def test_create_subject():
    # создание
    new_id = db.get_new_id()
    new_title = fake.country()
    db.create(new_id, new_title)

    # проверки
    assert db.get_all()[-1]['subject_id'] == new_id
    assert db.get_all()[-1]['subject_title'] == new_title

    # удаление
    db.delete(new_id)


def test_update():
    # создание
    id = db.get_new_id()
    title = fake.country()
    db.create(id, title)

    # обновление
    new_title = 'update'
    db.update(new_title, id)

    # проверки
    assert db.get_all()[-1]['subject_title'] == new_title
    assert db.get_all()[-1]['subject_id'] == id

    # удаление
    db.delete(id)


def test_delete():
    # создание
    new_id = db.get_new_id()
    new_title = fake.country()
    db.create(new_id, new_title)
    len1 = len(db.get_all())

    # удаление
    db.delete(new_id)
    len2 = len(db.get_all())
    assert len1 - len2 == 1
