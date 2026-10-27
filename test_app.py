import json
import threading
import unittest
from http.server import HTTPServer
from urllib.request import urlopen

from app import AppHandler


class TestDeploymentApp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.server = HTTPServer(("127.0.0.1", 0), AppHandler)

        cls.server_thread = threading.Thread(
            target=cls.server.serve_forever,
            daemon=True
        )
        cls.server_thread.start()

        cls.base_url = f"http://127.0.0.1:{cls.server.server_port}"

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.server_thread.join()

    def test_health_endpoint(self):
        with urlopen(f"{self.base_url}/health") as response:
            data = json.loads(response.read().decode())

            self.assertEqual(response.status, 200)
            self.assertEqual(data["status"], "healthy")
            self.assertEqual(data["application"], "deployment-demo")


if __name__ == "__main__":
    unittest.main()
