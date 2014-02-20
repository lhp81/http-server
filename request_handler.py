def parse_request(request):
    """ Given a request, the first line is split off and checked for a
    GET request. Given a GET request, the requested uri is identified and
    returned. Anything other than GET raises a an Exception (405 error). """
    first_rn = request.find('\r\n')
    first_line = request[:first_rn]
    if first_line.split()[0] == 'GET':
        uri = first_line.split()[1]
        return uri
    else:
        raise ParseException("405: Method not allowed. Only GET is allowed.")

class ParseException(Exception):
    """An empty class to pass useful exceptions."""
    pass
