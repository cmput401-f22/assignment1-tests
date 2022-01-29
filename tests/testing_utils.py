# testing_utils.py

def at_least_one_coffee(response):
    """Make sure that there is at least one coffee in the DB
    """
    assert response.json().get("total") > 0