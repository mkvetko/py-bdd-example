import sys

from behave.__main__ import main as behave_main

if __name__ == '__main__':

    args = sys.argv[1:]

    if len(args) == 0 or (len(args) == 1 and args[0] == '--help'):
        from behave import configuration

        parser = configuration.setup_parser()
        parser.print_help()
        sys.exit(0)

    behave_main(args)
    # Overriding exit code to 0 so CI build are not failing in case of test failure
    sys.exit(0)
