from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)



def get_token():

    response = client.post(
        "/login",
        data={
            "username": "mantu2@gmail.com",
            "password": "123456"
        }
    )

    return response.json()["access_token"]




def test_home():

    response = client.get("/")

    assert response.status_code == 200

    assert response.json() == {
        "message": "Finance Analytics API Running"
    }




def test_get_transactions():

    token = get_token()

    response = client.get(
        "/transactions",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 200

    assert isinstance(response.json(), list)




def test_get_analytics():

    token = get_token()

    response = client.get(
        "/analytics",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )


    assert response.status_code == 200

    data = response.json()

    assert "total_income" in data
    assert "total_expense" in data
    assert "savings" in data