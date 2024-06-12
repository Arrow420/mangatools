from click.testing import CliRunner
import unittest
from mangatools import mangatools

class MangaToolsSearchTests(unittest.TestCase):
    def test_search_title_solanin(self):
        title = 'solanin'
        runner = CliRunner()
        result = runner.invoke(mangatools, ['search', title], prog_name='solanin')
        expected_title = 'solanin'
        self.assertEqual(result.exit_code, 0)
        self.assertEqual(result.output.split("Title: ")[1].split("\n", 1)[0].lower().strip(), expected_title)
    
    def test_search_author_one_piece(self):
        title = 'one piece'
        runner = CliRunner()
        result = runner.invoke(mangatools, ['search', title], prog_name='one piece')
        expected_author = 'oda eiichiro'
        self.assertEqual(result.exit_code, 0)
        self.assertEqual(result.output.split("Author: ")[1].split("Artist: ")[0].lower().strip(), expected_author)
    
    def test_search_title_incorrect(self):
        runner = CliRunner()
        result = runner.invoke(mangatools, ['search', 'jkwgwgjwyufhjksdq'], prog_name='incorrect title')
        self.assertNotEqual(result.exit_code, 0)

if __name__ == '__main__':
    unittest.main(argv=[''],verbosity=2, exit=False)