# Fidelity Portfolio Review
## V 0.2.0 
### In Progress Branch

This is the changelog for the in-progress branch for a new version of the fidelity portfolio review script. In this version, instead of relying on the Fidelity Investments rapidAPI, it will instead use the selenium webdriver to gather information directly from the website. By using Selenium to automate the browser, users can safely and easily log in to the site, and the script can easily acquire the necessary information. See the 'Ideas for Future Versions' section of the readme for planned implementations.

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