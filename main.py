import argparse
import os
import logging.config
import requests
import pprint

import config as conf

logging.config.dictConfig(conf.dictLogConfig)
logger = logging.getLogger("DataParserApp")
logger.info("Program started")

parser = argparse.ArgumentParser(description='Data parse.')
parser.add_argument('-c', action="store", dest="categorie", default=conf.default_categorie,
                    choices=conf.categories_list)
args = parser.parse_args()
# create dir
if not os.path.exists(conf.results_path):
    os.mkdir(conf.results_path)
    logger.info("results dir created")
else:
    logger.info("results directory already exists")

# create report.csv if not exists
if not os.path.exists(conf.results_path + conf.rep_file_name):
    f = open(conf.results_path + conf.rep_file_name, "w")
    logger.info("file", conf.rep_file_name, "created")
else:
    logger.info("file " + conf.rep_file_name + " already exists")
request = requests.get(conf.categorie_url.format(args.categorie))
pprint.pprint(request.json())
