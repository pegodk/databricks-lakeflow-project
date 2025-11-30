"""
Utility functions for the Lakehouse Framework.

This module provides common utility functions used across the lakeflow pipelines.
"""

from typing import Optional


def get_spark_config(key: str, default: Optional[str] = None) -> Optional[str]:
    """
    Get a Spark configuration value.
    
    Args:
        key: Configuration key to retrieve
        default: Default value if key not found
        
    Returns:
        Configuration value or default
    """
    try:
        from pyspark.sql import SparkSession
        spark = SparkSession.getActiveSession()
        if spark:
            return spark.conf.get(key, default)
        return default
    except Exception:
        return default


def add_metadata_columns(df):
    """
    Adds metadata columns to the input DataFrame.

    Parameters:
        df (DataFrame): Input Spark DataFrame.

    Returns:
        DataFrame: DataFrame with an additional 'ingest_timestamp' column containing the current timestamp.
    """
    from pyspark.sql.functions import current_timestamp
    return df.withColumn("ingest_timestamp", current_timestamp())

