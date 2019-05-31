from unittest import TestCase

from src.main import sane_file_extensions, sane_file_naming_schema


class FileNamingTests(TestCase):

    def test_sane_file_extensions_positive(self):
        self.assertIs(sane_file_extensions(['test.txt'], ['.txt']), True)

    def test_sane_file_extensions_negative(self):
        self.assertIs(sane_file_extensions(['test.exe'], ['.txt']), False)

    def test_sane_file_extensions_many_extensions_positive(self):
        self.assertIs(sane_file_extensions(['test.txt', 'test.jpg'], ['.txt', '.jpg']), True)

    def test_sane_file_extensions_many_extensions_negative(self):
        self.assertIs(sane_file_extensions(['test.exe'], ['.txt', '.jpg']), False)

    def test_sane_file_naming_schema_simple_positive(self):
        self.assertIs(sane_file_naming_schema(['2019-05-27_Sonnenuntergang in Petershausen.jpg']), True)

    def test_sane_file_naming_schema_simple_negative(self):
        self.assertIs(sane_file_naming_schema(['2019-99-27_Sonnenuntergang in Petershausen.jpg']), False)

    def test_sane_file_naming_schema_extended_positive(self):
        self.assertIs(sane_file_naming_schema(['2019-05-27_20-41-36_Sonnenuntergang in Petershausen.jpg']), True)

    def test_sane_file_naming_schema_extended_negative(self):
        self.assertIs(sane_file_naming_schema(['2019-05-27_29-99-36_Sonnenuntergang in Petershausen.jpg']), False)

    def test_sane_file_naming_schema_more_underscores_no_problem(self):
        self.assertIs(sane_file_naming_schema(['2019-05-27_21-50-36_Sonnenuntergang in Petershausen_schön.jpg']), True)

    def test_sane_file_naming_schema_startswith_underscore_negative(self):
        self.assertIs(sane_file_naming_schema(['_2019-05-27_21-50-36_Sonnenuntergang in Petershausen_schön.jpg']),
                      False)
