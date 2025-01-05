# Xplore Path

Xplore Path is a tool for quick-and-dirty data exploration, designed for messy data spread across disparate files and formats.

 * **Simple syntax**: Query data with an intuitive, XPath-like syntax.
 * **Broad format support**: Search through CSVs, XLSXs, JSONs, YAMLs, DOCXs, PDFs, XMLs, HTMLs, ...
 * **Fuzzy search support**: Search using globs, regex, number ranges, or approximate string matching.
 * **Unified environment**: Search through disparate files and formats within a single context.
 * **Extendable**: Add functions and formats to customize to your use case (e.g. 3D scene graphs, flow cytometry, ...).

Xplore Path aims to be the first tool you reach for when inspecting / exploring new data "thrown over the wall" by a colleague or partner. It does not aim to be a database or a storage engine.

## Quick-Start Guide

The easiest way to get familiar with Xplore Path is to jump right in:

1. `python --version && pip install poetry` - Ensure Python and Poetry are installed.
2. `git clone https://github.com/offbynull/xplore-path.git` - Clone the repository.
3. `cd xplore-path` - Enter the cloned repository.
4. `poetry install` - Install the package.
5. `poetry shell` - Activate the package's environment. 
6. `xplore-path --path ./playground` - Launch the Xplore Path REPL.

The last step launches the Xplore Path REPL and sets the active directory to `./playground`, which contains dummy data (a mix of fabricated biological and general-purpose data).

![Screenshot of REPL interface](repl_example.png)

Queries use a syntax inspired by XPath, where the start of the hierarchy is the `./playground` directory. Try running a few of the example queries shown below.

<details><summary>Example queries</summary>

* `/*` - List top-level files.
* `$count(/*)` - Count top-level files.
* `//*` - List all data.
* `/mouse_assays.zip/*` - List mouse assays.
* `/mouse_assays.zip/Mouse_Assay_001.csv//*` - List first mouse assay's data.
* `/mouse_assays.zip/r'.*001.csv'//*` - List first mouse assay's data, but using regex to identify the first assay.
* `/mouse_assays.zip/g'*001.csv'//*` - List first mouse assay's data, but using glob to identify the first assay.
* `/goslim_mouse.json//*` - List mouse gene ontology entries.
* `/goslim_mouse.json//*[./meta//val = g'*neuro*']//*` - List mouse gene ontology entries related to neuro.
* `/goslim_mouse.json//*[./meta//val = g'*neuro*']//id` - List mouse gene ontology entries related to neuro, ids only.
* `/goslim_mouse.json//*[./meta//val = g'*neuro*']//lbl` - List mouse gene ontology entries related to neuro, labels only.
* `/goslim_mouse.json//*[./meta//val = g'*neuro*']//(id, lbl)` - List mouse gene ontology entries related to neuro, ids and labels.
* `/goslim_mouse.json//*[./meta//val = g'*neuro*']//r'id|lbl'` - List mouse gene ontology entries related to neuro, ids and labels using regex.
</details>

<details><summary>Example queries with filtering</summary>

* `/mouse_assays.zip//*/GO_Term[. = g'GO:*']` - For each mouse assay, list the gene ontology terms used.
* `$regex_extract(/goslim_mouse.json//*[./meta//val = g'*neuro*']//id, '\d{7}')` - List mouse gene ontology related to neuro, cleaned ids only.
* `$distinct(/mouse_assays.zip//*/GO_Term[. = g'GO:*'])` - Across all mouse assays, list distinct gene ontology terms used.
* `$frequency_count(/mouse_assays.zip//*/GO_Term[. = g'GO:*'])//*` - Across all mouse assays,  count how often each gene ontology term appears.

</details>

<details><summary>Example queries with joins</summary>

* `($distinct(/mouse_assays.zip/*/0/GO_Term) inner join /goslim_mouse.json/graphs//*[./meta/definition/val = g'*neuro*'] on [$regex_extract(//l, '\d{7}') = $regex_extract(//r//id, '\d{7}')])` - Across all mouse assays, list gene ontology terms in the mouse assay that are related to neuro

The query above is made up of thw two sub-queries `$distinct(/mouse_assays.zip/*/0/GO_Term)` amd `/goslim_mouse.json/graphs//*[./meta/definition/val = g'*neuro*']`. The former lists grabs the distinct gene ontology terms used across all mouse assays and the latter pulls out gene ontology terms related to neuro. The results are then inner joined.

:warning: **Xplore Path joins are currently slow.** At the moment, the joining logic hasn't been optimized. Expect joins to be incredibly slow: O(n^2).
</details>


If you've used XPath before, the queries above should feel familiar as Xplore Path's query language is heavily inspired by XPath. In addition to basic XPath syntax, Xplore Path provides several major updates:

* Fuzzy matching is available in various forms.
  * Prefix a string with `g` for glob matching (e.g. `g'hello*'`).
  * Prefix a string with `r` for regex matching (e.g. `r'hello.*'`).
  * Prefix a string with `f` for approximate string matching (e.g. `f'hello world'`).
  * Prefix a string with `s` for strict matching, as in not fuzzy/approximate in any way (e.g. `s'hello world'`).
  * `~number:number` for number ranges, optionally using brackets to define open/closed-ness (e.g. `~[4:9)`)
  * `~number@tolerance` for number within some tolerance (e.g. `~3.14@0.0001`)
* Variables are denoted by a `$` followed by a word (e.g. `$distinct`), and may be called / searched.
* Queries are joinable using `inner join`, `left join`, and `right join`.

The example queries above utilize some of this new functionality. The full grammar is available at [XplorePathGrammar.g4](xplore_path/XplorePathGrammar.g4).

<details>
  <summary>:warning: Xplore Path is not a database</summary>

  Xplore Path is not a database. That is, it doesn't index data, optimize storage, or optimize queries as a traditional database does. Xplore Path works best when doing quick-and-dirty inspection/exploration on reasonable amounts of data. For example, imagine you're a scientist/analyst and a partner (e.g. university lab / contract research organization) has sent you a ZIP containing experiment results / assays, Xplore Path can act as an initial step to inspect the data.

</details>

<details>
  <summary>More queries to play around with</summary>

  ```
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
  ```

</details>

# TODO

* TODO: comparison operators - ADD MODIFIER THAT MAKES IT STRICT (no coercions allowed except int/float)
* TODO: filesystem path - for each parsed file, inject invocations that can re-work the file
* TODO: change syntax so keywords must be followed by ::, ENFORCE IN LEXER (so people can still use the keywords as-is)
* TODO: add callback that notifies of what's happening when evaluation is running
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
* TODO: test function invocations syntax
* TODO: test code in the invocables package
* TODO: cache all_children() in PythonObjectPath + stream all_children() in other paths + take in max argument to cap number of children
* TODO: make use of variables in REPL - store results in var names and use those var names in queries
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