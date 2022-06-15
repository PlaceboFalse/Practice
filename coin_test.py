from unittest import TestCase, main
from coin_task import find_coin


class coin_test():
    def test(self):
        self.assertEqual(find_coin(100), [100])


if __name__ == '__main__':
    main()
