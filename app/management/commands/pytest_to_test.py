from _pytest.config import ExitCode


class PytestTestRunner: # pragma: no cover
    """Runs pytest to discover and run tests."""

    def __init__(self, verbosity=1, failfast=False, keepdb=False, coverage=True, **kwargs) -> None:
        self.verbosity = verbosity
        self.failfast = failfast
        self.keepdb = keepdb
        self.coverage = coverage

    @classmethod
    def add_arguments(cls, parser) -> None:
        parser.add_argument(
            '--keepdb', action='store_true',
            help='Preserves the test DB between runs.'
        )
        
        parser.add_argument(
            '--coverage', action='store_true',
            help='Measure code coverage during test execution.'
        )

    def run_tests(self, test_labels, **kwargs) -> int | ExitCode:
        """Run pytest and return the exitcode.

        It translates some of Django's test command option to pytest's.
        """
        import pytest

        argv = []
        if self.verbosity == 0:
            argv.append('--quiet')
        if self.verbosity == 2:
            argv.append('--verbose')
        if self.verbosity == 3:
            argv.append('-vv')
        if self.failfast:
            argv.append('--exitfirst')
        if self.keepdb:
            argv.append('--reuse-db')
        if self.coverage:
            argv.append('--cov')

        argv.extend(test_labels)
        return pytest.main(argv)