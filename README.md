# pdf-difference-finder
A PDF comparison utility in Python.
Inspired from the work of https://github.com/JoshData/pdf-diff (provides a terminal command for finding the differences between two pdfs).The above python snippet will help you in identifying the differences between two pdfs irrespective of the number of pages in it and to run it as a *python method or as an API*.The **config.py** helps you in changing the style of the output file, including color, file format and the markers for denoting the changes *eg: box or strike*. Two sample files is also provided for testing the code snippet.

# How to use the snippet ?
> Fork or Clone the repository. 

> Install the required packages
- pip install -r requirements.txt

> To run the snippet as a python method
- run the file **pdfdifferencefinder.py** by giving your filenames as input


## API Details
> To run the snippet as an API
- run the file **apiFile.py**
- The body of the API should be a form-data with *file1* and *file2* as the keys.
 ![API Input Sample](https://github.com/sreelekshmyselvin/pdf-difference-finder/blob/master/sampleAPI_Input.png)

  
> The outputs generated will have an **image file** which highlights the differences as well as a **.json file** which contains the details of the changes in the files.
