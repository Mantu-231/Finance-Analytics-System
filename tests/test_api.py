import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))


from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)



def test_home():

    response = client.get("/")

    assert response.status_code == 200

    assert response.json() == {
        "message": "Finance Analytics API Running"
    }



def test_get_transactions():

    response = client.get("/transactions")

    assert response.status_code == 200

    assert isinstance(response.json(), list)



def test_get_analytics():

    response = client.get("/analytics")

    assert response.status_code == 200

    data = response.json()

    assert "total_income" in data
    assert "total_expense" in data
    assert "savings" in data