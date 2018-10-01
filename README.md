# swim-data-processing
Python scripts for processing HY-TEK data from swim meets

# How-to
Select all data from a single event using CTRL+A
![hytek results page](https://github.com/kawilliams/swim-data-processing/blob/master/images/results.png)

Paste the results into a plain-text file (.txt)
![results in txt](https://github.com/kawilliams/swim-data-processing/blob/master/images/text.png)

Save the results file. 

To convert the txt data to a csv, first open TimesProcessor.py. You can either enter the filenames as Python user inputs or as command line arguments. Choose your method by commenting in the correct section of main. Save TimesProcessor.py.

## DEFAULT To run as command line arguments:
Run TimesProcessor.py and enter your filenames as arguments:
```
user$ python TimesProcessor.py data/naia_2018_men_100fr.txt 
Data from data/naia_2018_men_100fr.txt will be written to data/naia_2018_men_100fr.csv
```

## To run as Python input:
Run TimesProcessor.py and follow the prompts:
```
user$ python TimesProcessor.py
Enter filename (must be .txt):   
```
After entering the filename, you should see:
```
Enter filename (must be .txt): data/naia_2018_men_100fr.txt      
Data from data/naia_2018_men_100fr.txt will be written to data/naia_2018_men_100fr.csv
```
The new csv file will appear in the same location as the txt file.




