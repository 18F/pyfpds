# pyfpds
pyfpds is a basic python wrapper for accessing federal contracting data in the Federal Procurement Data System (FPDS). The only programmatic access to this data is via an ATOM feed that limits each request to 10 records. This can be quite frustrating if you want more than 10 records! This library will grab up to any number of records requested (the default being 100) and compile them into one data structure. Subsequently, the performance is not exemplary, as much of the processing time is spent in http transport. However, if you have the time, it makes life a bit easier :). Additionally, the ATOM feed does not support sorting. If you want to get complete data sorted by a field, you essentially have to pull down all records and sort them in python.

This project was created to assist with ETL tasks that are part of the [Mirage project](https://github.com/18F/mirage). If you have features, open an issue, or consider contributing to the project yourself (see CONTRIBUTING). 

### Requirements
This project supports python 2.7+. To install the dependencies, use pip:
``` pip install -r requirements.txt ```


### Some helpful links:
* [FPDS ATOM feed FAQ](http://beta.fpdsng.com/wiki/index.php/ATOM_Feed_FAQ)
* [FPDS ATOM feed query fields and example usage](https://www.fpds.gov/wiki/index.php/Atom_Feed_Usage)
* [FPDS search](https://www.fpds.gov/fpdsng_cms/index.php/en/)
* [Full documentation for pyfpds](https://pyfpds.readthedocs.org)







