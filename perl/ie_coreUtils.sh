#	VIM SETTINGS: {{{3
#	VIM: let g:mldvp_filecmd_open_tagbar=0 g:mldvp_filecmd_NavHeadings="" g:mldvp_filecmd_NavSubHeadings="" g:mldvp_filecmd_NavDTS=0 g:mldvp_filecmd_vimgpgSave_gotoRecent=0
#	vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#	vim: set foldlevel=2 foldcolumn=3: 
#	}}}1
#	{{{2
#	Syntax:
#	{{{
#	The syntax 
#			statment if expression
#	is the same as 
#			if (expression) { statement; }
#	The expression for pattern matching, usually written as:
#			'$value =~ /pattern/', 
#	can be abbreviated as simply 
#			'/pattern/' 
#			'm{pattern}' 
#	The default value is drawn from $_ (a built-in variable)
#	If the argument to print is missing, it prints the value of $_
#	}}}

#	Flags: -n, -e, -p
#	{{{
#	The command line flags -ne accomplish the following:
#		-e is used to specify the expression to evaluate.
#		-n wraps the expression inside a while loop that places each input line into $_ and evaluate the expression.
#	Alternatively, there is also a -p flag which replaces -n, and it allows Perl to simulate sed:
#		-p wraps the expression inside a while loop, placing each input line into $_, evaluate the expression which manipulates $_, and prints $_, the result.
#	}}}

#	Equivelent Statements: matching 'pattern'
#	egrep awk, sed, perl
#	{{{
#>%			cat | egrep 'pattern'
#>%			cat | awk '/pattern/ { print }'
#>%			cat | sed -n '/pattern/ p'
#>%			cat | perl -ne 'print if /pattern/'
#>%			cat | perl -ne '/pattern/ and print'
#	LINK: https://lifecs.likai.org/2008/10/using-perl-like-awk-and-sed.html
#	}}}

#	Perl as Grep:
#	Equivelent
#>%			grep <regex>
#>%			perl -wne 'print if /<regex>/'
#>%			perl -wne '/<regex>/ and print'
#	{{{

str_input=( "1) lkbnd" "2) basdf" "3) jlkj" )
str_regex="asdf"

printf "%s\n%s\n%s\n" "${str_input[@]}" | perl -wne "/$str_regex/ and print"
printf "\n"

#	Invert 
#		grep -v <regex>
#		perl -wne '/<regex>/ or print'
printf "%s\n%s\n%s\n" "${str_input[@]}" | perl -wne "/$str_regex/ or print"
printf "\n"

#	Only match
#		grep -o <regex>
#		perl -wne '/<regex>/ and print $&' 
printf "%s\n%s\n%s\n" "${str_input[@]}" | perl -wne "/$str_regex/ and print $&"
printf "\n"

#	Common lines from multiple files
#>%		grep -Fxf <files>
#>%		perl -ne 'if(!$#ARGV){$h{$_}=1; next} print if exists $h{$_}' <files>

#	Lines from second file not present in first
#>%		grep -vFxf <files>
#>%		perl -ne 'if(!$#ARGV){$h{$_}=1; next} print if !exists $h{$_}' <files>


#	}}}

#	Perl as Sed:
#>%			cat | sed 's/pattern/replacement/flags'
#>%			cat | perl -pe 's/pattern/replacement/flags'
#	In Perl
#>%			$value =~ s/pattern/replacement/flags
#>%			$value =~ s{pattern}{replacement}flags
#	Or to update file (inline replace):
#>%			perl -pi -e 's/search/replace/g' file
#	{{{
#	}}}


#	Perl as Awk:
#	Equivelent:
#>%			cat /etc/passwd | awk -F: '{ print $1 }'
#>%			cat /etc/passwd | perl -F: -lane 'print @F[0]'
#	{{{
#	Note that Perl fields are @F[0], @F[1], ...; awk fields are $1, $2, ... instead. However, awk $0 (the whole input line) corresponds to $_ in Perl.
cat /etc/passwd | awk -F: '{ print $1 }' | wc -l 
cat /etc/passwd | perl -F: -lane 'print @F[0]' | wc -l
printf "\n"
#	If we want to combine regular expression matching and field separation, we might have something like:
#	find . | awk -F/ '/hw[0-9]+/ { print $1 }'
#	find . | perl -F/ -lane 'print @F[0] if /hw[0-9]+/'
#	cat | awk '{ print NR, $0 }'
#	cat | perl -MEnglish -ne 'print $NR, " ", $_'

#	Get columns 0, 3, and 4 (0-indexed) from csv
cat "$mld_data/data.csv" | perl -F, -lane 'print @F[0,3,4]'
printf "\n"

#	Ongoing: 2020-11-11T20:39:59AEDT (how to) set output seperator for when using this method?
#	Get columns 0 through 4 (0-indexed) from csv
cat "$mld_data/data.csv" | perl -F, -lane 'print @F[0..4]'
printf "\n"
#	}}}


#	Print columns of 'uniq -c':
#			git log --date=short --pretty=format:%ad | sort | uniq -c | perl -lane 'print $F[0]'
#			git log --date=short --pretty=format:%ad | sort | uniq -c | perl -lane 'print $F[1]'


#	}}}1

