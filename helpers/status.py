#!/usr/bin/env python3

# Helper script for status printing
import sys
from argparse import ArgumentParser

from common import Icon, Language, Level, add_common_args, capture_cmd, get_name_and_target, get_stamp, pretty_print


def main(args: list) -> int:
    # Parse args
    parser = ArgumentParser(description="Helper script for status printing")
    add_common_args(parser)
    parser.add_argument("-s", "--status", required=True, help="Status to be displayed")
    parser.add_argument("-l", "--level", type=Level, default=Level.INFO, help="Color level")
    parser.add_argument("-i", "--icon", type=Icon, required=True, help="Displayed emoji")
    parser.add_argument("--lang", type=Language, default=None, help="Language (if applicable)")
    args, cmd = parser.parse_known_args(args)

    # Reckon project name and target
    name, target = get_name_and_target(args)

    # Get time
    stamp = get_stamp()

    # Print status
    pretty_print(stamp, args.icon, name, target, args.level, args.status, language=args.lang)

    # Is there something to run?
    if len(cmd) > 0:
        return capture_cmd(args, cmd, stamp)
    return 0


if __name__ == "__main__":  # pragma: no cover
    sys.exit(main(sys.argv[1:]))
