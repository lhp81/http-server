http-server
===========
This is an http server that can serve images and files. It was created as a join effort; my collaborators on the project were [Matt Dougherty](https://github.com/geekofalltrades) and [James White](https://github.com/jwhite007).

I created the request parser, Matt wrote the uri mapper, and James wrote the original code for the response builder.

I have used Matt's original and implemented suggestions from [Cris Ewing](https://github.com/cewing/) during our in-class code rewview.

The files are:

* **request_handler.py** This takes a request, splits off the first line, and checks for the GET request. If the request is anything other than GET, an Exception is raised.
If the request is a GET request, the uri is then passed along.

* **test.py** The tests at this point are quite simple. One passes along POST, DELETE, and PUT requests to check that an exception is raised. The other passes a GET request and makes sure that the correct is returned.

* **http-server.py** is the result of **request_handler.py** being merged with work from my classmates to create.

