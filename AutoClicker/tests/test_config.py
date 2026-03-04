import unittest
from config_manager import ConfigManager

class TestConfigManager(unittest.TestCase):
    
    def test_set_and_get(self):
        config = ConfigManager("test_config.json")
        config.set("speed", 2.0)
        self.assertEqual(config.get("speed"), 2.0)