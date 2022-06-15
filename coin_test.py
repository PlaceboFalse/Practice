from unittest import TestCase, main
from coin_task import find_coin


class coin_test(TestCase):

    def test_correct(self):
        self.assertEqual(find_coin(100), [100])
        self.assertEqual(find_coin(137), [1, 1, 10, 25, 100])
        self.assertEqual(find_coin(4), [1, 1, 1, 1])
        self.assertEqual(find_coin(50), [25, 25])

    def test_wa(self):
        self.assertEqual(find_coin(0), 0)
        self.assertEqual(find_coin(-1), 0)


if __name__ == '__main__':
    main()
