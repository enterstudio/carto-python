from carto.auth import APIKeyAuthClient
from carto.exceptions import CartoException
from carto.datasets import DatasetManager
import warnings
warnings.filterwarnings('ignore')
import os
import pprint
printer = pprint.PrettyPrinter(indent=4)
from carto.sql import SQLClient
import sys

if len(sys.argv) <= 2:
  print 'You have to pass 2 input arguments.Add username and table name as arguments in that order'

organization = 'cartoworkshops'
CARTO_BASE_URL='https://carto-workshops.carto.com/api/'
CARTO_API_KEY = os.environ['CARTO_API_KEY']


# Authenticate to CARTO account
auth_client = APIKeyAuthClient(CARTO_BASE_URL, CARTO_API_KEY, organization)
dataset_manager = DatasetManager(auth_client)

# SQL wrapper

sql = SQLClient(APIKeyAuthClient(CARTO_BASE_URL, CARTO_API_KEY))


current_database = "SELECT current_database()"
result_dat = sql.send(current_database)



for k,v in result_dat.items():
  if k == 'rows':
    for itr in v:
      data_base = itr['current_database']



queries = "SELECT pid, query from pg_stat_activity WHERE datname = '" + data_base + "'"
result = sql.send(queries)
for key, value in result.items():
  if key == 'rows':
    for itr in value:
      print itr

