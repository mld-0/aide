#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=3:
#   }}}1
use strict; 
use warnings;
no warnings 'shadow';
#	{{{2

#	match 				m//  or  //
#	substitute			s///
#	transliterate 		tr///

#	Binding operator =~
#		m/match/  
#	is equivelent to  
#		$_ =~ m/match/
#	When used with match, the string on the LHS is compared with the regex match. In a scalar context, true/false is returned, in a list context, all matches are returned if the 'g' modifier is used
#	!~ inverts the match
#	Returns a boolean in a sclar context, or the matches of any grouped expressions in a list context

#	Match 
my $bar = "This is food and again fool"; 
if ($bar =~ /foo\w/){
	print "First time is matching\n";
} else {
	print "First time is not matching\n"; 
}

#	With multiple matches for the named capture group, the last is stored
my @result = $bar =~ m/(?<group_foo>foo\w)/g;
print "result=(@result)\n";
print "group_foo=($+{group_foo})\n";
#	or
my @result;
push(@result, $&) while ($bar =~ /(?<group_foo>foo\w)/g);
print "result=(@result)\n";
while ( (my $k, my $v) = each %+) {
	print "k=($k), v=($v)\n";
}


$_ = "foo";
if (/foo/){
	print "Second time is matching\n"; 
} else {
	print "Second time is not matching\n"; 
}


#	Any other characters may be used as delimitor in place of /
my $bar = "This is foo and again foo"; 
if ($bar =~ m[foo]) {
    print "First time is matching\n";
} else {
	print "First time is not matching\n"; 
}
print "\n";

#	Match modifiers
#		i		case insensitive
#		m		match ^$ against newlines instead of against string boundry
#		o		evaluate expression only once
#		s		allows '.' to match newline
#		x		Allows whitespace in the expression for clarity
#		g		globally find all matches
#		cg		allow search to contine even after a global match fails
#		a 		use only ASCII versions of character classes
#		c		don't reset pos on failed matches when using /g
#	may be used in whichever order


#	Match only once  m?PATTERN?
#		matches only once within the string
my @list = qw/food foosball subeo footnote terfoot canic footbrdige/;
my ($first, $last);
foreach (@list)
{
   $first = $1 if m?(foo.*)?;
   $last = $1 if m/(foo.*)/;
}
print "first=($first), last=($last)\n";
print "\n";


#	Regex variables
#		$&  entire matched string
#		$`  before matched string
#		$'  after matched string
my $string = "The food is in the salad bar"; 
$string =~ m/foo/;
print "Before: $`\n";
print "Matched: $&\n";
print "After: $'\n";
print "\n";

if ("Hello there, neighbor" =~ /\s(\w+),/) {
	print "That was ($`)($&)($').\n"; 
}
print "\n";

#	Match in list context
#		When a pattern match (m//) is used in a list context, the return value is a list of the capture variables created in the match, or an empty list if the match failed
$_ = "Hello there, neighbor!";
my($first, $second, $third) = /(\S+) (\S+), (\S+)/; 
print "$second is my $third\n";
print "\n";

#	Match with g modifier
#		match at more than one place in a string. In this case, a pattern with a pair of parentheses will return a capture from each time it matches
my $text = "Fred dropped a 5 ton granite block on Mr. Slate"; 
my @words = ($text =~ /([a-z]+)/ig);
print "Result: @words\n";
print "\n";

#	Reading a string into a hash with match
#		Each time the pattern matches, it returns a pair of captures. Those pairs of values then become the key-value pairs in the newly-created hash.
my $data = "Barney Rubble Fred Flintstone Wilma Flintstone"; 
my %last_name = ($data =~ /(\w+)\s+(\w+)/g);
print "last_name=(@{[ %last_name ]})\n";
print "\n";

#	Matching multiple lines
#		Classic regular expressions were used to match just single lines of text. But since Perl can work with strings of any length, Perl’s patterns can match multiple lines of text as easily as single lines.
$_ = "I'm much better\nthan Barney is\nat bowling,\nWilma.\n";
print "Found 'wilma' at start of line\n" if /^wilma\b/im;
print "\n";

#	read an entire file into one variable,§ then add the file’s name as a prefix at the start of each line:
#>%		open FILE, $filename or die "Can't open '$filename': $!";
#>%		my $lines = join '', <FILE>; 
#>%		$lines =~ s/^/$filename: /gm;

#	s/// 	Substitution operator
my $my_string = "The cat sat on the mat"; 
print "$my_string\n";
$my_string =~ s/cat/dog/;
print "$my_string\n";
print "\n";

$_ = "fred flintstone"; 
if (s/fred/wilma/) {
	print "Successfully replaced fred with wilma!\n"; 
}
print "\n";

#	Substitution alternative delimiters
#>%			s/fred/barney/;
#>%			s{fred}{barney}; 
#>%			s[fred](barney); 
#>%			s<fred>#barney#;

#	Substitution modifiers
#		i		case insensitive
#		m		match ^$ against newlines instead of against string boundry
#		o		evaluate expression only once
#		s		allows '.' to match newline
#		x		Allows whitespace in the expression for clarity
#		g		Replace all occurences of the found expression
#		e		Evaluate the replacement as a perl statement, and use the return value as replacement text
#		r		Leave origional string alone and return modified copy
#	Example options
#>%		/k/aai  # only matches the ASCII K or k, not Kelvin sign 
#>%		/k/aia  # the /a's don't need to be next to each other 
#>%		/ss/aai  # only matches ASCII ss, SS, sS, Ss, not ß 
#>%		/ff/aai  # only matches ASCII ff, FF, fF, Ff, not ff

#	Nondestructive Substitutions
use 5.014;
my $original = 'Fred ate 1 rib'; 
my $copy = $original;
$copy =~ s/\d+ ribs?/10 ribs/;
#	or
(my $copy = $original) =~ s/\d+ ribs?/10 ribs/;
#	or
my $copy = $original =~ s/\d+ ribs?/10 ribs/r;
print "origional=($original), copy=($copy)\n";
print "\n";

#	Case shifting
#		The \U escape forces what follows to all uppercase
#		the \L escape forces lowercase
#		By default, these affect the rest of the (replacement) string, or you can turn off case shifting with \E
#		When written in lowercase (\l and \u ), they affect only the next character
#		You can even stack them up. Using \u with \L means “all lowercase, but capitalize the first letter”#
$_ = "I saw Barney with Fred.";
s/(fred|barney)/\U$1/gi; # $_ is now "I saw BARNEY with FRED."
s/(fred|barney)/\L$1/gi; # $_ is now "I saw barney with fred."
s/(\w+) with (\w+)/\U$2\E with $1/i; # $_ is now "I saw FRED with barney."
s/(fred|barney)/\u$1/ig; # $_ is now "I saw FRED with Barney."
s/(fred|barney)/\u\L$1/ig; # $_ is now "I saw Fred with Barney."
print "$_\n";
print "\n";
#	As it happens, although we’re covering case shifting in relation to substitutions, these escape sequences are available in any double-quotish string:
my $name = "babydoll";
print "Hello, \L\u$name\E, would you like to play a game?\n";
print "\n";

#	split(/separator, $string)
#		breaks up a string according to a pattern.
my @fields = split /:/, "abc:def:g:h"; # gives ("abc", "def", "g", "h")
my @fields = split /:/, "abc:def::g:h"; # gives ("abc", "def", "", "g", "h")
my @fields = split /:/, ":::a:b:c:::"; # gives ("", "", "", "a", "b", "c")
#	cleanup whitespace
my $some_input = "This is a \t test.\n";
my @args = split /\s+/, $some_input; # ("This", "is", "a", "test.")
#	The default for split is to break up $_ on whitespace: 
my @fields = split; # like split /\s+/, $_;

#	$result = join($glue, @pieces)
#		The join function doesn’t use patterns, but performs the opposite function of split: split breaks up a string into a number of pieces, and join glues together a bunch of pieces to make a single string.
my $x = join ":", 4, 6, 8, 10, 12; # $x is "4:6:8:10:12"
my @values = split /:/, $x; # @values is (4, 6, 8, 10, 12) 
my $z = join "-", @values; # $z is "4-6-8-10-12"
print "x=($x)\n";
print "\n";

#	Translation operator
#		Replace all occurences of the characters in SEARCHLIST with the corresponding characters in REPLACEMENTLIST 
#			 tr/SEARCHLIST/REPLACEMENTLIST/cds
#			 y/SEARCHLIST/REPLACEMENTLIST/cds
my $string = 'The cat sat on the mat'; 
print "string=($string)\n";
$string =~ tr/a/o/;
print "string=($string)\n";

#	Character ranges can also be used
$string =~ tr/a-z/A-Z/;
print "$string\n";
print "\n";

#	Translation modifiers
#		c		Complements SEARCHLIST
#		d		Delete found-but-unreplaced characters
#		s		Squashes duplicate replaced characters

#	Delete unreplaced
my $string = 'the cat sat on the mat.'; 
$string =~ tr/a-z/b/d;
print "$string\n";

#	Squash duplicate sequences
my $string = 'food';
$string =~ tr/a-z/a-z/s;
print "$string\n";
print "\n";

#	Continue: 2021-02-21T02:57:52AEDT unicode properties /\p{Digit}/ pg123 Learning Perl

#	Perl regex 
#		[...] 			any single character in ...
#		[^...]			any single character not in ...
#		*				0 or more occurences 
#		+				1 or more occurences
#		?				0 or 1 occurences
#		{n}				exactly n occurences
#		{n,}			n or more occurences
#		{,m}			at most m occurences
#		{n,m}			n to m occurences
#		a|b				a or b
#		\w				word character
#		\W				non-word character
#		\s				whitespace [\t\n\r\f]
#		\S				non-whitespace 
#		\d				digit [0-9]
#		\D				non-digit
#		^ or \A			match beginning of string
#		$ or \Z 		match end of string (before newline)
#		\z				end of string
#		\b{}			match at unicode boundry of specified type
#		\B{}			Match where corresponding \b{} doesn't match
#		\b				word bountry when outside brackets, backspace (0x08) inside brackets
#		\B				non word boundry
#		\G				match only after 'pos' position of previous match
#		\n				newline
#		\t				tab
#		\1 ... \9		n-th grouped subexpression
#		\10				10th grouped subexpression if matched, otherwise octal representation of character code
#	Non-greedy quanitifiers
#		??			0 or 1
#		*?			0 or more
#		+?			1 or more
#		{m,n}?		specific number


#	Using \G (previous match position) assertion
my $string = "The time is: 12:31:02 on 4/12/00";
$string =~ /:\s+/g;
(my $time) = ($string =~ /\G(\d+:\d+:\d+)/);
$string =~ /.+\s+/g;
(my $date) = ($string =~ m{\G(\d+/\d+/\d+)});
print "time=($time), date=($date)\n";
print "\n";

#	Perl variable names
#>%		[a-zA-Z0-9_]

#	[]  Character classes 
$_ = "The HAL-9000 requires authorization to continue."; 
if (/HAL-[0-9]+/) {
	print "The string mentions some model of HAL computer.\n"; 
}

#	Match horizontal and/or vertical whitespace
use 5.010;
if (/\h/) {
	say 'The string matched some horizontal whitespace.'; 
}
if (/\v/) {
	say 'The string matched some vertical whitespace.'; 
}
if (/[\v\h]/) { # same as \p{Space}, but not more than \s
	say 'The string matched some whitespace.'; 
}
print "\n";

#	Interpolating into patterns:
#>%		my $what = "larry";
#>%		while (<>) {
#>%			if (/\A($what)/) { # pattern is anchored at beginning of string
#>%				print "We saw $what in beginning of $_"; 
#>%			}
#>%		}

#	Capture group
$_ = "Hello there, neighbor";
if (/\s([a-zA-Z]+),/) { # capture the word between space and comma
	print "the word was $1\n"; # the word was there 
}
$_ = "Hello there, neighbor"; if (/(\S+) (\S+), (\S+)/) {
print "words were ($1) ($2) ($3)\n"; }
print "\n";

#	Capture group
my $string = "Cats go Catatonic\nWhen given Catnip"; 
my ($start) = ($string =~ /\A(.*?) /);
my @lines = $string =~ /^(.*?) /gm;
print "First word: $start\n","Line starts: @lines\n";
print "\n";

#	matching with capture groups
my $time = "12:05:30";
$time =~ m/(\d+):(\d+):(\d+)/;
my ($hours, $minutes, $seconds) = ($1, $2, $3);
print "Hours : $hours, Minutes: $minutes, Second: $seconds\n";
print "\n";

#	Substitution with capture groups
my $date = '03/26/1999';
$date =~ s#(\d+)/(\d+)/(\d+)#$3/$1/$2#;
print "$date\n";
print "\n";

#	Persistance of captures
#		An unsuccessful match leaves the previous capture values intact, but a successful one resets them all.
my $wilma = '123';
if ($wilma =~ /([a-zA-Z]+)/) { 
	print "Wilma's word was $1.\n";
} else {
	print "Wilma doesn't have a word.\n"; 
}
print "\n";

#	Non-capturing parentheses
#		(?:)
$_ = "Trisaurus steak";
if (/(?:bronto)?saurus (?:BBQ )?(steak|burger)/) {
	print "Fred wants a $1\n"; 
}
print "\n";

#	The \G assertion allows you to continue searching from the point where the last match occurred.
my $string = "The time is: 12:31:02 on 4/12/00";
$string =~ /:\s+/g;
my ($time) = ($string =~ /\G(\d+:\d+:\d+)/); 
$string =~ /.+\s+/g;
($date) = ($string =~ m{\G(\d+/\d+/\d+)});
print "Time: $time, Date: $date\n";
print "\n";


#	Named capture groups
#		(?<name>)
#		$+{name}
my $names = 'Fred or Barney';
if ( $names =~ m/(?<name1>\w+) (?:and|or) (?<name2>\w+)/ ) {
	say "I saw $+{name1} and $+{name2}"; 
}

#	Now that you have a way to label matches, you also need a way to refer to them for back references. Previously, you used either \1 or \g{1} for this. With a labeled group, you can use the label in \g{label}
my $names = 'Fred Flintstone and Wilma Flintstone';
if ( $names =~ m/(?<last_name>\w+) and \w+ \g{last_name}/ ) {
	say "I saw $+{last_name}"; 
}
#	Instead of using \g{label}, you use \k<label>
my $names = 'Fred Flintstone and Wilma Flintstone';
if ( $names =~ m/(?<last_name>\w+) and \w+ \k<last_name>/ ) {
	say "I saw $+{last_name}"; 
}
print "\n";

#	Using Perl 5.10+
if ("Hello there, neighbor" =~ /\s(\w+),/p) {
	print "That actually matched '${^MATCH}'.\n"; 
}
if ("Hello there, neighbor" =~ /\s(\w+),/p) {
	print "That was (${^PREMATCH})(${^MATCH})(${^POSTMATCH}).\n"; 
}
print "\n";

#	Regex expression precedence
#			Parentheses (grouping or capturing) 		(...) (?:...) (?<LABEL>..)
#			Qualifiers									a*, a+, a?, a{n,m}
#			Anchors and sequences						^ $ \A \b \z \Z
#			Alteration									a|b|c
#			Atoms										a [abc] \d \1 \g{2}

#	A pattern test program
#>%		while (<>) { # take one input line at a time
#>%			chomp;
#>%			if (/YOUR_PATTERN_GOES_HERE/) {
#>%				print "Matched: |$`<$&>$'|\n"; # the special match vars } else {
#>%				print "No match: |$_|\n"; 
#>%			}
#>%		}


#	Continue: 2021-02-19T19:48:35AEDT positive/negative look aheads/behinds

#	Continue: 2021-02-21T03:39:00AEDT Learning Perl Ch9 Processing Text with regex

#	Continue: 2021-02-21T04:29:50AEDT in-place editing with substitution, -I .bak file, 

#	Inplace editing from command line
#>%		perl -p -i.bak -w -e 's/Randall/Randal/g' fred*.dat#
#	which is equivelent to
#>%		#!/usr/bin/perl -w
#>%		$^I = ".bak";
#>%		while (<>) { 
#>%			s/Randall/Randal/g;
#>%			print; 
#>%		}


#	$^I		backup file
#		if set, creates a backup file when performing inplace editing
#>%		$^I = ".bak"

#	}}}1
