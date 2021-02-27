# Fidelity Portfolio Review
## V 0.2.0 
### In Progress Branch

This is the changelog for the in-progress branch for a new version of the fidelity portfolio review script. In this version, instead of relying on the Fidelity Investments rapidAPI, it will instead use the selenium webdriver to gather information directly from the website. By using Selenium to automate the browser, users can safely and easily log in to the site, and the script can easily acquire the necessary information. See the 'Ideas for Future Versions' section of the readme for planned implementations.

#### 02/27/2021 10:47
Started building the new notebook. At this time, there are going to be a lot of cells that are not organized the best way possible. A lot of these will be collapsed down into a final script in the final version of the project, with a few cells to be run prior to the main script being executed. This project may also possibly be reduced to a final single script. 

Progress so far:

- Imports modules
- Launches browser, loads homepage
- Loads the research page for a security, scrolls to the bottom of the page, determines security type