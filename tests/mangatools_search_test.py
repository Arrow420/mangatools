from click.testing import CliRunner
import unittest
from mangatools.mangatools import mangatools

class MangaToolsSearchTests(unittest.TestCase):
    def test_search_title_kaguya_sama(self):
        title = 'kaguya-sama wa kokurasetai'
        runner = CliRunner()
        result = runner.invoke(mangatools, ['search', title])
        expected_title = 'kaguya-sama wa kokurasetai: tensai-tachi no renai zunousen'
        self.assertEqual(result.exit_code, 0)
        self.assertEqual(result.output.split("Title: ")[1].split("\n", 1)[0].lower().strip(), expected_title)
    
    def test_search_author_one_piece(self):
        title = 'one piece'
        runner = CliRunner()
        result = runner.invoke(mangatools, ['search', title])
        expected_author = 'oda eiichiro'
        self.assertEqual(result.exit_code, 0)
        self.assertEqual(result.output.split("Author: ")[1].split("Artist: ")[0].lower().strip(), expected_author)
    
    def test_search_title_incorrect(self):
        runner = CliRunner()
        result = runner.invoke(mangatools, ['search', 'jkwgwgjwyufhjksdq'])
        self.assertNotEqual(result.exit_code, 0)
        #self.assertEqual(result.output.split("')",  1)[1], "\n\n\nCouldn't find any results\n")

if __name__ == '__main__':
    unittest.main(argv=[''],verbosity=2, exit=False)