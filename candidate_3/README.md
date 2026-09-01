# business-data-insights-

# Notes
Parquet is a binary, columnar format that:

Stores actual typed data (an integer is stored as an integer, not text), so reading it back is faster and doesn't require re-guessing dtypes.
Stores data column-by-column rather than row-by-row — so if you only need one column, tools can skip reading the others entirely (this is why DuckDB was fast in your upcoming Polars/DuckDB comparison).
Compresses much smaller than CSV for the same data. 

Note( CSV is a text format — every number, every date, is stored as literal characters, like "1149" 
instead of the actual number 1149. Every time you read a CSV, pandas has to re-guess and re-parse every column's type from scratch.)


pyarrow is the same columnar format both Polars and DuckDB read natively, 
which is part of why Parquet plays so well with those tools.

