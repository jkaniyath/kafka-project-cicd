import logging
from datetime import datetime, timezone
from zoneinfo import ZoneInfo



class Logger:
      
    """
        A custom logger class for managing logging with a timestamp formatted according to a specified timezone.

        This class provides a logging mechanism where log files are named dynamically based on the date, 
        and timestamps are formatted according to the specified timezone.

        Attributes:
            logger_name (str): The name of the logger instance.
            log_file_prefix (str): The prefix for log file names.
            timestamp_zone (str): The timezone for logging timestamps.

        Args:
            logger_name (str, optional): The name of the logger. Defaults to `"KafkaBricks_Logger"`.
            log_file_prefix (str, optional): Prefix for log files. Defaults to `"kafkabricks_log"`.
            timestamp_zone (str, optional): The timezone for timestamps. Defaults to `"Europe/Riga"`.

        Example:
            ```python
            logger = Logger().get_logger()
            logger.info("This is an info message.")
            logger.error("This is an error message.")
            ```
    """
      
    def __init__(self, logger_name:str="KafkaBricks_Logger", log_file_prefix:str="kafkabricks_log", 
                 timestamp_zone:str = "Europe/Riga") -> None:
        """
            Initializes the Logger instance with a specified name, log file prefix, and timezone.

            Args:
                logger_name (str, optional): The name of the logger. Defaults to `"KafkaBricks_Logger"`.
                log_file_prefix (str, optional): Prefix for log files. Defaults to `"kafkabricks_log"`.
                timestamp_zone (str, optional): The timezone for timestamps. Defaults to `"Europe/Riga"`.
        """
        self.logger_name = logger_name
        self.log_file_prefix = log_file_prefix
        self.timestamp_zone = timestamp_zone

    def _format_logging_time(self, record, datefmt: str = None) -> str:
        
        """
            Formats the timestamp for log messages according to the specified timezone.

            Args:
                record (logging.LogRecord): The log record containing the timestamp.
                datefmt (str, optional): Date format string (ignored in this implementation).

            Returns:
                str: The formatted timestamp string in "YYYY-MM-DD HH:MM:SS" format.
        """

        local_time = datetime.fromtimestamp(record.created, tz=ZoneInfo(self.timestamp_zone))
        return local_time.strftime("%Y-%m-%d %H:%M:%S")
    
    
    def get_logger(self):

        """
            Creates and configures a logger instance.

            - Log files are stored in `/tmp/` with the format `{log_file_prefix}_YYYY-MM-DD.log`.
            - The logger writes logs at the `DEBUG` level.
            - If the logger already has handlers, they are cleared before adding a new file handler.

            Returns:
                logging.Logger: The configured logger instance.

            Example:
                ```python
                logger = Logger().get_logger()
                logger.info("This is a log message.")
                ```
        """

        # Get current UTC time
        utc_timestamp = datetime.now(timezone.utc)

        # Convert UTC to local timestamp
        local_timestamp = utc_timestamp.astimezone(ZoneInfo(self.timestamp_zone))


        logfile_prefix = self.log_file_prefix
        file_date = local_timestamp.strftime('%Y-%m-%d')
        log_file_name = f'{logfile_prefix}_{file_date}.log'

       
        log_dir = "/tmp/"
        # Construct the full path for the log file
        log_file = f'{log_dir}{log_file_name}'

 
        logger = logging.getLogger(self.logger_name)
        logger.setLevel(logging.DEBUG)

        file_handler = logging.FileHandler(log_file, mode='a')
        logging.Formatter.formatTime = self._format_logging_time
        formatter = logging.Formatter('%(levelname)s:%(asctime)s:%(message)s')
        file_handler.setFormatter(formatter)

        if logger.hasHandlers():
            logger.handlers.clear()

        # add handlers
        logger.addHandler(file_handler)


        return logger
    





