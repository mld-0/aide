#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=3:
#   }}}1

#	$where = index($big, $small[, $index])
#		Finding the first occurence of $small within $big, returning the location of the first character, or -1 if not found. Starting at $index, if given.
my $stuff = "Howdy world!";
my $where = index($stuff, "wor");
print "stuff=($stuff), where=($where)\n";
print "\n";

#	$where = rindex($big, $small[, $index])
#		Find last occurence of $small within $big. End search at $index if given
my $fred = "Yabba dabba doo!";
my $where1 = rindex($fred, "abba"); # $where1 gets 7
my $where2 = rindex($fred, "abba", $where1 - 1); # $where2 gets 1 
my $where3 = rindex($fred, "abba", $where2 - 1); # $where3 gets –1
print "where1=($where1), where2=($where2), where3=($where3)\n";
print "\n";

#	$part = substr($string, $inital_position, $length)
#		Returns substring of $length characters, beginning at $inital_position, from $string
my $mineral = substr("Fred J. Flintstone", 8, 5); # gets "Flint" 
my $rock = substr "Fred J. Flintstone", 13, 1000; # gets "stone"
my $rock = substr "Fred J. Flintstone", 13; # gets "stone"
print("mineral=($mineral), rock=($rock)\n");
print("\n");

#	Update selected portion of string
#		the assigned (sub)string doesn’t have to be the same length as the substring it’s replacing. The string’s length is adjusted to fit.
my $string = "Hello, world!";
substr($string, 0, 5) = "Goodbye"; # $string is now "Goodbye, world!"
print "string=($string)\n";
print "\n";

#	The binding operator can restrict an operation to part of a string
#		replaces fred with barney wherever possible within just the last 20 characters of a string
my $string = "Hello, fred!";
substr($string, -20) =~ s/fred/barney/g;
print "string=($string)\n";
print "\n";

#	Inserting/replacing text with substr()
#		Insert "Goodbye" at position 0, replacing 5 characters from previous string 
my $string = "Hello, world!";
my $previous_value = substr($string, 0, 5, "Goodbye");  # previous_value becomes 'Hello', string becomes 'Goodbye, world!'
print "previous_value=($previous_value), string=($string)\n";
print "\n";

#	Ongoing: 2021-02-21T13:48:17AEDT dealing with money in a language where all numbers are floating point?

#	Format numerical output for money
sub big_money {
	my $number = sprintf "%.2f", shift @_;
	# Add one comma each time through the do-nothing loop 1 while $number =~ s/^(-?\d+)(\d\d\d)/$1,$2/;
	# Put the dollar sign in the right place
	$number =~ s/^(-?)/$1\$/;
	$number;
}

#	sprintf()  equivelent to printf(), but returns string instead of printing it
my $money = sprintf "%.2f", 2.49997;
print "money=($money)\n";
print &big_money($money) . "\n";
print "\n";

#	Intereting non-decimal numbers
hex('DEADBEEF');  # 3_735_928_559 decimal 
hex('OxDEADBEEF');  # 3_735_928_559 decimal
oct('0377');  # 255 decimal
oct('377');  # 255 decimal
oct('0xDEADBEEF');  # 3_735_928_559 decimal, saw leading 0x 
oct('0b1101');  # 13 decimal, saw leading 0b
oct("0b$bits");  # convert $bits from binary




