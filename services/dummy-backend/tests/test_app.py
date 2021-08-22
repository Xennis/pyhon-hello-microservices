import unittest

from fastapi.testclient import TestClient

from dummy_backend.main import app


class TestApp(unittest.TestCase):
    def test_user_data(self):
        client = TestClient(app)
        resp = client.get("/user/?id=dummy-123")
        self.assertEqual(200, resp.status_code, msg="status code")
        self.assertEqual(
            "application/json", resp.headers["Content-Type"], msg="header content-type"
        )
        self.assertEqual({"age": 34, "name": "Tony"}, resp.json(), msg="data")


if __name__ == "__main__":
    unittest.main()
