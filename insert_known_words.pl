#!/usr/bin/perl

use DBI;
use strict;
use warnings;

my $file = $ARGV[0];
my $fd;
open($fd, "<", $file);
my $fdw;
open($fdw, ">", "insert_known_words_log.txt");

my $driver   = "SQLite";
my $database = "jpvocab.db";
my $dsn = "DBI:$driver:dbname=$database";
my $userid = "";
my $password = "";
my $dbh = DBI->connect($dsn, $userid, $password, { RaiseError => 1 }) or die $DBI::errstr;
print "Opened database successfully\n";
my $line = "";

while (<$fd>) {
	$line = $_;
	$_ =~ /(.*)\t(.*)\t(.*)/;
	my $stmt = qq(INSERT INTO leveln2 VALUES (NULL, '$1', '$2', '$3', '', '', 100));
	
	eval {
		$dbh->do($stmt);
	};
	if ($@) {
		my $update = qq(UPDATE leveln2 SET hit = 100 WHERE kanji = '$1' AND hit < 3);
		my $ret = $dbh->do($update);
		
		if ($ret == 1) {
			print "$1\n";
			print $fdw "$1\r\n";
		}
	}
}

$dbh->disconnect();
close($fd);
close($fdw);
