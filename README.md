# GodWords
CSCI3200 Final Project by Sinuo Liu

This is basically a extension of the r2p.py file from canvas.
This language is basically writting sign operators looks like English which we are using normally.

The language is consisted of two parts: "I", and other "Gods". 
"I" can define variables, print variables without any other expressions such as if or while.
"Other Gods" have each roles within the language.
|Name|Function|
|---|---|
|Oschon|if statement and else statement|
|Nal|while statement|
|Thal|end the statement|

The language also support add and subtract operations. But currently it only support a number with a variable or variable with a variable, you can't assign a calculation directly to a variable. (you can't do x = 1+2).
|calculation|Formate|
|---|---|
|x + 1| I add 1 to x.|
|x - 1| I remove 1 from x|

Currently operators only have:
|operator|Formate|
|---|---|
|x > y |x is greater than y|
|x < y |x is less than y|
|x >= y|x is greater or equal to y|
|x <= y|x is less or equal to y|
|x == y|x is identical to y|
|x != y|x is not identical to y|

Currently I want to try to implement an else statement, but the program always say errors.
