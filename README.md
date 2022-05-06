# GodWords
CSCI3200 Final Project by Sinuo Liu

This is basically a extension of the r2p.py file from canvas.
This language is basically writting sign operators looks like English which we are using normally.

This language will translate into code which could be executed in Python.

The language is consisted of two parts: "I", and other "Gods". 
"I" can define variables, print variables without any other expressions such as if or while.
e.g.:
<code>I define x to be 45.</code>
"Other Gods" have each roles within the language.
|Name|Function|Example|
|---|---|---|
|Oschon|if statement and else statement|Oschon says: if y is greater than x, then <br /> &nbsp;{expression} <br /> Thal says end. <br /> <br /> Oschon then says: if not, <br /> &nbsp;{expression} <br /> Thal says end.|
|Nal|while statement|Nal says: while n is not identical to y, <br /> &nbsp;{expression} <br /> Thal says end.|
|Thal|end the statement| This will add to the end of all statements. See above examples|

The language also support add and subtract operations. But currently it only support a number with a variable or variable with a variable, you can't assign a calculation directly to a variable. (you can't do x = 1+2).
|calculation|Formate|
|---|---|
|x = x + 1| I add 1 to x.|
|x = x - 1| I remove 1 from x|

Usually if/else/while statement only accept one expression within it. But if you want to add more expression, you need to add "Also, " in front of the second and further expressions.
|Code|Example|
|---|---|
|if (a<b): <br /> &nbsp;b=b-1 <br /> &nbsp;a=a+1<br />|Oschon says: if a is greater than b, then,<br /> &nbsp;I remove 1 from b.<br /> &nbsp;Also, I add 1 to a.<br />Thal says end.|

Currently operators only have:
|operator|Formate|
|---|---|
|x > y |x is greater than y|
|x < y |x is less than y|
|x >= y|x is greater or equal to y|
|x <= y|x is less or equal to y|
|x == y|x is identical to y|
|x != y|x is not identical to y|
