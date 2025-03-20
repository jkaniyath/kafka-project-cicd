class ConfigError(Exception):
    """
        Custom exception class for configuration-related errors.

        This exception is raised when an error occurs in the `Config` class.

        Args:
            error_msg (str): The error message describing the issue.

        Attributes:
            message (str): The formatted error message.

        Example:
            ```python
            raise ConfigError("Invalid external storage location")
            ```
    """

    def __init__(self, error_msg:str):
        """
            Initializes the ConfigError exception with a formatted error message.

            Args:
                error_msg (str): The error message describing the issue.
        """
        super().__init__(f"Error occured in configuration class. Error message is {error_msg}")


class DatabaseCreationErrorHandler(Exception):
    """
        Custom exception raised when a database is not created before attempting to create tables.

        This exception is useful for handling cases where a required database is missing in a data pipeline.

        Args:
            db_name (str): The name of the database that was not found.

        Attributes:
            db_name (str): The name of the missing database.

        Example:
            ```python
            if not database_exists("bronze"):
                raise DatabaseCreationErrorHandler("bronze")
            ```

    """

    def __init__(self, db_name:str):
        """
            Initializes the exception with a message indicating that the database has not been created.

            Args:
                db_name (str): The name of the database that is missing.
        """

        super().__init__(
            f"Database '{db_name}' has not been created. Please ensure that the database '{db_name}' is created before attempting to create tables in this layer."
        )


class BronzeSetupError(Exception):
    """
        Custom exception raised when an error occurs during the Bronze layer setup.

        This exception is used to indicate failures specifically related to the Bronze setup process.

        Args:
            msg (str): The error message describing the failure.

        Attributes:
            message (str): A formatted error message including the provided `msg`.
        
        Example:
            ```python
            raise BronzeSetupError("Failed to create Bronze table")
            ```
    """

    def __init__(self, msg:str):
        """
            Initializes the BronzeSetupError exception with a formatted error message.

            Args:
                msg (str): The error message describing the failure.
        """
        super().__init__(
            f"Error occured while running bronze setup. Error message is {msg}"
        )


class IngestionError(Exception):
    """
        Custom exception class for handling errors during data ingestion.

        This exception is raised when an error occurs while ingesting data into a specific 
        database and table.

        Args:
            msg (str): The error message describing the issue.
            db_name (str): The name of the database where the error occurred.
            table_name (str): The name of the table where the error occurred.

        Attributes:
            msg (str): The original error message.
            db_name (str): The database name where ingestion failed.
            table_name (str): The table name where ingestion failed.

        Example:
            ```python
            raise IngestionError("Invalid data format", "bronze", "customer_data")
            ```
    """
    def __init__(self, msg:str, db_name:str, table_name:str):
        """
            Initializes the IngestionError exception with details about the failed ingestion.

            Args:
                msg (str): The error message describing the issue.
                db_name (str): The name of the database where the error occurred.
                table_name (str): The name of the table where the error occurred.
        """
        super().__init__(
            f"Error occured while ingesting data to {db_name}.{table_name}. Error message is {msg}")
        

class SilverSchemaError(Exception):
    def __init__(self, schema_list:list[str]):
        super().__init__(
            f"Error: The silver schema list should contain exactly five schemas in the following order: books, customers, orders, customers_orders, and books_sales. The provided list, {schema_list}, is incorrect.")
        

class SilverSetupError(Exception):
    def __init__(self, msg:str):
        super().__init__(
            f"Error occured while running bronze setup. Error message is {msg}"
        )

class UpsertError(Exception):
    def __init__(self, msg:str, func_name:str):
        super().__init__(
            f"Error occured while while running upsert function: {func_name}. Error message is {msg}")
        

class GoldSetupError(Exception):
    def __init__(self, msg:str):
        super().__init__(
            f"Error occured while running gold setup. Error message is {msg}"
        )