# Simplistic Python SysFS interface.

## Usage

    from sysfs import sys

    for bdev in sys.block:
        print bdev, str(int(bdev.size) / 1024 / 1024) + 'M'

