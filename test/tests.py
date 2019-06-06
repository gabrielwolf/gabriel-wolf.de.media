import os
from unittest import TestCase

from src.convert_txt_to_html_to_json import convert_txt_to_html_to_json
from src.main import sane_file_extensions, sane_file_naming_schema, Media, write_json, read_json


def create_media_object(**kwargs):
    print(kwargs)
    try:
        Media(**kwargs)
        return True
    except KeyError:
        print("Could not instantiate media object")
        return False
    except ValueError:
        print("Could not instantiate media object")
        return False


class MediaObjectTests(TestCase):

    def test_create_media_object_positive(self):
        print("--> ", self._testMethodName)
        self.assertTrue(create_media_object(date="2019-06-02", time="15-16-02", title="Tagebuch"))

    def test_create_media_object_no_date_negative(self):
        print("--> ", self._testMethodName)
        self.assertFalse(create_media_object(time="15-16-02", title="Tagebuch"))

    def test_create_media_object_no_time_positive(self):
        print("--> ", self._testMethodName)
        self.assertTrue(create_media_object(date="2019-06-02", title="Tagebuch"))

    def test_create_media_object_wrong_date(self):
        print("--> ", self._testMethodName)
        self.assertFalse(create_media_object(date="2019-22-22", time="15-16-02", title="Tagebuch"))

    def test_create_media_object_wrong_time(self):
        print("--> ", self._testMethodName)
        self.assertFalse(create_media_object(date="2019-12-22", time="55-16-02", title="Tagebuch"))

    def test_create_media_object_more_data_positive(self):
        print("--> ", self._testMethodName)
        self.assertTrue(create_media_object(date="2019-12-02", time="15-16-02", title="Tagebuch", class_name="blue"))


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

    def test_sane_file_naming_schema_date_positive(self):
        print("--> ", self._testMethodName)
        self.assertTrue(sane_file_naming_schema(['2019-05-27_Sonnenuntergang in Petershausen.jpg']))
        print("")

    def test_sane_file_naming_schema_date_negative(self):
        print("--> ", self._testMethodName)
        self.assertFalse(sane_file_naming_schema(['2019-99-27_Sonnenuntergang in Petershausen.jpg']))
        print("")

    def test_sane_file_naming_schema_datetime_positive(self):
        print("--> ", self._testMethodName)
        self.assertTrue(sane_file_naming_schema(['2019-05-27_20-41-36_Sonnenuntergang in Petershausen.jpg']))
        print("")

    def test_sane_file_naming_schema_datetime_negative(self):
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

    def tearDown(self):
        if os.path.isfile("test.json"):
            os.remove("test.json")


class ConvertTxtToHtmlToJsonTests(TestCase):

    def test_convert_txt_to_html_to_json_positive(self):
        print("--> ", self._testMethodName)
        text = "Lorem ipsum dolor sit amet.\nNeue Zeile.\n    Zeile mit 4 Leerzeichen\n   Zeile mit drei Leerzeichen."
        with open("test.txt", "w") as file:
            file.write(text)
        convert_txt_to_html_to_json("test.txt", "test.json")
        self.assertTrue(read_json("test.json"))
        print("")

    def tearDown(self):
        if os.path.isfile("test.txt"):
            os.remove("test.txt")
        if os.path.isfile("test.json"):
            os.remove("test.json")
