import pytest
from methods import Projects
from faker import Faker
fake = Faker()
api = Projects('https://ru.yougile.com')


@pytest.mark.positive_test
def test_positive_create_project():
    create = api.positive_create_project(title=fake.country())
    assert len(create) == 1
    assert create['id'] != None


@pytest.mark.negative_test  # нет авторизации
def test_negative_create_project():
    resp = api.negative_create_project(title=fake.country())
    assert len(resp) == 3
    assert resp['error'] == 'Unauthorized'


@pytest.mark.positive_test
def test_positive_change_project():
    # создание
    create = api.positive_create_project(title=fake.country())
    result = create["id"]

    # изменение
    update = api.change_project(id=result, title='Изменено')
    id_2 = api.get_list()['content'][-1]["id"]
    assert len(update) == 1
    assert id_2 == result


@pytest.mark.negative_test
def test_negative_change_project():
    # создание
    create = api.positive_create_project(title=fake.country())
    result = create['id']

    # изменение
    change = api.change_project(id=result, title='')
    assert change['message'][0] == 'title should not be empty'
    assert change['error'] == "Bad Request"


@pytest.mark.positive_test
def test_positive_get_by_id():
    # создание
    create = api.positive_create_project(title=fake.country())
    result = create['id']

    # получение
    get = api.get_by_id(result)
    assert len(get) == 4
    assert len(get['id']) == 36


@pytest.mark.negative_test
def test_negative_get_by_id():  # несуществующий id
    get = api.get_by_id('adc719f5-f8n3-43c6-re47-3n9u156971x3')
    assert get['error'] == 'Not Found'
    assert get['message'] == 'Проект не найден'
