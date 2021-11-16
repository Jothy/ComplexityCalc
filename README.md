# ComplexityCalc

VMAT modulation complexity index calculator based on https://github.com/victorgabr/ApertureComplexity

![ComplexityCalc](https://github.com/Jothy/ComplexityCalc/blob/master/Images/ComplexityCalc_Screenshot.png)

# Installation
1. If you already have latest Anaconda python (python version>=3.8), you might have most of the libraries to run it. If not downlaod individual edition of [Anaconda](https://www.anaconda.com/products/individual/) python distribution for Windows (should also work on linux & mac but I focus only on Windows here).

2. Downlaod ComplexityCalc source code from [GitHub](https://github.com/Jothy/ComplexityCalc.git) or if you have git on your system [git pull](https://github.com/Jothy/ComplexityCalc.git)

3. Go to cmd window and type *"pip install streamlit"*. This should install the [streamlit](https://streamlit.io/) library required to deploy apps in the web.

4. Go to the ComplexityCalc folder adn edit the ComplexityCalc.bat file. Modify this line *D:\Projects\ComplexityCalc/Main.py* in the file to point to Main.py in your current ComplexityCalc folder.

# Usage 
1. You are all done. Run the ComplexityCalc.bat file and that should open a winodws in your web browser. For the first time it will ask for email, just press enter. Old internet explorer is not supported by Streamlit, so set Chrome or Edge as your default browser or open a tab in Chrome or Edge and type the ip adn port shown in the command window that opens when running the .bat file.

2. Usage is pretty intutive. Open any VMAT or IMRT DICOM RT paln file by clicking the "Browse files" button and the rest is done for you.

3. You can switch between dark adn light theme by click the wrench icon on the top-right corner in the browser.

# Bug report & feature request
You can directly rreport bugs and request features by clicking the wrench icon on the page and clicking "Report a bug"

# Contact
* **Jothy Selvaraj** - *Email: Jothybasu@gmail.com*

## Acknowledgments
 https://github.com/victorgabr/ApertureComplexity
 
 University of Michigan, Radiation Oncology https://github.com/umro/Complexity
 

## Related publications
1. [Predicting deliverability of volumetric-modulated arc therapy (VMAT) plans using aperture complexity analysis, JACMP,2016,17(4),124-131](https://pubmed.ncbi.nlm.nih.gov/27455504/)


