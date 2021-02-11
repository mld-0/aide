#!/usr/bin/perl
#	VIM SETTINGS: {{{3
#	VIM: let g:mldvp_filecmd_open_tagbar=0 g:mldvp_filecmd_NavHeadings="" g:mldvp_filecmd_NavSubHeadings="" g:mldvp_filecmd_NavDTS=0 g:mldvp_filecmd_vimgpgSave_gotoRecent=0
#	vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#	vim: set foldlevel=2 foldcolumn=3: 
#	}}}1
#	{{{2
#	Working examples, all the basics of perl, (mostly) from:
#	LINK: https://www.tutorialspoint.com/perl
use strict; 
use warnings;

#	perlrun (perl flags/options)
#	-l: end-of-line processing, (chomp input when used with -n or -p), 
#	-p: Places a printing loop around your command so that it acts on each
#	    line of standard input. Used mostly so Perl can beat the
#	    pants off awk in terms of power AND simplicity :-)
#	-n: Places a non-printing loop around your command.
#	-e: Allows you to provide the program as an argument rather
#	    than in a file. You don't want to have to create a script
#	    file for every little Perl one-liner.
#	-i: Modifies your input file in-place (making a backup of the
#	    original). Handy to modify files without the {copy,
#	    delete-original, rename} process.
#	-w: Activates some warnings. Any good Perl coder will use this.
#	-d: Runs under the Perl debugger. For debugging your Perl code,
#	    obviously.
#	-t: Treats certain "tainted" (dubious) code as warnings (proper
#	    taint mode will error on this dubious code). Used to beef
#	    up Perl security, especially when running code for other
#	    users, such as setuid scripts or web stuff.

#	Command line options:
#	{{{
#	interactive 
#>%		-e <code>
#	Debugging:
#		-d[:debugger]
#	#include directory
#		-ldirectory 
#	tainting checks
#		-T
#	tainting warnings
#		-t
#	unsafe operations (allow)
#		-U
#	many warnings
#		-w
#	all warnings
#		-W
#	disable warnings
#		-X
#	file
#		given path to file -> run perl from said file
#	}}}

#	Hello world from within (.*)\.py
print "Hello World\n";
#>>		Hello World

#	Hello world from shell
#>%		perl -e 'print "Hello World\n"'

#	Comments:
#	{{{
#	Single line comments are denoted by '#'
=begin comment
This is all part of multiline comment.
You can use as many lines as you like
These comments will be ignored by the 
compiler until the next =cut is encountered.
=cut
#	}}}

# 	This prints with a line break in the middle, followed by a number of spaces
print "Hello
          world\n";
#	{{{
#>>		Hello
#>>		          world
#	}}}

#	Single vs double quoting
#	{{{
$a = 10;
print "Hello, world\n";
print 'Hello, world\n';
print "Value of a = $a\n";
print 'Value of a = $a\n';
print "\n";
#	{{{
#>>		Hello, world
#>>		Hello, world\nValue of a = 10
#>>		Value of a = $a\n
#	}}}
#	}}}

#	Heredoc
#	{{{
my $var = <<"EOF";
This is the syntax for here document and it will continue
until it encounters a EOF in the first line.
This is case of double quote so variable value will be 
interpolated. For example value of a = $a
EOF
print "$var\n";
print "\n";
#	{{{
#>>		This is the syntax for here document and it will continue
#>>		until it encounters a EOF in the first line.
#>>		This is case of double quote so variable value will be 
#>>		interpolated. For example value of a = 10
#	}}}
$var = <<'EOF';
This is case of single quote so variable value will be 
interpolated. For example value of a = $a
EOF
print "$var\n";
print "\n";
#	{{{
#>>		This is case of single quote so variable value will be 
#>>		interpolated. For example value of a = $a
#	}}}
#	}}}

#	Escaping characters
#	{{{
my $result = "This is \"number\"";
print "$result\n";
print "\$result\n";
print "\n";

#	{{{
#>>		This is "number" 
#>>		$result
#	}}}
#	}}}

#	Perl datatypes:
#		Scalars - denoted by '$'
#			number, string, or reference
#		Arrays - denoted by '@'
#			zero-indexed
#		Hashes - denoted by '%'
#			unordered key/value pairs

#	Numerical literals:
#	{{{
#	Integer	
#		1234
#	Negative integer	
#		-100
#	Scientific notation	
#		16.12E14
#	Hexadecimal	
#		0xffff
#	Octal	
#		0577
#	}}}

#	String Literals:
#	{{{
#		\\			Backslash
#		\'			Single quote
#		\"			Double quote
#		\a			Alert or bell
#		\b			Backspace
#		\f			Form feed
#		\n			Newline
#		\r			Carriage return
#		\t			Horizontal tab
#		\v			Vertical tab
#		\0nn		Creates Octal formatted numbers
#		\xnn		Creates Hexideciamal formatted numbers
#		\cX			Controls characters, x may be any character
#		\u			Forces next character to uppercase
#		\l			Forces next character to lowercase
#		\U			Forces all following characters to uppercase
#		\L			Forces all following characters to lowercase
#		\Q			Backslash all following non-alphanumeric characters
#		\E			End \U, \L, or \Q#
#	}}}

#	String Quoting (Interpolation) Examples:
#	{{{
#	This is case of interpolation.
my $str = "Welcome to \ntutorialspoint.com!";
print "$str\n";
# 	This is case of non-interpolation.
$str = 'Welcome to \ntutorialspoint.com!';
print "$str\n";
# 	Only W will become upper case.
$str = "\uwelcome to tutorialspoint.com!";
print "$str\n";
# 	Whole line will become capital.
$str = "\UWelcome to tutorialspoint.com!";
print "$str\n";
# 	A portion of line will become capital.
$str = "Welcome to \Ututorialspoint\E.com!"; 
print "$str\n";
# 	Backsalash non alpha-numeric including spaces.
$str = "\QWelcome to tutorialspoint's family";
print "$str\n";
print "\n";
#	{{{
#>>		Welcome to
#>>		tutorialspoint.com!
#>>		Welcome to \ntutorialspoint.com!
#>>		Welcome to tutorialspoint.com!
#>>		WELCOME TO TUTORIALSPOINT.COM!
#>>		Welcome to TUTORIALSPOINT.com!
#>>		Welcome\ to\ tutorialspoint\'s\ family
#	}}}
#	}}}

#	Variable Declarations:
#	{{{
#	Scalar
my $age = 25;             # An integer assignment
my $name = "John Paul";   # A string 
my $salary = 1445.50;     # A floating point
print "Age = $age\n";
print "Name = $name\n";
print "Salary = $salary\n";
print "\n";
#	{{{
#>>		Age = 25
#>>		Name = John Paul
#>>		Salary = 1445.5
#	}}}
#	}}}

#	Arrays (lists)
#	{{{
my @ages = (25, 30, 40);             
my @names = ("John Paul", "Lisa", "Kumar");
print "\$ages[0] = $ages[0]\n";
print "\$ages[1] = $ages[1]\n";
print "\$ages[2] = $ages[2]\n";
print "\$names[0] = $names[0]\n";
print "\$names[1] = $names[1]\n";
print "\$names[2] = $names[2]\n";
print "\n";
#	{{{
#>>		$ages[0] = 25
#>>		$ages[1] = 30
#>>		$ages[2] = 40
#>>		$names[0] = John Paul
#>>		$names[1] = Lisa
#>>		$names[2] = Kumar
#	}}}
#	}}}

#	Hash (dictionarys)
#	{{{
my %data = ('John Paul', 45, 'Lisa', 30, 'Kumar', 40);
print "\$data{'John Paul'} = $data{'John Paul'}\n";
print "\$data{'Lisa'} = $data{'Lisa'}\n";
print "\$data{'Kumar'} = $data{'Kumar'}\n";
print "\n";
#	{{{
#>>		$names[0] = John Paul
#>>		$names[1] = Lisa
#>>		$names[2] = Kumar
#>>		$data{'John Paul'} = 45
#>>		$data{'Lisa'} = 30
#>>		$data{'Kumar'} = 40
#	}}}
#	}}}

#	Variable context:
#	{{{
#	{{{
#	Scalar				Assignment evaluates RHS in scalar context
#	List				Assignment to an array or hash evaluates RHS in list context
#	Boolean				True/False
#	Void				Nil
#	Interpolative		Quoting
#	}}}
@names = ('John Paul', 'Lisa', 'Kumar');
my @copy = @names;
my $size = @names;
print "Given names are : @copy\n";
print "Number of names are : $size\n";#
print "\n";
#	{{{
#>>		Given names are : John Paul Lisa Kumar
#>>		Number of names are : 3
#	}}}
#	}}}

#	Scalar operations
#	{{{
#	Numerical
my $integer = 200;
my $negative = -300;
my $floating = 200.340;
my $bigfloat = -1.2E-23;
# 377 octal, same as 255 decimal
my $octal = 0377;
# FF hex, also 255 decimal
my $hexa = 0xff;
print "integer = $integer\n";
print "negative = $negative\n";
print "floating = $floating\n";
print "bigfloat = $bigfloat\n";
print "octal = $octal\n";
print "hexa = $hexa\n";
print "\n";
#	{{{
#>>		integer = 200
#>>		negative = -300
#>>		floating = 200.34
#>>		bigfloat = -1.2e-23
#>>		octal = 255
#>>		hexa = 255
#	}}}

#	Strings
$var = "This is string scalar!";
my $quote = 'I m inside single quote - $var';
my $double = "This is inside single quote - $var";
my $escape = "This example of escape -\tHello, World!";
print "var = $var\n";
print "quote = $quote\n";
print "double = $double\n";
print "escape = $escape\n";
print "\n";
#	{{{
#>>		var = This is string scalar!
#>>		quote = I m inside single quote - $var
#>>		double = This is inside single quote - This is string scalar!
#>>		escape = This example of escape -	Hello, World!
#	}}}

# Concatenates strings.
$str = "hello" . "world";       
# adds two numbers.
my $num = 5 + 10;                  
# multiplies two numbers.
my $mul = 4 * 5;                   
# concatenates string and number.
my $mix = $str . $num;             
print "str = $str\n";
print "num = $num\n";
print "mul = $mul\n";
print "mix = $mix\n";
print "\n";
#	{{{
#>>		str = helloworld
#>>		num = 15
#>>		mul = 20
#>>		mix = helloworld15
#	}}}

my #	Multi-line strings
$string = 'This is
a multiline
string';
print "$string\n";
#	{{{
#>>		This is
#>>		a multiline
#>>		string
#	}}}
print <<EOF;
This is
a multiline
string

EOF
#	{{{
#>>		This is
#>>		a multiline
#>>		string
#	}}}

#	V-strings
my $smile  = v9786;
my $foo    = v102.111.111;
my $martin = v77.97.114.116.105.110; 
print "smile = $smile\n";
print "foo = $foo\n";
print "martin = $martin\n";
print "\n";
#	{{{
#>>		Wide character in print at - line 368.
#>>		smile = ☺
#>>		foo = foo
#>>		martin = Martin
#	}}}

#	Special literals
print "File name ". __FILE__ . "\n";
print "Line Number " . __LINE__ ."\n";
print "Package " . __PACKAGE__ ."\n";
# they can not be interpolated
print "__FILE__ __LINE__ __PACKAGE__\n";
print "\n";
#	{{{
#>>		File name -
#>>		Line Number 381
#>>		Package main
#>>		__FILE__ __LINE__ __PACKAGE__
#	}}}
#	}}}

#	Array Usage:
#	{{{
@ages = (25, 30, 40);             
@names = ("John Paul", "Lisa", "Kumar");
print "\$ages[0] = $ages[0]\n";
print "\$ages[1] = $ages[1]\n";
print "\$ages[2] = $ages[2]\n";
print "\$names[0] = $names[0]\n";
print "\$names[1] = $names[1]\n";
print "\$names[2] = $names[2]\n";
print "\n";
#	{{{
#>>		$ages[0] = 25
#>>		$ages[1] = 30
#>>		$ages[2] = 40
#>>		$names[0] = John Paul
#>>		$names[1] = Lisa
#>>		$names[2] = Kumar
#	}}}

#	Declarations of an array:
my @array = (1, 2, 'Hello');
print "@array";
@array = qw/This is an array/;
print "@array";
print "\n";
#	{{{
#>>		$ages[0] = 25
#>>		$ages[1] = 30
#>>		$ages[2] = 40
#>>		$names[0] = John Paul
#>>		$names[1] = Lisa
#>>		$names[2] = Kumar
#	}}}

#	Access Array Elements by index
my @days = qw/Mon Tue Wed Thu Fri Sat Sun/;
print "$days[0]\n";
print "$days[1]\n";
print "$days[2]\n";
print "$days[6]\n";
print "$days[-1]\n";
print "$days[-7]\n";
print "\n";
#	{{{
#>>		Mon
#>>		Tue
#>>		Wed
#>>		Sun
#>>		Sun
#>>		Mon
#	}}}

#	Sequential arrays:
my @var_10 = (1..10);
my @var_20 = (10..20);
my @var_abc = ('a..z');
print "@var_10\n";   # Prints number from 1 to 10
print "@var_20\n";   # Prints number from 10 to 20
print "@var_abc\n";  # Prints number from a to z
print "\n";
#	{{{
#>>		1 2 3 4 5 6 7 8 9 10
#>>		10 11 12 13 14 15 16 17 18 19 20
#>>		a b c d e f g h i j k l m n o p q r s t u v w x y z
#	}}}

#	Array Size:
@array = (1,2,3);
$array[50] = 4;
$size = @array;
my $max_index = $#array;
print "Size:  $size\n";
print "Max Index: $max_index\n";
print "\n";
#	{{{
#>>		Size:  51
#>>		Max Index: 50
#	}}}

#	Array functions:
#		push
#		pop
#		shift
#		unshift
# 	create a simple array
my @coins = ("Quarter","Dime","Nickel");
print "1. \@coins  = @coins\n";
# 	add one element at the end of the array
push(@coins, "Penny");
print "2. \@coins  = @coins\n";
# 	add one element at the beginning of the array
unshift(@coins, "Dollar");
print "3. \@coins  = @coins\n";
# 	remove one element from the last of the array.
pop(@coins);
print "4. \@coins  = @coins\n";
# 	remove one element from the beginning of the array.
shift(@coins);
print "5. \@coins  = @coins\n";
print "\n";
#	{{{
#>>		1. @coins  = Quarter Dime Nickel
#>>		2. @coins  = Quarter Dime Nickel Penny
#>>		3. @coins  = Dollar Quarter Dime Nickel Penny
#>>		4. @coins  = Dollar Quarter Dime Nickel
#>>		5. @coins  = Quarter Dime Nickel
#	}}}

#	Slices:
@days = qw/Mon Tue Wed Thu Fri Sat Sun/;
#	indervidual elements:
my @weekdays = @days[3,4,5];
print "@weekdays\n";
@days = qw/Mon Tue Wed Thu Fri Sat Sun/;
#	ranges
@weekdays = @days[3..5];
print "@weekdays\n";
print "\n";
#	{{{
#>>		Thu Fri Sat
#>>		Thu Fri Sat
#	}}}

#	Replacing array elements: splice()
#>%		splice @ARRAY, OFFSET [ , LENGTH [ , LIST ] ]
my @nums = (1..20);
print "Before - @nums\n";
splice(@nums, 5, 5, 21..25); 
print "After - @nums\n";
print "\n";
#>>		Before - 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
#>>		After - 1 2 3 4 5 21 22 23 24 25 11 12 13 14 15 16 17 18 19 20

# 	string2array/array2string: split()/join()
my $var_string = "Rain-Drops-On-Roses-And-Whiskers-On-Kittens";
my $var_names = "Larry,David,Roger,Ken,Michael,Tom";
my @string = split('-', $var_string);
@names  = split(',', $var_names);
my $string1 = join( '-', @string );
my $string2 = join( ',', @names );
print "$string[3]\n";  # This will print Roses
print "$names[4]\n";   # This will print Michael
print "$string1\n";
print "$string2\n";
print "\n";
#	{{{
#>>		Roses
#>>		Michael
#>>		Rain-Drops-On-Roses-And-Whiskers-On-Kittens
#>>		Larry,David,Roger,Ken,Michael,Tom
#	}}}

#	Array Sorting:
my @foods = qw(pizza steak chicken burgers);
@foods = sort(@foods);
print "Before: @foods\n";
print "After: @foods\n";
print "\n";
#	{{{
#>>		Before: pizza steak chicken burgers
#>>		After: burgers chicken pizza steak
#	}}}

##	Special variable '$['
#@foods = qw(pizza steak chicken burgers);
#print "Foods: @foods\n";
## 	reset first index of all the arrays.
#$[ = 1;
#print "Food at \@foods[1]: $foods[1]\n";
#print "Food at \@foods[2]: $foods[2]\n";
#$[ = 0;
#print "Food at \@foods[1]: $foods[1]\n";
#print "Food at \@foods[2]: $foods[2]\n";
#print "\n";
##	{{{
##>>		Foods: pizza steak chicken burgers
##>>		Food at @foods[1]: pizza
##>>		Food at @foods[2]: steak
##>>		Food at @foods[1]: steak
##>>		Food at @foods[2]: chicken
##	}}}

#	Merging arrays
my @numbers = (1,3,(4,5,6));
print "numbers = @numbers\n";
my @odd = (1,3,5);
my @even = (2, 4, 6);
@numbers = (@odd, @even);
print "numbers = @numbers\n";
print "\n";
#	{{{
#>>		numbers = 1 3 4 5 6
#>>		numbers = 1 3 5 2 4 6
#	}}}

#	Select Element from List:
$var = (5,4,3,2,1)[4];
print "value of var = $var\n";
my @list = (5,4,3,2,1)[1..3];
print "Value of list = @list\n";
print "\n";
#	{{{
#>>	value of var = 1
#>>	Value of list = 4 3 2
#	}}}
#	}}}

#	Hashes
#	{{{
%data = ('John Paul', 45, 'Lisa', 30, 'Kumar', 40);
print "\$data{'John Paul'} = $data{'John Paul'}\n";
print "\$data{'Lisa'} = $data{'Lisa'}\n";
print "\$data{'Kumar'} = $data{'Kumar'}\n";
print "\n";
#	{{{
#>>		$data{'John Paul'} = 45
#>>		$data{'Lisa'} = 30
#>>		$data{'Kumar'} = 40
#	}}}

#	Creating hashes
%data = ('John Paul' => 45, 'Lisa' => 30, 'Kumar' => 40);
print "$data{'John Paul'}\n";
print "$data{'Lisa'}\n";
print "$data{'Kumar'}\n";
print "\n";
#	{{{
#>>		45
#>>		30
#>>		40
#	}}}

%data = (-JohnPaul => 45, -Lisa => 30, -Kumar => 40);
@array = @data{-JohnPaul, -Lisa};
print "Array : @array\n";
print "\n";
#	{{{
#>>		Array : 45 30
#	}}}

%data = ('John Paul' => 45, 'Lisa' => 30, 'Kumar' => 40);
@names = keys %data;
print "$names[0]\n";
print "$names[1]\n";
print "$names[2]\n";
print "\n";
#	{{{
#>>		John Paul
#>>		Lisa
#>>		Kumar
#	}}}

%data = ('John Paul' => 45, 'Lisa' => 30, 'Kumar' => 40);
@ages = values %data;
print "$ages[0]\n";
print "$ages[1]\n";
print "$ages[2]\n";
print "\n";
#	{{{
#>>		40
#>>		45
#>>		30
#	}}}

%data = ('John Paul' => 45, 'Lisa' => 30, 'Kumar' => 40);
if( exists($data{'Lisa'} ) ) {
   print "Lisa is $data{'Lisa'} years old\n";
} else {
   print "I don't know age of Lisa\n";
}
print "\n";
#	{{{
#>>		Lisa is 30 years old
#	}}}

%data = ('John Paul' => 45, 'Lisa' => 30, 'Kumar' => 40);
my @keys = keys %data;
$size = @keys;
print "1 - Hash size:  is $size\n";
my @values = values %data;
$size = @values;
print "2 - Hash size:  is $size\n";
print "\n";
#	{{{
#>>		1 - Hash size:  is 3
#>>		2 - Hash size:  is 3
#	}}}

#	Add/Remove elements
%data = ('John Paul' => 45, 'Lisa' => 30, 'Kumar' => 40);
@keys = keys %data;
$size = @keys;
print "1 - Hash size:  is $size\n";
# adding an element to the hash;
$data{'Ali'} = 55;
@keys = keys %data;
$size = @keys;
print "2 - Hash size:  is $size\n";
# delete the same element from the hash;
delete $data{'Ali'};
@keys = keys %data;
$size = @keys;
print "3 - Hash size:  is $size\n";
print "\n";
#	{{{
#>>		1 - Hash size:  is 3
#>>		2 - Hash size:  is 4
#>>		3 - Hash size:  is 3
#	}}}
#	}}}

#	Conditional Statements
#	{{{
#	The number 0, the strings '0' and "" , the empty list () , and undef are all false in a boolean context and all other values are true. Negation of a true value by ! or not returns a special false value.
#	Conditional operator '?'
$name = "Ali";
$age = 10;
my $status = ($age > 60 )? "A senior citizen" : "Not a senior citizen";
print "$name is  - $status\n";
print "\n";
#	{{{
#	}}}
#>>		Ali is  - Not a senior citizen

#	If Examples:
my $a = 100;
if( $a < 20 ) {
   printf "a is less than 20\n";
} else { 
   printf "a is greater than 20\n";
}
print "value of a is : $a\n";
$a = "";
if( $a ) {
   printf "a has a true value\n";
} else {
   printf "a has a false value\n";
}
print "value of a is : $a\n";
print "\n";
#	{{{
#>>		a is greater than 20
#>>		value of a is : 100
#>>		a has a false value
#>>		value of a is :
#	}}}

#	if-elsif-else
$a = 100;
# check the boolean condition using if statement
if( $a  ==  20 ) {
   # if condition is true then print the following
   printf "a has a value which is 20\n";
} elsif( $a ==  30 ) {
   # if condition is true then print the following
   printf "a has a value which is 30\n";
} else {
   # if none of the above conditions is true
   printf "a has a value which is $a\n";
}
print "\n";
#	{{{
#>>		a has a value which is 100
#	}}}

$a = 20;
# check the boolean condition using unless statement
unless( $a < 20 ) {
   # if condition is false then print the following
   printf "a is not less than 20\n";
}
print "value of a is : $a\n";
$a = "";
# check the boolean condition using unless statement
unless ( $a ) {
   # if condition is false then print the following
   printf "a has a false value\n";
}
print "value of a is : $a\n";
print "\n";
#	{{{
#>>		a is not less than 20
#>>		value of a is : 20
#>>		a has a false value
#>>		value of a is :
#	}}}

$a = 100;
# check the boolean condition using unless statement
unless( $a == 20 ) {
   # if condition is false then print the following
   printf "given condition is false\n";
} else { 
   # if condition is true then print the following
   printf "given condition is true\n";
}
print "value of a is : $a\n";
$a = "";
# check the boolean condition using unless statement
unless( $a ) {
   # if condition is false then print the following
   printf "a has a false value\n";
} else {
   # if condition is true then print the following
   printf "a has a true value\n";
}
print "value of a is : $a\n";
print "\n";
#	{{{
#>>		given condition is false
#>>		value of a is : 100
#>>		a has a false value
#>>		value of a is :
#	}}}

$a = 20;
# check the boolean condition using if statement
unless( $a  ==  30 ) {
   # if condition is false then print the following
   printf "a has a value which is not 20\n";
} elsif( $a ==  30 ) {
   # if condition is true then print the following
   printf "a has a value which is 30\n";
} else {
   # if none of the above conditions is met
   printf "a has a value which is $a\n";
}
print "\n";
#	{{{
#>>		a has a value which is not 20
#	}}}

#	Switch
#	use Switch;
#	$var = 10;
#	@array = (10, 20, 30);
#	%hash = ('key1' => 10, 'key2' => 20);
#	switch($var) {
#	   case 10           { print "number 100\n" }
#	   case "a"          { print "string a" }
#	   case [1..10,42]   { print "number in list" }
#	   case (\@array)    { print "number in list" }
#	   case (\%hash)     { print "entry in hash" }
#	   else              { print "previous case not true" }
#	}
#	use Switch;
#	$var = 10;
#	@array = (10, 20, 30);
#	%hash = ('key1' => 10, 'key2' => 20);
#	switch($var) {
#	   case 10           { print "number 100\n"; next; }
#	   case "a"          { print "string a" }
#	   case [1..10,42]   { print "number in list" }
#	   case (\@array)    { print "number in list" }
#	   case (\%hash)     { print "entry in hash" }
#	   else              { print "previous case not true" }
#	}
#	Not available on Minerva?

#	}}}

#	#	Loop Statements:
#	#	{{{
#	#	Infinite loop:
#	#>%		for( ; ; ) {
#	#>%		   printf "This loop will run forever.\n";
#	#>%		}
#	
#	#	Loop Examples:
#	#	while
#	$a = 10;
#	while( $a < 20 ) {
#	   printf "Value of a: $a\n";
#	   $a = $a + 1;
#	}
#	print "\n";
#	#	{{{
#	#>>		Value of a: 10
#	#>>		Value of a: 11
#	#>>		Value of a: 12
#	#>>		Value of a: 13
#	#>>		Value of a: 14
#	#>>		Value of a: 15
#	#>>		Value of a: 16
#	#>>		Value of a: 17
#	#>>		Value of a: 18
#	#>>		Value of a: 19
#	#	}}}
#	
#	#	until (negated while)
#	$a = 5;
#	until( $a > 10 ) {
#	   printf "Value of a: $a\n";
#	   $a = $a + 1;
#	}
#	print "\n";
#	#	{{{
#	#>>		Value of a: 5
#	#>>		Value of a: 6
#	#>>		Value of a: 7
#	#>>		Value of a: 8
#	#>>		Value of a: 9
#	#>>		Value of a: 10
#	#	}}}
#	
#	#	for
#	for( $a = 10; $a < 20; $a = $a + 1 ) {
#	   print "value of a: $a\n";
#	}
#	print "\n";
#	#	{{{
#	#>>		value of a: 10
#	#>>		value of a: 11
#	#>>		value of a: 12
#	#>>		value of a: 13
#	#>>		value of a: 14
#	#>>		value of a: 15
#	#>>		value of a: 16
#	#>>		value of a: 17
#	#>>		value of a: 18
#	#>>		value of a: 19
#	#	}}}
#	
#	#	foreach
#	@list = (2, 20, 30, 40, 50);
#	foreach $a (@list) {
#	   print "value of a: $a\n";
#	}
#	print "\n";
#	#	{{{
#	#>>		value of a: 2
#	#>>		value of a: 20
#	#>>		value of a: 30
#	#>>		value of a: 40
#	#>>		value of a: 50
#	#	}}}
#	
#	#	do-while
#	$a = 10;
#	# do...while loop execution
#	do {
#	   printf "Value of a: $a\n";
#	   $a = $a + 1;
#	} while( $a < 20 );
#	print "\n";
#	#	{{{
#	#>>		Value of a: 10
#	#>>		Value of a: 11
#	#>>		Value of a: 12
#	#>>		Value of a: 13
#	#>>		Value of a: 14
#	#>>		Value of a: 15
#	#>>		Value of a: 16
#	#>>		Value of a: 17
#	#>>		Value of a: 18
#	#>>		Value of a: 19
#	#	}}}
#	
#	#	nested while
#	$a = 0;
#	$b = 0;
#	while($a < 3) {
#	   $b = 0;
#	   while( $b < 3 ) {
#	      print "value of a = $a, b = $b\n";
#	      $b = $b + 1;
#	   }
#	   $a = $a + 1;
#	   print "Value of a = $a\n";
#	}
#	print "\n";
#	#	{{{
#	#>>		value of a = 0, b = 0
#	#>>		value of a = 0, b = 1
#	#>>		value of a = 0, b = 2
#	#>>		Value of a = 1
#	#>>		value of a = 1, b = 0
#	#>>		value of a = 1, b = 1
#	#>>		value of a = 1, b = 2
#	#>>		Value of a = 2
#	#>>		value of a = 2, b = 0
#	#>>		value of a = 2, b = 1
#	#>>		value of a = 2, b = 2
#	#>>		Value of a = 3
#	#	}}}
#	
#	#	while, next
#	#	next starts the next itteration of the loop. 
#	$a = 10;
#	while( $a < 20 ) {
#	   if( $a == 15) {
#	      # skip the iteration.
#	      $a = $a + 1;
#	      next;
#	   }
#	   print "value of a: $a\n";
#	   $a = $a + 1;
#	}
#	print "\n";
#	#	{{{
#	#>>		value of a: 10
#	#>>		value of a: 11
#	#>>		value of a: 12
#	#>>		value of a: 13
#	#>>		value of a: 14
#	#>>		value of a: 16
#	#>>		value of a: 17
#	#>>		value of a: 18
#	#>>		value of a: 19
#	#	}}}
#	
#	#	while, next label
#	#	next, with a label, start the next itteration of loop of corrisponding label
#	$a = 0;
#	OUTER: while( $a < 4 ) {
#	   $b = 0;
#	   print "value of a: $a\n";
#	   INNER:while ( $b < 4) {
#	      if( $a == 2) {
#	         $a = $a + 1;
#	         # jump to outer loop
#	         next OUTER;
#	      }
#	      $b = $b + 1;
#	      print "Value of b : $b\n";
#	   }
#	   $a = $a + 1;
#	}
#	print "\n";
#	#	{{{
#	#>>		value of a: 0
#	#>>		Value of b : 1
#	#>>		Value of b : 2
#	#>>		Value of b : 3
#	#>>		Value of b : 4
#	#>>		value of a: 1
#	#>>		Value of b : 1
#	#>>		Value of b : 2
#	#>>		Value of b : 3
#	#>>		Value of b : 4
#	#>>		value of a: 2
#	#>>		value of a: 3
#	#>>		Value of b : 1
#	#>>		Value of b : 2
#	#>>		Value of b : 3
#	#>>		Value of b : 4
#	#	}}}
#	
#	#	while, last
#	#	last, (break), start after the loop
#	$a = 10;
#	while( $a < 20 ) {
#	   if( $a == 15) {
#	      # terminate the loop.
#	      $a = $a + 1;
#	      last;
#	   }
#	   print "value of a: $a\n";
#	   $a = $a + 1;
#	}
#	print "\n";
#	#	{{{
#	#>>		value of a: 10
#	#>>		value of a: 11
#	#>>		value of a: 12
#	#>>		value of a: 13
#	#>>		value of a: 14
#	#	}}}
#	
#	#	while, last label
#	#	last, with a label, start at after the specified loop
#	$a = 0;
#	OUTER: while( $a < 4 ) {
#	   $b = 0;
#	   print "value of a: $a\n";
#	   INNER:while ( $b < 4) {
#	      if( $a == 2) {
#	         # terminate outer loop
#	         last OUTER;
#	      }
#	      $b = $b + 1;
#	      print "Value of b : $b\n";
#	   }
#	   $a = $a + 1;
#	}
#	print "\n";
#	#	{{{
#	#>>		value of a: 0
#	#>>		Value of b : 1
#	#>>		Value of b : 2
#	#>>		Value of b : 3
#	#>>		Value of b : 4
#	#>>		value of a: 1
#	#>>		Value of b : 1
#	#>>		Value of b : 2
#	#>>		Value of b : 3
#	#>>		Value of b : 4
#	#>>		value of a: 2
#	#	}}}
#	
#	#	continue
#	#	used with while, foreach loops, executed just before conditional is to be evaluated again
#	$a = 0;
#	while($a < 3) {
#	   print "Value of a = $a\n";
#	} continue {
#	   $a = $a + 1;
#	}
#	@list = (1, 2, 3, 4, 5);
#	foreach $a (@list) {
#	   print "Value of a = $a\n";
#	} continue {
#	   last if $a == 4;
#	}
#	print "\n";
#	#	{{{
#	#>>		Value of a = 0
#	#>>		Value of a = 1
#	#>>		Value of a = 2
#	#>>		Value of a = 1
#	#>>		Value of a = 2
#	#>>		Value of a = 3
#	#>>		Value of a = 4
#	#>>		#	}}}
#	
#	#	redo
#	#	restart loop wihtout evaluating conditional
#	#	redo either current loop, or loop corresponding to label
#	$a = 0;
#	while($a < 10) {
#	   if( $a == 5 ) {
#	      $a = $a + 1;
#	      redo;
#	   }
#	   print "Value of a = $a\n";
#	} continue {
#	   $a = $a + 1;
#	}
#	print "\n";
#	#	{{{
#	#>>		Value of a = 0
#	#>>		Value of a = 1
#	#>>		Value of a = 2
#	#>>		Value of a = 3
#	#>>		Value of a = 4
#	#>>		Value of a = 6
#	#>>		Value of a = 7
#	#>>		Value of a = 8
#	#>>		Value of a = 9
#	#	}}}
#	
#	#	goto
#	#	{{{
#	#	goto LABEL
#	#		The goto LABEL form jumps to the statement labeled with LABEL and resumes execution from there.
#	#	goto EXPR
#	#		The goto EXPR form is just a generalization of goto LABEL. It expects the expression to return a label name and then jumps to that labeled statement.
#	#	goto &NAME
#	#		It substitutes a call to the named subroutine for the currently running subroutine.#
#	#	}}}
#	$a = 10;
#	LOOP:do {
#	   if( $a == 15) {
#	      # skip the iteration.
#	      $a = $a + 1;
#	      # use goto LABEL form
#	      goto LOOP;
#	   }
#	   print "Value of a = $a\n";
#	   $a = $a + 1;
#	} while( $a < 20 );
#	print "\n";
#	#	{{{
#	#>>		Value of a = 10
#	#>>		Value of a = 11
#	#>>		Value of a = 12
#	#>>		Value of a = 13
#	#>>		Value of a = 14
#	#>>		Value of a = 16
#	#>>		Value of a = 17
#	#>>		Value of a = 18
#	#>>		Value of a = 19
#	#	}}}
#	
#	#	Example, produces infinite loop when run? 
#	#	{{{
#	#>%	$a = 10;
#	#>%	$str1 = "LO";
#	#>%	$str2 = "OP";
#	#>%	LOOP:do {
#	#>%	   if( $a == 15) {
#	#>%	      # skip the iteration.
#	#>%	      $a = $a + 1;
#	#>%	      # use goto EXPR form
#	#>%	      goto $str1.$str2;
#	#>%	   }
#	#>%	   print "Value of a = $a\n";
#	#>%	   $a = $a + 1;
#	#>%	} while( $a < 20 );
#	#>%	print "\n";
#	#	}}}
#	
#	#	}}}

#	Operators:
#	{{{
#	Numerical:
#		Arithmetic:
#			+		addition
#			-		subtraction
#			*		multiplication
#			/		division
#			%		modulus
#			**		exponent
#		Equality:
#			==		equal to
#			!=		not equal to
#			<=>		-1, 0, or 1, depending on whether LHS > RHS
#			>		greater than
#			<		less than
#			>=		greater than or equal
#			<=		less than or equal

#	String:
#		Equality:
#			lt		stringwise less than
#			gt		stringwise greater than
#			le		stringwise less than or equal
#			ge		stringwise greater than or equal
#			eq		stringwise equal
#			ne		not equal
#			cmp		-1, 0, or 1, depending on whether LHS > RHS

#	Assignment:
#		=			Simple assignment
#		+=			add and assign
#		-=			subtract and assign
#		*=			multiply and assign
#		/=			divide and assign
#		**=			exponent and assign

#	Bitwise:
#		&			binary and
#		|			binary or
#		^			binary xor
#		~			binary ones-complement
#		<<			left shift
#		>>			right shift

#	Logical
#		and
#		&&
#		or
#		||
#		not

#	Quote-like
#		q{}			enclose string single quotes ''
#		qq{}		enclose string double quotes ""
#		qx{}		enclose string inverted quotes ``

#	Misc Operators
#		.			concatinate strings
#		x			repeat left operand number of times given by right operand 'x' x 3 = ---
#		..			range operator (1..5) = (1, 2, 3, 4, 5)
#		++			increment 
#		--			decrement
#		->			dereferencing variable from object/class

#	Operator Precedence
#		<>

#	}}}

#	Date and Time
#	{{{
my @months = qw( Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec );
@days = qw(Sun Mon Tue Wed Thu Fri Sat Sun);
my ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime();
print "$mday $mon $wday\n";
print "$mday $months[$mon] $days[$wday]\n";
print "\n";
#	{{{
#>>		10 10 2
#>>		10 Nov Tue
#	}}}

my $datestring = localtime();
print "Local date and time $datestring\n";
$datestring = gmtime();
print "GMT date and time $datestring\n";
my $epoc = time();
print "Number of seconds since Jan 1, 1970 - $epoc\n";
($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime();
printf("Time Format - HH:MM:SS\n");
printf("%02d:%02d:%02d\n", $hour, $min, $sec);
print "\n";
#	{{{
#>>		Local date and time Tue Nov 10 11:38:27 2020
#>>		GMT date and time Tue Nov 10 00:39:50 2020
#>>		Number of seconds since Jan 1, 1970 - 1604968754
#>>		Time Format - HH:MM:SS
#>>		11:40:32
#	}}}

#	stfrtime
use POSIX qw(strftime);
$datestring = strftime "%a %b %e %H:%M:%S %Y", localtime;
printf("date and time - $datestring\n");
# or for GMT formatted appropriately for your locale:
$datestring = strftime "%a %b %e %H:%M:%S %Y", gmtime;
printf("date and time - $datestring\n");
print "\n";
#	{{{
#>>		date and time - Tue Nov 10 11:41:40 2020
#>>		date and time - Tue Nov 10 00:41:40 2020
#	}}}

#	strftime specifiers
#	{{{
#		Specifier	Replaced by	Example
#		%a	Abbreviated weekday name *	Thu
#		%A	Full weekday name *	Thursday
#		%b	Abbreviated month name *	Aug
#		%B	Full month name *	August
#		%c	Date and time representation *	Thu Aug 23 14:55:02 2001
#		%C	Year divided by 100 and truncated to integer (00-99)	20
#		%d	Day of the month, zero-padded (01-31)	23
#		%D	Short MM/DD/YY date, equivalent to %m/%d/%y	08/23/01
#		%e	Day of the month, space-padded ( 1-31)	23
#		%F	Short YYYY-MM-DD date, equivalent to %Y-%m-%d	2001-08-23
#		%g	Week-based year, last two digits (00-99)	01
#		%G	Week-based year	2001
#		%h	Abbreviated month name * (same as %b)	Aug
#		%H	Hour in 24h format (00-23)	14
#		%I	Hour in 12h format (01-12)	02
#		%j	Day of the year (001-366)	235
#		%m	Month as a decimal number (01-12)	08
#		%M	Minute (00-59)	55
#		%n	New-line character ('\n')	
#		%p	AM or PM designation	PM
#		%r	12-hour clock time *	02:55:02 pm
#		%R	24-hour HH:MM time, equivalent to %H:%M	14:55
#		%S	Second (00-61)	02
#		%t	Horizontal-tab character ('\t')	
#		%T	ISO 8601 time format (HH:MM:SS), equivalent to %H:%M:%S	14:55
#		%u	ISO 8601 weekday as number with Monday as 1 (1-7)	4
#		%U	Week number with the first Sunday as the first day of week one (00-53)	33
#		%V	ISO 8601 week number (00-53)	34
#		%w	Weekday as a decimal number with Sunday as 0 (0-6)	4
#		%W	Week number with the first Monday as the first day of week one (00-53)	34
#		%x	Date representation *	08/23/01
#		%X	Time representation *	14:55:02
#		%y	Year, last two digits (00-99)	01
#		%Y	Year	2001
#		%z	ISO 8601 offset from UTC in timezone (1 minute = 1, 1 hour = 100). If timezone cannot be termined, no characters. +100
#		%Z	Timezone name or abbreviation. If timezone cannot be termined, no characters. CDT
#		%%	A % sign	%
#	}}}
#	}}}

#	Subroutines:
#	{{{
# 	Function call
sub Hello {
   print "Hello, World!\n";
}
Hello();
print "\n";
#	{{{
#>>		Hello, World!
#	}}}

#	Muliple Scalar Arguments '@_'
#		Elements of @_ (length n) = $_[0], $_[1], ..., $_[n-1]
sub Average {
   my $n = scalar(@_);
   my $sum = 0;
   foreach my $item (@_) {
      $sum += $item;
   }
   my $average = $sum / $n;
   print "Average for the given numbers : $average\n";
}
Average(10, 20, 30);
print "\n";
#	{{{
#>>		Average for the given numbers : 20
#	}}}

#	Passing list to function - list is given as last argument, allowing 
sub PrintList {
   my $n = scalar(@_);
   #my $val = @_[0];
   my $val = $_[0];
   my @list = @_[1..$n];
   print "Given val is $val, list is @list\n";
}
$a = 10;
my @var = (1, 2, 3, 4);
PrintList($a, @var);
print "\n";
#	{{{
#>>		Given val is 10, list is 1 2 3 4
#	}}}

#	Passing hash to function
sub PrintHash {
   my (%hash) = @_;
   foreach my $key ( keys %hash ) {
      my $value = $hash{$key};
      print "$key : $value\n";
   }
}
my %hash = ('name' => 'Tom', 'age' => 19);
PrintHash(%hash);
print "\n";
#	{{{
#>>		name : Tom
#>>		age : 19
#	}}}

#	Return Scalar
sub FuncAverage {
   my $n = scalar(@_);
   my $sum = 0;
   foreach my $item (@_) {
      $sum += $item;
   }
   my $average = $sum / $n;
   return $average;
}
$num = FuncAverage(10, 20, 30);
print "Average for the given numbers : $num\n";
print "\n";
#	{{{
#>>		Average for the given numbers : 20
#	}}}

#	Private variables 'my'
#	called lexical variables, keyword 'my' makes variable local to a code block, (i.e: function, if, while, for, foreach, eval)
my $arg_str = "Hello, World!";
sub PrintHelloA {
   my $arg_str;
   $arg_str = "Hello, Perl!";
   print "Inside the function $arg_str\n";
}
PrintHelloA();
print "Outside the function $arg_str\n";
print "\n";
#	{{{
#>>		Inside the function Hello, Perl!
#>>		Outside the function Hello, World!
#	}}}

#	Temporary variables:
#	keyword 'local' is used to assign a different value to a variable within a given scope 
sub PrintHello {
   my $arg_str;
   $arg_str = "Hello, Perl!";
   PrintMe();
   print "Inside the function PrintHello $arg_str\n";
}
sub PrintMe {
   print "Inside the function PrintMe $arg_str\n";
}
PrintHello();
print "Outside the function $arg_str\n";
print "\n";
#	{{{
#>>		Inside the function PrintMe Hello, Perl!
#>>		Inside the function PrintHello Hello, Perl!
#>>		Outside the function Hello, World!
#	}}}

#	State variables:
#	keyword 'state', private variables which are not re-initalised (they retain their value) on subsiquent calls to subroutine (akin to static variables?)
use feature 'state';
sub PrintCount {
   state $count = 0; # initial value
   print "Value of counter is $count\n";
   $count++;
}
for (1..5) {
   PrintCount();
}
print "\n";
#	{{{
#>>		Value of counter is 0
#>>		Value of counter is 1
#>>		Value of counter is 2
#>>		Value of counter is 3
#>>		Value of counter is 4
#	}}}

#	Subroutine call context
#	Example, 'localtime()' returns wither a string, or a list, depending on the 'context' in which it is called:
$datestring = localtime( time );
($sec,$min,$hour,$mday,$mon, $year,$wday,$yday,$isdst) = localtime(time);
print "$datestring\n";
print "$sec,$min,$hour,$mday,$mon, $year,$wday,$yday,$isdst\n";
print "\n";
#	{{{
#>>		Tue Nov 10 13:15:18 2020
#>>		18,15,13,10,10, 120,2,314,1
#	}}}

#	}}}

#	References
#	{{{
#	References are scalars which store the location of another variable, subroutine, or value:
#	Denoted by prefixing the item, with a backslash:
my $scalarref = \$foo;
my $arrayref  = \@ARGV;
my $hashref   = \%ENV;
my $coderef   = \&handler;
my $globref   = \*foo;

#	Anonymous list reference:
$arrayref = [1, 2, ['a', 'b', 'c']];

#	Anonymous hash reference:
$hashref = {
   'Adam'  => 'Eve',
   'Clyde' => 'Bonnie',
};

#	Anonymous subroutine reference:
$coderef = sub { print "Boink!\n" };

#	Dereferencing:
$var = 10;
# Now $r has reference to $var scalar.
my $r = \$var;
# Print value available at the location stored in $r.
print "Value of $var is : ", $$r, "\n";
@var = (1, 2, 3);
# Now $r has reference to @var array.
$r = \@var;
# Print values available at the location stored in $r.
print "Value of @var is : ",  @$r, "\n";
my %var = ('key1' => 10, 'key2' => 20);
# Now $r has reference to %var hash.
$r = \%var;
# Print values available at the location stored in $r.
print "Value of %var is : ", %$r, "\n";
print "\n";
#	{{{
#>>		Value of 10 is : 10
#>>		Value of 1 2 3 is : 123
#>>		Value of %var is : key110key220
#	}}}

#	Using 'ref' to determine type
$var = 10;
$r = \$var;
print "Reference type in r : ", ref($r), "\n";
@var = (1, 2, 3);
$r = \@var;
print "Reference type in r : ", ref($r), "\n";
%var = ('key1' => 10, 'key2' => 20);
$r = \%var;
print "Reference type in r : ", ref($r), "\n";#
print "\n";
#	{{{
#>>		Reference type in r : SCALAR
#>>		Reference type in r : ARRAY
#>>		Reference type in r : HASH
#	}}}

#	Circular references: references which point to each other
$foo = 100;
$foo = \$foo;
print "Value of foo is : ", $$foo, "\n";#
print "\n";
#	{{{
#>>		Value of foo is : REF(0x7fc797960638)
#	}}}

#	References to functions:
# Function definition
sub PrintHashB {
   my (%hash) = @_;
   foreach my $item (%hash) {
      print "Item : $item\n";
   }
}
%hash = ('name' => 'Tom', 'age' => 19);
# Create a reference to above function.
my $cref = \&PrintHashB;
# Function call using reference.
&$cref(%hash);#
print "\n";
#	{{{
#>>		Item : name
#>>		Item : Tom
#>>		Item : age
#>>		Item : 19
#	}}}
#	}}}

#	Formats
#	{{{
#	A 'format' defines an output 'report' in perl
#	fieldholders
#	{{{
#		@<<<< left-justified (space 5)
#		@>>>> right-justified
#		@|||| centered
#		@####.## numeric field holder
#		@* multiline field holder
#	}}}

#	set the number of lines per page using special variable $= ( or $FORMAT_LINES_PER_PAGE ). Default=60

format EMPLOYEE =
===================================
@<<<<<<<<<<<<<<<<<<<<<< @<< 
$name, $age
@#####.##
$salary
===================================
.

format EMPLOYEE_TOP =
===================================
Name                    Age
===================================
.

#	TODO: 2020-11-10T19:38:37AEDT How footer works, and what (see below) this means
#	{{{
#	LINK: https://www.tutorialspoint.com/perl/perl_formats.htm
#	While $^ or $FORMAT_TOP_NAME contains the name of the current header format, there is no corresponding mechanism to automatically do the same thing for a footer. If you have a fixed-size footer, you can get footers by checking variable $- or $FORMAT_LINES_LEFT before each write() and print the footer yourself if necessary using another format defined as follows - 
#	}}}
#>%		format EMPLOYEE_BOTTOM =
#>%		End of Page @<
#>%		            $%
#>%		.

select(STDOUT);
$~ = "EMPLOYEE";
$^ = "EMPLOYEE_TOP";

my @var_n = ("Ali", "Raza", "Jaffer");
my @var_a  = (20,30, 40);
my @var_s = (2000.00, 2500.00, 4000.000);

my $i = 0;
foreach (@var_n) {
   $name = $_;
   $age = $var_a[$i];
   $salary = $var_s[$i++];
   write;
}

#	}}}

#	Env:
#	{{{
#	LINK: https://alvinalexander.com/perl/edu/articles/pl020002/

#	username, path, pwd
my $userName =  $ENV{'LOGNAME'}; 
my $path = $ENV{'PATH'}; 
my $pwd  = $ENV{'PWD'};
print "userName=($userName)\n"; 
print "path=($path)\n";
print "pwd=($pwd)\n";
print "\n";
#	{{{
#>>		userName=(mldavis)
#>>		path=(/usr/local/MacGPG2/bin:/usr/local/opt/make/libexec/gnubin:/usr/local/opt/grep/libexec/gnubin:/usr/local/opt/gnu-which/libexec/gnubin:/usr/local/opt/gnu-tar/libexec/gnubin:/usr/local/opt/gnu-sed/libexec/gnubin:/usr/local/opt/gnu-indent/libexec/gnubin:/usr/local/opt/gawk/libexec/gnubin:/usr/local/opt/findutils/libexec/gnubin:/usr/local/opt/ed/libexec/gnubin:/usr/local/opt/coreutils/libexec/gnubin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/Applications/VMware Fusion.app/Contents/Public:/opt/X11/bin:/Library/Apple/usr/bin:/Users/mldavis/.pyenv/shims:/Users/mldavis/bin:/usr/local/opt/fzf/bin)
#>>		pwd=(/Users/mldavis)
#
#	}}}

#	#	print variable names and values for each env variable
#	foreach (sort keys %ENV) { 
#	  print "$_  =  $ENV{$_}\n"; 
#	}
#	print "\n";

#	}}}

#	File I/O
#	{{{
#	{{{
#	The basics of handling files are simple: you associate a filehandle with an external entity (usually a file) and then use a variety of operators and functions within Perl to read and update the data stored within the data stream associated with the filehandle.
#	A filehandle is a named internal Perl structure that associates a physical file with a name. All filehandles are capable of read/write access, so you can read from and update any file or device associated with a filehandle. However, when you associate a filehandle, you can specify the mode in which the filehandle is opened.
#	Three basic file handles are - STDIN, STDOUT, and STDERR, which represent standard input, standard output and standard error devices respectively.
#	}}}

#	Open file methods:
#	Read only:
#			< or r
#	Create, write, and truncate
#			> or w
#	Write, append, create
#			>> or a
#	Read, write, create, and truncates
#			+>> or a+

my $path_data = $ENV{'mld_data'};
my $path_nums = "$path_data/nums.txt";

#	Read file line-by-line
#	'<' denotes readonly
open (DATA, "<$path_nums") or die "Failed to open path_nums=($path_nums)";
while (<DATA>) {
	print "$_";
}
close (DATA) || die "failed to close file";
print "\n";
#	{{{
#>>		10
#>>		15
#>>		6
#>>		33
#>>		45
#	}}}

#	use the <FILEHANDLE> operator in a list context, it returns a list of lines from the specified filehandle.
my $path_larry="$path_data/larry.txt";
open(FP, "<$path_larry") or die "Failed to open path_larry=($path_larry), $!";
my @larry_lines = <FP>;
close (FP);

#	Write lines read eariler to file
my $path_output = "/tmp/cmcat_perl_example.temp";
open(FP, ">$path_output") or die "Couldn't open path_output=($path_output), $!";
foreach ( @larry_lines ) {
	print FP "$_";
}
close (FP);

#	Sysopen
#	uses the system open() function, using the parameters supplied to it as the parameters 
#>%		sysopen(DATA, "file.txt", O_RDWR|O_TRUNC );
#	{{{
#	Read and Write
#		O_RDWR
#	Read only
#		O_RDONLY
#	Write only
#		O_WRONLY
#	Create file
#		O_CREAT
#	Append file
#		O_APPEND
#	Truncate file
#		O_Truncate
#	Stop if file exists
#		O_EXCL
#	non-blocking usability
#		O_NONBLOCK
#	}}}

#	Check whether session is interactive, and read stdin (as a filehandle), in scalar context, returns a single line from filehandle.
#	In a shell session, this allows user to enter value, in vim system() environemnt used in :Exe, we get a '$name is empty' warning
if (-t STDIN && -t STDOUT) {
	print "What is your name?\n";
	my $name = <STDIN>;
	print "Hello $name\n";
}
else {
	print "Non-interactive, skip input\n";
}

#	Return a single chraracter from a given handle
#			getc FILEHANDLE
#	Reaad a block of information from buffered filehandle - binary file IO
#			read FILEHANDLE, SCALAR, LENGTH, [OFFSET]
#	The length of the data read is defined by LENGTH, and the data is placed at the start of SCALAR if no OFFSET is specified. Otherwise data is placed after OFFSET bytes in SCALAR. The function returns the number of bytes read on success, zero at end of file, or undef if there was an error.

#	Writing to a file handle is handled by 'print'
#>%			print FILEHANDLE LIST
#	Print resolved value of 'LIST' to 'FILEHANDLE' (stdout by default)


#	Copy file:
#>%		# 	Open file to read
#>%		open(DATA1, "<file1.txt");
#>%		# 	Open new file to write
#>%		open(DATA2, ">file2.txt");
#>%		# 	Copy data from one file to another.
#>%		while(<DATA1>) {
#>%		   print DATA2 $_;
#>%		}
#>%		close( DATA1 );
#>%		close( DATA2 );

#	Rename file
#>%		rename ("/usr/test/file1.txt", "/usr/test/file2.txt" );

#	Delete file
#>%		unlink ("/usr/test/file1.txt");

#	Positioning in file:
#	Find position:
#>%			tell FILEHANDLE
#	Update file pointer 
#>%			seek FILEHANDLE, POSITION, WHENCE

#	set pointer to 256th byte
#>%		seek FILEHANDLE, 256, 0;


#	File information
#>%		my $file = "/usr/test/file1.txt";
#>%		my (@description, $size);
#>%		if (-e $file) {
#>%		   push @description, 'binary' if (-B _);
#>%		   push @description, 'a socket' if (-S _);
#>%		   push @description, 'a text file' if (-T _);
#>%		   push @description, 'a block special file' if (-b _);
#>%		   push @description, 'a character special file' if (-c _);
#>%		   push @description, 'a directory' if (-d _);
#>%		   push @description, 'executable' if (-x _);
#>%		   push @description, (($size = -s _)) ? "$size bytes" : 'empty';
#>%		   print "$file is ", join(', ',@description),"\n";
#>%		}
#	{{{
#		-A
#		Script start time minus file last access time, in days.
#		-B
#		Is it a binary file?
#		-C
#		Script start time minus file last inode change time, in days.
#		-M
#		Script start time minus file modification time, in days.
#		-O
#		Is the file owned by the real user ID?
#		-R
#		Is the file readable by the real user ID or real group?
#		-S
#		Is the file a socket?
#		-T
#		Is it a text file?
#		-W
#		Is the file writable by the real user ID or real group?
#		-X
#		Is the file executable by the real user ID or real group?
#		-b
#		Is it a block special file?
#		-c
#		Is it a character special file?
#		-d
#		Is the file a directory?
#		-e
#		Does the file exist?
#		-f
#		Is it a plain file?
#		-g
#		Does the file have the setgid bit set?
#		-k
#		Does the file have the sticky bit set?
#		-l
#		Is the file a symbolic link?
#		-o
#		Is the file owned by the effective user ID?
#		-p
#		Is the file a named pipe?
#		-r
#		Is the file readable by the effective user or group ID?
#		-s
#		Returns the size of the file, zero size = empty file.
#		-t
#		Is the filehandle opened by a TTY (terminal)?
#		-u
#		Does the file have the setuid bit set?
#		-w
#		Is the file writable by the effective user or group ID?
#		-x
#		Is the file executable by the effective user or group ID?
#		-z
#		Is the file size zero?
#	}}}

#	}}}

#	Directory Operations:
#	{{{
#	Directory functions:
#>%		opendir DIRHANDLE, EXPR  # To open a directory
#>%		readdir DIRHANDLE        # To read a directory
#>%		rewinddir DIRHANDLE      # Positioning pointer to the begining
#>%		telldir DIRHANDLE        # Returns current position of the dir
#>%		seekdir DIRHANDLE, POS   # Pointing pointer to POS inside dir
#>%		closedir DIRHANDLE       # Closing a directory.#

# 	Display all non-hidden items in /tmp 
my $path_tmp = "/tmp";
my @files = glob( "$path_tmp/*" );
foreach (@files ) {
   print $_ . "\n";
}
print "\n";
#	{{{
#>>		/tmp/_VimH_Reader_UniquePaths
#>>		/tmp/cmcat_perl_example.temp
#>>		/tmp/com.apple.launchd.6YZx009p24
#>>		/tmp/com.apple.launchd.L7lBwMhLlS
#>>		/tmp/com.google.Keystone
#>>		/tmp/devio_semaphore_devio_0xb017
#>>		/tmp/devio_semaphore_devio_0xc539
#>>		/tmp/devio_semaphore_USB_Receiver@02424000
#>>		/tmp/mld_deltas.log
#>>		/tmp/Mldvp_CallerFuncName.stderr
#>>		/tmp/powerlog
#>>		/tmp/Pulse.build.1604982235
#>>		/tmp/stderr-log
#>>		/tmp/tmux-501
#	}}}

# 	Display all hidden items in /tmp
$path_tmp = "/tmp";
@files = glob( "$path_tmp/.*" );
foreach (@files ) {
   print $_ . "\n";
}
print "\n";
#	{{{
#>>		/tmp/.
#>>		/tmp/..
#>>		/tmp/.debug.mldvp.log
#>>		/tmp/.fast_var2path
#>>		/tmp/.test-hidden
#	}}}


#	Display all (non-hidden) file / directories in /tmp 
use File::Basename; 
my @tmp_list_files= ();
my @tmp_list_dirs= ();
foreach my $loop_item ( glob( "$path_tmp/*" ) ) {
	if (-f "$loop_item") {
		push(@tmp_list_files, basename($loop_item));
	}
	if (-d "$loop_item") {
		push(@tmp_list_dirs, basename($loop_item));
	}
}
print "tmp_list_files=(@tmp_list_files)\n";
print "tmp_list_dirs=(@tmp_list_dirs)\n";
print "\n";
#	{{{
#>>		tmp_list_files=(cmcat_perl_example.temp mld_deltas.log Mldvp_CallerFuncName.stderr)
#>>		tmp_list_dirs=(_VimH_Reader_UniquePaths com.apple.launchd.6YZx009p24 com.apple.launchd.L7lBwMhLlS com.google.Keystone devio_semaphore_devio_0xb017 devio_semaphore_devio_0xc539 devio_semaphore_USB_Receiver@02424000 powerlog Pulse.build.1604982235 stderr-log tmux-501)
#	}}}

#	Display all file / directories in /tmp 
use File::Basename; 
@tmp_list_files= ();
@tmp_list_dirs= ();
foreach my $loop_item ( glob( "$path_tmp/{.,}*" ) ) {
   if($loop_item eq "." || $loop_item eq ".."){ next;}
	if (-f "$loop_item") {
		push(@tmp_list_files, basename($loop_item));
	}
	if (-d "$loop_item") {
		push(@tmp_list_dirs, basename($loop_item));
	}
}
print "tmp_list_files=(@tmp_list_files)\n";
print "tmp_list_dirs=(@tmp_list_dirs)\n";
print "\n";
#	{{{
#>>		tmp_list_files=(.debug.mldvp.log cmcat_perl_example.temp mld_deltas.log Mldvp_CallerFuncName.stderr)
#>>		tmp_list_dirs=(. .. .fast_var2path .test-hidden _VimH_Reader_UniquePaths com.apple.launchd.6YZx009p24 com.apple.launchd.L7lBwMhLlS com.google.Keystone devio_semaphore_devio_0xb017 devio_semaphore_devio_0xc539 devio_semaphore_USB_Receiver@02424000 powerlog Pulse.build.1604982235 stderr-log tmux-501)
#	}}}

#	Display all file / directories in /tmp
@tmp_list_files= ();
@tmp_list_dirs= ();
opendir (DIR, "$path_tmp") or die "Couldn't open directory, $!";
while (my $loop_item = readdir DIR) {
   #print "$loop_item\n";
   if($loop_item eq "." || $loop_item eq ".."){ next;}
	if (-f "$path_tmp/$loop_item") {
		push(@tmp_list_files, $loop_item);
	}
	if (-d "$path_tmp/$loop_item") {
		push(@tmp_list_dirs, $loop_item);
	}
}
closedir DIR;
print "tmp_list_files=(@tmp_list_files)\n";
print "tmp_list_dirs=(@tmp_list_dirs)\n";
print "\n";
#	{{{
#>>		tmp_list_files=(mld_deltas.log Mldvp_CallerFuncName.stderr .debug.mldvp.log cmcat_perl_example.temp)
#>>		tmp_list_dirs=(com.apple.launchd.L7lBwMhLlS devio_semaphore_devio_0xb017 com.google.Keystone devio_semaphore_devio_0xc539 powerlog com.apple.launchd.6YZx009p24 .fast_var2path devio_semaphore_USB_Receiver@02424000 Pulse.build.1604982235 _VimH_Reader_UniquePaths stderr-log tmux-501 .test-hidden)
#	}}}


#	Create directory
my $tmp_new_dir = "/tmp/cmcat-perl-testdir";
mkdir ($tmp_new_dir) or die "failed to create tmp_new_dir=($tmp_new_dir)";

#	Remove directory
rmdir ($tmp_new_dir) or die "failed to remote tmp_new_dir=($tmp_new_dir)";

#	Change directory (within perl only?)
chdir ($path_tmp) or die "failed to chdir path_tmp=($path_tmp)";

#	}}}

#	Error handling
#	{{{
my $path_tmp = "/tmp";

#	warn function
chdir ($path_tmp) or warn "failed chdir path_tmp=($path_tmp)";
#	die function
chdir ($path_tmp) or die "failed chdir path_tmp=($path_tmp)";

#	Errors within module
package T;

require Exporter;
my @ISA = qw/Exporter/;
my @EXPORT = qw/function/;
use Carp;
use Carp qw(cluck);

sub functionexample {
	#	Produces warning message describing line in module
   warn "Warning in module!";

	#	carp produces warning message describing line in module, and the line making the call to module which produced warning (up 1 level)
   carp "Warning in module!";

   #	cluck is similar to carp, but produces a full stack trace of modules leading to call which produced warning
   cluck "Warning in module!";

   #	croak, as per carp, but with an error instead of a warning
   #>%		croak "Error in module!";
   
   #	confess, asp per cluck, but with an error instead of a warning
   #>%		confess "Error in module!";
}
1;
functionexample();

#	}}}

#	Special Variables:
#	{{{
#	Default input and pattern-searching string:
#			$_
foreach ('hickory','dickory','doc') {
   print $_;
   print "\n";
}
print "\n";
#	{{{
#>>		hickory
#>>		dickory
#>>		doc
#	}}}

#	special variable '$_' can also be used implicitly
foreach ('hickory','dickory','doc') {
   print;
   print "\n";
}
print "\n";
#	{{{
#>>		hickory
#>>		dickory
#>>		doc
#	}}}

#	'$_' is used implicitly by:
#		various unary functions, such as ord, int, and all file test except '-t'
#		various list functions, such as print() and unlink()
#		pattern matching operations, m//, s//, tr// (when used without =~ operator)
#		implicit iterator variable in grep and map
#		<The default place to put an input record when a line-input operation's result is tested by itself as the sole criterion of a while test (i.e., ). Note that outside of a while test, this will not happen.>

#	Special variable types
#		global scalars
#		global arrays
#		global hashes
#		global filehandlers
#		global constants
#		regex
#		filehandles

#	Global scalar special vars:
#		$_		$ARG		Default input / pattern-searching space
#		$.		$NR			Current input linenum of last filehandle. Reset on close
#		$/		$RS			Input record seperator. if null, treat blank line as delim. default=(newline).
#		$,		$OFS				Output field seperator
#		$\		$ORS				Output record seperator
#		$"		$LIST_SEPERATOR		Like '$,' for list values interpolated into interpreted string. Default=(space)
#		$;		$SUBSCRIPT_SEPERATOR	Seperator for multidimensional array emulation. Default=(\034) 
#		$^L		$FORMAT_FORMFEED		Default=(\f)
#		$:		$FORMAT_LINE_BREAK_CHARACTERS		 characters after which a string may be broken to fill continuation fields (beginning with '^'). Default=(\n)
#		$^A		$ACCUMULATOR		Accumulator for format lines
#		$#		$OFMT				(deprecated) output format for printed numbers
#		$?		$CHILD_ERROR		Status returned by last pipe close, backtick command, or system operator
#		$!		$OS_ERROR / $ERRNO	Numeric context: value of last system call error. String context: corrisponding system error string
#		$@		$EVAL_ERROR			error message from last eval command
#		$$		$PROCESS_ID / $PID	pid of perl script execution
#		$<		$REAL_USER_ID / $UID	real user id (uid) of this process
#		$>		$EFFECTIVE_USER_ID / $EUID		effective user id of this process
#		$(		$REAL_GROUP_ID / $GID	real group id (gid) of this process
#		$)		$EFFECTIVE_GROUP_ID / $EGID		effective group id (gid) of this process
#		$0		$PROGRAM_NAME		name of file of perl script
#		$[							index of first array element
#		$]		$PERL_VERSION		patchlevel / 1000
#		$^D		$DEBUGGING			debugging flags
#		$^E		$EXTENDED_OS_ERROR	extended error messages (platform specific?)
#		$^F		$SYSTEM_FD_MAX		maximum system file descriptor (usually 2)
#		$^H							internal compiler hints
#		$^I		$INPLACE_EDIT		value of inplace-edit extension
#		$^M							emergency memory pool (installation specific)
#		$^O		$OSNAME				OS 
#		$^P		$PERLDB				internal debugger flag
#		$^T		$BASETIME			epoch of script start
#		$^W		$WARNING			(value of) warning switch
#		$^X		$EXECUTABLE_NAME	path of perl binary
#		$ARGV						name of file (when reading <ARGV>

#	Global array special vars:
#		@ARGV	command line arguments of script
#		@INC	places evaluated for 'do', 'require', or 'use'
#		@F		array containing input lines from '-a' option


#	Global hash special vars:
#		%INC	hash containing filename of includes from 'do' and 'require'
#		%ENV	hash containing shell environment
#		%SIG	hash used to set signal handler

#	Global filehandles:
#		ARGV		iterates over cli filenames in @ARGV, usually written <>
#		STDERR		standard error
#		STDIN		standard input
#		STDOUT		standard output
#		DATA		anything following __END__ in file of script, or, in a file from an included package
#		_			last stat, lstat, or file test

#	Global constants:
#		__END__		logical end of program
#		__FILE__	filename at location of usage
#		__LINE__	current line number
#		__PACKAGE__		package name at compile time

#	regex:
#		$digit				corresponds to last <digit> pattern matched - $1 is first capture group, ect.
#		$&		$MATCH		string of last successful pattern match
#		$`		$PREMATCH	string preceding last successful pattern match
#		$'		$POSTMATCH	string following last successful pattern match
#		$+		$LAST_PAREN_MATCH	last bracket matched by last search pattern

#	filehandles:	
#		$|		$OUTPUT_AUTOFLUSH		if set to nonzero, force fflush(3) after very write or print on current output channel
#		$%		$FORMAT_PAGE_NUMBER		page number of the current output channel
#		#=		$FORMAT_LINES_PER_PAGE	page length of current output channel. Default=(60)
#		$-		$FORMAT_LINES_LEFT		number of lines remaining for current output channel
#		$~		$FORMAT_NAME			name of the current output channel. 
#		$^		$FORMAT_TOP_NAME		top-of-page format for current output channel. Default=(<filehandle>_TOP)

#	}}}

#	Perl Standard:
#	{{{
#	The closing curly bracket of a multi-line BLOCK should line up with the keyword that started the construct

#	Other best-practice recomentations: 
#		4-column indent.
#		Opening curly on same line as keyword, if possible, otherwise line up.
#		Space before the opening curly of a multi-line BLOCK.
#		One-line BLOCK may be put on one line, including curlies.
#		No space before the semicolon.
#		Semicolon omitted in "short" one-line BLOCK.
#		Space around most operators.
#		Space around a "complex" subscript (inside brackets).
#		Blank lines between chunks that do different things.
#		Uncuddled elses.
#		No space between function name and its opening parenthesis.
#		Space after each comma.
#		Long lines broken after an operator (except and and or).
#		Space after last parenthesis matching on current line.
#		Line up corresponding items vertically.
#		Omit redundant punctuation as long as clarity doesn't suffer.

#	Equivelent statements, the first is considered the more legiable
#>%		open(FOO,$foo) || die "Can't open $foo: $!";
#>%		die "Can't open $foo: $!" unless open(FOO,$foo);

#	Equivelent, Again, consider the first better than the second:
#>%		print "Starting analysis\n" if $verbose;
#>%		$verbose && print "Starting analysis\n";

#	Don't be afraid to use loop labels--they're there to enhance readability as well as to allow multilevel loop breaks. See the previous example.
#
#	Avoid using grep() (or map()) or `backticks` in a void context, that is, when you just throw away their return values. Those functions all have return values, so use them. Otherwise use a foreach() loop or the system() function instead.

#	For portability, when using features that may not be implemented on every machine, test the construct in an eval to see if it fails. If you know what version or patchlevel a particular feature was implemented, you can test $] ($PERL_VERSION in English) to see if it will be there. The Config module will also let you interrogate values determined by the Configure program when Perl was installed.

#	Choose mnemonic identifiers. If you can't remember what mnemonic means, you've got a problem.

#	While short identifiers like $gotit are probably ok, use underscores to separate words in longer identifiers. It is generally easier to read $var_names_like_this than $VarNamesLikeThis, especially for non-native speakers of English. It's also a simple rule that works consistently with VAR_NAMES_LIKE_THIS.

#	Package names are sometimes an exception to this rule. Perl informally reserves lowercase module names for "pragma" modules like integer and strict. Other modules should begin with a capital letter and use mixed case, but probably without underscores due to limitations in primitive file systems' representations of module names as files that must fit into a few sparse bytes.

#	If you have a really hairy regular expression, use the /x modifier and put in some whitespace to make it look a little less like line noise. Don't use slash as a delimiter when your regexp has slashes or backslashes.

#	Always check the return codes of system calls. Good error messages should go to STDERR, include which program caused the problem, what the failed system call and arguments were, and (VERY IMPORTANT) should contain the standard system error message for what went wrong. Here's a simple but sufficient example −
#>%			opendir(D, $dir) or die "can't opendir $dir: $!";

#	Think about reusability. Why waste brainpower on a one-shot when you might want to do something like it again? Consider generalizing your code. Consider writing a module or object class. Consider making your code run cleanly with use strict and use warnings (or -w) in effect. Consider giving away your code. Consider changing your whole world view. Consider... oh, never mind.

#	Be consistent.
#	Be nice.

#	}}}

#	Regex:
#	{{{
#	Basic regex comparison operators:
#		=~	or	!~

#	Match				m//
#	Substitute			s///
#	Transliterate		tr///		
#
#	If '/' is used, the leading 'm' can be ommited.

#	Match
my $bar = "This is foo and again foo";
if ($bar =~ /foo/) {
   print "First time is matching\n";
} else {
   print "First time is not matching\n";
}
$bar = "foo";
if ($bar =~ /foo/) {
   print "Second time is matching\n";
} else {
   print "Second time is not matching\n";
}
print "\n";
#	{{{
#>>		First time is matching
#>>		Second time is matching
#	}}}

#	The delmitors '/' can be replaced with other characters, as per sed, but 'm' must be included

$bar = "This is foo and again foo";
if ($bar =~ m[foo]) {
   print "First time is matching\n";
} else {
   print "First time is not matching\n";
}
$bar = "foo";
if ($bar =~ m{foo}) {
   print "Second time is matching\n";
} else {
   print "Second time is not matching\n";
}
print "\n";
#	{{{
#>>		First time is matching
#>>		Second time is matching
#	}}}

#	Regex expressions using =~ / !~ return 1 or 0 for (each) regex match(s)
my $time = "12:30:22";
my $foo = "foo";
my $var_true = ($foo =~ m/foo/);
my ($hours, $minutes, $seconds) = ($time =~ m/(\d+):(\d+):(\d+)/);
print "time=$time\n";
print "hours=$hours, minutes=$minutes, seconds=$seconds\n";
print "\n";
#	{{{
#>>		time=12:30:22
#>>		hours=12, minutes=30, seconds=22
#	}}}

#	Modifiers:
#		i		case insensitive
#		m		use newline boundry (instead of string boundry) for ^ / $
#		o		evaluate only once
#		s		allow '.' to match newline
#		x		allows (ignores?) whitespace in expression (clarity?)
#		g		global matching
#		cg		continue search even after global match fails

#	Match once:
my @var_list = qw/food foosball subeo footnote terfoot canic footbrdige/;
my $var_first=0;
my $var_last=0;
foreach (@var_list) {
   $var_first = $1 if /(foo.*?)/;
   $var_last = $1 if /(foo.*)/;
}
print "var_first=$var_first, var_last=$var_last\n";
print "\n";
#	{{{
#>>		var_first=foo, var_last=footbrdige
#	}}}

#	Regex variables:
#		$&		matched string
#		$`		before matched string
#		$'		after matched string
my $var_string = "The food is in the salad bar";
$var_string =~ m/foo/;
print "Before (\$`)=($`)\n";
print "Matched (\$&)=($&)\n";
print "After (\$')=($')\n";
print "\n";
#	{{{
#>>		Before ($`)=(The )
#>>		Matched ($&)=(foo)
#>>		After ($')=(d is in the salad bar)
#	}}}

#	Substitution:
$var_string = "The cat sat on the mat";
$var_string =~ s/cat/dog/;
print "$var_string\n";
print "\n";
#	{{{
#>>		The dog sat on the mat
#	}}}

#	Translation:
#	translation (or transliteration) does not use regular expressions for its search on replacement values
$var_string = 'the cat sat on the mat.';
$var_string =~ tr/a-z/b/d;
print "$var_string\n";
print "\n";
#	{{{
#>>		 b b   b.
#	}}}

$var_string = 'food';
$var_string = 'food';
$var_string =~ tr/a-z/a-z/s;
print "$var_string\n";
print "\n";
#	{{{
#>>		fod
#	}}}

#	Regex characters/examples:
#		^			Beginning of line
#		$			End of line
#		.			Any character by newline. Include newlines: 'm'
#		[aeiou]		single character in set
#		[^aeiou]	single character not in set
#	Quantifiers:
#		*			0 or more
#		+			1 or more
#		?			0 or 1 
#		*?			0 or more (nongreedy)
#		+?			1 or ore (nongreedy)
#		??			0 or 1 (nongreedy)
#		{n}			n occurences
#		{n,m}		between [n,m] occurences
#		a|b			a or b
#	Character sets
#		\w			word characters
#		\W			nonword characters
#		\s			whitespace
#		\S			non-whitespace
#		\d			digit
#		\D			non-digit
#	Boundries:
#		\A			beginning of string
#		\Z			end of string, just before trailing newline (if present)
#		\z			end of string
#		\G			last match finished
#		\b			word boundry outside brackets, matches backspace (0x08) inside brackets
#		\B			non-wordboundry
#		\n, \t		newline, tab
#	Matches:
#		\1..\9		1st - 9th (n-th) group subsitution
#		\10			Matches nth grouped subexpression if it matched already. Otherwise refers to the octal representation of a character code.	

my $string = "Cats go Catatonic\nWhen given Catnip";
my ($first_word) = ($string =~ /\A(.*?) /);
my @line_first_word = $string =~ /^(.*?) /gm;
print "First word=($first_word)\n","Line line_first_word=(@line_first_word)\n";
print "\n";
#	{{{
#>>		First word=(Cats)
#>>		Line line_first_word=(Cats When)
#	}}}

#	Group Matching
my $time = "12:05:30";
$time =~ m/(\d+):(\d+):(\d+)/;
my ($hours, $minutes, $seconds) = ($1, $2, $3);
print "Hours : $hours, Minutes: $minutes, Second: $seconds\n";
print "\n";
#	{{{
#>>		Hours : 12, Minutes: 05, Second: 30
#	}}}

#	Group match and replace
my $date = '03/26/1999';
$date =~ s#(\d+)/(\d+)/(\d+)#$3/$1/$2#;
print "$date\n";
print "\n";
#	{{{
#>>		1999/03/26
#	}}}

#	Searching from the point where the last match occurred. 
#		\G
#	NB: (Amazingly), the magic variables @-/@+ don't appear in the perl docs chapter on regex?
#	The built-in variables @- and @+ hold the start and end positions, respectively, of the last successful match. $-[0] and $+[0] correspond to entire pattern, while $-[N] and $+[N] correspond to the $N ($1, $2, etc.) submatches.
#	Note that $+[0] etc. (the "end positions") give the index of the character following the match, not the last character of the match itself.
$string = "The time is: 12:31:02 on 4/12/00";
$string =~ /:\s+/g;
($time) = ($string =~ /\G(\d+:\d+:\d+)/);
print "(\@-, \@+)=(@-, @+)\n";
$string =~ /.+\s+/g;
($date) = ($string =~ m{\G(\d+/\d+/\d+)});
print "(\@-, \@+)=(@-, @+)\n";
print "Time: $time, Date: $date\n";
print "\n";
#	{{{
#>>		(@-, @+)=(13 13, 21 21)
#>>		(@-, @+)=(25 25, 32 32)
#>>		Time: 12:31:02, Date: 4/12/00
#	}}}

$_ = "The year 1752 lost 10 days on the 3rd of September";
while (/(\d+)/gc) {
    print "Found number $1\n";
}
if (/\G(\S+)/g) {
    print "Found $1 after the last number.\n";
}
print "\n";
#	{{{
#>>		Found number 1752
#>>		Found number 10
#>>		Found number 3
#>>		Found rd after the last number.
#	}}}

print "The position in \$a is ", pos($a);
pos($a) = 30;
print "The position in \$_ is ", pos;
pos = 30;
print "\n";
print "\n";
#	{{{
#>>		Use of uninitialized value in print at - line 2455.
#>>		Use of uninitialized value $a in scalar assignment at - line 2456.
#>>		The position in $a is The position in $_ is 37
#	}}}

#	}}}

#	Email:
#	{{{

#	Requires <email server> to be running on machine (which it does not check for)
#>%		my $to = 'mld.zz@protonmail.com';
#>%		my $from = 'cmcat_perl';
#>%		my $subject = 'Test Email';
#>%		my $message = 'This is test email sent by Perl Script';
#>%		open(MAIL, "|/usr/sbin/sendmail -t");
#>%		# Email Header
#>%		print MAIL "To: $to\n";
#>%		print MAIL "From: $from\n";
#>%		print MAIL "Subject: $subject\n\n";
#>%		# Email Body
#>%		print MAIL $message;
#>%		close(MAIL);
#>%		print "Email Sent Successfully\n";

#	Sending email via smtp server
#>%		$msg->send('smtp', "smtp.myisp.net", AuthUser=>"id", AuthPass=>"password" );

#	MIME (is it available by default) -> no.
#>%		# first, create your message
#>%		use Email::MIME;
#>%		my $message = Email::MIME->create(
#>%		  header_str => [
#>%		    From    => 'mld.zz@protonmail.com',
#>%		    To      => 'mld.c@protonmail.com',
#>%		    Subject => 'Happy birthday!',
#>%		  ],
#>%		  attributes => {
#>%		    encoding => 'quoted-printable',
#>%		    charset  => 'ISO-8859-1',
#>%		  },
#>%		  body_str => "Happy birthday to you!\n",
#>%		);
#>%		# send the message
#>%		use Email::Sender::Simple qw(sendmail);
#>%		sendmail($message);

#	}}}

#	(List of) Advanced (Topics):
#	{{{
#	LINK: https://www.tutorialspoint.com/perl/index.htm
#	Socket programming
#	Object Oriented
#	Database Access
#	CGI Programming
#	Packages and Modules
#	Process Management
#	Embedded Documentation
#	Functions References
#	}}}

#	}}}1



