#!/usr/bin/env ruby

# Check if there is a command-line argument
if ARGV.empty?
  puts "Usage: #{$PROGRAM_NAME} <input_string>"
  exit 1
end

# Get the input string from the command-line argument
input_string = ARGV[0]

# Define the regular expression to match "School"
pattern = /School/

# Use the match method to find "School" in the input string
match = input_string.match(pattern)

# Check if a match was found
if match
  # Print the matched string followed by a newline
  puts "#{match[0]}"
else
  # If no match was found, print just a newline
  puts ""
end
