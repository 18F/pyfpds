# -*- coding: utf-8 -*-

__author__ = 'Kaitlin Devine'
__email__ = 'katycorp@gmail.com'
__version__ = '0.1.0'

from collections import OrderedDict
import xmltodict
import requests
import json
import warnings

warnings.filterwarnings('ignore')

field_map = {
    
    'piid': 'PIID',
    'idv_piid': 'REF_IDV_PIID',
    'idv_agency_id': 'REF_IDV_AGENCY_ID',
    'modification_number': 'MODIFICATION_NUMBER',
    
    'contracting_agency_id': 'CONTRACTING_AGENCY_ID',
    'contracting_agency_name': 'CONTRACTING_AGENCY_NAME', 
    'contracting_office_id': 'CONTRACTING_OFFICE_ID',
    'contracting_office_name': 'CONTRACTING_OFFICE_NAME',
    'funding_agency_id': 'FUNDING_AGENCY_ID',
    'funding_office_id': 'FUNDING_OFFICE_ID',
    'funding_office_name': 'FUNDING_OFFICE_NAME',
    'agency_code': 'AGENCY_CODE',
    'agency_name': 'AGENCY_NAME',
    'department_id': 'DEPARTMENT_ID',
    'department_name': 'DEPARTMENT_NAME',

    'last_modified_date': 'LAST_MOD_DATE',
    'last_modified_by': 'LAST_MODIFIED_BY',
    'award_completion_date': 'AWARD_COMPLETION_DATE',
    'created_on': 'CREATED_DATE',
    'date_signed': 'SIGNED_DATE',
    'effective_date': 'EFFECTIVE_DATE',
    'estimated_completion_date': 'ESTIMATED_COMPLETION_DATE',
    
    'obligated_amount': 'OBLIGATED_AMOUNT',
    'ultimate_contract_value': 'ULTIMATE_CONTRACT_VALUE',
    'contract_pricing_type': 'TYPE_OF_CONTRACT_PRICING',
    
    'award_status': 'AWARD_STATUS',
    'contract_type': 'CONTRACT_TYPE',
    'created_by': 'CREATED_BY',
    'description': 'DESCRIPTION_OF_REQUIREMENT',
    'modification_reason': 'REASON_FOR_MODIFICATION',
    'legislative_mandates': 'LEGISLATIVE_MANDATES',
    'local_area_setaside': 'LOCAL_AREA_SET_ASIDE',
    'socioeconomic_indicators': 'SOCIO_ECONOMIC_INDICATORS',
    'multiyear_contract': 'MULTIYEAR_CONTRACT',
    'national_interest_code': 'NATIONAL_INTEREST_CODE',
    'national_interest_description': 'NATIONAL_INTEREST_DESCRIPTION',
    
    'naics_code': 'PRINCIPAL_NAICS_CODE',
    'naics_description': 'NAICS_DESCRIPTION',
    'product_or_service_code': 'PRODUCT_OR_SERVICE_CODE',
    'product_or_service_description': 'PRODUCT_OR_SERVICE_DESCRIPTION',
    
    'place_of_performance_district': 'POP_CONGRESS_DISTRICT_CODE',
    'place_of_performance_country': 'POP_CONGRESS_COUNTRY',
    'place_of_performance_state': 'POP_STATE_NAME',

    'vendor_city': 'VENDOR_ADDRESS_CITY',
    'vendor_district': 'VENDOR_CONGRESS_DISTRICT_CODE',
    'vendor_country_code': 'VENDOR_ADDRESS_COUNTRY_CODE',
    'vendor_country_name': 'VENDOR_ADDRESS_COUNTRY_NAME',
    'vendor_duns': 'VENDOR_DUNS_NUMBER',
    'vendor_dba_name': 'VENDOR_DOING_BUSINESS_AS_NAME',
    'vendor_name': 'VENDOR_NAME',
    'vendor_state_code': 'VENDOR_ADDRESS_STATE_CODE',
    'vendor_state_name': 'VENDOR_ADDRESS_STATE_NAME',
    'vendor_zip': 'VENDOR_ADDRESS_ZIP_CODE',

}

boolean_map = {
    True: 'Y',
    False: 'N',
}


class Contracts():
    
    feed_url = "https://www.fpds.gov/ezsearch/FEEDS/ATOM?FEEDNAME=PUBLIC&q="
    feed_size = 10
    query_url = ''
   
    def __init__(self, logger=None):
        #point logger to a log function, print by default
        if logger:
            self.log = logger 
        else:
            self.log = print

    def pretty_print(self, data):
        self.log(json.dumps(data, indent=4))


    def convert_params(self, params):

        new_params = {}
        for k,v in params.items():
            new_params[field_map[k]] = v
        return new_params

    def combine_params(self, params):
        return " ".join("%s:%s" % (k,v) for k,v in params.items())

    def process_data(self, data):
        #todo
        if isinstance(data, dict):
            #make a list so it's consistent
            data = [data,]
        return data

    def get(self, num_records=100, order='desc', **kwargs):

        params = self.combine_params(self.convert_params(kwargs))

        data = []
        i = 0
        #for n in range(0, num_records, 10):
        while num_records == "all" or i < num_records:
            
            self.log("querying {0}{1}&start={2}".format(self.feed_url, params, i))
            resp = requests.get(self.feed_url + params + '&start={0}'.format(i), timeout=60, verify = False)
            self.query_url = resp.url
            self.log("finished querying {0}".format(resp.url))
            resp_data = xmltodict.parse(resp.text, process_namespaces=True, namespaces={'http://www.fpdsng.com/FPDS': None, 'http://www.w3.org/2005/Atom': None})
            try:
                processed_data = self.process_data(resp_data['feed']['entry'])
                for pd in processed_data:
                    data.append(pd)
                    i += 1
                
                #if data contains less than 10 records, break out of loop
                if  len(processed_data) < 10:
                    break
            
            except KeyError as e:
                #no results
                self.log("No results for query")
                break

        return data








