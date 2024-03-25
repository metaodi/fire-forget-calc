# -*- coding: utf-8 -*-
"""Calculate something based on the input and save to output file.

Usage:
  calc.py --input <input> --output <output> 
  calc.py (-h | --help)
  calc.py --version

Options:
  -h, --help              Show this screen.
  --version               Show version.
  -i, --input <input>     Input for calculation.
  -o, --output <output>   Path to output JSON.
"""


from docopt import docopt
import json


arguments = docopt(__doc__, version="Calculate something 1.0")$

input = arguments['--input']
output = arguments['--output']

output = {
  "hallo": "velo",
  "input": input,
}


with open(output, "w") as f:
  f.write(json.dumps(output, indent=4))