
class Error(Exception):
    pass


class UnknownError(Error):
    pass


class EmptyKey(Error):
    pass


class IncorrectKey(Error):
    pass


class WrongType(Error):
    pass


class WrongFields(Error):
    pass


class TooManyRequests(Error):
    pass


class IncorrectID(Error):
    pass


class IncorrectIDEntityRelated(Error):
    pass


class IPBlock(Error):
    pass


class APIDisabled(Error):
    pass


class KeyOwnerFederalJail(Error):
    pass


class KeyChangeError(Error):
    pass


class KeyReadError(Error):
    pass
