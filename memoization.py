import datetime

# (ttl - Time to Live) and (dt - Date Time)

# Dictionary for adding resolver keys and memoize value when resolver is pass
# Dictionary timeout for calculating and deleting memoize value when time is exceeded
dictMemoize = {}
dictTimeout_dictMemoize = {}

# List for adding memoize value when resolver is not pass hence (None)
# List timeout for calculating and deleting memoize value when time is exceeded
lstMemoize = []
lstTimeout_lstMemoize = {}


# Return resolver key for memoization value
def resolver(varResolver):
    if type(varResolver) is tuple:
        return varResolver[0]
    else:
        return varResolver


def memoize(varMemoizeValue, varResolver, intTimeout: int):
    # Get resolver key even when multiple arguments are given, only doesn't get called when it is (None)
    if varResolver is not None:
        varResolver = resolver(varResolver)

    # dtCurrent = Get current time
    # ttlMemoizeValue = Current Time + Timeout Time (offset) -> for deleting memoize value in dict or list
    dtCurrent = datetime.datetime.now()
    ttlMemoizeValue = dtCurrent + datetime.timedelta(milliseconds=intTimeout)

    # If resolver key is None than memoize value is stored in list
    if varResolver is None:
        # If their is no memoize value in list then memoize value is stored in list
        # as well as TTL for memoize value is stored in lstTimeout_lstMemoize dict
        # with the Key of memoize value
        if varMemoizeValue not in lstMemoize:
            lstMemoize.append(varMemoizeValue)
            lstTimeout_lstMemoize[varMemoizeValue] = ttlMemoizeValue

        # If memoize value is in the list and current date time is now greater than
        # timeout of memoize value, the old memoize value and timeout are deleted
        # and new memoize value and timeout are saved
        elif dtCurrent > lstTimeout_lstMemoize[varMemoizeValue]:
            lstMemoize.remove(varMemoizeValue)
            del lstTimeout_lstMemoize[varMemoizeValue]
            lstMemoize.append(varMemoizeValue)
            lstTimeout_lstMemoize[varMemoizeValue] = ttlMemoizeValue

        return varMemoizeValue

    # If resolver key is provided than memoize value is stored in dictionary
    else:
        # If their is no memoize value in dictionary then memoize value is stored in dictionary
        # as well as TTL for memoize value is stored in dictTimeout_dictMemoize
        # with the Key as resolver key
        if varResolver not in dictMemoize.keys():
            dictMemoize[varResolver] = varMemoizeValue
            dictTimeout_dictMemoize[varResolver] = ttlMemoizeValue
            
        # If memoize value is in the dictionary and current date time is now greater than
        # timeout of memoize value, the old memoize value and timeout are deleted
        # and new memoize value and timeout are saved
        elif dtCurrent > dictTimeout_dictMemoize[varResolver]:
            del dictMemoize[varResolver]
            del dictTimeout_dictMemoize[varResolver]
            dictMemoize[varResolver] = varMemoizeValue
            dictTimeout_dictMemoize[varResolver] = ttlMemoizeValue

        return dictMemoize[varResolver]
