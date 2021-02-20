#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=3:
#   }}}1
use strict; 
use warnings;
no warnings 'shadow';
use feature qw(say);
#	{{{2

#	Reading and chomp (stripping) a line from standard input
#>%		$line = <STDIN>;
#>%		chomp($line);
#	or
#		chomp($line = <STDIN>);

#	Iterate over lines from STDIN
#>%		while (defined($line = <STDIN>)) {
#>%			print "$line";
#>%		}
#	or
#>%		while (<STDIN>) {
#>%			print "$_";
#>%		}
#	If you put anything else into the conditional expression, this shortcut won't apply

#	Input from the Diamond Operator '<>'
#		The diamond operator is actually a special kind of line-input operator. But instead of getting the input from the keyboard, it comes from the user’s choice of input
#		So, if you run this program with the invocation arguments fred, barney, and betty, it will say something like: It was [a line from file fred] that I saw!, It was [another line from file fred] that I saw!, on and on until it reaches the end of file fred. Then, it will automatically go on to file barney, printing out one line after another, and then on through file betty. Note that there’s no break when you go from one file to another; when you use the diamond, it’s as if the input files have been merged into one big file.
#		Since you generally use the diamond operator to process all of the input, it’s typically a mistake to use it in more than one place in your program.
#		The diamond will return undef (and we’ll drop out of the while loop) only at the end of all of the input.
#	usage:
#>%		while (<>) {
#>%			chomp;
#>%			print "$_";
#>%		}
#	or
#>%		while (defined($line = <>)) {
#>%			chomp($line);
#>%			print "$line";
#>%		}
#	Ongoing: 2021-02-20T22:06:06AEDT distinguishing arguments from files with <>

#	@ARGV	Invocation Arguments
#		array containing invocation arguments for script.


#	Output to standard output
#		The print operator takes a list of values and sends each item (as a string, of course) to standard output in turn, one after another.
my $name = "Larry Wall";
print "Hello there, $name, did you know that 3+4 is ", 3+4, "?\n";
print "\n";

my @array = qw/ fred barney betty /;
#$, = ":";  # default = ''
say @array;
#$" = ",";  # default = ' '
say "@array";
print "\n";

#	Enable autoflush
#>%		$|++;
#	or 
#>%		BEGIN{ $| = 1; }


#	Formatted output with printf
printf("%g %g %g\n", 5/2, 51/17, 51 ** 17);  # 2.5 3 1.0683e+29
printf "in %d days!\n", 17.85;  # in 17 days!
print "\n";

#	arrays and printf
#		Generally, you won’t use an array as an argument to printf. That’s because an array may hold any number of items, and a given format string will work with only a certain fixed number of items.
my @items = qw( wilma dino pebbles );
my $format = "The items are:\n" . ("%10s\n" x @items); 
printf $format, @items;  # print "the format is >>$format<<\n"; # for debugging 
#	or
printf "The items are:\n".("%10s\n" x @items), @items;
print "\n";

#	Filehandles
#		A filehandle is the name in a Perl program for an I/O connection between your Perl process and the outside world. That is, it’s the name of a connection, not necessarily the name of a file.
#		System filehandle names: STDIN, STDOUT, STDERR, DATA, ARGV, and ARGVOUT
#	Opening a filehandle
#>%		open CONFIG, 'dino'; 
#>%		open CONFIG, '<dino'; 
#>%		open BEDROCK, '>fred'; 
#>%		open LOG, '>>logfile';
#	In modern versions of Perl (starting with Perl 5.6), you can use a “three-argument” open:
#>%		open CONFIG, '<', 'dino';
#>%		open BEDROCK, '>', $file_name; 
#>%		open LOG, '>>', &logfile_name();
#	If you know that your input file is UTF-8, you can specify that by putting a colon after the file mode and naming the encoding:
#>%		open CONFIG, '<:encoding(UTF-8)', 'dino';

#	Perl ignores any leading whitespace in a file name. See perlfunc and perlopentut 

#	Get list of all supported encodings
#>%		perl -MEncode -le "print for Encode->encodings(':all')"

#	Support CR-LF (windows) encoding
#>%		open BEDROCK, '>:crlf', $file_name;
#>%		open BEDROCK, '<:crlf', $file_name;

#	Binmoding Filehandles
#		In older Perls, if you didn’t want to translate line endings, such as a random value in a binary file that happens to have the same ordinal value as the newline, you used binmode to turn off line ending processing
#>%		binmode STDOUT;  # don't translate line endings 
#>%		binmode STDERR;  # don't translate line endings
#	If you want to output Unicode to STDOUT, you want to ensure that STDOUT knows how to handle what it gets:
#>%		binmode STDOUT, ':encoding(UTF-8)';

#	Close a filehandle
#		Perl automatically closes a filehandle if you reopen it (that is, if you reuse the filehandle name in a new open) or if you exit the program.
#		Good pratice is having a call to close() for each call to open()
#>%		close BEDROCK;

#	Bad Filehandles
#		If you try to read from a bad filehandle (that is, a filehandle that isn’t properly open or a closed network connection), you’ll see an immediate end-of-file.

#	Fatal errors with die
#		where $! is the error message/code
#>%		die "error message $!";

#	autodie
#		When a system call fails, autodie invokes die
#>%		use autodie;

#>%		if ( ! open PASSWD, "/etc/passwd") {
#>%			die "How did you get logged in? ($!)"; 
#>%		}
#>%		while (<PASSWD>) { 
#>%			chomp;
#>%			... 
#>%		}

#	Changing default output filehandle
#		by default, print/printf output to stdout
#	Select a default filehandle with:
#>%		select BEDROCK;

#	if one of the three system filehandles STDIN, STDOUT, or STDERR— fails to reopen, Perl kindly restores the original one.

#	say()
use feature qw(say);
say "Hello";  # say includes a trailing newline, which print does not 


#	Filehandle in a Scalar
#	Since Perl 5.6, you can create a filehandle in a scalar variable so you don’t have to use a bareword.
#	Input fh
#>%		my $rocks_fh;
#>%		open $rocks_fh, '<', 'rocks.txt' or die "Could not open rocks.txt: $!";
#	or
#>%		open my $rocks_fh, '<', 'rocks.txt' or die "Could not open rocks.txt: $!";
#	Output fh
#	The '{} around the filehandle are not (always) required, but serve to make clear to python that $rocks_fh is a filehandle
#	Note there is no ',' between rocks_fh and rock in the function usage of say (which would be) 'say( $rocks_fh $rock )'
#>%		open my $rocks_fh, '>>', 'rocks.txt' or die "Could not open rocks.txt: $!";
#>%		foreach my $rock ( qw( slate lava granite ) ) {
#>%			say { $rocks_fh } $rock 
#>%		}

#	}}}1
