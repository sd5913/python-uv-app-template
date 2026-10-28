import unittest

from main import add_signal, capped_position


class InteractionTests(unittest.TestCase):
    def test_signal_counter_increases_once(self):
        self.assertEqual(add_signal(0), 1)
        self.assertEqual(add_signal(3), 4)

    def test_position_stays_in_window(self):
        self.assertEqual(capped_position(-10, 900, 800, 500), (0, 499))
        self.assertEqual(capped_position(25, 35, 800, 500), (25, 35))


if __name__ == '__main__':
    unittest.main()
