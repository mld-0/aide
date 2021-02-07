#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=3:
#   }}}1
import re

#   {{{2
#   LINK: https://www.w3schools.com/python/python_regex.asp
#   LINK: https://realpython.com/regex-python/

#   Matching string within string, conventionally:
s = 'foo123bar'
print('123' in s)
print(s.find('123'))
print(s.index('123'))
print()

print(re.search('123', s))

#   Match objects are truthy:
if re.search('123', s):
    print("Found match")
else:
    print("No match")

s = 'foo123bar'
print(re.search('[0-9][0-9][0-9]', s))

#   Regex Characters
#   {{{
#       .	    Matches any single character except newline
#       ^	    Anchors a match at the start of a string
#               Complements a character class
#       $	    Anchors a match at the end of a string
#       *	    Matches zero or more repetitions
#       +	    Matches one or more repetitions
#       ?	    Matches zero or one repetition
#               Specifies the non-greedy versions of *, +, and ?
#               Introduces a lookahead or lookbehind assertion
#               Creates a named group
#       {}	    Matches an explicitly specified number of repetitions
#       \	    Escapes a metacharacter of its special meaning
#               Introduces a special character class
#               Introduces a grouping backreference
#       []	    Specifies a character class
#       |	    Designates alternation
#       ()	    Creates a group
#       :
#       #
#       =
#       !	Designate a specialized group
#       <>	Creates a named group
#   }}}

#   Escaping '\'
s = r'foo\bar'
print(re.search('\\\\', s))
print(re.search(r'\\', s))
print()

#   Unnamed capture groups - multiple matches with location
#   m.groups()
#   Returns a tuple containing all the captured groups from a regex match.
m = re.search('(\w+),(\w+),(\w+)', 'foo,quux,baz')
print(m)
#   All results
print(m.groups())
#   All spans (match locations)
loop_span = [m.span(i) for i in range(1, len(m.groups())+1)]
print(loop_span)
#   itterate over matches
for loop_group in m.groups():
    print(loop_group)
print()


#   Named capture groups - multiple matches, with name and location
m = re.search('(?P<w1>\w+),(?P<w2>\w+),(?P<w3>\w+)', 'foo,quux,baz')
print(m)
#   Get named capture groups as dict
print(m.groupdict())
#   span (location) from all matches
print(m.span())
#   Get list of 'spans' (match locations)
loop_span = [m.span(i) for i in range(1, len(m.groups())+1)]
print(loop_span)
#   Iterate over groupdict
for loop_group, loop_key in zip(m.groupdict().values(), m.groupdict().keys()):
    print("loop_group=(%s), loop_key=(%s)" % (str(loop_group), str(loop_key)))
print()

#   Continue: 2021-02-07T23:11:00AEDT backreferences, flags example, multi-line, <...>, (see above) realpython link.

#   Continue: 2021-02-07T23:12:44AEDT alternative regex functions

#   re functions:
#       findall	    Returns a list containing all matches
#       search	    Returns a Match object if there is a match anywhere in the string
#       split	    Returns a list where the string has been split at each match
#       sub	        Replaces one or many matches with a string


#   }}}1
