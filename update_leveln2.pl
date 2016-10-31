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
my $dbh = DBI->connect($dsn, $userid, $password, { RaiseError => 1 }) or die $DBI::errstr;
print "Opened database successfully\n";

my $select = qq(SELECT vocab_id FROM common_vocab WHERE studied = 2);
my $sth = $dbh->prepare($select);
my $rv = $sth->execute() or die $DBI::errstr;

if($rv < 0){
	print $DBI::errstr;
}

while (my @row = $sth->fetchrow_array()) {
	my $vocab_id = $row[0];
	eval {
		my $ret = $dbh->do(qq(UPDATE leveln2 SET hit = 3 WHERE id = $vocab_id AND hit = 100));
		if ($ret == 1) {
			print $vocab_id, "\n";
		}
	};
	if ($@) {
		print $fdw "$vocab_id\n";
	}	
}


$dbh->disconnect();
close($fdw);
