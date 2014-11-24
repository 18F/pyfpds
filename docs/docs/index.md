# pyfpds
pyfpds is a basic python wrapper for accessing federal contracting data in the Federal Procurement Data System (FPDS). The only programmatic access to this data is via an ATOM feed that limits each request to 10 records. This can be quite frustrating if you want more than 10 records! This library will grab up to any number of records requested (the default being 100) and compile them into one data structure. Subsequently, the performance is not exemplary, as much of the processing time is spent in http transport. However, if you have the time, it makes life a bit easier :). Additionally, the ATOM feed does not support sorting. If you want to get complete data sorted by a field, you essentially have to pull down all records and sort them in python.

This project was created to assist with ETL tasks that are part of the [Mirage project](https://github.com/18F/mirage). If you have suggestions for features, open an issue, or consider contributing to the project yourself (see CONTRIBUTING). 

### Requirements
This project supports python 2.7+. To install the dependencies, use pip:
``` pip install -r requirements.txt ```


### Some helpful links:
* [FPDS ATOM feed FAQ](http://beta.fpdsng.com/wiki/index.php/ATOM_Feed_FAQ)
* [FPDS ATOM feed query fields and example usage](http://beta.fpdsng.com/wiki/index.php/ATOM_Feed_FAQ)
* [FPDS search](https://www.fpds.gov/fpdsng_cms/index.php/en/)
* [Full documentation for pyfpds](https://pyfpds.readthedocs.org)

### Usage

The `Contracts` object can be used to fetch records filtered by several attributes using keyword arguments. The result returned is a list of `OrderedDict` objects.

Example:

```
from pyfpds import Contracts

c = Contracts()

#filter by a specific contract ID number
records = c.get(piid="FA865014M5002")

r = records[0]['content']['award']

#pretty print the first record
c.pretty_print(r)
```

Possible Keyword Arguments:

```
    piid
    idv_piid
    idv_agency_id
    modification_number     
    contracting_agency_id     
    contracting_agency_name
    contracting_office_id
    contracting_office_name
    funding_agency_id
    funding_office_id
    funding_office_name
    agency_code
    agency_name
    department_id
    department_name

    last_modified_date
    last_modified_by
    award_completion_date
    created_on
    date_signed
    effective_date
    estimated_completion_date
   
    obligated_amount
    ultimate_contract_value
    contract_pricing_type
   
    award_status
    contract_type
    created_by
    description
    modification_reason
    legislative_mandates
    local_area_setaside
    socioeconomic_indicators
    multiyear_contract
    national_interest_code
    national_interest_description
   
    naics_code
    naics_description
    product_or_service_code
    product_or_service_description
   
    place_of_performance_district
    place_of_performance_country
    place_of_performance_state

    vendor_city
    vendor_district
    vendor_country_code
    vendor_country_name
    vendor_duns
    vendor_dba_name
    vendor_name
    vendor_state_code
    vendor_state_name
    vendor_zip

    piid
    idv_piid
    idv_agency_id
    modification_number
   
    contracting_agency_id
    contracting_agency_name 
    contracting_office_id
    contracting_office_name
    funding_agency_id
    funding_office_id
    funding_office_name
    agency_code
    agency_name
    department_id
    department_name

    last_modified_date
    last_modified_by
    award_completion_date
    created_on
    date_signed
    effective_date
    estimated_completion_date
   
    obligated_amount
    ultimate_contract_value
    contract_pricing_type
   
    award_status
    contract_type
    created_by
    description
    modification_reason
    legislative_mandates
    local_area_setaside
    socioeconomic_indicators
    multiyear_contract
    national_interest_code
    national_interest_description
   
    naics_code
    naics_description
    product_or_service_code
    product_or_service_description
    
    place_of_performance_district
    place_of_performance_country
    place_of_performance_state

    vendor_city
    vendor_district
    vendor_country_code
    vendor_country_name
    vendor_duns
    vendor_dba_name
    vendor_name
    vendor_state_code
    vendor_state_name
    vendor_zip
```

To find valid values for these arguments, please see the [FPDS Data Dictionary](https://www.fpds.gov/downloads/Version_1.4_specs/FPDSNG_DataDictionary_V1.4.pdf) which enumerates valid values for each attribute name. 



