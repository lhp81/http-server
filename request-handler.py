def parse_request(request):
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
