import unittest

from keypop.lib import get_key, get_all_keys
from keypop.commands import add, remove

class Testlib(unittest.TestCase):
    def test_get_key_exists(self):
        add(name="example", key="test_value")
        assert get_key(name="example") == "test_value"
        remove("example")
    
    def test_get_key_missing(self):
        assert get_key(name="nonexistent") is None
    
    def test_get_all_keys_return_dict(self):
        assert isinstance(get_all_keys(), dict)


if __name__ == "__main__":
    unittest.main()