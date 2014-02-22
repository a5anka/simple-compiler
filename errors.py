#!/usr/bin/env python2

class EndOfFileError(Exception):
    def __str__(self):
        return repr("End of File")
