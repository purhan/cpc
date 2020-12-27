import click
import yaml
from click_aliases import ClickAliasedGroup

from .utils import solution_tester, submission_scraper


def CommandWithConfigFile(config_file_param_name):
    """
    Adds ability to import options/arguments from a file
    NOTE: Do not use `default` with this in decorator
    """

    class CustomCommandClass(click.Command):
        def invoke(self, ctx):
            try:
                config_file = ctx.params[config_file_param_name]
            except:
                return
            if config_file is not None:
                with open(config_file) as f:
                    config_data = yaml.safe_load(f)
                    for param, value in ctx.params.items():
                        if value is None and param in config_data:
                            ctx.params[param] = config_data[param]

            return super(CustomCommandClass, self).invoke(ctx)

    return CustomCommandClass


@click.group(
    cls=ClickAliasedGroup, context_settings=dict(help_option_names=["-h", "--help"])
)
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


@main.command("scrape")
def scrape():
    """
    Start interactive solution scraper
    """
    submission_scraper.main()


@main.command(
    cls=CommandWithConfigFile("config_file"), name="stress_test", aliases=["st", "test"]
)
@click.option("--count", "-c")
@click.option("--precommand", "-p")
@click.option("--no_halt", "-nh")
@click.option("--bruteforce", "-b", type=click.Path())
@click.option("--optimized", "-o", type=click.Path())
@click.option("--testcase_generator", "-tg", type=click.Path())
@click.option("--config_file", "-cf", type=click.Path(), default=".cpcrc")
def test(precommand, *args, **kwargs):
    """
    Stress test a solution against bruteforce
    """
    solution_tester.main(precommand, *args, **kwargs)


if __name__ == "__main__":
    main()
