# XML Cowboy
## Read, Wrangle and Write XML file
Using standard Python Library Read, transform and write multiple XML files into single unified file.

### Modules
>xml.etree.ElementTree
https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.ElementTree._setroot

### Supported XPath syntax
Syntax  |Meaning  
----------|-------
tag       |	Selects all child elements with the given tag. For example, spam selects all child elements named spam, and spam/egg selects all grandchildren named egg in all children named spam.
\*	      |  Selects all child elements. For example, \*/egg selects all grandchildren named egg.
.	        |  Selects the current node. This is mostly useful at the beginning of the path, to indicate that it’s a relative path.
//	      |  Selects all subelements, on all levels beneath the current element. For example, .//egg selects all egg elements in the entire tree.
..	      |  Selects the parent element. Returns None if the path attempts to reach the ancestors of the start element (the element find was called on).
[@attrib] |	Selects all elements that have the given attribute.
[@attrib='value']	| Selects all elements for which the given attribute has the given value. The value cannot contain quotes.
[tag]	    | Selects all elements that have a child named tag. Only immediate children are supported.
[tag='text']  |	Selects all elements that have a child named tag whose complete text content, including descendants, equals the given text.
[position]	|  Selects all elements that are located at the given position. The position can be either an integer (1 is the first position), the expression last() (for the last position), or a position relative to the last position (e.g. last()-1).
