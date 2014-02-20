def x(request):
    if request.split()[0] == 'GET':
        uri = request.split()[1]
        return uri
    else:
        raise ParseException("405: Method not allowed. Only GET is allowed.")

class ParseException(Exception):
    """An empty class to pass useful exceptions."""
    pass

