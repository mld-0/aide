#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=3:
#   }}}1
#   {{{2
import pandas as pd

column_subset = [
    "id",
    "make",
    "model",
    "year",
    "cylinders",
    "fuelType",
    "trany",
    "mpgData",
    "city08",
    "highway08"
]

df_vehicles = pd.read_csv('data/vehicles.csv', usecols=column_subset)
print(df_vehicles)

#   Sort rows by column
print(df_vehicles.sort_values('highway08'))

#   Sort by highway08 for each unique fueltype
unique_fueltypes = df_vehicles['fuelType'].unique()
unique_fueltypes_count = df_vehicles['fuelType'].value_counts()

print(unique_fueltypes)
print(unique_fueltypes_count)
for loop_fueltype in unique_fueltypes:
    print(df_vehicles[df_vehicles.fuelType == loop_fueltype].sort_values('highway08'))

#   Sort rows by index
print(df_vehicles.sort_index())

#   }}}1
