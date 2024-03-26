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
import pytz
import uuid
import time


arguments = docopt(__doc__, version="Calculate something 1.0")

input = arguments['--input']
output = arguments['--output']

tz = pytz.timezone('Europe/Zurich')
zurich_now = datetime.now(tz)

result = {
  "hallo": "velo",
  "input": f"{input} {str(uuid.uuid4())}",
  "update_datetime": zurich_now.isoformat(),
}

# pretend to do something time consuming
time.sleep(60)

print("Result:")
pprint(result)

with open(output, "w") as f:
  f.write(json.dumps(result, indent=4))
