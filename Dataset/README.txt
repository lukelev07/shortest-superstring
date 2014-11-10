This contains data you can use to test your DNA assembly program.
The file format is described in the HW9 assignment.

reads1.txt, reads6.txt are a very easy warmup you can use to test your code.
reads2.txt, reads7.txt are an easy case.
reads3.txt, reads8.txt are a slightly harder case.
reads4.txt, reads5.txt, reads9.txt, reads10.txt are standard size cases.
reads11.txt, reads14.txt are slightly harder cases.
reads12.txt, .., reads16.txt are extra-hard cases.

answer1.txt, ..., answer5.txt are the correct answer for
reads1.txt, ..., reads5.txt.

We expect you to handle all of reads1.txt-reads11.txt
and reads14.txt.  For full credit, make sure your program
can handle all of reads{1-11,14}.txt.  For an extra challenge,
try handling reads{12,13,15,16}.txt -- we may award a few
extra points for a correct answer to those.

This is the final and complete data set.

We have also provided a script to make it easy to run your program.
If your program can be executed with, say, 'python code/assemble.py',
then you can run './runall python code/assemble.py' on the Unix
command line, and it will run your program on all of the inputs,
save its output to the appropriate files (output1-16.txt), and
compare your output1-5.txt to the known-good answer1-5.txt.
Note that this will likely only work on Unix.
