# Sets in Python 
## Properties of a set 
- Sets are unordered 
- Set elements are unique. No duplicates. 
- A set itself may be modified, but the elements contained in the set must be of an immutable type.

## _Set Creation_
A set can be created in 2 ways:

1. You can define a set with the built-in set() function:
    ```python
    x = set(<iter>)
    ```
    An example can be:
    ```python
    x = set(['foo', 'bar', 'baz', 'foo', 'qux'])
    ```
    **OR**
    
    ```python
    x = set(('foo', 'bar', 'baz', 'foo', 'qux'))
    ```
2. Alternately, a set can be defined with curly braces ({}):
    ```python
    x = {<obj>, <obj>, ..., <obj>}
    ```
    An example:
    ```python
    x = {'foo', 'bar', 'baz', 'foo', 'qux'}
    ```

