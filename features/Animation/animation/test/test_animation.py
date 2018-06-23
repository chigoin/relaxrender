import unittest
from features.animatiom.animation import Animation

class TestAnimation(unittest.TestCase):
    def test_main(self):
            t=Animation()
            t.main()
            assert True