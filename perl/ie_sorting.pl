#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=3:
#   }}}1
#	{{{2

#	the sort subroutine doesn’t need to sort many items after all. It merely has to be able to compare two items. If it can put two items in the proper order, Perl will be able to tell (by repeatedly consulting the sort subroutine) what order you want for your data.
#

#	A sort function has $a, $b implicitly declared, and must return how these items compare.
#	using a conventional function
sub by_number {
	if ($a < $b) { -1 } elsif ($a > $b) { 1 } else { 0 } 
}
#	or in a compact format:
sub by_number { $a <=> $b }

#		<=>		Compares numbers
#		cmp		Comapres strings
#	The default sort uses cmp
my @some_numbers = ( 1..10 );
my @result = sort by_number @some_numbers;

#	An alternative format:
my @result = sort { $a <=> $b } @some_numbers;

#	Normalising unicode
#>%		use Unicode::Normalize;
#>%		sub equivalents { NFKD($a) cmp NFKD($b) }

#	Reversing order
my @result = reverse sort { $a <=> $b } @some_numbers;
my @result = sort { $b <=> $a } @some_numbers;


#	Sorting a hash by value
my %score = ("barney" => 195, "fred" => 205, "dino" => 30); 
sub by_score { $score{$b} <=> $score{$a} }
my @winners = sort by_score keys %score;
print "winners=(@winners)\n";
print "\n";

#	Sorting by multiple keys
my %score = ( "barney" => 195, "fred" => 205, "dino" => 30, "bamm-bamm" => 195, );
sub by_score_and_name { $score{$b} <=> $score{$a} or $a cmp $b }  # use short-circuting to specify multiple conditions
my @winners = sort by_score_and_name keys %score;
print "winners=(@winners)\n";
print "\n";

#	5-level sort example
#>%		@patron_IDs = sort {
#>%			&fines($b) <=> &fines($a) or
#>%			$items{$b} <=> $items{$a} or 
#>%			$family_name{$a} cmp $family_name{$b} or 
#>%			$personal_name{$a} cmp $family_name{$b} or 
#>%			$a <=> $b
#>%		} @patron_IDs;

#	}}}1
