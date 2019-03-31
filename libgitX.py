import argparse
import collections
import configparser
import hashlib
import os
import re
import sys
import zlib

argparser = argparse.ArgumentParser(description="content tracker")
argsubparsers = argparser.add_subparseres(title="Commands",dest="command")
argsubparsers.required = True

