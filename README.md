* TODO: add join syntax - inner, left, right
* ~~TODO: add distinct/unique syntax - just coerce it into a set~~
* ~~TODO: add count syntax - just coerce it into a set~~~~
* ~~TODO: add 'frequency count' syntax to count value collisions?~~
* TODO: add 'histogram' function to generate histogram?
* ~~TODO: add 'strip'/'collapse' to trim leading/trailing whitespace + collapse multiple contig whitespace to single~~
  much of the above is be added in as variable functions
    make the following variable functions? "to", "intersect", "union", etc.. -- maybe not the set operations, but definitely "to"
* TODO: comparison operators - ADD MODIFIER THAT MAKES IT STRICT (no coercions allowed except int/float)
* ~~TODO: add string concat operator back in~~
* ~~TODO: add label directive to extract label name~~
* ~~TODO: new matcher to test ignorecase~~
* ~~TODO: new matcher to test if a number is "close to" - floating point check~~
* ~~TODO: new matcher to test for a number range  start:stop OR start:stop wrapped in square/curved parenthesis for inclusive/exclusive~~
* ~~TODO: test matchers more thoroughly~~
* ~~TODO: matchers need to be applied properly if one of the operands is ==~~
* ~~TODO: add invocations into atomicorencapsulation~~
* ~~TODO: filesystem path~~
* ~~TODO: filesystem path support for zips, tars, and tar.gz~~
* ~~TODO: filesystem add caching layer~~ (not great, but workable for now)
* TODO: filesystem path - for each parsed file, inject invocations that can re-work the file
* TODO: change syntax so keywords must be followed by ::, ENFORCE IN LEXER (so people can still use the keywords as-is)
* TODO: add callback that notifies of what's happening when evaluation is running
* ~~TODO: html parser~~
* TODO: xml and html parser - tag value should be returned directly as opposed to going inside .text child
* ~~TODO: test matchers raw~~
* ~~TODO: REPL should autocomplete variable names~~
* TODO: test matchers when used in path predicates
* TODO: test matchers when used in = and !=
* TODO: test paths
* TODO: test paths with predicates
* TODO: test complex math (order of operations)
* TODO: test label directive
* TODO: test function invocations syntax
* TODO: test code in the invocables package
* ~~TODO: test filesystem file loaders~~
* TODO: make use of variables in REPL - store results in var names and use those var names in queries
* ~~TODO: ANTLR grammar rule names must be fixed - make rules camelcase~~
* ~~TODO: REPL/CLI filesystem add option to pre-cache on launch - just get //* and output results after the fact~~
* ~~TODO: filesystem notify of caching/loadings ops~~
* TODO: Cache results for each call to expr(), reset it every time xplore() called
    this doesn't work because ./b and ./b will hit the same cache, but the result may be different depending on context
    how to work around this?
      rather than just caching on expr().getText(), cache on the full path the parser took? - that wont work /a/b/c[./d=5] - ./d=5 part wil
    factor in self.context somehow to disambiguate? pickle it and mix it with expr().getText() to get cache key?
    NEW PLAN:
      cache based on the operation being performed WITH full paths as operands
          - if operation is happening on a root path, cache it - it'll always be hte same
          - if operation is happening on a context path, convert it to a root path and cache it
       e.g. /a/b/c/*[./e = /x/f]
         for each child of c, the cache key predicate expands ./e to full pat
            /a/b/c/d1 and what gets cached is key '/a/b/c/d1/e = /x/e'
            /a/b/c/d2 and what gets cached is key '/a/b/c/d2/e = /x/e'
         once that's complete, /a/b/c/*[./e = /x/f] itself gets cached (it's already root path, no conversion needed)
       CAVEAT: some paths are dynamically generated (e.g. results from function callsm such as frequency_count), so you should also also check to see if the root object is the same when checking cache 
* TODO: Python object path, put in invocable members
* TODO: Python object path, value override
* ~~TODO: wrap evaluate() in a new class that can be passed around~~
    ~~add context object to new class - repl can use context object to access variables~~
    ~~repl can use this context obj to autocomplete variables~~
* ~~TODO: sqlite support~~
* TODO: instead using list as the collection holding paths, use a custom type Sequence? just to help differentiate / reason better