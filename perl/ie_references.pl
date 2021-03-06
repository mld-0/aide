#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=3:
#   }}}1
use strict; 
use warnings;
no warnings 'shadow';
#	{{{2
#	References are the basis for complex data structures, object-oriented programming, and fancy subroutine handling.
#	A Perl scalar variable holds a single value. An array holds an ordered list of scalars. A hash holds an unordered collection of scalars as values, keyed by strings. Although a scalar can be an arbitrary string, which lets us encode complex data in an array or hash, none of the three data types are well suited to complex data interrelationships. This is a job for the reference.

#	create a reference for any variable, subroutine or value by prefixing it with a backslash as follows:
#		$scalarref = \$foo;
#		$arrayref  = \@ARGV;
#		$hashref = \%ENV;
#		$coderef = \&handler;
#		$globref = \*foo;

my $arrayref = [1, 2, ['a', 'b', 'c']];
 
my $hashref = { 'Adam' => 'Eve', 'Clyde' => 'Bonnie', };

print "$hashref\n";
print "$arrayref\n";
print "$hashref\n";
print "\n";

#	Dereferencing returns the value from a reference point to the location.
my $var = 10;
my $p_var = \$var;
print "Reference type in p_var : ", ref($p_var), "\n";
print "Value of \$var is: " , $$p_var, "\n";

my @var = (1, 2, 3);
print "Value of \$var is: " , $$p_var, "\n";
$p_var = \@var;
print "Reference type in p_var : ", ref($p_var), "\n";
print "Value of \@var is: " , @$p_var, "\n";
my %var = ('key1' => 10, 'key2' => 20);
print "Value of \@var is: " , @$p_var, "\n";
$p_var = \%var;
print "Reference type in p_var : ", ref($p_var), "\n";
print "Value of \%var is: " , %$p_var, "\n";
print "\n";

#	Circular references
#		two references containing reference to each other
my $foo = 100;
$foo = \$foo;
print "Value of foo is : ", $$foo, "\n";
print "\n";

#	References to functions
sub PrintHash {
	my (%hash) = @_;
	foreach my $item (%hash) {
		print "Item: $item\n";
	}
}
my %hash = ('name' => 'Tom', 'age' => 19);
my $cref = \&PrintHash;
&$cref(%hash);
print "\n";


#	Referencing:
#		prefix variable with '\'

#	Dereferencing:
#		@{ $items } where $items is a reference to a list

#	Both these lines refer to the entire array
#>%		@ skipper 
#>%		@{ $items }

sub check_required_items {
	my $who = shift;
	my $items = shift;
	my %whos_items = map { $_, 1 } @{$items}; # the rest are the person's items
	my @required = qw(preserver sunscreen water_bottle jacket);
	my @missing = ( );
	for my $item (@required) {
		unless ( $whos_items{$item} ) { # not found in list?
			print "$who is missing $item.\n"; 
			push(@missing, $item);
		}
	} 
	if (@missing) {
		print "Adding @missing to @$items for $who.\n"; 
		push @$items, @missing;
	}
}
my @gilligan = qw(red_shirt hat lucky_socks water_bottle); 
check_required_items('gilligan', \@gilligan);
my @skipper = qw(blue_shirt hat jacket preserver sunscreen);
check_required_items('skipper', \@skipper); 
my @professor = qw(sunscreen water_bottle slide_rule batteries radio); 
check_required_items('professor', \@professor);
print "\n";

#	Nested data structures
my @skipper = qw(blue_shirt hat jacket preserver sunscreen); 
my @skipper_with_name = ('Skipper' => \@skipper);
my @professor = qw(sunscreen water_bottle slide_rule batteries radio); 
my @professor_with_name = ('Professor' => \@professor);
my @gilligan = qw(red_shirt hat lucky_socks water_bottle); 
my @gilligan_with_name = ('Gilligan' => \@gilligan);
my @all_with_names = ( \@skipper_with_name, \@professor_with_name, \@gilligan_with_name,);

#	Passing our new nested data structure to our (unchanged) check_required_items functions
for my $person (@all_with_names) {
	my $who = $$person[0];
	my $provisions_reference = $$person[1]; 
	check_required_items($who, $provisions_reference);
}
#	or
#>%		for my $person (@all_with_names) { 
#>%			check_required_items(@$person);
#>%		}
#	or
#>%		check_required_items(@$_) for @all_with_names;
print "\n";

#	For reference to our nested data structure, get:
my $root = \@all_with_names;
#	gilligans first item:
print( ${${${$root}[2]}[1]}[0] . "\n");
#	all of gilligans provisions
$, = " ";
print( @{$root->[2][1]} ); print "\n";
print "\n";
$, = "";

#	References to Hashes
my %gilligan_info = (
	name => 'Gilligan', 
	hat => 'White', 
	shirt => 'Red', 
	position => 'First Mate',
);
my $hash_ref = \%gilligan_info;
#	Getting a value for a given key
my $name = $ gilligan_info { 'name' }; 
#	or
my $name = $ { $hash_ref } { 'name' };
#	if the only thing inside the curly braces is a simple scalar variable (as shown in these examples so far), we can drop the curly braces:
my $name = $$hash_ref{'name'}; 
my $name = $hash_ref->{'name'};
my @keys = keys %$hash_ref;
print "name=($name), keys=(@keys)\n";
print "\n";

#	Because a hash reference fits wherever a scalar fits, we can create an array of hash references
my %gilligan_info = (
	name => 'Gilligan', hat => 'White', shirt => 'Red', position => 'First Mate',
);
my %skipper_info = (
	name => 'Skipper', hat => 'Black', shirt => 'Blue', position => 'Captain',
);
my @crew = (\%gilligan_info, \%skipper_info);
#	Get Gilligan's name via any of:
#>%		${ $crew[0] } { 'name' }
#>%		my $ref = $crew[0]; $$ref{'name'} 
#>%		$crew[0]−>{'name'} 
#>%		$crew[0]{'name'}
my $format = "%-15s %-7s %-7s %-15s\n"; 
printf $format, qw(Name Shirt Hat Position); 
foreach my $crewmember (@crew) {
	printf $format, @$crewmember{qw(name shirt hat position)};
}
print "\n";

#		Once we start using references and passing them around, we have to ensure that we know which sort of reference we have. If we try to use the reference as a type that it is not, our program will blow up

#	ref()	Checking reference types
#		Examines the value of EXPR, expecting it to be a reference, and returns a string giving information about the reference and the type of referent. If EXPR is not specified, $_ will be used.
use Carp qw(croak);
use Scalar::Util qw(reftype);
sub show_hash {
	my $hash_ref = shift;
	my $ref_type = reftype $hash_ref; # works with objects 
	croak "I expected a hash reference!" unless $ref_type eq ref {};
	foreach my $key ( %$hash_ref ) {
		...
	}
}


#	A symbolic reference is just a string that happens to name something in a package symbol table.

#	Perl arrays and hashes are internally one-dimensional. That is, their elements can hold only scalar values (strings, numbers, and refer- ences). When we use a phrase like “array of arrays”, we really mean “array of references to arrays”, just as when we say “hash of functions”, we really mean “hash of references to subroutines”
#

#	anonymous array composer
#		You can create a reference to an anonymous array with square brackets
my $arrayref = [1, 2, ["a", "b", "c", "d"]];

#	anonymous hash composer
my $bonnie = "someone-or-other";
$hashref = {
        "Adam"   => "Eve",
        "Clyde"  => $bonnie,
        "Antony" => "Cleo" . "patra",
};

#	hash of arrays
my $table = {
"john" => [ 47, "brown", 186 ],
"mary" => [ 23, "hazel", 128 ],
"bill" => [ 35, "blue",  157 ],
};

#	hash of hashes
my $table = {
"john" => { age    => 47,
            eyes   => "brown",
            weight => 186,
          },
"mary" => { age    => 23,
            eyes   => "hazel",
            weight => 128,
          },
"bill" => { age    => 35,
            eyes   => "blue",
            weight => 157,
          },
};

#	Anonymous subroutine composer
my $coderef = sub { print "Boink!\n" };  # Now &$coderef prints "Boink!"

#	Object constructors

#	Symbol table references
#>%		$scalarref = *foo{SCALAR};  # Same as \$foo
#>%		$arrayref  = *ARGV{ARRAY};  # Same as \@ARGV
#>%		$hashref = *ENV{HASH};  # Same as \%ENV
#>%		$coderef = *handler{CODE};  # Same as \&handler
#>%		$globref = *foo{GLOB}  # Same as \*foo


#	Continue: 2021-02-21T22:05:09AEDT Programming Perl, Ch8, topics:
#	Using a variable name as a variable name
#	Using a BLOCK as a variable name
#	Using the arrow operator
#	Using Object Methods
#	Tricks with Hard References
#	Closures
#	Symbolic References

#	}}}1
