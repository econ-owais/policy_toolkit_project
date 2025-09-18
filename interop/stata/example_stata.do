
* Example Stata Do-file: load CSV and run regression
import delimited using "exports/data_for_stata.csv", clear
regress y x1 x2
