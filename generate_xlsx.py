import pandas as pd
import datetime

def generate_excel(crawlerId,company_name,CS_link,industry_code,company_profile,classification_of_company):
    data={
        'crawlerId':crawlerId,
        'Company Name':company_name,
        'CS link':CS_link,
        'Industry Code':industry_code,
        'Company Profile':company_profile,
        'Company/Consultant':classification_of_company,
    #    'Flag Status(code/words)':flag_status
    }
    dataframe=pd.DataFrame(data)
    current_time=datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    new_excel_file=dataframe.to_excel('Created_Excel_Files/Industrial_Mapping_'+current_time+'.xlsx',index=False)
    return new_excel_file

