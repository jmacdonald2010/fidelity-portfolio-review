# Fidelity Portfolio Review
## V 0.2.0 
### In Progress Branch

This is the changelog for the in-progress branch for a new version of the fidelity portfolio review script. In this version, instead of relying on the Fidelity Investments rapidAPI, it will instead use the selenium webdriver to gather information directly from the website. By using Selenium to automate the browser, users can safely and easily log in to the site, and the script can easily acquire the necessary information. See the 'Ideas for Future Versions' section of the readme for planned implementations.

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