
import logging

# Create a logging object
logger = logging.getLogger()

# Create a file to write the log messages
fh = logging.FileHandler("a.log")

# Create a format in which the messgages needs to be put in to
fmt = logging.Formatter("%(levelname)s %(asctime)s %(message)s")

# Add the formatter to file handler
fh.setFormatter(fmt)

#Add the file handler to logger
logger.addHandler(fh)

# Set the level of logging. By default WaRNING is set
logger.setLevel(logging.INFO)

logger.debug("This is a DEBUG message")
logger.info("This is a INFO message")
logger.warning("This is a WARNING message")
logger.error("This is a ERROR message")
logger.critical("This is a CRITICAL message")