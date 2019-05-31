import os
import shutil
from unittest import TestCase

from src.main import dir_sane_file_extensions, dir_sane_file_naming_schema

test_directory = './test/'


def fill_a_test_directory(directory, test_file_names: list):
    if not os.path.exists(directory):
        os.makedirs(directory)
    test_file_names = map(lambda file: directory + file, test_file_names)
    # Write empty files to disk
    for file in test_file_names:
        open(file, 'a').close()


def rm_a_test_directory(directory):
    shutil.rmtree(directory)


class MediaFilesTests(TestCase):

    def test_dir_sane_file_extensions_positive(self):
        fill_a_test_directory(test_directory, ['test.txt'])
        self.assertIs(dir_sane_file_extensions(test_directory, ['.txt']), True)
        rm_a_test_directory(test_directory)

    def test_dir_sane_file_extensions_negative(self):
        fill_a_test_directory(test_directory, ['test.exe'])
        self.assertIs(dir_sane_file_extensions(test_directory, ['.txt']), False)
        rm_a_test_directory(test_directory)

    def test_dir_sane_file_extensions_dotfiles_dont_matter(self):
        fill_a_test_directory(test_directory, ['.DS_Store'])
        self.assertIs(dir_sane_file_extensions(test_directory, ['.txt']), True)
        rm_a_test_directory(test_directory)

    def test_dir_sane_file_extensions_many_extensions_positive(self):
        fill_a_test_directory(test_directory, ['test.txt', 'test.jpg'])
        self.assertIs(dir_sane_file_extensions(test_directory, ['.txt', '.jpg']), True)
        rm_a_test_directory(test_directory)

    def test_dir_sane_file_extensions_many_extensions_negative(self):
        fill_a_test_directory(test_directory, ['test.exe'])
        self.assertIs(dir_sane_file_extensions(test_directory, ['.txt', '.jpg']), False)
        rm_a_test_directory(test_directory)

    def test_dir_sane_file_naming_schema_simple_positive(self):
        fill_a_test_directory(test_directory, ['2019-05-27_Sonnenuntergang in Petershausen.jpg'])
        self.assertIs(dir_sane_file_naming_schema(test_directory), True)
        rm_a_test_directory(test_directory)

    def test_dir_sane_file_naming_schema_simple_negative(self):
        fill_a_test_directory(test_directory, ['2019-23-27_Sonnenuntergang in Petershausen.jpg'])
        self.assertIs(dir_sane_file_naming_schema(test_directory), False)
        rm_a_test_directory(test_directory)

    def test_dir_sane_file_naming_schema_extended_positive(self):
        fill_a_test_directory(test_directory, ['2019-05-27_20-41-36_Sonnenuntergang in Petershausen.jpg'])
        self.assertIs(dir_sane_file_naming_schema(test_directory), True)
        rm_a_test_directory(test_directory)

    def test_dir_sane_file_naming_schema_extended_negative(self):
        fill_a_test_directory(test_directory, ['2019-05-27_29-99-36_Sonnenuntergang in Petershausen.jpg'])
        self.assertIs(dir_sane_file_naming_schema(test_directory), False)
        rm_a_test_directory(test_directory)

    def test_dir_sane_file_naming_schema_more_underscores_no_problem(self):
        fill_a_test_directory(test_directory, ['2019-05-27_29-99-36_Sonnenuntergang in Petershausen_schön.jpg'])
        self.assertIs(dir_sane_file_naming_schema(test_directory), True)
        rm_a_test_directory(test_directory)
