#!/usr/bin/env python
# coding: utf-8

import pandas as pd
from location_name_formatter import LocationNameFormatter

name_formatter = LocationNameFormatter()
before_format = "Chittagong"
formatted_string = name_formatter.formatter(before_format)
print(formatted_string)
