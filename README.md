# CMPUT 401 Assignment 1: Tests

Here are the public tests that you may use to check your API. We will use different (but mostly similar) tests for marking.

## Installation

Clone the repo.

Set up Python 3 virtual environment.

```
python -m venv venv
source venv/bin/activate
```

Install required packages.

```
pip install -r requirements.txt
```

Update your host and port settings in `includes.yaml`. Leave `127.0.0.1` if you're running tests on the instance where your API is running. Otherwise, indicate the IPv6/IPv4 address or the hostname. Don't forget to set the correct port number.

Run the tests.

On Linux:

```
PYTHONPATH=$PYTHONPATH:tests pytest tests/ -v
```

On Windows (replace: `C:\my_folder` with your actual path to the `assignment1-tests`, don't forget to use quotes if your path includes spaces).

```
set PYTHONPATH=%PYTHONPATH%;C:\my_folder\assignment1-tests\tests
pytest tests/ -v
```

## Writing new tests

These tests use [Tavern](https://tavern.readthedocs.io/en/latest/index.html).

Feel free to develop more tests.
