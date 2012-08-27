# Simplistic Python SysFS interface.

Shamelessly stolen from <http://stackoverflow.com/questions/4648792/>.

## Usage

    from sysfs import sys

    for bdev in sys.block:
        print bdev, str(sys.block[bdev].size / 1024 / 1024) + 'M'

