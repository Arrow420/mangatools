from click.testing import CliRunner
import unittest
from mangatools.mangatools import mangatools

class MangaToolsSearchTests(unittest.TestCase):    
    def test_search_title_kaguya_sama(self):
        title = 'kaguya-sama'
        runner = CliRunner()
        result = runner.invoke(mangatools, ['search', title, '--no-covers', '--no-details', '--no-logo'])
        expected_title = 'kaguya-sama wa kokurasetai: tensai-tachi no renai zunousen'
        self.assertEqual(result.exit_code, 0)
        self.assertEqual(result.output.split("\n")[0].lower(), expected_title)
    
    def test_search_author_one_piece(self):
        title = 'one piece'
        runner = CliRunner()
        result = runner.invoke(mangatools, ['search', title, '--no-covers', '--no-details', '--no-logo'])
        expected_author = 'oda eiichiro'
        self.assertEqual(result.exit_code, 0)
        self.assertEqual(result.output.split("Author: ")[1].split("Artist: ")[0].lower().strip(), expected_author)
    
    def test_search_title_incorrect(self):
        runner = CliRunner()
        result = runner.invoke(mangatools, ['search', 'jkwgwhjksdq', '--no-covers', '--no-details', '--no-logo'])
        self.assertNotEqual(result.exit_code, 0)
        self.assertEqual(result.output, '\nERROR: Incorrect title\n')

if __name__ == '__main__':
    unittest.main()