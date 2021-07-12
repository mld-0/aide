#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=3:
#   }}}1
use strict; 
use warnings;
no warnings 'shadow';
#	{{{2
#	If you have two subroutine definitions with the same name,§ the later one overwrites the earlier one.
#	you may use any global variables within the subroutine body.
#	Whatever calculation is last performed in a sub- routine is automatically also the return value.

#	A way of declaring functions presumedly not of particuarly much use
#		using variables in this way (with script enabled), we must declare said variables before we can declare the function in which we use them. 
my $fred = 3;
my $barney = 4;
my $wilma = &sum_of_fred_and_barney;
print "wilma=($wilma)\n";
sub sum_of_fred_and_barney {
	print "Hey, you called the sum_of_fred_and_barney subroutine!\n";
	$fred + $barney;  # That's the return value 
}

#	The '&' infront of a function call is optional, but serves to specify that this is a function call
#	it also allows calling of subroutines which share names which builtin subroutines

#	Calling a subroutine (with arguments)
my $n = &max(10, 15); # This sub call has two parameters
print "n=($n)\n";
print "\n";


#	@_		
#	arguments array
#		unrelated to $_ variable
#		private to (this invocation of the) subroutine, stored upon calling further subroutine and restored upon return
#			$_[0], first argument
#			$_[1], second argument, ect.
#	my $fred, $barney;  # fails to declare barney
# 	my ($fred, $barney);  # declares both

#	Private variables in subroutines
#		my	(lexical)
#				scoped to current block (or file)
#				callees?
#				alternative (is?)

#	'return' with no arguments will return undef in a scalar context, or an empty list in a list context

#	Implementing 'max()'
sub max {
	my ($max_so_far) = shift(@_);  # first value is largest so-far
	foreach (@_) {
		if ($_ > $max_so_far) {
			$max_so_far = $_;
		}
	}
	return $max_so_far;
}

my $maximum = &max(3, 5, 10, 4, 6);
print "maximum=($maximum)\n";
print "\n";

foreach (1..10) {
	my ($square) = $_ * $_;
	print "$_ squared is $square\n";
}
print "\n";

#	Passing scalar and list as args -> scalar must be first (unless using references)
sub which_element_is {
	my ($what, @array) = @_;
	foreach (0..$#array) {
		if ($what eq $array[$_]) {
			return $_;
		}
	}
	return -1;
}
my @names = qw/ fred barney betty dino wilma pebbles bamm-bamm /;
my $results = &which_element_is("dino", @names);
print "names=(@names), results=($results)\n";
print "\n";

#	wantarray()
#		returns true if caller is looking for a list value, or false for a scalar.
#		usage:
#>%			return wantarray ? @a : "@a";

#	Omitting the Ampersand '&' on function calls
#		If the compiler sees the subroutine definition before invocation, or if Perl can tell from the syntax that it’s a subroutine call, the subroutine can be called without an ampersand, just like a built-in function.
#		This means that if Perl can see that it’s a subroutine call without the ampersand, from the syntax alone, that’s generally fine. That is, if you’ve got the parameter list in parentheses, it’s got to be a function call
#		Or, if Perl’s internal compiler has already seen the subroutine definition, that’s generally okay, too. In that case, you can even omit the parentheses around the argument list
#		If the subroutine has the same name as a Perl built-in, you must use the ampersand to call your version
#		So, the real rule to use is this one: until you know the names of all Perl’s built-in functions, always use the ampersand on function calls.

#	Non-Scalar values
#		A subroutine called in a list context can return a list of values
#	Continue: 2021-02-20T21:25:32AEDT example of list return from subroutine (example list_from_fred_to_barney doesn't give correct output?)
#	Continue: 2021-02-20T21:26:06AEDT subroutine, detecting static vs list output 


#	Persistent, Private Variables
#		With state, you can still have private variables scoped to the subroutine but Perl will keep their values between calls.
#		The first time you call the subroutine, Perl declares and initializes $n. Perl ignores the statement on all subsequent calls. Between calls, Perl retains the value of $n for the next call to the subroutine.
#	state requires:
use 5.010;
sub marine {
	state $n = 0; # private, persistent variable $n 
	$n += 1;
	print "Hello, sailor number $n!\n";
}
&marine;
&marine;
&marine;
print "\n";

#	subroutine which remembers its arguments and provides a running sum by using a state array:
sub running_sum { 
	state $sum = 0; 
	state @numbers;
	foreach my $number ( @_ ) { 
		push @numbers, $number;
		$sum += $number; 
	}
	say "The sum of (@numbers) is $sum"; 
}
&running_sum( 5, 6 ); 
&running_sum( 1..3 ); 
&running_sum( 4 );
print "\n";

#	state list cant be initalised from list context
#>%		state @array = qw(a b c);  # error


#	Continue: 2021-03-12T22:39:57AEDT Subroutine signatures
use feature qw(signatures);
no warnings qw(experimental::signatures);
sub max2( $m, $n ) {
	if ($m > $n) { $m } else { $n }
}


#	}}}1
