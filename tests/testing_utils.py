# testing_utils.py

def at_least_one_set(response):
    """Make sure that there is at least one set in the DB
    """
    assert response.json().get("total") > 0