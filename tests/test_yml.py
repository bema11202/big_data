from importlib.resources import files
from operator import is_

import yaml
from assertpy import assert_that
from pandas.compat.numpy.function import validate_min


# Create a dataframe using the yml file.
def test_create_yml_df(test_read_yaml_into_df):
    """Read yaml file using open method."""
    assert_that(test_read_yaml_into_df).is_not_none()
    print(test_read_yaml_into_df)


# Find all vmImages that are in the response body.
def test_find_all_vmImages(test_read_yaml_into_df):
    """Find all vmImages that are in the response body."""
    assert_that(test_read_yaml_into_df).is_not_none()
    validate_vm = (test_read_yaml_into_df.get("pool").get("vmImage"))
    assert_that(validate_vm).is_equal_to("ubuntu-latest")


# Open the csv file in the test_read_yaml_into_df fixture with task's archiveType equal to csv.
def test_open_csv_file(test_read_yaml_into_df):
    """Open the csv file in the test_read_yaml_into_df fixture with task's archiveType equal to csv."""
    assert_that(test_read_yaml_into_df).is_not_none()
    csv_file = (test_read_yaml_into_df.get("steps")[2].get("inputs").get("inputs")["archiveType"])
    arc_file = (test_read_yaml_into_df.get("steps")[2].get("inputs").get("inputs")["archiveFile"])
    for i in csv_file:
        if i == "csv":
            with open(arc_file.value) as file:

                # convert the yaml file to a json file
                df = yaml.load(file, Loader=yaml.FullLoader)
            print(df)
        else:
            print(csv_file)

# Check if the csv file has the expected columns.
