# twosets

Twosets is a small python application that easily compares two lists of data and outputs a table showing which element was in which list and which was in both lists.
The process is as follows:

1. Open up twosets;

2. Copy your first set of identifiers to the clipboard. Best way is to copy a column of data from Excel, or pgAdmin. Any spaces, tabs, commas, quotes or apostrophes that are either side of the identifier will be removed when twosets takes the data in;

3. Give the set a name in twosets, you'll then be given the number of entries and the top few rows so you can check the data has been brought in properly;

4. Do the same again with the second set;

5. Twosets will then compare the twosets and produce a tab-delimited table that has on each row each of the unique identifiers found in the data you provided, and columns showing whether the identifiers was in the first, second or both sets. A small table provides a summary of the result;

6. The tab-delimited table is written to the clipboard, so just go into an Excel spreadsheet to paste and view the table.

# quicktab

Quicktab is a small python application that produces a frequency table from a single column of data. The process is as follows:

1. Open up quicktab;

2. Copy your column of data to the clipboard. Best way is to copy a column of data from Excel, or pgAdmin. Any spaces, tabs, commas, quotes or apostrophes that are either side of the row will be removed when quicktab takes the data in;

3. A tab-delimited frequency table (sorted by frequency) for all values found in the data is produced and written to the clipboard, paste it into an Excel spreadsheet to see the values.

# mquicktab

mQuicktab is a small python application that is analogous to Quicktab but creates counts of combinations of data across multiple columns, rather than just counting values in a single column.

1. Open up mquicktab;

2. Copy your columns of data to the clipboard. Best way is to copy columns of data from Excel or dBeaver. The first row should have the column headers. Any spaces, commas, quotes or apostrophes that are either side of the row will be removed when mquicktab takes the data in;

3. A tab-delimited frequency table (sorted by frequency) for all combinations of values found in the data is produced and written to the clipboard, paste it into an Excel spreadsheet to see the values.
