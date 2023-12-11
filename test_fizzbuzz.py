#!/usr/bin/python3

import atheris

with atheris.instrument_imports():
  import fizzbuzz
  import sys

def TestOneInput(data):
  fizzbuzz.fizz_buzz(data)

atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()