# Fidelity Portfolio Review

This application is intended to automate a lot of the manual data-entry I would do when periodically reviewing my Fidelity portfolio. The application takes the portfolio information as exported from Fidelity's website saved as an excel document and acquires additional information for each security, such as P/E Ratio, Recognia Technical Analysis, Institutional Ownership, and more.

This application does not constitute investment or financial advice. This application was made for the sole purpose of automating manual data-entry that I would do periodically. Please consult a qualified financial professional for investment or financial advice. 

## Prerequisites

This application makes use of the following:

The openpyxl library
RapidAPI's Fidelity Investments API

Please consult the fee structure for using RapidAPI's Fidelity Investments API. If you use this application frequently or if your portfolio has a large number of different securities, you may not be able to use the API for free.

## Installation and Usage

1. Using your preferred web browser, navigate to fidelity.com, login, and go to your Portfolio homepage. From there, click on the 'positions' tab. On the right-hand side above your portfolio information is a button that says 'download' with a Microsoft Excel logo next to it. Click that link to download your portfolio information as a .csv file. As of 12/20/2020, if you are using the beta mode, click on the share icon, then click download to download a .csv file with your portfolio information.

2. For this application to properly read your portfolio information, the file will need to be resaved as a .xlsx file. You will also need to sort the rows alphabetically by stock symbol.

3. In the Fidelity_Python_Review.py file, replace the file name for the source_workbook variable with your file name (line 8). You will also need to update the source_portfolio variable with the name of the sheet in the .xlsx file (line 10).

4. In line 139, change the max_row value to the number of rows in your portfolio .xlsx file.

5. In line 227, place your RapidAPI key in the quotes where it currently says "your RapidAPI Key goes here".

6. Run the application. The application will copy the data from your source portfolio file into a new target portfolio file and will add in additional useful information. The target portfolio file also uses color for the values of certain financial statistics. These were color-coded for my use, you may change them as needed for your use.

## Contributions

As this is a project intended for my personal use, if you would like to contribute or adapt the project for your means, please fork the project. 

## Acknowledgements and Resources

Openpyxl information can be found at:
https://openpyxl.readthedocs.io/en/stable/

The RapidAPI Fidelity Investments
https://rapidapi.com/apidojo/api/fidelity-investments

## Ideas for future versions

Instead of requiring a .xlsx file to read from for the source portfolio, use the .csv format that Fidelity provides when downloading portfolio information.

Alphabetically sort the source portfolio to save the user from having to use a program like Excel to do this on their own.

Find a way to get Fidelity's "Fundamental Analysis" values such as Growth Stability and Financial Health, which are not included in the get-mashup API call at this time (as of 12/01/2020).

## License

MIT License
https://github.com/jmacdonald2010/fidelity-portfolio-review/blob/main/LICENSE