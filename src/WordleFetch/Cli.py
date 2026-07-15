import sys
import logging
import argparse
import datetime
from .Theme import *
from .Wordle import fetch_wordle_data
from importlib.metadata import version, PackageNotFoundError
logger = logging.getLogger("WordleFetch")

running_as_main = False

def main():
    parser = argparse.ArgumentParser(
        description="WordleFetch\nget the answers\nyou want quickly.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        prog="wordlefetch"
    )
    display_flags = parser.add_argument_group("Display Flags (can be used more than once!)")
    Configuration_flags = parser.add_argument_group("Advanced configuration flags")
    Misc_Flags = parser.add_argument_group("Miscellaneous flags")
    
    Misc_Flags.add_argument(
            "-V", "--version",
            action="store_true",
            help="Shows installed\nWordleFetch package\nversion and exits"
    )
    Configuration_flags.add_argument(
            "-u", "--url",
            action="store",
            help="Allows using a\ndifferent url instead\nof normal url."
    )
    Configuration_flags.add_argument(
            "-d", "--customdate",
            action="store",
            help="Allows using a\ndifferent date instead\nof todays date."
    )
    display_flags.add_argument(
            "-H", "--header",
            action="append_const",
            dest="displayflags",
            const="header",
            help="Adds showing\nthe header"
    )
    display_flags.add_argument(
            "-A", "--answer",
            action="append_const",
            dest="displayflags",
            const="answer",
            help="Adds showing\nthe Wordle answer"
    )
    display_flags.add_argument(
            "-D", "--date-display",
            action="append_const",
            dest="displayflags",
            const="date",
            help="Adds showing\nthe date"
    )
    display_flags.add_argument(
            "-E", "--editor",
            action="append_const",
            dest="displayflags",
            const="editor",
            help="Adds showing\nthe Wordle editor"
    )
    display_flags.add_argument(
            "-I", "--id",
            action="append_const",
            dest="displayflags",
            const="id",
            help="Adds showing\nthe Wordle ID"
    )
    display_flags.add_argument(
            "-L", "--launch",
            action="append_const",
            dest="displayflags",
            const="days_since_launch",
            help="Adds showing\ndays since\nWordle launch"
    )


    args = parser.parse_args()

    if args.version:
        try:
            package_version = version('WordleFetch')
            print(package_version)
            sys.exit(0)
        except PackageNotFoundError:
            logger.error(
                "Error: Pip package not found. To resolve this error, "
                "please install the package from PyPI with: "
                "pip install WordleFetch"
            )
            if running_as_main:
                sys.exit(1)
            else:
                pass
    if args.customdate:
        entered_date = datetime.datetime.strptime(args.customdate, "%Y-%m-%d").date()
    else:
        entered_date = datetime.date.today()

    if args.url:
        entered_url = args.url
    else:
        entered_url = f'https://www.nytimes.com/svc/wordle/v2/{entered_date:%Y-%m-%d}.json'
    
    data_fetch = fetch_wordle_data(date=entered_date, url=entered_url)

    if not args.displayflags:
        args.displayflags = ['header', 'answer', 'date', 'editor']
    for item in args.displayflags:
        print(data_fetch[item])
if __name__ == "__main__":
    main()
    running_as_main = True