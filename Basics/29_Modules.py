# for better organizing code

import converters
from converters import kilo_to_lbs  # importing a specific function
from converters import lbs_to_kgs

weight_in_lbs=converters.kilo_to_lbs(10)
print(weight_in_lbs)
weight_in_kgs=converters.lbs_to_kgs(200)
print(weight_in_kgs)
