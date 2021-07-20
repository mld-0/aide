
#	The diamond operator, <>, will read line-by-line files specified by @ARGV, or stdin if no files are specified

#	@ARGV can be manipulated, doing so will change which files are read by <>:
#@ARGV = ( '-', 'input-one.txt', 'input-two.txt' );

print "ARGV=(@ARGV)\n";

while (<>) {
	#	Print the current filename ($ARGV), current line number ($.), and current line ($_).
	print "$ARGV, $., $_";
} continue {
	#	closing each file upon eof gives us the correct line number for each file:
	close ARGV if eof;
}

