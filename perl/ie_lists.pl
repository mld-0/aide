#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=3:
#   }}}1
use strict; 
use warnings;
no warnings 'shadow';
use feature qw(say);

#	Each assignment in perl is either in a scalar or list context

my @fred = ();
$fred[0] = "yabba"; 
$fred[1] = "dabba"; 
$fred[2] = "doo";

#	List seperator (for quoted lists)
$" = ",";
say "@fred";

#	Output field seperator (for unquoted lists)
$, = ",";
say @fred;
print "\n";

$, = " ";

#	If given a decimal as an index, perl will truncate the value

#	If you store into an array element that is beyond the end of the array, the array is automatically extended as needed—there’s no limit on its length, as long as there’s available memory for Perl to use. If Perl needs to create the intervening elements, it creates them as undef values:
my @rocks = ();
$rocks[0] = 'bedrock'; 
$rocks[1] = 'slate'; 
$rocks[2] = 'lava'; 
$rocks[3] = 'crushed rock'; 
$rocks[99] = 'schist';

my $end = $#rocks; # 99, which is the last element's index 
my $number_of_rocks = $end + 1; # okay, but you'll see a better way later 
$rocks[ $#rocks ] = 'hard rock'; # the last rock

#	$rocks[-1] is equivelent to $rocks[ $#rocks - 1] (last element)
say $rocks[-1];
say $rocks[-100];
print "\n";

#	Range operator, 1..10 = (1, 2, ..., 10)
say (1..10);
print "\n";

#	List literals
#		 list literal (the way you represent a list value within your program) is a list of comma- separated values enclosed in parentheses. These values form the elements of the list.

my @var = (1, 2, 3);  # list of three values 1, 2, and 3
my @var = (1, 2, 3,);  # the same three values (the trailing comma is ignored) 
my @var = ("fred", 4.5);  # two values, "fred" and 4.5
my @var = ();  # empty list - zero elements
my @var = (1..100);  # list of 100 integers
my @var = ("fred", "barney", "betty", "wilma", "dino");  # list of strings

#	qw() 	single quote-words
#		Each item seperated by whitespace is added to list as a single-quoted value
#		Any character may be used as opening closing
my @var = qw(fred, barney, betty, wilma, dino);  # list of strings
my @var = qw<fred, barney, betty, wilma, dino>;  # list of strings
say @var;

#	qq()	double-quote words
#		As per qw(), but using double quotes
my @var = qq(fred, barney, betty, wilma, dino);  # list of strings
my @var = qq<fred, barney, betty, wilma, dino>;  # list of strings
say @var;
print "\n";


#	List assignment
my ($fred, $barney, $dino) = ("flintstone", "rubble", undef);
#	swap variables (in single statement)
($fred, $barney) = ($barney, $fred); # swap those values

#	If there are more list items that variables, the extra list items are silently ignored
my ($fred, $barney) = qw< flintstone rubble slate granite >;  # two ignored items

#	If there are more variables than list items, extra variables are assigned undef
my ($wilma, $dino) = qw[flintstone];  # $dino gets undef

#	@  refer to entire array
my @rocks = qw/ bedrock slate lava /;
my @tiny = ();  # empty list
my @giant = 1..1e5;  # list with 100,000 elements
my @stuff = (@giant, undef, @giant);  # list with 200,001 elements
my $dino = "granite";  
my @quarry = (@rocks, "crushed rock", @tiny, $dino);

#	Arrays contain only scalars, not other arrays. An array of arrays can be created using references

#	Copying an array
#		the new array is a copy, not a reference to the origional array
my @copy_quarry = @quarry;
$copy_quarry[0] = "first";
say @copy_quarry;
say @quarry;
print "\n";

#	pop(@array)
#		Remove and return last value of array. Returns undef if array is empty
my @array = 5..9;
say @array;
my $fred = pop(@array);
my $barney = pop(@array);
pop @array;
say @array;

#	push(@array, $value)
#		Add an element (or list of elements) to end of array
push(@array, 0);
push @array, 8;
push @array, 1..10;
my @others = qw/ 9 0 2 1 0 /;
push @array, @others;
say @array;
print "\n";

#	shift(@array)
#		Remove and return first value of array
my @array = qw# dino fred barney#;
my $m = shift(@array);
my $n = shift @array;
shift @array;  # array now empty
my $o = shift @array;  # o = undef, @array is unmodified

#	unshift(@array, $value)
#		Add an element (or list of elements) to start of array
unshift(@array, 5);
unshift(@array, 4);
my @others = 1..3;
unshift @array, @others;
say @array;
print "\n";

#	splice(@array[, $offset, $length, @list)
#		Remove elements designated by $offset and $length from array, and replace them with elements of @list (if any)
#		returns removed elements in list context, or last element removed in scalar context
#		specify $length=0 to insert @list values (at $offset) without removing anything from list
my @array = qw( pebbles dino fred barney betty );
my @removed = splice(@array, 2);  # remove everything after second index (fred, barney, betty)
say @array;
say @removed;
print "\n";

my @array = qw( pebbles dino fred barney betty );
my @removed = splice(@array, 1, 2);  # remove 2 elements, starting at 1st element (dino, fred)
say @array;
say @removed;
print "\n";

my @array = qw( pebbles dino fred barney betty );
my @removed = splice(@array, 1, 2, qw(wilma));  # remove 2 elements, starting at 1st element, and insert 'wilma'
say @array;
say @removed;
print "\n";

my @array = qw( pebbles dino fred barney betty );
my @removed = splice(@array, 1, 0, qw(wilma));  # insert 'wilma' at position 1, without deleting elements
say @array;
say @removed;
print "\n";

#	Interpolate array into string
$" = " ";
my @rocks = qw{ flintstone slate rubble };
print "rocks=(@rocks)\n";
#	A single element of an array interpolates into its value
print "rocks[1]=($rocks[1])\n";
#	Interpolate list length
print "len(rocks)=($#rocks)\n";
print "\n";


#	foreach loop
#		using default $_
foreach (qw/ bedrock slate lava/) {
	print "\$_=($_)\n";
}

foreach my $loop_rock (@rocks) {
	print "loop_rock=($loop_rock)\n";
}
print "\n";

#	reverse()
#		takes a list of values, and returns said list in oppositie order
#		does not alter list passed as argument
my @fred = 6..10;
my @barney = reverse(@fred);
say @fred;
say @barney;
print "\n";

#	sort()
#		take a list of values, and sort them per internal character ordering.
#		does not alter list passed as argument
my @sorted = sort(@rocks);
my @back = reverse sort(@rocks);
my @rocks = sort @rocks;
my @numbers_alpha = sort 97..102;  # sort by default uses alphabetical order, which does not sort numbers correctly
my @numbers_num = sort {$a <=> $b} 97..102;  # sort by numerical value
say @sorted;
say @back;
say @rocks;
say @numbers_alpha;
say @numbers_num;
print "\n";


#	Scalar and List contexts
#		a fundamental aspect of perl, a given expression maybean different things depending on context
my @people = qw( fred barney betty );
#	in list context, a list is a list of elements
my @sorted = sort(@people);  # list context
#	in a scalar context, a list gives the number of elements
my $people_len = @people;

#	Examples of scalar context for 'something'
#>%		$fred = something
#>%		$fred[3] = something
#>%		123 + something
#>%		something + 654
#>%		if (something) {...}
#>%		while (something) {...}
#>%		$fred[something] = something

#	Examples of list context for 'something'
#>%		@fred = something
#>%		($fred, $barney) = something
#>%		($fred) = something
#>%		push(@fred, something)
#>%		foreach $fred (something) {...}
#>%		sort(something)
#>%		reverse(something)
#>%		print(something)

#	List producing expressions in scalar context:
#		varies from expression to expression
#		sort() in scalar context returns undef
#		reverse() in scalar context returns a string (the results of concatenating all strings in given list)

#	Scalar producing expressions in list context
#		If an expression doesn't have a list value, the scalar value is converted into a single-element list
my @fred = 6 * 7; # gets the one-element list

#	scalar()	Forcing scalar context
@rocks = qw( talc quartz jade obsidian );
print "How many rocks do you have?\n";  
print "I have ", scalar @rocks, " rocks!\n";  # Correct, gives a number
print "I have ", @rocks, " rocks!\n";  # WRONG, prints names of rocks i
print "\n";


#	Length of an array:
#		$#array + 1 
#	or
#		scalar @array
#	@{[ ... ]}		Embed perl expression in string
print "len(rocks)=(@{[ scalar @rocks ]})\n";
#	$#array 		Index of last element (len(array) - 1)
print "\$\#rocks=($#rocks)\n";
print "\n";

#	<STDIN> in scalar/list context
#		In scalar context, <STDIN> returns next line of input
#		In list context, <STDIN> returns all remaining lines of input (each line as a list element)

#	Read and chomp all lines from stdin
#>%		@lines = <STDIN>; 
#>%		chomp(@lines);
#	or
#>%		chomp(@lines = <STDIN>);


#	Format numerical output for money
sub big_money {
	my $number = sprintf "%.2f", shift @_;
	# Add one comma each time through the do-nothing loop 1 while $number =~ s/^(-?\d+)(\d\d\d)/$1,$2/;
	# Put the dollar sign in the right place
	$number =~ s/^(-?)/$1\$/;
	$number;
}

#	grep()
#		Get odd numbers between 1..1000
my @odd_numbers = grep { $_ % 2 } 1..1000;
#		Get only lines containing 'fred' from file fh
#>%		my @matching_lines = grep { /\bfred\b/i } <$fh>;


#	map()
my @data = (4.75, 1.5, 2, 1234, 6.9456, 12345678.9, 29.95);
my @formatted_data = map { big_money($_) } @data;


#	Other list utilities
#	first()
use List::Util qw(first);
my @characters = qw( Abc Def pebble Pebbles );
my $first_match = first { /\bPebbles\b/i } @characters;
print "first_match=($first_match)\n";

#	sum()
use List::Util qw(sum);
my $total = sum( 1..1000 ); # 500500
print "total=($total)\n";

#	max()
use List::Util qw(max);
my $max = max( 3, 5, 10, 4, 6 );
print "max=($max)\n";

#	maxstr()
use List::Util qw(maxstr);
my $max = maxstr( @characters);
print "max=($max)\n";

#	shuffle()
use List::Util qw(shuffle);
my @shuffled = shuffle(1..10); # randomized order of elements
print "shuffled=(@shuffled)\n";

#	natatime() 		N at a time
use List::MoreUtils qw(natatime);
my $iterator = natatime 3, @array;
while( my @triad = $iterator->() ) {
	print "Got @triad\n";
}
print "\n";

#	mesh()
#		
#>%		use List::MoreUtils qw(mesh);
#>%		my @abc = 'a' .. 'z';
#>%		my @numbers = 1 .. 20;
#>%		my @dinosaurs = qw( dino );
#>%		my @large_array = mesh @abc, @numbers, @dinosaurs;
#>%		print "large_array=(@large_array)\n";


