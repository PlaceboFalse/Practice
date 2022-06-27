from unittest import TestCase, main
from archiver import Archiver


class ArchiveTest(TestCase):

    def test_archive(self):
        self.assertEqual(Archiver.zip_line('aaaaffff'), 'af')

    def test_unzip(self):
        key = []
        key.append([0, 1, 2, 3])
        key.append([4, 5, 6, 7])

        self.assertEqual(Archiver.unzip('af', key), 'aaaaffff')


if __name__ == "__main__":
    main()
