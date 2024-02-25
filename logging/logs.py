import logging
import time
import datetime

def main():
    set_logger(logger_name=__name__, logLevel=logging.DEBUG, logFile="test.log")

    logger = logging.getLogger(__name__)

    for i in range(10):
        logger.critical(f"----- logger Message -----")
        logger.critical(f"  CRITICAL message")
        logger.error(f"  ERROR message")
        logger.warning(f"  WARNING message")
        logger.info(f"  INFO message")
        logger.debug(f"  DEBUG message")
        logger.critical(f"--------------------------")

        time.sleep(0.5)


def set_logger(logger_name, logLevel=logging.DEBUG, logFile="run.log"):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logLevel)
    # create file handler which logs even debug messages
    fh = logging.FileHandler(logFile)
    fh.setLevel(logLevel)
    # create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.ERROR)
    # create formatter and add it to the handlers
#     formatter = logging.Formatter(
#         "%(asctime)s\t%(levelname)s\t%(message)s", datefmt="%Y-%m-%dT%H:%M:%S%z\t(%Z)"
#     )
    formatter = ISOTimeFormatter("%(asctime)s\t%(levelname)s\t%(message)s")

    ch.setFormatter(formatter)
    fh.setFormatter(formatter)
    # add the handlers to logger
    logger.addHandler(ch)
    logger.addHandler(fh)

class ISOTimeFormatter(logging.Formatter):
    def formatTime(self, record: logging.LogRecord, datefmt=None):
        tz_jst = datetime.timezone(datetime.timedelta(hours=+9), 'JST')
        ct = datetime.datetime.fromtimestamp(record.created, tz=tz_jst)
        s = ct.isoformat(timespec="milliseconds")

        return s

if __name__ == "__main__":
    main()

