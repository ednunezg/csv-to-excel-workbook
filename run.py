#!/usr/bin/env python

import os
import glob
import pandas as pd
from pandas import ExcelWriter

def merge_dir_to_excel(merge_dir, workbook_filename):
  writer = ExcelWriter("./{}.xlsx".format(workbook_filename))

  files = sorted(glob.glob("{}/*.csv".format(merge_dir)))

  # For each file, insert a 'null' column if number of records is 0
  # This is to avoid users from being confused from seeing an Excel
  # sheet with headers and no records
  for filename in files:
    df_csv = pd.read_csv(filename, delimiter=',')
    if df_csv.size == 0:
      f = open(filename, "a")
      f.write("No records found")

  for filename in files:
      df_csv = pd.read_csv(filename, delimiter=',')
      (_, f_name) = os.path.split(filename)
      (f_without_ext, _) = os.path.splitext(f_name)
      f_shortname = f_without_ext[0:30]
      df_csv.to_excel(writer, f_shortname, index=False)

  writer.save()

merge_dir_to_excel('./inputs', 'DataPull')