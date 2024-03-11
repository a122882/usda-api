
from esr.main import get_esr_regions
from esr.main import get_esr_countries
from esr.main import get_esr_commodities
from esr.main import get_esr_unitsofmeasure
from esr.main import get_esr_allcountries_export
from esr.main import get_esr_country_export

api='d317a077-50d7-4949-9958-42d7cb97a1d3'

#region = get_esr_regions(api)
#country = get_esr_countries(api)
#commodities = get_esr_commodities(api)
#unitofmeasure = get_esr_unitsofmeasure(api)
#for i in country:
#    print(i['country_name'], i['country_code'])
#allcountriesexport = get_esr_allcountries_export(api,401,2023)
countryexport = get_esr_country_export(api, '401', '5700','2022')
print(countryexport)
