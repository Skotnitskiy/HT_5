categories_list = ["skstories", "showstories", "newstories", "jobstories"]
default_categorie = "newstories"
results_path = "../results/"
rep_file_name = "report.csv"
log_file_name = "hn_parser.log"
categorie_url = "https://hacker-news.firebaseio.com/v0/{}.json?print=pretty"
item_url = 'https://hacker-news.firebaseio.com/v0/item/{}.json?print=pretty'
dictLogConfig = {
    "version": 1,
    "handlers": {
        "fileHandler": {
            "class": "logging.FileHandler",
            "formatter": "logFormatter",
            "filename": results_path + log_file_name
        }
    },
    "loggers": {
        "DataParserApp": {
            "handlers": ["fileHandler"],
            "level": "INFO",
        }
    },
    "formatters": {
        "logFormatter": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        }
    }
}
