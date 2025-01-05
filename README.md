YOU CAN INTEGRATE YOUR OWN FILE TYPES: scene graphs, flow cytometry data, custom APIs

1. ensure you have python and poetry installed
2. git clone the repository: `git clone https://github.com/offbynull/xplore-path.git`
3. navigate to cloned project: `cd xplore-path`
4. `poetry intall`
5. `poetry shell`
6. `xplore-path --path ./playground`
pip install poetry
poetry install
poetry shell
cd playground
xplore-path

# Inspect root
/*          # List all files
$count(/*)  # Count number of files

# Inspect mouse assays
/mouse_assays.zip/*                                           # List individual mouse assays
/mouse_assays.zip/Mouse_Assay_001.csv//*                      # List first mouse assay's data
/mouse_assays.zip/r'.*001.csv'//*                             # List first mouse assay's data, using regex
/mouse_assays.zip/g'*001.csv'//*                              # List first mouse assay's data, using glob
label /mouse_assays.zip/Mouse_Assay_001.csv/0/*               # List first mouse assay's headers (labels in first row)
/mouse_assays.zip//*/GO_Term                                  # For each assay, list all values under the GO terms column
/mouse_assays.zip//*/GO_Term[. = g'GO:*']                     # For each assay, list all values under the GO terms column starting with "GO:" (these are the actual GO terms)
/mouse_assays.zip//0/GO_Term                                  # For each assay, list first value under the GO terms column (these are the actual GO terms)
$distinct(/mouse_assays.zip//0/GO_Term)                       # Across all assays, list distinct GO terms
$frequency_count(/mouse_assays.zip//0/GO_Term)//*             # Across all assays, count how often each GO term appears


# Well data
position /mouse_assays.zip/Mouse_Assay_001.csv/*[.//*=Well]   # Get row where Well data starts
label /mouse_assays.zip/Mouse_Assay_001.csv/*[.//*=Well]      # Get row where Well data starts (using label instead of position)
/mouse_assays.zip/Mouse_Assay_001.csv/*[position . > position /mouse_assays.zip/Mouse_Assay_001.csv/*[.//*=Well]]//* # Truncate rows to those after Well


# Inspect mouse GO terms
/goslim_mouse.json//*                                                         # List all
/goslim_mouse.json//*[./meta//val = g'*neuro*']//*                            # List only related to neuro
/goslim_mouse.json//*[./meta//val = g'*neuro*']//id                           # List only related to neuro, ids only
/goslim_mouse.json//*[./meta//val = g'*neuro*']//lbl                          # List only related to neuro, labels only
/goslim_mouse.json//*[./meta//val = g'*neuro*']//(id, lbl)                    # List only related to neuro, ids and labels
/goslim_mouse.json//*[./meta//val = g'*neuro*']//r'id|lbl'                    # List only related to neuro, ids and labels using regex
$regex_extract(/goslim_mouse.json//*[./meta//val = g'*neuro*']//id, '\d{7}')  # List only related to neuro, cleaned ids only


# Get GO terms in assays related to neuro
$distinct(/mouse_assays.zip/*/0/GO_Term)                 # List GO terms in assays
/goslim_mouse.json/graphs//*[./meta/definition/val = g'*neuro*']  # List GO terms related to neuro
($distinct(/mouse_assays.zip/*/0/GO_Term) inner join /goslim_mouse.json/graphs//*[./meta/definition/val = g'*neuro*'] on [$regex_extract(//l, '\d{7}') = $regex_extract(//r//id, '\d{7}')]) # List GO terms in assays related to neuro


* ~~TODO: add join syntax - inner, left, right~~
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
* ~~TODO: xml and html parser - tag value should be returned directly as opposed to going inside .text child~~
* ~~TODO: test matchers raw~~
* ~~TODO: REPL should autocomplete variable names~~
* ~~TODO: test matchers when used in = and !=~~
* ~~TODO: test paths~~
* ~~TODO: test paths with predicates~~
* ~~TODO: test matchers when used in path predicates~~
* TODO: test join syntax more
  * left non-path with right path
  * left path with right non-path
  * left and right both path
  * left and right both non-path
  * left and right empty / one empty but not the other
  * when in condition, root MUST BE THE TEST OBJECT as opposed to the actual root (e.g. if it wasn't, //l = //r would search everything for a tag named l and r)
* TODO: update syntax so variable calls can go into path expression without wrapping e.g. $var(a,b,c)/d/e instead of ($var(a,b,c))/d/e 
* TODO: test complex math (order of operations)
* TODO: evalutor context - hide direct access to context varaibles
* TODO: evaluator: entities -> sequence
* ~~TODO: test label directive~~
* ~~TODO: ../* doesn't work because th parser doesn't recognize it~~
* TODO: test function invocations syntax
    ~~BUG comma misinterpreted func(a,b) interpretes args as a single argument of [a,b]~~
* TODO: function invocation 
* TODO: test code in the invocables package
* TODO: cache all_children() in PythonObjectPath + stream all_children() in other paths + take in max argument to cap number of children
* ~~BUG: path.py label tests are no good because multiple children can have same mame~~
     ~~if p.label() == self.label()    CHANGE THIS TO    if p.position_in_parent() == self.position_in_parent()~~
* ~~BUG: //* must be returned in DOCUMENT ORDER, right now its not~~
   ~~instead using list as the collection holding paths, use a custom type Sequence? just to help differentiate / reason better~~
   ~~MUST ALSO DEDUPLICATE if not concatenating~~
* ~~TODO: test filesystem file loaders~~
* TODO: make use of variables in REPL - store results in var names and use those var names in queries
* ~~TODO: test join syntax~~
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