import argparse
import config as conf

parser = argparse.ArgumentParser(description='Data parse.')
parser.add_argument('-c', action="store", dest="categorie", default=conf.default_categorie,
                    choices=conf.categories_list)

