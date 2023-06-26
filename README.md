# File Merger

Used to merge files of data into a singe CSV.

Inputs: A folder with multiple files of the same format

Outputs: A single file that has merged the files of the same format into a single CSV file.

The input files can be CSV, ASCII, TXT, or similar files but they must all be formatted the same with common dependent variables and the same number of independent variables. They must be formatted such that an independent variable is a column not a row, an example is given at run time. They must also all share the same delimiter (separator between values). The program can account for different file types in given folder, a header or footer that is the same across each input file, more than one dependent file in each folder. The user is also able to specify the name of the merged CSV, and whether they wish to transpose the merged data. It is recommended to transpose the data if using my Python PCA or PLSR programs later.
