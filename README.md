# Quadratic Equation for the TI-Nspire calculator (ARCHIVED)


### History
I never realy liked school work, and prefered computers to book work.
For some fun I created this app for my graphical caculator while in math class.
My teacher did tell me that I would be unable to use this in the exam (yr 10) or Year 12 Final Exam.
I didn't really care, I couldn't be bothered writing out all the workings and indvidully caculating the information,
So I created this app to display the workings and annswer in one nice neat package.

All you required to do was to place in the a, b and c values and it would work out the rest.


ie.

quad_equ(1,2,0);
+-x = (sqrt(b^2-4ac)/2a

### NOTE:
I haven't used a TI-Nspire calculator since I fnished school, and have no idea if this will work with the new TI caculators.

This is for archival purposes.

### V2 (Python remake):
If you wish to use the `quad.py` file you will require to have `sympy` installed.

You can do this by

`pip install --user sympy`


Then use the format of
` python quad.py <a> <b> <c> `

or import the module into another python program and use either of the two functions

`solve_quad(a,b,c)`
 ** which will return the x values as `{'x1':x_1,'x2':x_2}` **

`print_quad(a,b,c)`
 ** which will show the workings for the maths the same as running the program from the cli **


#### Python Note:

If the equation never passes the x axis the value will contain `j` and be an imaginary number.
I will look at getting this working with ignoring imaginary numbers, and showing an error
