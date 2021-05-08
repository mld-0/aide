# Define required macros here
SHELL = /bin/sh

OBJS =  main.o factorial.o hello.o
CFLAG = -Wall -g
CC = g++
INCLUDE =
LIBS = -lm

#	LINK: https://www.tutorialspoint.com/makefile/makefile_quick_guide.htm

#	Syntax of a makefile rule
#>%		target1 [target2 ...]: [pre-req1 pre-req2 ...]
#>%			[command1
#>%			command2
#>%			...]


#	Automatic Variables
#		$@		target filename
#		$*		target filename without extension
#		$<		first prerequisite filename
#		$^		filenames of all prerequisites, seperated by spaces, disregard duplicates
#		$+		As $^, but including duplicates
#		$?		Names of all prerequisites newer than the target, seperated by spaces


#	Conditional directives
#>%		conditional-directive
#>%		   text-if-true
#>%		else
#>%		   text-if-false
#>%		endif
#	Using: ifeq, ifneq, ifdef, ifndef, else, endif


#	Include directive
#>%		include [filename]
#	suspends reading of current makefile, processes additional makefile(s) before continuing
#

hello:$(OBJS)
	$(CC) $(CFLAGS) $(INCLUDE) -o $@ $(OBJS) $(LIBS)

clean:
	-rm -f *.o core *.core

#	Implicit rule: create object files for each cpp source file
.cpp.o:
	$(CC) $(CFLAGS) $(INCLUDE) -c $<
