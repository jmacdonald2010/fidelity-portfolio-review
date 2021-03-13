# Fidelity Portfolio Review

## Description

This application is intended to automate a lot of the manual data-entry I would do when periodically reviewing my Fidelity portfolio. The application takes the portfolio information as exported from Fidelity's website and acquires additional information for each security, such as P/E Ratio, Recognia Technical Analysis, Institutional Ownership, and more.

This application does not constitute investment or financial advice. This application was made for the sole purpose of automating manual data-entry that I would do periodically and as an educational project to learn more about data analysis and visualization. Please consult a qualified financial professional for investment or financial advice. 

## Dependencies

This application makes use of the following:

- Jupyter Notebooks
- Pandas
- Numpy
- Matplotlib
- Bokeh
- Selenium Webdriver (with Gecko Webdriver installed in system path)

## Installation and Usage

1. From fidelity.com, log in and navigate to your account positions. Be sure you are viewing your positions with the Beta view (as of 3/13/2021). Click on the 'Share' icon, and click download. This will download a .csv of your account positions. Place this .csv file in the same folder as this notebook.

2. In the first python code cell, replace the .csv file name with the name of your .csv file.

3. Run the first cell to import the necessary libraries and modules and open a Firefox browser window that can be controlled by the Selenium Webdriver.

4. Before running the next cell, log in to Fidelity as you normally would. The stock research data we're looking for is only available if you are logged into your account. No account information is gathered in the running of this cell.

5. Run the data extraction cell. This will take some time, as there are pauses written in to avoid overloading the servers.

6. Once the data extraction cell has finished running successfully, you can run the data cleaning cells (if necessary) and the visualization cells.

### Note:

- The conditional formatting used in the excel document is based on what are typically considered 'good' values (largely according to Investopedia): 

    - Total Gain/Loss and 52-Week Performance are based on what is often described as the average annual return on the S&P 500 (8&).

    - Conditional formatting for key statistics is based on what Investopedia and NASDAQ refer to as good values. 

    - Conditional formatting for Percent of Account is set for a max of 3.5%. This is a personal choice.

    - Conditional formatting for fundamental analysis and equity summary score is based on higher is better (100 and 10 as the best respectively).

    - Once again, this project does not constitute investment/financial advice, and was created entirely for personal use and as an educational project to give me more experience with data analysis and visualization. Please consult a qualified financial professional for investment/financial advice.

## Examples

Please see the "example_images" folder for images of visualizations and a screenshot of the output of the excel document. Actual example notebooks and excel documents are not included for security reasons.

## Contributions

If you have suggestions for changes, bug fixes, improvements, please feel free to fork the project and create a pull request. Contributions for improved visualizations (especially for color/theme selections/design) are greatly welcomed.

## Acknowledgements and Resources

Special thanks to two particular Stack Overflow answers which assisted greatly with various parts of the development of this notebook:

https://stackoverflow.com/questions/39529662/python-automatically-adjust-width-of-an-excel-files-columns

https://stackoverflow.com/questions/35090498/how-to-calculate-percent-change-compared-to-the-beginning-value-using-pandas

## Ideas for future versions/Known Issues

- The conditional formatting for the 1-Yr Price Target highlights blank cells in red; in a future version, empty cells in this column should be left blank.

- The autosize-column formatting for the "Account" column creates a column that is unreasonably large, possibly due to additional text at the bottom of the .csv file provided from Fidelity. A future version should size the column more appropriately.

- Add a blank "Notes" column to the excel document.

## Project Status

This project will likely not see any immediate updates unless a feature of it is broken when I attempt to use it again. Since this was a project made for personal use, I am not terribly bothered the by known issues listed above. 

## License

MIT License
https://github.com/jmacdonald2010/fidelity-portfolio-review/blob/main/LICENSE