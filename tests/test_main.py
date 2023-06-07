from starlette.testclient import TestClient


def test_hello_endpoint(testclient: TestClient):
    response = testclient.get("/hello")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_get_item(testclient: TestClient):
    response = testclient.get("/item/foo")
    assert response.status_code == 200
    assert response.json() == {"name": "foo", "price": 19.99, "is_offer": True}


def test_add_item(testclient: TestClient):
    response = testclient.post(
        "/item", json={"name": "foo", "price": 19.99, "is_offer": True}
    )
    assert response.status_code == 200
    response_list = testclient.get("/items")
    assert response_list.json() == [{"name": "foo", "price": 19.99, "is_offer": True}]


def test_list_items(testclient: TestClient):
    response = testclient.post(
        "/item", json={"name": "foo1", "price": 19.99, "is_offer": True}
    )
    assert response.status_code == 200
    response = testclient.post(
        "/item", json={"name": "foo2", "price": 19.99, "is_offer": True}
    )
    assert response.status_code == 200
    response = testclient.get("/items")
    assert response.status_code == 200
    items_list = response.json()
    assert items_list is not None
    assert {"name": "foo1", "price": 19.99, "is_offer": True} in items_list
    assert {"name": "foo2", "price": 19.99, "is_offer": True} in items_list
