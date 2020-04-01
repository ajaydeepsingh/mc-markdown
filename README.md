# How to use:

```python3 markdowntohtml.py <file.md>```

Note program will create a new html file in the folder.

## Running Tests:

```python3 test_convert.py -v```


### Initial Thoughts:

Cases to Consider:

- Lines that are just headers (1 - 6 levels)
- Unformatted Text
- Inline Links
- Blank lines are ignored

### Solutions:
- Just go line by line and parse the strings
    - How do you handle cases where there is a link in the header?

- Abstract Syntax Tree
    - never used before

- Regular Expressions
    - Could make unsafe changes

- Dissassemble into paragraph objects and manipulate
    - Might be inefficient because I would need to iterate over the paragraph objects multiple times

