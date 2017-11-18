import argparse
import os
import config as conf

parser = argparse.ArgumentParser(description='Data parse.')
parser.add_argument('-c', action="store", dest="categorie", default=conf.default_categorie,
                    choices=conf.categories_list)
# create dir
if not os.path.exists(conf.results_path):
    os.mkdir(conf.results_path)

# create report.csv if not exists
if not os.path.exists(conf.results_path + conf.rep_file_name):
    f = open(conf.results_path + conf.rep_file_name, "w")
