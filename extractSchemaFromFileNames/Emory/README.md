#Overview

This contains scripts we have developed at Emory that will walk through
a collection in Girder and look at the file names and folders and try and
match metadata, and then upload the data to the girder server

#How to use

Open the notebook

Cell by cell:

0. Basic Jupyter Notebook settings
1. Assorted imports
2. Authing girder client
3. Setting collection ID of interest
4. This function actually pulls data, including existing metadata, and attempts to apply the current algorithm to the file/folder info. The results are then compared to the existing metadata, and the record is updated if there is a difference
5. Generate summaries of existing values in metadata in order to identify persistent patterns of errors. Setting outputRecords to False will print a sample of the data which would otherwise be saved to csv if this is passed as True
6. Bug from this point forward (getSummaryStats produces empty DF)
