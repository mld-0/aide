#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=3:
#   }}}1
use strict; 
use warnings;
no warnings 'shadow';
use feature qw(say);
#	{{{2
#	A hash is a data structure, not unlike an array in that it can hold any number of values and retrieve them at will. But instead of indexing the values by number, as you did with arrays, you look up hash values by name.
#	These keys are arbitrary strings-you can use any string expression for a hash key. And they are unique strings—just as there’s only one array element numbered 3, there’s only one hash element named wilma.
#	The keys and values are both arbitrary scalars, but the keys are always converted to strings. So, if you used the numeric expression 50/20 as the key, it would be turned into the three-character string "2.5" 
#	As usual, Perl's "no unnecessary limits" philosophy applies: a hash may be of any size, from an empty hash with zero key-value pairs, up to whatever fills up your memory.

#	When you store something into an existing hash element, it overwrites the previous value:

#	To refer to an entire hash
#		%hash
#	Access the elements of a hash
#>%		$hash{$some_key}

my %family_name = ();
$family_name{'fred'} = 'flintstone'; 
$family_name{'barney'} = 'rubble';
$family_name{'wilma'} = 'flintstone';  # adds a new key (and value) 
$family_name{'betty'} .= $family_name{'barney'};  # creates the element if needed

#	Creating a hash from a list
my %some_hash = ('foo', 35, 'bar', 12.4, 2.5, 'hello', 'wilma', 1.72e30, 'betty', "bye");
#	or
#	quotes may be ommited from keys when using big-arrows, provided the key isn't an (expression/operator), ie: '+'
my %some_hash = (foo => 35, bar => 12.4, 2.5 => 'hello', wilma => 1.72e30, betty => "bye");
print "some_hash=(@{[ %some_hash ]})\n";

#	The value of the hash (in a list context) is a simple list of key-value pairs (which won't necessarily be in the same order)
my @any_array = %some_hash;
print "any_array=(@any_array)\n";
print "\n";

#	hash assignment
my %new_hash = %some_hash;

#	reverses key/value pairs -> only 1:1 if values are all unique, otherwise last value (during unpacking) becomes value 
my %inverse_hash = reverse %some_hash;

#	if there’s anything inside the curly braces besides a bareword, Perl will interpret it as an expression. For instance, if there is a ., Perl interprets it as a string concatenation:
#>%		$hash{ bar.foo } = 1;  # that's the key 'foobar'

#	A hash is truthy if it contains at least one key-value pair

#	keys(), values()	 hash functions
#		The keys function yields a list of all the keys in a hash, while the values function gives the corresponding values. If there are no elements to the hash, then either function returns an empty list
my %hash = ('a' => 1, 'b' => 2, 'c' => 3); 
my @k = keys %hash;
my @v = values %hash;
#	scalar context, gets *length* of keys
my $count = keys %hash;  # gets 3, meaning three key-value pairs
print "k=(@k)\n";
print "v=(@v)\n";
print "count=($count)\n";
#	each()		hash function
#		 which returns a key-value pair as a two-element list.
while ( my($k, $v) = each(%hash) ) {
	print "k=($k), v=($v)\n";
}
#	Using sort with foreach
foreach my $k (sort keys %hash) {
	print "k=($k), value=($hash{$k})\n";
}
print "\n";


my %books = ();
$books{'fred'} = 3; 
$books{'wilma'} = 1;
$books{"barney"} = 0; # no books currently checked out 
$books{"pebbles"} = undef; # no books EVER checked out; a new library card
#	exists()
#		To see whether a key exists in the hash (that is, whether someone has a library card or not), use the exists function, which returns a true value if the given key exists in the hash, whether the corresponding value is true or not
if (exists $books{"dino"}) { 
	print "There's a library card for dino\n";
}
#	delete()
#		The delete function removes the given key (and its corresponding value) from the hash (if there’s no such key, its work is done; there’s no warning or error in that case)
delete $books{"betty"};


#	Hash interpolation
#		$hash{$item} can be interpolated into a string, however %hash cannot. To interpolate a hash, use
#>%		print "${[ %hash ]}";


#	%ENV 	The ENV hash
#		Perl stores the shell environement from which it was launched in hash %ENV
say "$ENV{HOME}";
say "$ENV{PATH}";
print "\n";


#	}}}1
