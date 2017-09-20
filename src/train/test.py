# -*- coding: utf-8 -*-

import sys

from nose.core import run
from nose.loader import TestLoader


def run_test():
    try:
        loader = TestLoader()

        run(
            argv=[
                "--nocapture",
                "--nologcapture",
                "--where=/root/tests",
                "--with-coverage",
                "--cover-erase",
                "--cover-package=/root/src/train",
                "--cover-xml",
                "--cover-xml-file=/root/tests/results/coverage.xml",
                "--with-xunit",
                "--xunit-file=/root/tests/results/nosetests.xml"
            ],
            testLoader=loader
        )
    except (KeyboardInterrupt):
        sys.exit(0)


if __name__ == "__main__":
    run_test()
