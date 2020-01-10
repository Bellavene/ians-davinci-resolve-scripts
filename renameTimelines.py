#!/usr/bin/env python3

# import os
import argparse
import ResolveLib.ianresolvelib as resolve
import re

parser = argparse.ArgumentParser(description="Add timelines to Resolve's render queue by specifying a suffix.")
parser.add_argument("search", help="Search term, adoy")
parser.add_argument("replace", help="Replace term innit")
# parser.add_argument("-r", "--regexp", help="")
# parser.add_argument("-t", "--test", help="Check out what will happen before doing it")
args = parser.parse_args()

p = re.compile(args.search)
for tl in resolve.GetTimelinesByRegexp(args.search):
    # resolve.AddTimelineToRender(tl, renderPreset, args.dest)

    x = p.sub(args.replace, tl.GetName())
    print(x)
    tl.SetName(x)