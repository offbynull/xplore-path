from antlr4.error.ErrorListener import ErrorListener


class ParseException(Exception):
    def __init__(self, message, line=None, column=None):
        super().__init__(message)
        self.line = line
        self.column = column


class RaiseParseErrorListener(ErrorListener):
    def __init__(self):
        super(RaiseParseErrorListener, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise ParseException(f'Syntax Error: {line}:{column} {msg}', line, column)

    # def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
    #     raise ParseException('Ambiguity Error')
    #
    # def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
    #     raise ParseException('Attempting Full Context Error')
    #
    # def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
    #     raise ParseException('Context Sensitivity Error')