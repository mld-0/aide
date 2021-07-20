# 	VIM SETTINGS: {{{3
# 	VIM: let g:mldvp_filecmd_open_tagbar=0 g:mldvp_filecmd_NavHeadings="" g:mldvp_filecmd_NavSubHeadings="" g:mldvp_filecmd_NavDTS=0 g:mldvp_filecmd_vimgpgSave_gotoRecent=0
# 	vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
# 	vim: set foldlevel=2 foldcolumn=3: 
# 	}}}1
# 	{{{2
source "$HOME/._exports.sh"
PWD_previous="$PWD"
cd "$mld_data/example"

#	gnu-equivelents:
#		grep '<regex>'				
#		perl -wne '/<regex>/ and print'
#
#		sed 's/find/replace/
#		perl -pe 's/find/replace/'
#
#		awk -F$delim '{print $0}'		
#		perl -F$delim -lane 'print @F[0]'

#	Command line options:
#		-e 'script'		execute given perl code 
#		-l<octnum>		end-of-line processing, (set $\ to octnum?, or to $/ if not given)
#		-p				printing loop around command
#		-n				nonprinting loop around command
#		-a				split linewise into array @F (using -F<delim>)
#		-F<delim>		linewise split delim character (if empty, split all characters)
#		-i				modify input file inplace
#		-w				general warnings (-W for all warnings)
#		-d				debugger

#	Special variables:
#		$_			default var
#		$/			input record seperator
#		$\			output record seperator (line seperator)
#		$,			output field seperator (delimitor between elements of unquoted list)
#		$"			output list seperator (delimitor between elements of quoted list)

#	Provide variable
#		perl -sE 'say $myvar' -- -myvar="abc"

#	(Other) command line options:
#	{{{
#		-F//		alt syntax for linewise split
#		-0<octal>	linewise split (as per -F) with split char in octal
#		-s			rudimentary switch 
#		-E			extended features
#		-t			taint (security)
#		-U			allow unsafe
#		-C			unicode
#		-X			disable warnings
#		-P			use C pre-processor
#		-I<dir>		include <dir> in C pre-processor
#		LINK: https://www.cs.cmu.edu/afs/cs/user/rgs/mosaic/pl-opt.html
#	}}}

#	Resources:
#	{{{
#	LINK: https://learnbyexample.gitbooks.io/command-line-text-processing/content/perl_the_swiss_knife.html
#	LINK: https://gist.github.com/joyrexus/7328094
#	LINK: https://blogs.oracle.com/linux/the-top-10-tricks-of-perl-one-liners-v2
#	LINK: https://catonmat.net/introduction-to-perl-one-liners
#	LINK: https://catonmat.net/perl-book
#	}}}

#	Quote constructs
#	{{{
#		Customary	Genetic		Meaning					Interpolates
#		'' 			q// 		Literal string			no
#		"" 			qq// 		Literal string			yes
#		`` 			qx// 		Command execution		yes
#		() 			qw// 		word list				no
#		// 			m// 		pattern match			yes
#		s/// 		s/// 		pattern substitution	yes
#		tr/// 		y/// 		character translation	no
#		"" 			qr//		regular expression		yes
#	}}}

#	Special variables (Full):
#	{{{
#		$_			(arg) default variable
#		$/			input record seperator
#		$\			output record seperator
#		$"			list seperator
#		$,			output field seperator
#		$.			last linenumber
#		$<num>		match group <num>
#		@+			offset of end of last submatch in scope
#		$^N			text match by group most recently closed
#		$*			set to 0 for single line strings, non-zero for multiline matching
#		$&			last pattern match
#		$+			The text matched by the highest used capture group of the last successful search pattern.
#		$'			string following last match
#		$`			string preceding last match
#		$=			page length
#		$-			pages remaining
#		$;			seperator for multi-dim array emulation
#		$[			array-index (default=0)
#		@F			array from '-a|-F'
#		%ENV		env hash 
#		@ARGV		arguments
#		$ARGV		script filename
#		$^O			OS
#		$]			perl interpreter version
#		$^L			formfeed
#		$?			childerror (return status of last pipe)
#		$#			printed numbers format
#		$a $b		used by sort()
#		$|			if non-zero, flush after each input/output
#		$~			report format name
#		$^			report top-of-page
#		$:			format line break characters
#		$\L			formfeed
#		$!			os error (code)
#		#^E			os error extra information
#		$<			real uid
#		$>			effective uid
#		$$			process num
#		$(			real groupid
#		$)			effective groupid
#		$0			program name
#		$^T			application start epoch
#		ARGVOUT		filehandle for open file for inplace edits
#		%SIG		singal handlers hash
#		
#	LINK: https://catonmat.net/ftp/perl.predefined.variables.pdf
#	}}}

#	arrays:
#	{{{
#		$#		index of last item (length - 1)
#	}}}

#	logical statement ordering:
#	{{{
perl -l -e 'if (2<3) { print("2 is less than 3") }'
perl -l -e 'print "2 is less than 3" if 2<3'
perl -l -e 'if("a" lt "b"){$x=5; $y=10} print "x=$x; y=$y"'
perl -l -e 'print "x=$x; y=$y" if "a" lt "b" and $x=5,$y=10'
printf "\n"
#	}}}

#	BEGIN{}/END{} statement syntax:
perl -le 'BEGIN{print "start";} print "abc"; END{print "done";}'
printf "\n"

#	Examples:
#	{{{

#	Indent all lines:
printf "abc\ndef\nhij\n" | perl -pe 's/^/\t/' 
printf "\n"

#	Get columns 0, 3, and 4 (0-indexed) from csv
cat "$mld_data/data.csv" | perl -F, -lane 'print @F[0,3,4]'
printf "\n"

#	Get columns 0 through 4 (0-indexed) from csv
cat "$mld_data/data.csv" | perl -F, -lane 'print @F[0..4]'
printf "\n"

#	Trim lines to 80 chars:

#	}}}

# 	LINK: https://perldoc.perl.org/perlrun
#	Command line perl
#	{{{
#	The normal way to run a Perl program is by making it directly executable, or else by passing the name of the source file as an argument on the command line. (An interactive Perl environment is also possible--see perldebug for details on how to do that.) Upon startup, Perl looks for your program in one of the following places:
#		Specified line by line via -e or -E switches on the command line.
#		Contained in the file specified by the first filename on the command line. (Note that systems supporting the #! notation invoke interpreters this way. See "Location of Perl".)
#		Passed in implicitly via standard input. This works only if there are no filename arguments--to pass arguments to a STDIN-read program you must explicitly specify a "-" for the program name.
#	With methods 2 and 3, Perl starts parsing the input file from the beginning, unless you've specified a "-x" switch, in which case it scans for the first line starting with #! and containing the word "perl", and starts there instead. This is useful for running a program embedded in a larger message. (In this case you would indicate the end of the program using the __END__ token.)
#	The #! line is always examined for switches as the line is being parsed. Thus, if you're on a machine that allows only one argument with the #! line, or worse, doesn't even recognize the #! line, you still can get consistent switch behaviour regardless of how Perl was invoked, even if "-x" was used to find the beginning of the program.
#	}}}

#	LINK: https://learnbyexample.gitbooks.io/command-line-text-processing/content/perl_the_swiss_knife.html#executing-perl-code
#	Command line arguments
#	{{{
#	perlrun (perl flags/options)
#	-a:	split line (specify delimitor -F'delim')
#	-l: end-of-line processing, (chomp input when used with -n or -p), 
#	-p: Places a printing loop around your command so that it acts on each
#	    line of standard input. 
#	-n: Places a non-printing loop around your command.
#	-e: Allows you to provide the program as an argument rather
#	    than in a file. 
#	-i: Modifies your input file in-place (making a backup of the
#	    original unless no argument given to -i)
#	-w: Activates some warnings. Any good Perl coder will use this.
#	-d: Runs under the Perl debugger. For debugging your Perl code,
#	    obviously.
#	-t: Treats certain "tainted" (dubious) code as warnings (proper
#	    taint mode will error on this dubious code). Used to beef
#	    up Perl security, especially when running code for other
#	    users, such as setuid scripts or web stuff.
#	}}}


#	Basics:
#	{{{
#	-E flag, use features like say (automatic newline)
perl -E 'say "Hello World"'
printf "\n"

#	Use of '-l' to eliminate need for '\n'
perl -l -e 'if (2<3) { print("2 is less than 3") }'
perl -l -e 'print "2 is less than 3" if 2<3'
printf "\n"
#	{{{
#>>		2 is less than 3
#>>		2 is less than 3
#	}}}

#	Perl syntax can use/avoid (){} 
perl -l -e 'if (2<3) { print("2 is less than 3") }'
perl -l -e 'print "2 is less than 3" if 2<3'
perl -l -e 'if("a" lt "b"){$x=5; $y=10} print "x=$x; y=$y"'
perl -l -e 'print "x=$x; y=$y" if "a" lt "b" and $x=5,$y=10'
printf "\n"
#	{{{
#>>		2 is less than 3
#>>		2 is less than 3
#>>		x=5; y=10
#>>		x=5; y=10
#	}}}

x="abc"
#	resolve shell variable x=abc
perl -le "\$x='def'; print 'ab $x 123'"
#	resolve perl variable x=def
perl -le '$x="def"; print "ab $x 123"'
printf "\n"
#	{{{
#>>		ab abc 123
#>>		ab def 123
#	}}}


#	The 'q//' operator is a stand-in for single quotation, when perl command itself being in single quotations makes their use otherwise tedious
perl -le 'print '"'"'ab $x 123'"'"
perl -le "print 'ab \$x 123'"
perl -le 'print q/ab $x 123/'
printf "\n"
#	{{{
#>>		ab $x 123
#>>		ab $x 123
#>>		ab $x 123
#	}}}

#	}}}

#	Substitution:
#	{{{
#	syntax is variable =~ s/REGEXP/REPLACEMENT/FLAGS 
#	and by default acts on $_ if variable is not specified

#	-p	loop-by-line, print
#	-n	loop-by-line, non-printing
#	$_	input record content (including seperator)

#	Change first ',' to ' : '
seq 10 | paste -sd, | perl -pe 's/,/ : /'
#	Change all ',' to ' : '
seq 10 | paste -sd, | perl -pe 's/,/ : /g'
printf "\n"
#	{{{
#>>		1 : 2,3,4,5,6,7,8,9,10
#>>		1 : 2 : 3 : 4 : 5 : 6 : 7 : 8 : 9 : 10
#	}}}
#	}}}

#	inplace editing
#	{{{
#		-i'bak.*'	Replace string in file, save backup as bak.\1
perl -i'bak.*' -pe "s/Fool me once/Can't get fooled again/" "replace-test.txt"
#		Reset 
cp "bak.replace-test.txt" "replace-test.txt"
rm "bak.replace-test.txt" 
#	}}}


#	regex line filtering
#	{{{
#	check for match
#		variable =~ m/REGEXP/FLAGS 
#	check for negated match
#		variable !~ m/REGEXP/FLAGS 
#	by default acts on $_ if variable is not specified
#	as we need to print only selective lines, use -n option
#	by default, contents of $_ will be printed if no argument is passed to print#

# 	Equivelents
# 		/^[RS]/ 
# 		$_ =~ m/^[RS]/#
#
#		!/are/ 
#		$_ !~ m/are/

#		m/abc/
#		m|abc|

# 	Equivelents:
# 		grep '^[RS]' 
# 		sed -n '/^[RS]/p' 
# 		awk '/^[RS]/'
#		perl -ne 'print if /^[RS]/' 
#		perl -ne '/^[RS]/ and print' 

#	Match first character R|S 
perl -ne 'print if /^[RS]/' "poem.txt"
#	Match 'and', ignore case
perl -ne 'print if /and/i' "poem.txt"
#	Match not 'are'
perl -ne 'print if !/are/' "poem.txt" 
printf "\n"
#	{{{
#>>		Roses are red,
#>>		Sugar is sweet,
#>>		And so are you.
#>>		Sugar is sweet,
#	}}}

#	Match 'are' and not 'so'
perl -ne 'print if /are/ && !/so/' "poem.txt"
printf "\n"
#	{{{
#>>		Roses are red,
#>>		Violets are blue,
#	}}}

#	Use alternative character as delimitor with 'm' (match) specifier
perl -ne 'print if m#/foo/a/#' "paths.txt"
printf "\n"
#	{{{
#>>		/foo/a/report.log
#	}}}

#	Fixed string matching:
#	Equivelent to
#		grep -F 'a[5]' 
#		awk 'index($0, "a[5]")'
echo 'int a[5]' | perl -ne 'print if index($_, "a[5]") != -1'
printf "\n"
#	}}}

#	ENV variables, PWD, SHELL
#	{{{
perl -le 'print $ENV{PWD}'
perl -le 'print $ENV{SHELL}'
printf "\n"
#	{{{
#>>		/Users/mldavis/Dropbox/_data/example
#>>		/usr/local/bin/zsh
#	}}}

#	Passing values to perl using ENV, (alternative approach when nested single-quoting is called for)
echo 'a#$%d' | perl -ne 'print if index($_, "#$%") != -1' 	#	string is not matched when given using double-quotes
echo 'a#$%d' | perl -ne 'print if index($_, q/#$%/) != -1'
echo 'a#$%d' | s='#$%' perl -ne 'print if index($_, $ENV{s}) != -1'
printf "\n"
#	{{{
#>>		a#$%d
#>>		a#$%d
#	}}}
#	}}}


#	Line based filtering
#	{{{

#	Match string at beginning of line
s='a+b' perl -ne 'print if index($_, $ENV{s})==0' "equns.txt"
#	Ongoing: 2020-11-13T15:40:44AEDT doesn't work?	Match string at end of line (length() is equivelent to length($_))
s='a+b' perl -ne '$pos = length() - length($ENV{s}) - 1; print if index($_, $ENV{s}) == $pos' "equns.txt"
printf "\n"


#	Equivelents:
#	{{{
#>%		head -n2 poem.txt | tail -n1
#>%		sed -n '2p'
#>%		awk 'NR==2'
#	}}}
#	Print line 2:
perl -ne 'print if $.==2' "poem.txt"
#	Print lines 2 and 4
perl -ne 'print if $.==2 || $.==4' "poem.txt"
#	Print last line:
perl -ne 'print if eof' "poem.txt"
printf "\n"
#	{{{
#>>		Violets are blue,
#>>		Violets are blue,
#>>		And so are you.
#>>		And so are you.
#	}}}

#	For large inputs -> use exit after printing desired line 
seq 14323 14563435 | perl -ne 'if($.==234){print; exit}'
printf "\n"
#	{{{
#>>		14556
#	}}}

#	Print first three lines
seq 14 25 | perl -pe 'exit if $.>3'
printf "\n"
#	{{{
#>>		14
#>>		15
#>>		16
#	}}}

#	Print range of lines:
seq 14 25 | perl -ne 'print if 3..5'
printf "\n"
#	{{{
#>>		16
#>>		17
#>>		18
#	}}}

#	print from line ten to end
seq 14 25 | perl -ne 'print if $.>=10'
printf "\n"
#	{{{
#>>		23
#>>		24
#>>		25
#	}}}

#	}}}

#	Field processing
#	{{{
#		-a		autosplit input by whitepace (as per default awk behaviour)
#				'@F' contains elements from given line
#	unlike awk, columns are zero indexed

#	Print first (0-th) column
perl -lane 'print $F[0]' "fruit.txt"
printf "\n"
#	{{{
#>>		fruit
#>>		apple
#>>		banana
#>>		fig
#>>		guava
#	}}}

#	Print second (1-st) column
perl -lane 'print $F[1]' "fruit.txt"
printf "\n"
#	{{{
#>>		qty
#>>		42
#>>		31
#>>		90
#>>		6
#	}}}

#	Number of fields:
#		$#F 	index of last variable, (meaning) len(@F) = $#F + 1
echo '1 a 7' | perl -lane 'print $#F + 1'
echo '1 a 7' | perl -lane 'print scalar @F'
echo '1 a 7\na b' | perl -lane 'print scalar @F'
printf "\n"
#	{{{
#>>		3
#>>		3
#>>		2
#	}}}

#	Field comparision:
#	Equivelent:		awk '$1=="apple"{print $2}'

#	Comparison Operators
#	Equality				Numeric		String
#		Equal				==			eq
#		Not Equal			!=			ne
#		Comparison			<=>			cmp
#	Relational
#		Less-than			<			lt
#		Greather-than		>			gt
#		less-than-equal		<=			le
#		greater-than-equal	>=			ge

#	Comparison operator
perl -le 'print(1 <=> 2)'
perl -le 'print(2 <=> 2)'
perl -le 'print(3 <=> 2)'
printf "\n"
#	{{{
#>>		-1
#>>		0
#>>		1
#	}}}

#	output $2 if $1 matches 'apple'
perl -lane 'print $F[1] if $F[0] eq "apple"' "fruit.txt"
printf "\n"
#	{{{
#>>		42
#	}}}

#	print first field if second field > 35 (excluding header)
#	Equivelent:		awk 'NR>1 && $2>35{print $1}' fruits.txt
perl -lane 'print $F[0] if $F[1]>35 && $.>1'  "fruit.txt"
printf "\n"
#	{{{
#>>		apple
#>>		fig
#	}}}

#	print if first field does not contain 'a'
#	Equivelent: 	awk '$1 !~ /a/' fruits.txt
perl -ane 'print if $F[0] !~ /a/' "fruit.txt"
printf "\n"
#	{{{
#>>		fruit   qty
#>>		fig     90
#	}}}

#	Input delimitor: 
#			-F				split line characterwise
#			-F<delim>		split lines by <delim>
#			-F/pattern/     split() pattern for -a switch (//'s are optional)
#	print second field, with seperator ':'
#	Equivelent: 	awk -F: '{print $2}'
echo 'foo:123:bar:789' | perl -F: -lane 'print $F[1]'
echo 'foo:123:bar:789' | perl -F: -lane 'print $F[-1]'
echo 'foo:123:bar:789' | perl -F: -lane 'print $F[-2]'
printf "\n"
#	{{{
#>>		123
#>>		789
#>>		bar
#	}}}

#	use quotes to escape ';' from shell
echo 'one;two;three;four' | perl -F';' -lane 'print $F[2]'
printf "\n"
#	{{{
#>>		three
#	}}}

#	Regex field seperator
echo 'Sample123string54with908numbers' | perl -F'\d+' -lane 'print $F[0]'
printf "\n"

#	Equivelent: awk -F'[{}= ]+' '{print $1}'
#	\x20 is space character, can't use literal space within [] when using -F
echo '{foo}   bar=baz' | perl -F'[{}=\x20]+' -lane 'print $F[1]'
echo '{foo}   bar=baz' | perl -F'[{}=\x20]+' -lane 'print $F[2]'
printf "\n"
#	{{{
#>>		foo
#>>		bar
#	}}}

#	Equivelent: gawk -v FS= '{print $1}'
echo 'apple' | perl -F -lane 'print $F[0]'
echo 'apple' | perl -F -lane 'print $F[1]'
echo 'apple' | perl -F -lane 'print $F[-1]'
printf "\n"
#	{{{
#>>		a
#>>		p
#>>		e
#	}}}

#	-C support for unicode
#	printf 'hi👍 how are you?' | perl -CS -F -lane 'print $F[2]'

#	Specify output field seperator
#	Method 1, use '$,' (output field seperator for print)
echo 'foo:123:bar:789' | perl -F: -lane '$,=q/-/; print @F'
echo 'foo:123:bar:789' | perl -F: -lane '$,=q/ - /; print @F'
#	Method 2, use 'join'
echo 'foo:123:bar:789' | perl -F: -lane 'print join "-", @F'
#	Method 3, use '$"' (list seperator)
echo 'foo:123:bar:789' | perl -F: -lane '$"="-"; print "@F"'
printf "\n"
#	{{{
#>>		foo-123-bar-789
#>>		foo - 123 - bar - 789
#>>		foo-123-bar-789
#>>		foo-123-bar-789
#	}}}

#	Input record seperator:
#	given by: '$/'
#	default: newline
#	cli option -0, accepts octal value of char as input record seperator (three digit number, see ASCII table)
#	-0 option used without argument will use the ASCII NUL character as input record separator

#	If -l specified:
#		chomp record seperator from input
#		if no argument is given for -l, output seperator = input seperator
#		Order of: -l, -0, $/  matters
s='this is a sample string'
#	Equivelent: 	awk -v RS=' ' '{print NR, $0}'
printf "$s" | perl -lne 'BEGIN{$/=" "} print "$. $_"'
printf "\n" 
#	{{{
#>>		1 this
#>>		2 is
#>>		3 a
#>>		4 sample
#>>		5 string
#	}}}

#	-0(040) use ascii oct 040 (space)
#	Equivelent: 	awk -v RS=' ' '/a/'
printf "$s" | perl -l -0040 -ne 'print if /a/'
printf "\n" 
#	{{{
#>>		a
#>>		sample
#	}}}

# 	if the order is changed, ORS will be space, not newline
printf "$s" | perl -0040 -l -ne 'print if /a/'
printf "\n\n"
#	{{{
#>>		a sample
#	}}}

#	-0 without argument -> use ASCII NUL as IFS
printf 'foo\0bar\0' | cat -A
printf "\n"
printf 'foo\0bar\0' | perl -l -0 -ne 'print'
printf "\n"
#	{{{
#>>		foo^@bar^@
#>>		foo
#>>		bar
#	}}}

# 	Remove everything between 'red' and (last instance of) 'are'
#	-0(777)	Slurp file (read entire file into string)
# 	s modifier allows . to match newline as well
cat "poem.txt" | perl -0777 -pe 's/red.*are //s'
printf "\n"
#	{{{
#>>		Roses are you.
#	}}}

#	Use $/="\n\n" to preserve multiple consecutive newlines

#	Print all paragraphs containing 'it'
#	Equivelent: 	awk -v RS= -v ORS='\n\n' '/it/' sample.txt
#	-0(0) assign empty string to $/ (input record seperator)
cat "paragraphs.txt" | perl -00 -ne 'print if /it/' 
printf "\n"
#	{{{
#>>		Just do-it
#>>		Believe it
#>>		
#>>		Today is sunny
#>>		Not a bit funny
#>>		No doubt you like it too
#	}}}


#	Print all paragraphs which are one line in length
cat "paragraphs.txt" | perl -F'\n' -00 -ane 'print if $#F==0'
#	Print all paragraphs which are two lines in length
cat "paragraphs.txt" | perl -F'\n' -00 -ane 'print if $#F==1'
printf "\n"
#	{{{
#>>		Hello World
#>>		
#>>		Good day
#>>		How are you
#>>		
#>>		Just do-it
#>>		Believe it
#>>		
#>>		Much ado about nothing
#>>		He he he
#	}}}

#	Print two line paragraph(s) containing 'do'
#	Equivelent: 	awk -F'\n' -v RS= -v ORS='\n\n' 'NF==2 && /do/' 
#	(produces trailing newline which perl command does not)
cat "paragraphs.txt" | perl -F'\n' -00 -ane 'print if $#F==1 && /do/'
#	{{{
#>>		Just do-it
#>>		Believe it
#>>		
#>>		Much ado about nothing
#>>		He he he
#	}}}

#	Combine lines of each paragraph.
#	Equivelent: 	awk 'BEGIN{FS="\n"; OFS=". "; RS=""; ORS="\n\n"} {$1=$1} 1'
cat "paragraphs.txt" | perl -F'\n' -00 -ane 'print join ". ", @F; print "\n\n"'
#	{{{
#>>		Good day. How are you
#>>		
#>>		Just do-it. Believe it
#>>		
#>>		Today is sunny. Not a bit funny. No doubt you like it too
#>>		
#>>		Much ado about nothing. He he he
#	}}}

#	For 'report.txt', records are obtained by splitting file by text 'Error: '
#	Print each record inside '()'
cat "report.txt" | perl -lne 'BEGIN{$/="Error: "} print "($_)"'
printf "\n"
#	{{{
#>>		(blah blah
#>>		)
#>>		(something went wrong
#>>		more blah
#>>		whatever
#>>		)
#>>		(something surely went wrong
#>>		some text
#>>		some more text
#>>		blah blah blah
#>>		)
#	}}}

#	number of records (number of last record)
#	Equivelent: 	awk -v RS='Error:' 'END{print NR}'
cat "report.txt" | perl -lne 'BEGIN{$/="Error: "} print $. if eof' 
printf "\n"
#	{{{
#>>		3
#	}}}

#	Print record(s) containing 'surely'
cat "report.txt" | perl -lne 'BEGIN{$/="Error:"} print "$/$_" if /surely/'
printf "\n"
#	{{{
#>>		Error: something surely went wrong
#>>		some text
#>>		some more text
#>>		blah blah blah
#	}}}

#	Join lines if preceding line ends with '-'
#	Equivelent: 	awk -v RS='-\n' -v ORS= '1'
#	or				perl -pe 's/-\n//'
cat "msg.txt" | perl -pe 'BEGIN{$/="-\n"} chomp'
printf "\n"
#	{{{
#>>		Hello there.
#>>		It will rain today. Have a safe
#>>		and pleasant journey.
#	}}}

#	Output record seperator:	$\		
#	$\ is not set, however output is still newline-delimited by newline seperator which has not been removed
seq 3 | perl -ne 'print'
printf "\n"
#	{{{
#>>		1
#>>		2
#>>		3
#	}}}
#	Equivelent: 	awk -v ORS='---\n' '{print $0}'
seq 3 | perl -ne 'BEGIN{$\="---\n"} print'
printf "\n"
#	{{{
#>>		1
#>>		---
#>>		2
#>>		---
#>>		3
#>>		---
#	}}}

#	Dynamic ouput record seperator
#	Equivelent: 	awk '{ORS = NR%2 ? " " : "\n"} 1'
#	If output record seperator is set by '-l', that is then overridden by value of $\
seq 6 | perl -lpe '$\ = $.%2 ? " " : "\n"'
printf "\n"
#	{{{
#>>		1 2
#>>		3 4
#>>		5 6
#	}}}
#	Set $\ to \n for every third line
seq 6 | perl -lpe '$\ = ($. % 3 != 0) ? "-" : "\n"'
#	Can also be written as:
seq 6 | perl -lpe '$\ = $.%3 ? "-" : "\n"'
printf "\n"
#	{{{
#>>		1-2-3
#>>		4-5-6
#>>		1-2-3
#>>		4-5-6
#	}}}

#	#	print with no output seperator
#	seq 3 | perl -F'\n' -ne 'print @F; END{printf "\n"};'
#	printf "\n"
#	#	{{{
#	#>>		123
#	#	}}}

#	Use -l to set output record seperator
seq 8 | perl -ne 'print if /[24]/'
printf "\n"

#	Null seperator, with chomped input record seperator
seq 8 | perl -l0 -ne 'print if /[24]/; END{$\=""; print "\n"}' | cat -A
printf "\n"

#	-l(054) comma seperator 
seq 8 | perl -l054 -ne 'print if /[24]/; END{$\=""; print "\n"}'
printf "\n"


#	}}}

#	Multiline Processing
#	{{{
#	Typically Implemented a (rudimentary) state machine 

#	Match consecutive lines, where first contains 'are', second contains 'is'
#	Equivelent: 	awk 'p~/are/ && /is/{print p ORS $0} {p=$0}'
cat "poem.txt" | perl -ne 'print $p,$_ if /is/ && $p=~/are/; $p=$_'
printf "\n"
#	{{{
#>>		Violets are blue,
#>>		Sugar is sweet,
#	}}}

#	Print line where (2nd next contains 'is'), (next contains 'blue'), (current contains 'red')
#	Equivelent: 	awk 'p2~/red/ && p1~/blue/ && /is/{print p2} {p2=p1; p1=$0}'
cat "poem.txt" | perl -ne 'print $p2 if /is/ && $p1=~/blue/ && $p2=~/red/; $p2=$p1; $p1=$_'
printf "\n"

#	Print line where (current contains 'is'), (previous contains 'blue'), (2nd previous contains 'red')
#	Note: the '$_' in print is redundent
cat "poem.txt" | perl -ne 'print $_ if /is/ && $p1=~/blue/ && $p2=~/red/; $p2=$p1; $p1=$_'
printf "\n"


#	Extract lines around matching line
#		$n && $n--		only evaluates $n-- if $n>0

#	print 2 line(s) matches of /BEGIN/ and subsiquent 
#	Equivelent: 	awk '/BEGIN/{n=2} n && n--' 
cat "range.txt" | perl -ne '$n=2 if /BEGIN/; print if $n && $n--'
printf "\n"
#	{{{
#>>		BEGIN
#>>		1234
#>>		BEGIN
#>>		a
#	}}}

#	print 1 line(s) after line matching /BEGIN/ 
#	Equivelent:		awk 'n && n--; /BEGIN/{n=1}'
cat "range.txt" | perl -ne 'print if $n && $n--; $n=1 if /BEGIN/'
printf "\n"
#	{{{
#>>		1234
#>>		a
#	}}}

#	
#	Print line prior to match /END/
#	Equivelent:		 awk '/END/{print p2} {p2=p1; p1=$0}'
cat "range.txt" | perl -ne 'print $p2 if /END/; $p2=$p1; $p1=$_'
printf "\n"
#	{{{
#>>		1234
#>>		b
#	}}}

#	Get 3rd line before each match 
#	Equivelent:		tac range.txt | awk 'n && !--n; /END/{n=3}' | tac
tac "range.txt" | perl -ne 'print if $n && !--$n; $n=3 if /END/' | tac
printf "\n"
#	{{{
#>>		BEGIN
#>>		a
#	}}}


#	}}}

#	Regex, Perl vs Sed:
#	{{{
#	perl substitute includes newline amoung replaced string -> resulting in no newline as part of output, whereas output from command with sed does include newline
echo 'foo:123:bar:789' | sed -E 's/[^:]+$/xyz/' | xxd
echo 'foo:123:bar:789' | perl -pe 's/[^:]+$/xyz/' | xxd
printf "\n"
#	{{{
#>>		00000000: 666f 6f3a 3132 333a 6261 723a 7879 7a0a  foo:123:bar:xyz.
#>>		00000000: 666f 6f3a 3132 333a 6261 723a 7879 7a    foo:123:bar:xyz
#	}}}

#	use '-l' to replace newline
echo 'foo:123:bar:789' | perl -lpe 's/[^:]+$/xyz/' | xxd
printf "\n"
#	{{{
#>>		00000000: 666f 6f3a 3132 333a 6261 723a 7879 7a0a  foo:123:bar:xyz.
#	}}}

#	use paste to remove trailing delimitor before using sed
seq 10 | paste -sd, | sed 's/,/ : /g'
#	perl has 'if !eof' to skip trailing line during substitution
seq 10 | perl -pe 's/\n/ : / if !eof'
printf "\n"
#	{{{
#>>		1 : 2 : 3 : 4 : 5 : 6 : 7 : 8 : 9 : 10
#>>		1 : 2 : 3 : 4 : 5 : 6 : 7 : 8 : 9 : 10
#	}}}

#	does not include trailing newline
seq 10 | perl -pe 's/\n/ : /g' && printf "\n"
#	sed doesn't combine lines, use tr as intermediate. Also excludes trailing newline
seq 10 | tr $'\n' $'\t' | sed 's/\t/ : /g' && printf "\n"
printf "\n"
#	{{{
#>>		1 : 2 : 3 : 4 : 5 : 6 : 7 : 8 : 9 : 10 :
#>>		1 : 2 : 3 : 4 : 5 : 6 : 7 : 8 : 9 : 10 :
#	}}}

#	sed choses largest match,
#	perl matches empty and non-empty strings given '*'
echo ',baz,,xyz,,,' | sed 's/[^,]*/A/g'
echo ',baz,,xyz,,,' | perl -lpe 's/[^,]*/A/g'
printf "\n"
#	{{{
#>>		A,A,A,A,A,A,A
#>>		A,AA,A,AA,A,A,A
#	}}}
echo 'foo,baz,,xyz,,,123' | sed 's/[^,]*/A/g'
echo 'foo,baz,,xyz,,,123' | perl -lpe 's/[^,]*/A/g'
printf "\n"
#	{{{
#>>		A,A,A,A,A,A,A
#>>		AA,AA,A,AA,A,A,AA
#	}}}
#	note perl requires "$&" compared to sed "$" -> (the function of which is?)
echo '42,789' | sed 's/[0-9]*/"&"/g'
echo '42,789' | perl -lpe 's/[0-9]*/"$&"/g'
#	Using \d+ in perl gives same behaviour as [0-9]* in sed
echo '42,789' | perl -lpe 's/\d+/"$&"/g'
printf "\n"
#	{{{
#>>		"42","789"
#>>		"42""","789"""
#>>		"42","789"
#	}}}

#	backslashes inside classes
# sed '\w' matches w
echo 'w=y-x+9*3' | sed 's/[\w=]//g'
# perl '\w' matches any word character
echo 'w=y-x+9*3' | perl -pe 's/[\w=]//g'
printf "\n"
#	{{{
#>>		y-x+9*3
#>>		-+*
#	}}}


#	sed Replace 2nd instance of ':'
echo 'foo:123:bar:baz' | sed 's/:/-/2'
printf "\n"
#>>		foo:123-bar:baz
#	specifying instance number as option not valid in perl

#	option 'e' - allow perl code inside replacement
echo 'foo:123:bar:baz' | perl -pe '$c=0; s/:/++$c==2 ? "-" : $&/ge'
printf "\n"
#>>		foo:123-bar:baz

#	replace 3rd instance 'and'
#	use non-greedy *? matching and \K 
#	Equivelent:		sed 's/and/-/3'
echo 'foo and bar and baz land good' | perl -pe 's/(and.*?){2}\Kand/-/'
printf "\n"
#>>		foo and bar and baz l- good

#	(gnu) sed <num>+g replace all after <num>-th instance (1-indexed)
a='456:foo:123:bar:789:baz
x:y:z:a:v:xc:gf'
echo "$a" | sed 's/:/-/3g'
printf "\n"
#>>		456:foo:123-bar-789-baz
#>>		x:y:z-a-v-xc-gf



#	}}}

cd "$PWD_previous"

#	}}}1



