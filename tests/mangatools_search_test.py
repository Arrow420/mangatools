from click.testing import CliRunner
import unittest
from mangatools.cli import mangatools
from mangatools.commands import manga_search

class MangaToolsSearchTests(unittest.TestCase):
    def test_search_title_solanin(self):
        title = 'solanin'
        runner = CliRunner()
        result = runner.invoke(mangatools, ['search', title], prog_name='Mangatools')
        print(result.output.split("Title: ")[1])
        title = result.output.split("Title: ")[1].split("\n", 1)[0].lower().strip()
        expected_title = 'solanin'
        self.assertEqual(result.exit_code, 0)
        self.assertEqual(title, expected_title)
    
    def test_search_author_chainsaw_man(self):
        title = 'chainsaw man'
        runner = CliRunner()
        result = runner.invoke(mangatools, ['search', title], prog_name='Mangatools')
        author = result.output.split("Author: ")[1].split("Artist: ")[0].lower().strip()
        expected_author = 'fujimoto tatsuki'
        self.assertEqual(result.exit_code, 0)
        self.assertEqual(author, expected_author)
    
    def test_search_title_incorrect(self):
        title = 'jkwgwgjwyufhjksdqwio829y8wdioadjio32y83kkn'
        runner = CliRunner()
        result = runner.invoke(mangatools, ['search', title], prog_name='Mangatools')
        self.assertNotEqual(result.exit_code, 0)

if __name__ == '__main__':
    unittest.main(argv=[''],verbosity=2, exit=False)