# The data for the number employed at severla famus It companies is maintained in the COMPANY table. Write a query to print the IDs of the companies that have more than 10000 employees, in ascending order of ID.
import sqlite3
import os
import pytest


@pytest.fixture(scope="module")
def conn():
    conn = sqlite3.connect('test.db')
    yield conn
    conn.close()
    os.remove('test.db')


def get_company_ids_with_more_than_10000_employees():
    """:return: """
    return "SELECT ID FROM COMPANY WHERE EMPLOYEES > 10000 ORDER BY ID ASC;"
