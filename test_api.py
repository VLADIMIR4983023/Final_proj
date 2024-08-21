import requests
import allure

# объявляем переменные

token = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3VzZXItcmlnaHQiLCJzdWIiOjIwOTMwOTMwLCJpYXQiOjE3MjQyMTcyMTQsImV4cCI6MTcyNDIyMDgxNCwidHlwZSI6MjB9.57xaVa2lLpATTdSDNmRDgHJtDVI7OppNZLqetQo00ZY
base_URL = 'https://web-gate.chitai-gorod.ru/api/v1'


def test_search_name():
    """
        Поиск книги по названию
    """
    with allure.step("передать токен"):
        headers = {'authorization': token}
    response = requests.get(
        base_URL + '/recommend/semantic?phrase=алые%20паруса', headers=headers)
    with allure.step("проверка статус кода"):
        assert response.status_code == 200
    print("Тест успешно отработан!")


def test_searh_id():
    """
        Поиск книги по ID
    """
    with allure.step("передать токен"):
        headers = {'authorization': token}
    response = requests.get(base_URL + '/products/slug/alye-parusa-2505205',
                            headers=headers)
    with allure.step("проверка статус кода"):
        assert response.status_code == 200



def test_add_book_v_korz():
    """
        Добавление книги в корзину
    """
    with allure.step("передать токен"):
        headers = {'authorization': token}
    body = {"id": 2505205}
    response = requests.post(base_URL + '/cart/product', headers=headers,
                             json=body)
    with allure.step("проверка статус кода"):
        assert response.status_code == 200


def test_clear_korz():
    """
        Очистка корзины
    """
    with allure.step("передать токен"):
        headers = {'authorization': token}
    response = requests.delete(base_URL + '/cart', headers=headers)
    with allure.step("проверка статус кода"):
        assert response.status_code == 204


def test_lich_dan():
    """
        Получение личных данных пользователя
    """
    with allure.step("передать токен"):
        headers = {'authorization': token}
    response = requests.get(base_URL + '/profile/personal-data',
                            headers=headers)
    with allure.step("проверка статус кода"):
        assert response.status_code == 200


