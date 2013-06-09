kill-testlog
============

Delete console.log's you used for testing before committing.


###Usage
Mark your logging statements for testing purposes this way:
```
console.log(theVariableToLog);//t
```
Any amount of whitespace will be acceptable, but whitespace between the slashes are not acceptable since with that it's no longer legal commentting in JavaScript.

Change the string in `regexp` to clean logs for other languages.
