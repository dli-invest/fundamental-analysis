import flask_minimal.fundamental_indicators_provider as fundamental_indicators_provider
import asyncio
config = {}
company = fundamental_indicators_provider.Company('ADCO.TO')
# Note: 
# You might want to create an event loop and run within the loop:
fundamental_indicators_provider.get_fundamental_indicators_for_company(config, company)
print(company.fundamental_indicators)
