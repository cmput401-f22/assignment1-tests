# testing_utils.py
def book_deleted(response, isbn13):
    """Make sure that the given book is deleted
    """
    assert not response.json().get("isbn13") == isbn13

def at_least_one_book(response):
    """Make sure that there is at least one book in the DB
    """
    assert response.json().get("total") > 0