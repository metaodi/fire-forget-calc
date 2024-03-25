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
from pprint import pprint
from datetime import datetime


arguments = docopt(__doc__, version="Calculate something 1.0")

input = arguments['--input']
output = arguments['--output']

result = {
  "hallo": "velo",
  "input": f"{input} {datetime.now().isoformat()}",
}

print("Result:")
pprint(result)

with open(output, "w") as f:
  f.write(json.dumps(result, indent=4))
