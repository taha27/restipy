# restipy

A simple project to learn about REST API development in Python

## Requirements

### Python

`restipy` has been written to work in and tested with **Python 3.6+**, and as such a compatible version of python needs to be installed on the system where `restipy` will be run.

### MongoDB

`restipy` relies on a mongodb server for storage and retrieval of information. For `restipy` to know the location of the mongodb instance, an environment variable named **RESTIPY_DB_URI** needs to be set before starting the server, which can be set using the following command:

```sh
echo "export RESTIPY_DB_URI=mongodb://[username:password@]host[:port>][/db]" >> ~/.bash_profile
```

In the command above, everything denoted in square brackets is optional and depends on how the mongodb instance is set up. More detailed information on the URI format can be found [here][1].

## Installation and Start-up

This `Flask` http server can be run with a few simple commands:

```sh
git clone https://github.com/taha27/restipy.git
cd restipy
python3 -m pip install requirements.txt
python3 server.py
```

## Testing

### Test Suite

The included test cases can be run using the python `unittest` module by running the following command from the project's root directory:

```sh
python3 -m unittest test_lib/test_cases/*test.py
```

### Test Coverage

The test coverage can be determined by using the python `coverage` package.

First, install `coverage` using the following command:

```sh
python3 -m pip install coverage
```

Then, run the following commands from `restipy`'s root directory to determine and display the coverage statistics:

```sh
coverage run --source api/companies -m unittest discover -p "*_test.py"
coverage report -m
```

[1]: https://docs.mongodb.com/manual/reference/connection-string/
