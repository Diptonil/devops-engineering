# Bencoding

Bencoding supports strings, lists, integers and dictionaries. The techniques for encoding are given below.


## Strings

It follows the format of `<length>:<string>`. So, a string called "DevOps" would get encoded as "6:DevOps".


## Integers

It follows the format of `i<integer>e`. So, a number "420" would get encoded as "i420e".


## Lists

It follows the format of `l<bencoded values>e`. So, a list with contents of '["DevOps", 69, "MLOps"]' would get encoded as "l6:DevOpsi69e5:MLOpse".


## Dictionary

It follows the format of `d<bencoded string><bencoded value>e`. It is compulsory for the key to be an integer. So, a dictionary called '{"one":1, "two":2}' would get encoded as "d3:onei1e3:twoi2ee".