import requests


def test_check_status():
    r = requests.get("http://localhost:8080/check_status").json()
    assert "status" in r
    assert len(r["status"]) > 0
