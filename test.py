import unittest

def x(request):
    # here I need to get a new string that goes from start to first '\r\n'
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

# tests to see if non-get requests raise an exception
class ExceptionTest(unittest.TestCase):

    def testFailUnlessRaises(self):
        self.failUnlessRaises(ParseException, x, 'POST /index.html HTTP/1.1 \
                        Host: www.example.com \
                        <CRLF>')




if __name__ == '__main__':
    unittest.main()