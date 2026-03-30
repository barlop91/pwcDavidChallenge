import requests


def test_get_post_by_id():
    url = "https://jsonplaceholder.typicode.com/posts/1"

    response = requests.get(url)

    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    data = response.json()

    required_keys = ["userId", "id", "title", "body"]
    for key in required_keys:
        assert key in data, f"Missing key in response: {key}"

    assert data["id"] == 1, f"Expected id to be 1, but got {data['id']}"

    print("Positive API test passed")

### Agregue un test negativo para asegurarme
def test_get_invalid_post():
    url = "https://jsonplaceholder.typicode.com/posts/999999"

    response = requests.get(url)

###en caso de fallar mostraria el mensaje
    assert response.status_code == 404 or response.json() == {}, \
        f"Expected 404 or empty response, but got status {response.status_code} and body {response.text}"

    print("Negative API test passed")