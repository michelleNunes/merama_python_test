import unittest
from MockRediMethod import MockRedis
from unittest.mock import patch, MagicMock

class MyTestCase(unittest.TestCase):

    @patch("redis.StrictRedis")
    def RedisTest(self, mock_redis):
        redis_cache = {
            "access_key": "bar"
        }

        mock_redis_obj = MockRedis(redis_cache)
        mock_redis_method = MagicMock()
        mock_redis_method.get = Mock(side_effect=mock_redis_obj.get)
        mock_redis_method.set = Mock(side_effect=mock_redis_obj.set)

        mock_redis.return_value = mock_redis_method

if __name__ == '__main__':
    unittest.main("")
