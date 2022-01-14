# testing_utils.py

def coffee_deleted(response, id):
    """Make sure that the given coffee is deleted
    """
    assert not response.json().get("id") == id

def at_least_one_coffee(response):
    """Make sure that there is at least one coffee in the DB
    """
    assert response.json().get("total") > 0