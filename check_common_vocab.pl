#!/usr/bin/perl

use DBI;
use strict;
use warnings;

my $fdw;
open($fdw, ">", "update_leveln2_log.txt");

my $driver   = "SQLite";
my $database = "jpvocab.db";
my $dsn = "DBI:$driver:dbname=$database";
my $userid = "";
my $password = "";
my $dbh = DBI->connect($dsn, $userid, $password, { PrintError => 0, RaiseError => 1 }) or die $DBI::errstr;
print "Opened database successfully\n";

my $select = qq(SELECT id FROM leveln2 WHERE hit >=3);
my $sth = $dbh->prepare($select);
my $rv = $sth->execute() or die $DBI::errstr;

if($rv < 0){
	print $DBI::errstr;
}

my $count = 0;
while (my @row = $sth->fetchrow_array()) {
	my $id = $row[0];
	eval {
		my $ret = $dbh->do(qq(INSERT INTO common_vocab VALUES (NULL, $id, 2)));
		print $id, "\n";
	};
	if ($@) {
		$count++;
	}
}

print "Checked: $count\n";

$dbh->disconnect();
print "Closed database successfully\n";
close($fdw);
