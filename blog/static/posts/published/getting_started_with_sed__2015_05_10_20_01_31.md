<!-- 
title: Getting Started with Sed, or How I learned to Stop Worrying and Start Typing 's///g' All the Time 
author: alex
short_text: Sed is a very useful tool.
-->

<a href="" class="link-wrap"><h1>Getting Started with Sed, or How I Learned to Stop Worrying and Start Typing sed 's///g' All the Time</h1></a>

<h2></h2>

Sed is a stream editor that lets you specify a pattern in the Regular Expression language and do replacements and other manipulations on text that matches that pattern.

an example:

	user@host:~ $ echo 1 | sed s/1/2/
	2

1 wasn't sent to stdout, it was piped into the standard input stream that sed has open. From there, sed used the Regular Expression language to yield matches. 1 was matched and replaced with 2. This is the basic structure in the substitution command: 

	sed s/<PATTERN TO MATCH>/<REPLACEMENT PATTERN>/ 

Note that you need to quote any arguments you give to sed that contain special characters, such as `-` and `*` and `.` and `;` and `+` and `?` and so on. The following would produce an error:

	sed s/one-two/two-three/g < sed_practice.txt

Okay, how about a file-renaming example:


	## adjust some filenames in an image directory
	## FLAGS = [-i]
	## TARGET = <TARGET PATTERN>
	## REPLACEMENT = <TARGET PATTERN>
	## this 'parsing method' is just a stub, do not use
	
	FLAGS=$1
	TARGET=$2
	REPLACEMENT=$3

	if [ "FLAGS" -eq "-i" ]
	  then
	    METHOD=mv
	  else
	    METHOD=cp
	fi

	for i in *;
	  do $METHOD $i $(echo $i | sed s/$TARGET/$REPLACEMENT/)
	done

