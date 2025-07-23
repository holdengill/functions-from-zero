from mylib.bot import scrape
import click

@click.command()
@click.option('--name', prompt='Wikipedia page to scrape',
              help='Web page we want to scrape')
@click.option('--length',help='length of output for wikibot')
def cli(name='Microsoft',length=1):
    result = scrape(name, length=length)
    click.echo(click.style(f"{result}", bg="green",fg="red"))

if __name__ == '__main__':
    cli()