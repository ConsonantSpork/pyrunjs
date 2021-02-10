from .abstract import AbstractBackend


__all__ = ['V8Backend']


class V8Backend(AbstractBackend):
    """This backend uses v8."""

    def run(self, func=None, fargs=None):
        """
        run js code with libraries and return result as
            python string or as dict

        :param str func: (optional) js function name
        :param list fargs: (optional) list of js function args

        :raise syntaxerror: js syntax error or runtime error
        """

        raise NotImplementedError()
