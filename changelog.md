# Fidelity Portfolio Review
## V 0.2.0 
### In Progress Branch

This is the changelog for the in-progress branch for a new version of the fidelity portfolio review script. In this version, instead of relying on the Fidelity Investments rapidAPI, it will instead use the selenium webdriver to gather information directly from the website. By using Selenium to automate the browser, users can safely and easily log in to the site, and the script can easily acquire the necessary information. See the 'Ideas for Future Versions' section of the readme for planned implementations.

#### 03/09/2021 21:31
Began adding in a cell that adds conditional formatting to the excel document, and also makes a copy of that document (for now, this may be removed later). Still working on adding in the conditional formatting. 

#### 03/09/2021 09:41
I added a while loop to the data extraction cell, as I noticed that if an error occured that caused the cell to redirect the browser to the fidelity homepage, that it would continue to the next symbol in the dataframe, which caused some issues with the integrity of the data. Adding in a while loop to only proceed with the for loop if extraction was successful (or failed three times) cleaned up the initial dataframe significantly, and rendered much of this past weekend's work unnecessary.

Next steps are:
- Add conditional formatting to the excel document using openpyxl.
    - Add in color-coding for the extracted data columns and select other columns from the orignal CSV.
    - Alternating gray/white for alternating symbols.
- Some basic visualization.

#### 03/09/2021 08:22
Data cleaning cells are getting there; I've now completed the cells that look for rows of the same symbol where the webscraped data doesn't match, and correct them by giving them the values of the row with the least np.nans. Might do some tidying up of the data extraction cell; it looks like it missed a few symbols. Might try to get the program so that it adjusts the index values by alphabetical order.

#### 03/07/2021 20:24
Working on data cleaning; trying to figure out the best way to deal w/ rows of duplicate symbols where some of the rows are missing the webscraped data and others are not. Working on sketching out how that will work.

#### 03/07/2021 17:32
Added in the first cells to clean the data in the dataframe. This one converts the values that are provided in the source csv file and converts them to np.floats. Next, will be to check to see what duplicate symbols have missing values (perhaps just run the execution block a second time?) and fill them in from the rows where that symbol has complete values.

#### 03/07/2021 14:32
Data extraction cell ran through once completely. Need to verify the data in the second half of the file, as it seems some data is missing (some, it seems from the original csv file, and some from the webscraping). Planning on having the cell after data extraction to be data cleaning, then after that, adding in some conditional formatting to the excel document. Cells after that will be misc. data analysis, charting, etc.

#### 03/06/2021 21:58
Started testing the actual extraction cell. Fixes have been added in wherever deemed necessary, but I'm currently running into an issue with the ETF stats extraction function, where it crashes on a ValueError if the P/E value in the ETF is '--'. For some reason, the error is located at the actual function call itself, and within the module, it occurs on the actual 'else' line, which I can't seem to figure out. Need to figure out how to carefully place this specific try/except statement. Will try to figure that out tomorrow.

#### 03/06/2021 10:41
Added in some code in the extraction cell to skip rows in the dataframe that are already full if the cell needs to be rerun. Also updated the etf key stats extraction function, because fixed-income ETFs do not have the same research page layouts as sector or index ETFs (this patch has not yet been tested.) Commit/Push prior to going to work.

#### 03/05/2021 09:43
Added in some try/except blocks in the extract.py file and through the extraction cell. These have not yet been tested. Testing is the next thing on the agenda.

#### 03/05/2021 08:59
Started testing the extraction block. Ran into the following issues:

- Issue copying row data from previous symbols.
    - Resolved.
- Issue when certain statistics are not present (e.g. Dividends) that cause the program to crash.
    - This was expected; I need to modify the extract.py file to provide exceptions for what to do when no information is found. 
    - In addition to that, I think I also need to provide an exception to allow a security to be skipped entirely if it is problematic. A list should be created containing securities that caused issues that required them to be skipped.

#### 03/04/2021 22:59
Made significant progress on the notebook. Fixed issues with creating the initial dataframe. Cell for data extraction has been written but not yet tested. Once the extraction block has been successfully tested, conditional formatting will be added.

The following either still needs done or likely will need to be done:

- Error/exception handling for missing values (e.g. a non-existant P/E ratio, etc.)
- Conditional Formatting

#### 03/04/2021 09:43
Started working on the notebook. Have decided to make some changes for the final notebook:

- Keep data in dataframe for later processing in notebook (visualizing).
- Perform conditional formatting using openpyxl, instead of using a template excel file.
- At the end of the project, upload an example notebook, full of graphs, etc. that shows some example analyses of the data.

#### 03/04/2021 08:57
Functions have been tested in the sketches notebook. Starting to assemble everything in the actual notebook.

#### 03/03/2021 22:45
Testing all functions in the sketch notebook. Updating as needed. Haven't retested the ones I've fixed yet as it would involve closing the browser window and having to log in again. Will test the ones I think I fixed when I open the project up again in the morning.

#### 03/03/2021 21:50
Functions are compiled in the extract.py file. They have not been tested yet. Commit/Push before making big changes. Will test functions in the sketches notebook before adding to the actual notebook.

#### 03/03/2021 09:37
Working on compiling the final notebook. Placing all of the functions used to get data in a separate file in order to keep the code cleaner. Unsure of how well these functions will take to having the driver as a function parameter. Code has not been tested yet.

What has been done:

- Moving working code into the extract.py file as functions.
- Set up most of the first cell in the notebook, which sets everything up.

What needs to be done:

- Complete the first cell
    - Need to add in the browser launch and data copying to a new excel file.
- Finish copying functions into the extract.py file
    - Need the following copied over still:
        - 52-Week performance for stocks
        - Anything for ETFs (except recognia analysis)
        - Anything for Mutual Funds
- Write code blocks that run the functions and copy the data.
- ReadMe documentation in notebook.

#### 03/02/2021 09:$0
Test notebook has what I think is everything I need to begin compiling the final notebook. Following changes/additions were made:

- Remove instituation ownership from dataframe, excel document.
- Add a method to get 1-Yr price targets from YF (not using yfinance, as this stat is not available)
- Not yet tested, but determined a way to get recognia data for ETFs in a more efficient, less repetitive manner.
- Added price target to excel document, dataframe
- Added Debt/Equity stats to excel, dataframe, added extraction method.

#### 03/01/2021 22:05
Commit/Push for a lot of progress done before making bigger changes. Following progress was made:

- Extract necessary data (see exceptions below)
- Reduce redundancy in code.
    - Mainly applies to the extraction of recognia technical analysis data.

The following decisions have been made:

- Final project will be in the form of a jupyter notebook
- Not using institutional ownership as a metric, as I haven't used it too much in decision making recently.

The following still needs to be done:

- Configure new recognia technical analysis code block to work for ETFs
- Remove institutional ownership from target_workbook.xlsx, dataframe.
- Add code to use yfinance to gather price target data.
- Assemble final notebook and test.


#### 02/28/2021 22:36
Last commit/push prior to end of night. Working on creating the file to run as one whole script. Goal is to accomplish the following:

- Open csv file as dataframe (done)
- Copy data in source csv to target workbook (excel file, requires new columns added)
- Add columns to dataframe for things not in the source CSV file
- Iterate through symbols in dataframe, acquire/extract information, write to dataframe, every ten or so rows, save to the excel file.
- Update the conditional formatting in the excel file.
- Figure out the best way to extract data from the research pages for Mutual Funds and ETFs.
- Use yfinance to gather 1 year price target information.

#### 02/28/2021 21:20
Commit/Push prior to major change. I am going to be ultimately creating this project as a singular python script instead of a jupyter notebook. I'll need to figure out how to work w/ loading the source .csv file, but that shouldn't be terribly difficult. The script will require user input prior to iterating thru the documents, mainly to ensure that the user is signed into the fidelity website once the browser is opened. The project will also hold the data in nested dictionaires, or possibly pandas dataframes, to be exported to the target workbook. I have already accomplished acquiring key statistics information and storing them in nested dictionaires. I feel it may be more efficient to use a pandas dataframe, as it can more effectively be exported to an excel file.

#### 02/27/2021 22:35
Working on extracting the text from the notebook. A lot of these cells will later be condensed down. For now, using a lot of small cells is the easiest way to ensure everything is working the way that it should. So far this has only been tested on one symbol. Tomorrow I will test this on additional symbols (stocks only) to ensure that it is working.

#### 02/27/2021 10:47
Started building the new notebook. At this time, there are going to be a lot of cells that are not organized the best way possible. A lot of these will be collapsed down into a final script in the final version of the project, with a few cells to be run prior to the main script being executed. This project may also possibly be reduced to a final single script. 

Progress so far:

- Imports modules
- Launches browser, loads homepage
- Loads the research page for a security, scrolls to the bottom of the page, determines security type