from click.testing import CliRunner
import unittest
import mangatools

class MangaToolsSearchTests(unittest.TestCase):
    def test_search_title_solanin(self):
        title = 'solanin'
        runner = CliRunner()
        result = runner.invoke(mangatools, ['search', title], prog_name='Mangatools')
        expected_title = 'solanin'
        self.assertEqual(result.exit_code, 0)
        self.assertEqual(result.output.split("Title: ")[1].split("\n", 1)[0].lower().strip(), expected_title)
    
    def test_search_author_one_piece(self):
        title = 'one piece'
        runner = CliRunner()
        result = runner.invoke(mangatools, ['search', title], prog_name='Mangatools')
        expected_author = 'oda eiichiro'
        self.assertEqual(result.exit_code, 0)
        self.assertEqual(result.output.split("Author: ")[1].split("Artist: ")[0].lower().strip(), expected_author)
    
    def test_search_title_incorrect(self):
        title = 'jkwgwgjwyufhjksdq'
        runner = CliRunner()
        result = runner.invoke(mangatools, ['search', title], prog_name='Mangatools')
        self.assertNotEqual(result.exit_code, 0)

if __name__ == '__main__':
    unittest.main(argv=[''],verbosity=2, exit=False)