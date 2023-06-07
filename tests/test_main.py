from starlette.testclient import TestClient


def test_hello_endpoint(testclient: TestClient):
    response = testclient.get("/hello")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_get_item(testclient: TestClient):
    response = testclient.get("/item/foo")
    assert response.status_code == 200
    assert response.json() == {"name": "foof", "price": 19.99, "is_offer": True}


def test_add_item(testclient: TestClient):
    response = testclient.post(
        "/item", json={"name": "foo", "price": 19.99, "is_offer": True}
    )
    assert response.status_code == 200
    response_list = testclient.get("/items")
    assert response_list.json() == [{"name": "foo", "price": 19.99, "is_offer": True}]
