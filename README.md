http-server
===========
Currently the two files are:

* **request_handler.py** This takes a request, splits off the first line, and checks for the GET request. If the request is anything other than GET, an Exception is raised.
If the request is a GET request, the uri is then passed along.

* **test.py** The tests at this point are quite simple. One passes along POST, DELETE, and PUT requests to check that an exception is raised. The other passes a GET request and makes sure that the correct is returned.

The above represent my original work. **request_handler.py** will be merged with work from my classmates to make a working http server.