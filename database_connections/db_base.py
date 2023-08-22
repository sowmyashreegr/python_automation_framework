import pymysql
import yaml
import os
from utils import config_setup as mc, config_setup
import psycopg2

if mc.master_config()['environment'] == 'uat':
    database_shard_number = 1
else:
    database_shard_number = 0


def establish_connection(shard=None):
    if shard is None:
        shard_number = database_shard_number
    else:
        shard_number = shard

    if shard_number == 0:
        yaml_shard = 'default'
    elif shard_number == 1:
        yaml_shard = 'shard01'
    elif shard_number == 2:
        yaml_shard = 'shard02'
    elif shard_number == 3:
        yaml_shard = 'shard03'

    current_path = os.path.join(os.path.dirname(__file__), "../config/")
    yaml_path = f"{current_path}{mc.master_config()['environment']}/database.yml"

    with open(yaml_path) as file:
        config = yaml.load(file, Loader=yaml.FullLoader)[yaml_shard]

    if config_setup.master_config()['environment'] != 'uat':
        mydb = pymysql.connect(host=config['host'],
                               database=config['database'],
                               user=config['username'],
                               password=config['password'])
        return mydb
    else:
        mydb = pymysql.connect(host=config['host'],
                               database=config['database'],
                               user=config['username'],
                               password=config['password'],
                               ssl={"ssl_enabled": True})
        return mydb


def establish_hcm_service_database():
    postgres_connection = psycopg2.connect(database="hcm_service_production",
                            user='readonly',
                            password='STARTSELECT',
                            host='stage-hcm.plansource.com',
                            port='30517')

    return postgres_connection
