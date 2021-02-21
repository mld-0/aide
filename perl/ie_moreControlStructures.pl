#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=3:
#   }}}1
use strict; 
use warnings;
no warnings 'shadow';

#	Unless
my $fred = "qwerty*";
unless ($fred =~ /\A[A-Z_]\w*\z/i) {
	print "The value of \$fred doesn't look like a Perl identifier name.\n"; 
}
print "\n";

#	Until
my $i = 3;
my $j = 1;
until ($j > $i) {
	$j *= 2; 
	print "$j\n";
}
print "\n";

#	Expression modifiers
my $n = -5;
print "$n is a negative number.\n" if $n < 0;
print "\n";

#>%		&error("Invalid input") unless &valid($input); 
#>%		$i *= 2 until $i > $j;
#>%		print " ", ($n += 2) while $n < 10;
#>%		&greet($_) foreach @person;

#	Naked block
#		one of its features is that it provides a scope for temporary lexical variables
#>%		{
#>%			print "Please enter a number: ";
#>%			chomp(my $n = <STDIN>);
#>%			my $root = sqrt $n; # calculate the square root print "The square root of $n is $root.\n";
#>%		}


#	elsif
my $dino = "chicken";
if ( ! defined $dino) {
	print "The value is undef.\n";
} elsif ($dino =~ /^-?\d+\.?$/) {
	print "The value is an integer.\n";
} elsif ($dino =~ /^-?\d*\.\d+$/) {
	print "The value is a _simple_ floating-point number.\n";
} elsif ($dino eq '') {
	print "The value is the empty string.\n";
} else {
	print "The value is the string '$dino'.\n"; 
}
print "\n";

#	autoincrement, autodecrement
my $bedrock = 42;
$bedrock++; # add one to $bedrock; it's now 43
$bedrock--; # subtract one from $bedrock; it's 42 again

my @people = qw{ fred barney fred wilma dino barney fred pebbles };
my %count; # new empty hash
$count{$_}++ foreach @people; # creates new keys and values as needed
print "count=(@{[ %count ]})\n";
print "\n";

#	$a++ returns a then increments it
#	$++a increments a then returns it

my @people = qw{ fred barney bamm-bamm wilma dino barney betty pebbles }; 
my %seen;
foreach (@people) {
	print "I've seen you somewhere before, $_!\n"
		if $seen{$_}++;
}
print "seen=(@{[ %seen ]})\n";
print "\n";

for ($_ = "bedrock"; s/(.)//; ) { # loops while the s/// is successful
	print "One character is: $1\n"; 
}
for ($i = 10; $i >= 1; $i--) {
	print "I can count down to $i\n"; 
}
print "\n";



my $a = 10;
 # while loop execution
while( $a < 20 ) {
	printf "Value of a: $a\n";
	$a = $a + 1; 
}
print "\n";

$a = 5;
 # until loop execution
until( $a > 10 ) {
	printf "Value of a: $a\n";
	$a = $a + 1; 
}
print "\n";

# for loop execution
for( $a = 10; $a < 20; $a = $a + 1 ){
	print "value of a: $a\n"; 
}
print "\n";

my @list = (2, 20, 30, 40, 50);
# foreach loop execution
foreach $a (@list) {
	print "value of a: $a\n"; 
}
print "\n";

$a = 10;
 # do...while loop execution
do {
	printf "Value of a: $a\n";
    $a = $a + 1;
} while( $a < 20 );
print "\n";

my $a = 0;
my $b = 0;
 # outer while loop
 while($a < 3) {
    $b = 0;
    # inner while loop
    while( $b < 3 ) {
		print "value of a = $a, b = $b\n";
		$b = $b + 1; 
	}
	$a = $a + 1;
    print "Value of a = $a\n";
}
print "\n";

#	Loop control statements:
#	next [label]
#		skip remainder of body and immediately retest loop condition before reiteraterating
#	last [label]
#		terminate loop and jump to statement immediately following loop
#	continue
#		always executed just before the loop condition is to be evaluated again
#	redo
#		restart loop block, without evaluating continue block
#	goto
#		goto label
#		goto expr
#		goto &name
#		bad bad bad bad bad

#	next example
$a = 10;
 while( $a < 20 ){
    $a = $a + 1;
	if( $a == 15) {
		next;
	}
    print "value of a: $a\n";
}
print "\n";

#	next with labels INNER, OUTER
$a = 0;
OUTER: while( $a < 4 ){
   $b = 0;
   print "value of a: $a\n";
   INNER:while ( $b < 4) {
      if( $a == 2){
			$a = $a + 1;
			next OUTER; 
		}
		$b = $b + 1;
		print "Value of b : $b\n";
	}
	$a = $a + 1; 
}
print "\n";

#	last example
 $a = 10;
 while( $a < 20 ){
	if( $a == 15) {
		last;
	}
    print "value of a: $a\n";
    $a = $a + 1;
}
print "\n";

#	last with labels INNER, OUTER
$a = 0;
 OUTER: while( $a < 4 ){
    $b = 0;
    print "value of a: $a\n";
    INNER:while ( $b < 4){
       if( $a == 2){
           # terminate outer loop
           last OUTER;
       }
       $b = $b + 1;
       print "Value of b : $b\n";
    }
    $a = $a + 1;
}
print "\n";

#	continue example, foreach loop
@list = (1, 2, 3, 4, 5);
 foreach $a (@list){
    print "Value of a = $a\n";
 } continue {
    last if $a == 4;
 }
print "\n";


#	redo example
$a = 0;
while($a < 10){
	if( $a == 5 ){
		$a = $a + 1;
		redo; 
	}
    print "Value of a = $a\n";
 } continue {
$a = $a + 1; 
}
print "\n";

#	loop using goto
$a = 10;
LOOP:do {
	if( $a == 15){
 		$a = $a + 1;
		goto LOOP;
	}
	print "Value of a = $a\n";
     $a = $a + 1;
} while( $a < 20 );
print "\n";




