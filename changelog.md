# Fidelity Portfolio Review Version Changelog

## V 0.2.0 

Following changes were made:

- Completely redesigned the project to run in a notebook instead of a single python script.

- Now use Selenium Webdriver to webscrape data instead of using the Fidelity Investments RapidAPI.

- Start using the csv file straight from Fidelity's website without any modification or conversion.

- Minimal changes needed to code cells to run.

- Code cells in notebook add in conditional formatting and create a new excel document, eliminating the need for a target workbook file.

- Notebook performs basic visualizations.

## V 0.1.0

- Project uses Rapid API's Fidelity Investments API to gather data.

- Fills in a target excel workbook with new information, copies original information.