#!/usr/bin/env perl
use strict;
use warnings;

# Print a welcome message
print "Hello, World!\n";

# Ask for the user's name
print "Please enter your name: ";
my $name = <STDIN>;
chomp($name); # Remove the trailing newline character

# Greet the user conditionally
if ($name eq "") {
    print "Hello, stranger!\n";
} else {
    print "Nice to meet you, $name!\n";
}

# Simple loop example
print "\nCounting to 3:\n";
foreach my $i (1..3) {
    print "Count: $i\n";
}
