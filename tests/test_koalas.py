# Show the data in the DataFrame.
from tkinter.font import names
import pytest
from assertpy import assert_that


def test_show_data_pandas(pandas_df):
    """Show the data in the DataFrame."""
    print(type(pandas_df))


# Show the data in the Koalas DataFrame.
def test_show_data_koalas(koalas_df):
    """Show the data in the Koalas DataFrame."""
    print(type(koalas_df))


# Create a new koalas DataFrame with the first 5 columns in the Koalas DataFrame.
def test_new_koalas_df(koalas_df):
    """Create a new koalas DataFrame with the first 5 columns in the Koalas DataFrame."""
    new_koalas_df = koalas_df.size()
    print(new_koalas_df)


# Show the first 5 rows in the Koalas DataFrame.
def test_show_first_5_rows(koalas_df):
    """Show the first 5 rows in the Koalas DataFrame."""
    print(koalas_df.head())


# Show the value of field at row 2 and column 3 in the Koalas DataFrame.
def test_value_at_row_2_col_3(koalas_df):
    """Show the value of field at row 2 and column 3 in the Koalas DataFrame."""
    print(koalas_df.at[2, 'Gender'])


# Convert the Koalas DataFrame to a spark DataFrame.
def test_convert_koalas_to_spark(koalas_df):
    """Convert the Koalas DataFrame to a spark DataFrame."""
    spark_df = koalas_df.to_spark()
    print(spark_df.show())


# Create a dataframe with people from France.
def test_people_from_france(koalas_df):
    """Create a dataframe with people from France."""
    people_from_france = koalas_df.to_spark().filter("Country == 'France'")
    people_from_france.show()


# Create a dataframe with people from France using Koalas.
def test_people_from_france_koalas(koalas_df):
    """Create a dataframe with people from France using Koalas."""
    people_from_france = koalas_df.loc[koalas_df['Country'] == 'France']
    print(people_from_france.values)


# Create a new koalas DataFrame with the first 5 columns in the Koalas DataFrame.
def test_five_columns_koalas_df(koalas_df):
    """Create a new koalas DataFrame with the first 5 columns in the Koalas DataFrame."""
    koalas_df.to_spark().select('First Name', 'Last Name', 'Gender', 'Age', 'Country').show(5)


# Create a koalas DataFrame with people that are younger than 30.
def test_people_younger_than_30(koalas_df):
    """Create a koalas DataFrame with people that are younger than 30."""
    people_younger_than_30 = koalas_df.loc[koalas_df['Age'] < 30]
    people_older_than_30 = koalas_df.loc[koalas_df['Age'] > 30]
    assert_that(people_younger_than_30.values).does_not_contain(people_older_than_30.values.any())
    print(people_younger_than_30)
    print(f'People older than 30 --------------------\n\n: {people_older_than_30.values}')


# Create a series with the first column of the Koalas DataFrame.
def test_series_first_column(koalas_df):
    """Create a series with the first column of the Koalas DataFrame."""
    series = koalas_df['First Name']
    print(series.to_numpy().size)


# Convert the Koalas DataFrame to numpy.
def test_convert_koalas_to_numpy(koalas_df):
    """Convert the Koalas DataFrame to numpy."""
    numpy_array = koalas_df.to_numpy().reshape(-1, 0)
    print(numpy_array)


# Convert the Koalas DataFrame to a pandas DataFrame.
def test_convert_koalas_to_pandas(koalas_df):
    """Convert the Koalas DataFrame to a pandas DataFrame."""
    pandas_df = koalas_df.to_pandas()

