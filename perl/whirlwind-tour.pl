#!/usr/bin/perl

@lines = `perldoc -u -f atan2`; 
foreach (@lines) {
	s/\w<([^>]+)>/\U$1/g;
	print; 
}

#	This is equivelent to:
#		@lines = `perldoc -u -f atan2`; 
#		foreach (@lines) {
#			$_ =~ s/\w<([^>]+)>/\U$1/g;
#			print $_; 
#		}
