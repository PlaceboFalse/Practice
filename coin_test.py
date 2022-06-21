from unittest import TestCase, main
from coin_task import Searching


class CoinTest(TestCase):

    def test_found_amount_in_coin(self):
        self.assertEqual(Searching.amount_in_coin(100), [100])
        self.assertEqual(Searching.amount_in_coin(137), [1, 1, 10, 25, 100])
        self.assertEqual(Searching.amount_in_coin(4), [1, 1, 1, 1])
        self.assertEqual(Searching.amount_in_coin(50), [25, 25])

    def test_not_been_found_amount_in_coin(self):
        self.assertEqual(Searching.amount_in_coin(0), 0)
        self.assertEqual(Searching.amount_in_coin(-1), 0)


if __name__ == '__main__':
    main()
