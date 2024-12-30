* TODO: add join syntax - inner, left, right
* TODO: add distinct/unique syntax - just coerce it into a set
* ~~TODO: add string concat operator back in~~
* ~~TODO: add label directive to extract label name~~
* ~~TODO: new matcher to test ignorecase~~
* ~~TODO: new matcher to test if a number is "close to" - floating point check~~
* ~~TODO: new matcher to test for a number range  start:stop OR start:stop wrapped in square/curved parenthesis for inclusive/exclusive~~
* ~~TODO: test matchers more thoroughly~~
* ~~TODO: matchers need to be applied properly if one of the operands is ==~~
* TODO: add invocations into atomicorencapsulation
* ~~TODO: filesystem path~~
* ~~TODO: filesystem path support for zips, tars, and tar.gz~~
* ~~TODO: filesystem add caching layer~~ (not great, but workable for now)
* TODO: filesystem path - for each parsed file, inject invocations that can re-work the file
* TODO: change syntax so keywords must be followed by ::, ENFORCE IN LEXER (so people can still use the keywords as-is)
* TODO: add callback that notifies of what's happening when evaluation is running
* ~~TODO: html parser~~
* TODO: xml and html parser - tag value should be returned directly as opposed to going inside .text child
* ~~TODO: test matchers raw~~
* TODO: test matchers when used in path predicates
* TODO: test matchers when used in = and !=
* TODO: test paths
* TODO: test paths with predicates
* TODO: test complex math (order of operations)
* TODO: test label directive
* ~~TODO: test filesystem file loaders~~
* TODO: make use of variables in REPL - store results in var names and use those var names in queries
* ~~TODO: ANTLR grammar rule names must be fixed - make rules camelcase~~
* ~~TODO: REPL/CLI filesystem add option to pre-cache on launch - just get //* and output results after the fact~~
* ~~TODO: filesystem notify of caching/loadings ops~~