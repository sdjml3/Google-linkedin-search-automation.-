import time
from query_config import gemini_paraphrase_data
from google_search_pattern import google_search_data
from Regex_data_extraction import extract_industry_code, extract_company_profile
from generate_xlsx import generate_excel
import pandas as pd
from tqdm import tqdm


file_name='Copy of 183 industrytype -55 clients(2025-01-07)'
dataframe=pd.read_excel('Source Files/'+file_name+".xlsx")
Career_page_url=dataframe['careerSiteUrl']
Company_Name=dataframe['companyName']
crawlerId=dataframe['crawlerId']
company_name=[]
company_description=[]
industry_type=[]

#print("wait while the details are being fetched...\n")
for name,i in zip(Company_Name,tqdm(range(0,100),total=len(Company_Name),desc='site processed:')):
    res=google_search_data(name)
    company_name.append(res['company_name'])
    company_description.append(res['company_description'])
    industry_type.append(res['industry_type'])
    time.sleep(3)

#company_profile=[gemini_company_description(desc,cs_link) for desc,cs_link,i in zip(company_description,Career_page_url,tqdm(range(len(company_description))))]
company_data_rephrased=[gemini_paraphrase_data(desc,code) for desc,code,i in zip(company_description,industry_type,tqdm(range(len(Company_Name))))]
code_data=[extract_industry_code(code_data) for code_data in company_data_rephrased]
classification_of_company=['Consultant' if x==127 else 'Company' for x in code_data]
company_profile=[extract_company_profile(profile) for profile in company_data_rephrased]


try:
    generate_excel(crawlerId,Company_Name,Career_page_url,code_data,company_profile,classification_of_company)
    print("Excel File has been Created!!!.............")
except Exception as e:
    print(f"ALERT!! there might be an error!!! {e}")

