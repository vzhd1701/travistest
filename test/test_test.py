import unittest
import requests

class TestBoop(unittest.TestCase):
    def test_root(self):
        r = requests.get("https://ipinfo.io/ip")
        print(r.content)

if __name__ == "__main__":
    unittest.main()
