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

### Element Objects
`class xml.etree.ElementTree.Element(tag, attrib={}, **extra)`
```
Element class. This class defines the Element interface, and provides a reference implementation of this interface.

The element name, attribute names, and attribute values can be either bytestrings or Unicode strings. tag is the element name. attrib is an optional dictionary, containing element attributes. extra contains additional attributes, given as keyword arguments.

tag
A string identifying what kind of data this element represents (the element type, in other words).

text
tail
These attributes can be used to hold additional data associated with the element. Their values are usually strings but may be any application-specific object. If the element is created from an XML file, the text attribute holds either the text between the element’s start tag and its first child or end tag, or None, and the tail attribute holds either the text between the element’s end tag and the next tag, or None. For the XML data

<a><b>1<c>2<d/>3</c></b>4</a>
the a element has None for both text and tail attributes, the b element has text "1" and tail "4", the c element has text "2" and tail None, and the d element has text None and tail "3".

To collect the inner text of an element, see itertext(), for example "".join(element.itertext()).

Applications may store arbitrary objects in these attributes.

attrib
A dictionary containing the element’s attributes. Note that while the attrib value is always a real mutable Python dictionary, an ElementTree implementation may choose to use another internal representation, and create the dictionary only if someone asks for it. To take advantage of such implementations, use the dictionary methods below whenever possible.

The following dictionary-like methods work on the element attributes.

clear()
Resets an element. This function removes all subelements, clears all attributes, and sets the text and tail attributes to None.

get(key, default=None)
Gets the element attribute named key.

Returns the attribute value, or default if the attribute was not found.

items()
Returns the element attributes as a sequence of (name, value) pairs. The attributes are returned in an arbitrary order.

keys()
Returns the elements attribute names as a list. The names are returned in an arbitrary order.

set(key, value)
Set the attribute key on the element to value.

The following methods work on the element’s children (subelements).

append(subelement)
Adds the element subelement to the end of this element’s internal list of subelements. Raises TypeError if subelement is not an Element.

extend(subelements)
Appends subelements from a sequence object with zero or more elements. Raises TypeError if a subelement is not an Element.

New in version 3.2.

find(match, namespaces=None)
Finds the first subelement matching match. match may be a tag name or a path. Returns an element instance or None. namespaces is an optional mapping from namespace prefix to full name.

findall(match, namespaces=None)
Finds all matching subelements, by tag name or path. Returns a list containing all matching elements in document order. namespaces is an optional mapping from namespace prefix to full name.

findtext(match, default=None, namespaces=None)
Finds text for the first subelement matching match. match may be a tag name or a path. Returns the text content of the first matching element, or default if no element was found. Note that if the matching element has no text content an empty string is returned. namespaces is an optional mapping from namespace prefix to full name.

getchildren()
Deprecated since version 3.2: Use list(elem) or iteration.

getiterator(tag=None)
Deprecated since version 3.2: Use method Element.iter() instead.

insert(index, subelement)
Inserts subelement at the given position in this element. Raises TypeError if subelement is not an Element.

iter(tag=None)
Creates a tree iterator with the current element as the root. The iterator iterates over this element and all elements below it, in document (depth first) order. If tag is not None or '*', only elements whose tag equals tag are returned from the iterator. If the tree structure is modified during iteration, the result is undefined.

New in version 3.2.

iterfind(match, namespaces=None)
Finds all matching subelements, by tag name or path. Returns an iterable yielding all matching elements in document order. namespaces is an optional mapping from namespace prefix to full name.

New in version 3.2.

itertext()
Creates a text iterator. The iterator loops over this element and all subelements, in document order, and returns all inner text.

New in version 3.2.

makeelement(tag, attrib)
Creates a new element object of the same type as this element. Do not call this method, use the SubElement() factory function instead.

remove(subelement)
Removes subelement from the element. Unlike the find* methods this method compares elements based on the instance identity, not on tag value or contents.

Element objects also support the following sequence type methods for working with subelements: __delitem__(), __getitem__(), __setitem__(), __len__().

Caution: Elements with no subelements will test as False. This behavior will change in future versions. Use specific len(elem) or elem is None test instead.
```
