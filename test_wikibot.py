from mylib.bot import scrape
from wikibot import cli
from click.testing import CliRunner

def test_scrape():
    assert 'Microsoft' in scrape('Microsoft')

def test_wikibot():
    runner = CliRunner()
    result = runner.invoke(cli, ['--name', 'Facebook', '--length','1'])
    assert result.exit_code == 0
    assert 'facebook' in result.output 