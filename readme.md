#PDF Splitter
- #### Description: 
    PDF Splitter automatically sends your employees paycheck by email
- #### How to use
    Just put the path of your pdf, a path of csv file with the format {[CUIL/CUIT], [Name], [Email]}
    Enter your email address and your password (Don't worry, your data is safe... We're not facebook)
- #### How it works
    That program take the first page of your pdf file, search if it page have a number of cuil that 
    match with some cuil/cuit of the csv file. If it matches, send an email to the employee associate with the cuil/cuit, and attachment the paycheck
    Just run the following command in your terminal \
    ```python splitter.py``` \
    and complete all the fields
- #### Package that you need installed
- textract
- csv
- smtplib
- email
- PyPDF2