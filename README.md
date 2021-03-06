http-server
===========
This is an http server that can serve images and files. It was created as a join effort; **my collaborators on the project were [Matt Dougherty](https://github.com/geekofalltrades) and [James White](https://github.com/jwhite007).**

I created the request parser, Matt wrote the uri mapper and contributed the server code, and James wrote the original code for the response builder.

I have built from Matt's original, leaving some code as is and also implementing suggestions from [Cris Ewing](https://github.com/cewing/) during our in-class code review.

The files are:

* **request_handler.py** This takes a request, splits off the first line, and checks for the GET request. If the request is anything other than GET, an Exception is raised.
If the request is a GET request, the uri is then passed along.
This was my original contribution. The 'first draft' is commented out and replaced with the current version, which was based off our in-class code review.

* **test.py** The tests at this point are quite simple. One passes along POST, DELETE, and PUT requests to check that an exception is raised. The other passes a GET request and makes sure that the correct is returned.

* **http-server.py** is the result of **request_handler.py** being merged with work from my classmates to create a working server. Some code is verbatim from my classmates, much has been tweaked by me based upon code review or my own ideas.

