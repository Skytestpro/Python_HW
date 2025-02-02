import pytest
from StringUtils import StringUtils


# capitilize
# Принимает на вход текст, делает первую букву заглавной
# и возвращает этот же текст
@pytest.mark.positive_capitilize
@pytest.mark.parametrize('string, result', [
    ("текст", "Текст"),
    ("text text", "Text text"),
    ('Текст', 'Текст')
    ])
def test_positive_capitilize(string, result):
    res = StringUtils()
    assert res.capitilize(string) == result


@pytest.mark.negative_capitilize
@pytest.mark.parametrize('string, result', [
    ('!!!', '!!!'),
    (' ', ' '),
    ('', ''),
    ('132', '132'),
    ('♦', '♦')
    ])
def test_negative_capitilize(string, result):
    res = StringUtils()
    assert res.capitilize(string) == result


# trim
# Принимает на вход текст и удаляет пробелы в начале, если они есть
@pytest.mark.positive_trim
@pytest.mark.parametrize('string, result', [
    ('    Текст', 'Текст'),
    ('   Text', 'Text'),
    ('Текст ♦', 'Текст ♦'),
    ('   123', '123'),
    ('текст    ', 'текст    ')
    ])
def test_positive_trim(string, result):
    res = StringUtils()
    assert res.trim(string) == result


@pytest.mark.negative_trim
@pytest.mark.parametrize('string, result', [
    ('', ''),
    ('   ', ''),
    ])
def test_negative_trim(string, result):
    res = StringUtils()
    assert res.trim(string) == result


# to_list
# Принимает на вход текст с разделителем и возвращает список строк
@pytest.mark.positive_to_list
@pytest.mark.parametrize('string, result', [
     ('1,2,3,4',  ['1', '2', '3', '4']),
     ('a,b,c,d', ['a', 'b', 'c', 'd']),
     ('a,3,5', ['a', '3', '5']),
     ('♦,♣,♠', ['♦', '♣', '♠'])
     ])
def test_positive_to_list(string, result):
    res = StringUtils()
    assert res.to_list(string) == result


@pytest.mark.positive_to_list
@pytest.mark.parametrize('string, delimeter, result', [
    ('1:4:2', ":", ['1', '4', '2']),
    ('a:b:c', ":", ['a', 'b', 'c'])
    ])
def test_positive_to_list_2(string, delimeter, result):      # через :
    res = StringUtils()
    assert res.to_list(string, delimeter) == result


@pytest.mark.negative_to_list
@pytest.mark.parametrize('string, result', [
    ('', [])
    ])
def test_negative_to_list(string, result):
    res = StringUtils()
    assert res.to_list(string) == result


@pytest.mark.negative_to_list
@pytest.mark.xfail          # ожидается наличие :, но его нет > ошибка
@pytest.mark.parametrize('string, result', [
    ('1:5:4', ['1', '5', '4'])
    ])
def test_negative_to_list_2(string, result):
    res = StringUtils()
    assert res.to_list(string) == result


# contains
# Возвращает `True`, если строка содержит искомый символ
#  и `False` - если нет
@pytest.mark.positive_contains
@pytest.mark.parametrize('string, symbol, result', [
    ('Text', 'T', True),
    ('Тестовое', 'Тест', True),
    ('Test text', 'st', True),
    ('♣♦♠', '♦', True),
    ('458652', '5', True),
    ('Abc', '', True),
    ('', '', True)
])
def test_positive_contains(string, symbol, result):
    res = StringUtils()
    assert res.contains(string, symbol) == result


@pytest.mark.negative_contains
@pytest.mark.parametrize('string, symbol, result', [
    ('', 'N', False),
    ('Text', ' ', False),
    ('Нет', 'Да', False)
])
def test_negative_contains(string, symbol, result):
    res = StringUtils()
    assert res.contains(string, symbol) == result


# delete_symbol
# Удаляет все подстроки из переданной строки
@pytest.mark.positive_delete_symbol
@pytest.mark.parametrize('string, symbol, result', [
    ('Text', 'e', 'Txt'),
    ('Textext', 'ext', 'T'),
    ('Текст', 'Т', 'екст'),
    ('Правило №1', '№', 'Правило 1'),
    ('♦♣♠◘', '♠◘', '♦♣')
])
def test_positive_delete_symbol(string, symbol, result):
    res = StringUtils()
    assert res.delete_symbol(string, symbol) == result


@pytest.mark.negative_delete_symbol
@pytest.mark.parametrize('string, symbol, result', [
    ('Text', '', 'Text'),
    ('', 'Ь', '')
])
def test_negative_delete_symbol(string, symbol, result):
    res = StringUtils()
    assert res.delete_symbol(string, symbol) == result


# starts_with
# Возвращает `True`, если строка начинается
# с заданного символа и `False` - если нет
@pytest.mark.positive_starts_with
@pytest.mark.parametrize('string, symbol, result', [
    ('Test', 'T', True),
    ('123', '1', True),
    ('Абвгд', 'А', True),
    ('Обычный текст', 'О', True),
    ('Password', '', True)
])
def test_positive_stars_with(string, symbol, result):
    res = StringUtils()
    assert res.starts_with(string, symbol) == result


@pytest.mark.negative_starts_with
@pytest.mark.parametrize('string, symbol, result', [
    ('', 'F', False),
    ('Платформа', 'п', False),
    ('47856', ' ', False),
    ('321', '1', False),
    ('•♣', '♣', False),
])
def test_negative_stars_with(string, symbol, result):
    res = StringUtils()
    assert res.starts_with(string, symbol) == result


# end_with
# Возвращает `True`, если строка заканчивается
# заданным символом и `False` - если нет
@pytest.mark.positive_end_with
@pytest.mark.parametrize('string, symbol, result', [
    ('Test', 't', True),
    ('Тест', 'т', True),
    ('1235468', '8', True),
    ('..!$#', '#', True),
    ('Выключи свет', 'свет', True)
])
def test_positive_end_with(string, symbol, result):
    res = StringUtils()
    assert res.end_with(string, symbol) == result


@pytest.mark.negative_end_with
@pytest.mark.parametrize('string, symbol, result', [
    ('', 'A', False),
    ('1235468', '6', False),
    ('Tea', 'а', False),            # поиск русской буквы
    ('abcD', 'd', False),
    ('Текст текст', ' ', False)
])
def test_negative_end_with(string, symbol, result):
    res = StringUtils()
    assert res.end_with(string, symbol) == result


# # is_empty
# Возвращает `True`, если строка пустая и `False` - если нет
@pytest.mark.positive_is_empty
@pytest.mark.parametrize('string, result', [
    ('', True),
    (' ', True)
])
def test_positive_is_empty(string, result):
    res = StringUtils()
    assert res.is_empty(string) == result


@pytest.mark.negative_is_empty
@pytest.mark.parametrize('string, result', [
    ('123', False),
    ('•♣☻', False),
    ('Test test', False)
])
def test_negative_is_empty(string, result):
    res = StringUtils()
    assert res.is_empty(string) == result


# list_to_string
# Преобразует список элементов в строку с указанным разделителем
@pytest.mark.positive_list_to_string
@pytest.mark.parametrize('lst, result', [
    ([1, 2, 3, 4], '1, 2, 3, 4'),
    (['a', 'b', 'c', 'd'], 'a, b, c, d'),
    (['текст1', 'текст2', 'текст3'], 'текст1, текст2, текст3'),
    (['♣', '○'], '♣, ○'),
    (['Cfd456'], 'Cfd456')
])
def test_positive_list_to_string(lst,  result):
    res = StringUtils()
    assert res.list_to_string(lst) == result


@pytest.mark.positive_list_to_string    # через разделитель не по умолчанию
@pytest.mark.parametrize('lst, joiner, result', [
    ([1, 2, 36, 4], ':', '1:2:36:4'),
    (['Cat', 'Dog', 'Mouse'], ' - ', 'Cat - Dog - Mouse'),
    ([6, 5, 4, 7], '   ', '6   5   4   7')
])
def test_postive_list_to_string_2(lst, joiner, result):  # с joiner
    res = StringUtils()
    assert res.list_to_string(lst, joiner) == result


@pytest.mark.negative_list_to_string
@pytest.mark.parametrize('lst, result', [
    ([], ''),
    ('555, 444', '555, 444')
])
def test_negative_list_to_string(lst, result):
    res = StringUtils()
    assert res.list_to_string(lst) == result


@pytest.mark.negative_list_to_string                    # с joiner
@pytest.mark.parametrize('lst, joiner, result', [
    (['-'], ':', '-'),
    ([], '--', '')
])
def test_negative_list_to_string_2(lst, joiner, result):
    res = StringUtils()
    assert res.list_to_string(lst, joiner) == result
