
#   LINK: https://dbader.org/blog/meaning-of-underscores-in-python
#   Pattern	            Example	        Meaning
#   Single Leading      _var	        Naming convention indicating a name is meant for internal use. 
#                                       Generally not enforced by the Python interpreter (except in wildcard 
#                                       imports) and meant as a hint to the programmer only.

#   Single Trailing     var_	        Used by convention to avoid naming conflicts with Python keywords.

#   Double Leading      __var	        Triggers name mangling when used in a class context. Enforced by the Python interpreter.

#   Double Leading      __var__	        Indicates special methods defined by the Python language. Avoid this naming scheme for 
#   and Trailing                        your own attributes.

#   Single Underscore	    _	        Sometimes used as a name for temporary or insignificant variables (“don’t care”). Also: 
#                                       The result of the last expression in a Python REPL.
