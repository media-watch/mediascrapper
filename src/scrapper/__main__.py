import logging as lg 
from src.scrapper.dataLoader import DataLoader
# from src.app import App

_logger = lg.getLogger(__name__)

sources = [
    {
        "website": "leaders",
        "url": "https://www.leaders.com.tn/article/32138-les-revelations-de-mohamed-abbou-les-derniers-jours-de-fakhfakh-a-la-kasbah"
    },
    {
        "website": "realites",
        "url": "https://www.realites.com.tn/2021/07/le-japon-dispose-a-aider-la-tunisie-dans-sa-lutte-contre-le-covid-19/"
    },
    {
        "website": "lapresse",
        "url": "http://lapresse.tn/103337/le-japon-dispose-a-aider-la-tunisie-dans-sa-lutte-contre-la-pandemie/"
    }
]

def setup_logging():
    # capture warnings issued by the warnings module
    lg.captureWarnings(True)

    logger = lg.getLogger()
    logger.setLevel(lg.DEBUG)

    # Configure stream logging if applicable
    stream_handler = lg.StreamHandler()
    stream_handler.setLevel(lg.INFO)

    fmt = "%(asctime)s %(levelname)s %(name)s: %(message)s"
    stream_handler.setFormatter(lg.Formatter(fmt))
    logger.addHandler(stream_handler)

def main():
    setup_logging()    
    loaders = [DataLoader(source) for source in sources]
    for loader in loaders:
        loader.start()

if __name__ == '__main__':
    main()
    