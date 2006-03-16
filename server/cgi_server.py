#!/usr/bin/env python
"""$URL: svn+ssh://svn.mems-exchange.org/repos/trunk/quixote/server/cgi_server.py $
$Id: cgi_server.py 27684 2005-11-10 15:25:17Z dbinger $
"""

import sys
import os

def run(create_publisher):
    if sys.platform == "win32":
        # on Windows, stdin and stdout are in text mode by default
        import msvcrt
        msvcrt.setmode(sys.__stdin__.fileno(), os.O_BINARY)
        msvcrt.setmode(sys.__stdout__.fileno(), os.O_BINARY)
    publisher = create_publisher()
    response = publisher.process(sys.__stdin__, os.environ)
    try:
        response.write(sys.__stdout__)
    except IOError, err:
        publisher.log("IOError while sending response ignored: %s" % err)


if __name__ == '__main__':
    from quixote.demo import create_publisher
    run(create_publisher)
