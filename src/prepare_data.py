import pandas as pd, sys, re
from pathlib import Path
from typing import List
from pandas import DataFrame, Index

def clean_col_names(index_of_cols: pd.Index):
    return [re.sub(r'[^a-zA-Z0-9\s]', '', col).lower().replace(r" ", "_") for col in index_of_cols]

def extract_dates(data: DataFrame) -> DataFrame:
    data['date'] = pd.to_datetime(data['date'], format="%d/%m/%Y")
    data.sort_values(['date', 'hour'], inplace=True)
    data["year"] = data['date'].dt.year
    data["month"] = data['date'].dt.month
    data["week"] = data['date'].dt.isocalendar().week
    data["day"] = data['date'].dt.day
    data["day_of_week"] = data['date'].dt.dayofweek
    data["day_of_year"] = data['date'].dt.dayofyear
    data["is_month_end"] = data['date'].dt.is_month_end
    data["is_month_start"] = data['date'].dt.is_month_start
    data["is_quarter_end"] = data['date'].dt.is_quarter_end
    data["is_quarter_start"] = data['date'].dt.is_quarter_start
    data["is_year_end"] = data['date'].dt.is_year_end
    data["is_year_start"] = data['date'].dt.is_year_start
    data.drop('date', axis=1, inplace=True)
    return data

def save_data(data: DataFrame, data_path: Path, file_name: str) -> None:
    if not data_path.exists(): data_path.mkdir(parents=True)
    data.to_parquet(data_path.joinpath(file_name), compression="snappy")

if __name__ == "__main__":
    
    # the path and files we need
    path = Path().cwd().joinpath('data', '02_part')
    raw_data_path = path.joinpath("raw", 'SeoulBikeData.csv')
    data_interim = path.joinpath("interim")
    file_name = 'clean_data.parquet'
    
    # get the data with its peculiar encoding
    data = pd.read_csv(raw_data_path, encoding='iso-8859-1')
    
    # start preparation process
    data.columns = clean_col_names(data.columns)
    data = extract_dates(data)
    data = pd.get_dummies(data=data, columns=['holiday', 'seasons', 'functioning_day'])
    
    # save it very snappily
    save_data(data, data_interim, file_name)
    print("File Cleaned Successfully!")
