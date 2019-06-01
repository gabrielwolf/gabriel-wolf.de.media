from unittest import TestCase

from src.main import sane_file_extensions, sane_file_naming_schema, Media


class MediaObjectTests(TestCase):
    def test_create_media_object_positive(self):
        print("--> ", self._testMethodName)
        self.assertTrue(Media("2019-06-02", "15-16-02", "Tagebuch"))

    def test_create_media_object_negative(self):
        t = Media("2019-22-02", "15-16-02", "Tagebuch")
        self.assertRaises(ValueError)


class FileNamingTests(TestCase):

    def test_sane_file_extensions_positive(self):
        print("--> ", self._testMethodName)
        self.assertTrue(sane_file_extensions(['test.txt'], ['.txt']))
        print("")

    def test_sane_file_extensions_negative(self):
        print("--> ", self._testMethodName)
        self.assertFalse(sane_file_extensions(['test.exe'], ['.txt']))
        print("")

    def test_sane_file_extensions_many_extensions_positive(self):
        print("--> ", self._testMethodName)
        self.assertTrue(sane_file_extensions(['test.txt', 'test.jpg'], ['.txt', '.jpg']))
        print("")

    def test_sane_file_extensions_many_extensions_negative(self):
        print("--> ", self._testMethodName)
        self.assertFalse(sane_file_extensions(['test.exe'], ['.txt', '.jpg']))
        print("")

    def test_sane_file_naming_schema_simple_positive(self):
        print("--> ", self._testMethodName)
        self.assertTrue(sane_file_naming_schema(['2019-05-27_Sonnenuntergang in Petershausen.jpg']))
        print("")

    def test_sane_file_naming_schema_simple_negative(self):
        print("--> ", self._testMethodName)
        self.assertFalse(sane_file_naming_schema(['2019-99-27_Sonnenuntergang in Petershausen.jpg']))
        print("")

    def test_sane_file_naming_schema_extended_positive(self):
        print("--> ", self._testMethodName)
        self.assertTrue(sane_file_naming_schema(['2019-05-27_20-41-36_Sonnenuntergang in Petershausen.jpg']))
        print("")

    def test_sane_file_naming_schema_extended_negative(self):
        print("--> ", self._testMethodName)
        self.assertFalse(sane_file_naming_schema(['2019-05-27_29-99-36_Sonnenuntergang in Petershausen.jpg']))
        print("")

    def test_sane_file_naming_schema_more_underscores_no_problem(self):
        print("--> ", self._testMethodName)
        self.assertTrue(sane_file_naming_schema(['2019-05-27_21-50-36_Sonnenuntergang in Petershausen_schön.jpg']))
        print("")

    def test_sane_file_naming_schema_startswith_underscore_negative(self):
        print("--> ", self._testMethodName)
        self.assertFalse(sane_file_naming_schema(['_2019-05-27_21-50-36_Sonnenuntergang in Petershausen_schön.jpg']))
        print("")

    def test_write_json_positive(self):
        print("--> ", self._testMethodName)
        self.assertTrue(write_json(['2019-05-27_Sonnenuntergang in Petershausen.jpg'], "test.json"))
        print("")
