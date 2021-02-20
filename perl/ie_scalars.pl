#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=3:
#   }}}1

#	{{{2

#	Numbers
#		Perl represents integers internally as double floating point values

#	Floating point literals
my $var = 1.25;
my $var = 255.000;
my $var = 255.0;
my $var = 7.25e45 ;
my $var = -12e-24 ;
my $var = -1.2E-23 ;

#	Integer literals
my $var = 0;
my $var = 2001;
my $var = -40;
my $var = 255;
my $var = 61298040283768;
my $var = 100_000_000;  # Perl allows underscores within integers for ease of reading

#	Nondecimal integer literal
my $var = 0377;  # 377 octal = 255 decimal
my $var = 0xff;  # FF hex = 255 decimal
my $var = 0b11111111;  # also FF hex = 255 decimal
my $var = 0x50_65_72_7C;  # Perl also allows underscores in nondecimal literals

#	Numeric Operators
#		+		Plus
#		-		Minus
#		*		Times
#		/		Divided
#		%		Modulus 		(Inconsistent results with negitive numbers?)
#		**		Power


#	Strings
#	Unicode literal prama:
#		full support for unicode in data, plus one can (but presumedly shouldn't) use unicode in variable names
use utf8;


#	Single quoted literals
#		Single quoting does not interpolate. Every character, except single quote, and backslash stands for itself. 
#		Represent \ as \\, and ' as \'
#		\n is not lineline, $value is not a variable, ect.

my $var = 'fred'; # those four characters: f, r, e, and d 'barney' # those six characters
my $var = ''; # the null string (no characters)
my $var = '5⁄6∞☃☠ ' ; # Some "wide" Unicode characters
my $var = 'Don\'t let an apostrophe end this string prematurely!';
my $var = 'the last character is a backslash: \\';
my $var = 'hello\n'; # hello followed by backslash followed by n 
my $var = 'hello
there';  # hello, newline, there (11 characters total) 
my $var = '\'\\'; # single quote followed by backslash

#	Double Quoted literals
#		Double quoted strings interpolate variables, that is, substitute their values
#	Special characters:
#		\n			newline
#		\r			return
#		\t			tab
#		\f			formfeed
#		\b			backspace
#		\a			bell
#		\e			Escape (ASCII escape character)
#		\007		Octal ASCII value
#		\x7f		Hex ASCII value
#		\x{2744}	Hex Unicode value
#		\cC			Control character (Ctrl + c)
#		\I			lowercase next letter
#		\L			lowercase until \E
#		\u			uppercase next letter
#		\U			uppercase until \E
#		\Q			Quote nonword characters by adding backslash until \E
#						Use characters between \Q...\E as (literal) characters, not regex symbols
#		\E			End \L, \U, or \Q

my $var = "barney"; # just the same as 'barney'
my $var = "hello world\n"; # hello world, and a newline
my $var = "The last character of this string is a quote mark: \"" ;
my $var = "coke\tsprite"; # coke, a tab, and sprite
my $var = "\x{2668}"; # Unicode HOT SPRINGS character code point

#	String operators
#			.		Concatenation
#			x		repetition


#	Automatic conversion between numbers and strings
#		done by perl for the most part (depending on operator)
#		only unquoted values are treated as octal, decimal-as-strings with leading zeros are treated as decimals

#	Warnings
#		perl -w 

use strict; 
use warnings;
no warnings 'shadow';  # disable warnings about repeated use of 'my'
#use diagnostics;  # slows launch of program, makes additional information available about any failures


#	Scalar variables
#		Hold one value,
#		Prefixed with $ (sigil)
my $fred = 17;  # give $fred the value of 17
my $barney = 'hello';  # give $barney the five-character string 'hello'
my $barney = $fred + 3;  # give $barney the current value of $fred plus 3 (20)
my $barney = $barney * 2;  # $barney is now $barney multiplied by 2 (40)

#	Binary assignment
#		+=		plus equals
#		-=		minus equals
#		*=		times equals
#		.=		concatenate equals
#		%=		mod equals
#		**=		power equals


#	Print
#		perl's print does not include a newline
print "hello world\n";  # say hello world, followed by a newline
print "The answer is ", 6 * 7, "\n";  # You can give print a series of values, separated by commas

#	Variable interpolation
#		Use ${var} to limit the variable name to text within brackets
my $what = "brontosaurus steak";
my $n = 3;
# print "fred ate $n $whats.\n";  # Fails with use strict enabled, variable 'whats' is not defined
print "fred ate $n ${what}s.\n";
print "fred ate $n $what" . "s.\n";
print "\n";

#	Get code of character
#		ord()
my $code_point = ord('א');
print "code_point=($code_point)\n";
my $hex = sprintf("0x%X", $code_point);
print "hex=($hex)\n";

#	Create character by code
my $alef = chr(0x5d0);
my $alef = chr(1488);
my $alef = chr($code_point);
print "alef=($alef)\n";
print "\n";


#	Operator Precedence
#	Ongoing: 2021-02-20T16:14:31AEDT && has a higher priority than || ? 
#	{{{
#		left 	parentheses and arguments to list operators
#		left 	->
#		left 	++ -- (autoincrement and autodecrement)
#		right	**
#		right 	\!~+- (unary operators)
#		left	=~ !~ 
#		left 	*/%x
#		left	+-. (binary operators)
#		left 	<< >>
#		left	-X (filetests), named unary operators
#		left 	< <= > >= lt le gt gt ge (unequal comparison)
#		left 	== != <=> eq ne cmp (equals comparision)
#		left 	&
#		left 	| ^	
#		left	&&
#		left	||
#		...
#		right	? : (conditional operator)
#		right 	= += -= .= (asignments)
#		left	, => (list operators)
#		right	not
#		left	and
#		left	or xor
#	}}}

#	Comparison Operators			numeric		string
#		Equal						==			eq	
#		Not Equal					!=			ne
#		Less than					<			lt
#		Greater than				>			gt
#		Less than equal 			<=			le
#		Greater than equal			>=			ge

#	If statements
my $name = "Larry";
if ($name gt 'fred') {
	print "'$name' comes after 'fred' in sorted order.\n";
} else {
	print "'$name' does not come after 'fred'.\n";
}
print "\n";

#	Read from stdin
#	my $text = <STDIN>; 
#	chomp($text); 

#	While loop
my $count = 0;
while ($count < 10) {
	$count += 2;
	print "count is now $count\n"; # Gives values 2 4 6 8 10 }
}
print "\n";

#	Undef 
#		undef evaluates to zero when used as a number
#		undef evaluates to an empty string when used as a string
my $var = undef;

#	defined()
#		returns false for undef, and true for anything else
my $madonna = <STDIN>;
if ( defined($madonna) ) {
	print "The input was $madonna"; 
} else {
	print "No input available!\n"; 
}

#	}}}1
