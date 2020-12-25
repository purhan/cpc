import click
from click_aliases import ClickAliasedGroup
from .utils import (
    submission_scraper,
    solution_tester,
)


@click.group(cls=ClickAliasedGroup, context_settings=dict(help_option_names=["-h", "--help"]))
def main():
    """
    \b
      _________  _____
     / ___/ __ \/ ___/
    / /__/ /_/ / /__  
    \___/ .___/\___/  
       /_/            

    CPC is a command-line utility
    aimed towards competitive programmers.
    """
    pass


@main.command('scrape')
def scrape():
    """
    Start interactive solution scraper
    """
    submission_scraper.main()


@main.command(name='stress_test', aliases=['st', 'test'])
@click.option('--input', '-i', required=True)
@click.option('--count', '-c', default=10)
def test(*args, **kwargs):
    """
    Stress test a solution against bruteforce
    """
    solution_tester.main(*args, **kwargs)


if __name__ == "__main__":
    main()
