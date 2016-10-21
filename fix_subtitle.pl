#!/usr/bin/perl


my $input = $ARGV[0];
print $input, "\n";

my $interval = $ARGV[1];

if (not $interval) {
	$interval = 2
}

print $interval, "\n";

my $MODE = $ARGV[2];

if (not $MODE) {
	$MODE = 1;
}

print $MODE, "\n";


# Open file to read
open(DATA1, "<$input");
#
# Open new file to write
open(DATA2, ">$input.out");
#
# # Copy data from one file to another.

my $id = 0;

while(<DATA1>)
{
	if ($MODE < 0) {

		if ($_ =~ /^600/) {
			$id = 600;
		}
		
		if ($id == 600 and $_ =~ /(\d{2}):(\d{2}):(\d{2}),(\d{3}) --> (\d{2}):(\d{2}):(\d{2}),(\d{3})/) {
			my $h1 = int($1);
			my $m1 = int($2);
			my $s1 = int($3);
			my $k1 = int($4);
			
			my $h2 = int($5);
			my $m2 = int($6);
			my $s2 = int($7);
			my $k2 = int($8);

			$s1 = $s1 - $interval;
			
			if ($s1 < 0) {
				$s1 = 0;
				$m1 = $m1 - 1;

				if ($m1 < 0) {
					$m1 = 0;
					$h1 = $h1 - 1;

					if ($h1 < 0) {
						$h1 = 0;
					}
				}
			}

			$s2 = $s2 - $interval;
			
			if ($s2 < 0) {
				$s2 = 0;
				$m2 = $m2 - 1;

				if ($m2 < 0) {
					$m2 = 0;
					$h2 = $h2 - 1;

					if ($h2 < 0) {
						$h2 = 0;
					}
				}
			}

			my $timeline = sprintf("%02d:%02d:%02d,%03d --> %02d:%02d:%02d,%03d", $h1, $m1, $s1, $k1, $h2, $m2, $s2, $k2);
			print DATA2 "$timeline\r\n";
		} else {
			print DATA2 $_;
		}

	} else {

		if ($_ =~ /(\d{2}):(\d{2}):(\d{2}),(\d{3}) --> (\d{2}):(\d{2}):(\d{2}),(\d{3})/) {
			my $h1 = int($1);
			my $m1 = int($2);
			my $s1 = int($3);
			my $k1 = int($4);
			
			my $h2 = int($5);
			my $m2 = int($6);
			my $s2 = int($7);
			my $k2 = int($8);

			$s1 = $s1 + 2;
			my $r1 = $s1 / 60;
			$s1 = $s1 % 60;	
			$m1 = $m1 + $r1;
			$r1 = $m1 / 60;
			$m1 = $m1 % 60;
			$h1 = $h1 + $r1;

			$s2 = $s2 + 2;
			my $r2 = $s2 / 60;
			$s2 = $s2 % 60;
			$m2 = $m2 + $r2;
			$r2 = $m2 / 60;
			$m2 = $m2 % 60;
			$h2 = $h2 + $r2;

			my $timeline = sprintf("%02d:%02d:%02d,%03d --> %02d:%02d:%02d,%03d", $h1, $m1, $s1, $k1, $h2, $m2, $s2, $k2);
			print DATA2 "$timeline\r\n";
		} else {
			print DATA2 $_;
		}
	}
}
close( DATA1 );
close( DATA2 );
