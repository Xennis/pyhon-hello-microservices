import unittest

from fastapi.testclient import TestClient

from dummy_api.main import app


class TestApp(unittest.TestCase):
    def test_user_profile(self):
        # TODO: Mock backend and re-add tests
        pass
        # client = TestClient(app)
        # resp = client.get("/user/dummy-1234/profile")
        # self.assertEqual(200, resp.status_code, msg="status code")
        # self.assertEqual(
        #    "application/json", resp.headers["Content-Type"], msg="header content-type"
        # )
        # self.assertEqual({"user_id": "dummy-1234"}, resp.json(), msg="data")


if __name__ == "__main__":
    unittest.main()
