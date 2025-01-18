"""Custom ANTLR error / warning handlers."""

from antlr4.error.ErrorListener import ErrorListener


class ParseException(Exception):
    """Exception indicating an ANTLR parse error."""

    def __init__(self, message, line=None, column=None):
        """
        Construct a ``ParseException`` object.
        :param message: Error message.
        :param line: Error line number.
        :param column: Error column number.
        """
        super().__init__(message)
        self.line = line
        self.column = column


class RaiseParseErrorListener(ErrorListener):
    """
    An ANTLR error listener that generates a ``ParseException`` on any syntax error.
    """
    def __init__(self):
        """
        Construct a ``RaiseParseErrorListener`` object.
        """
        super(RaiseParseErrorListener, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise ParseException(f'Syntax Error: {line}:{column} {msg}', line, column)

    # def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
    #     text_segment = recognizer.getInputStream().getText(startIndex, stopIndex)
    #     raise ParseException(f'Ambiguity Error\n\n'
    #                          f'Ambiguity from {startIndex} to {stopIndex}: "{text_segment}"\n'
    #                          f'{ambigAlts=}, {configs=}, {dfa=}')
    #
    # def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
    #     raise ParseException('Attempting Full Context Error')
    #
    # def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
    #     raise ParseException('Context Sensitivity Error')