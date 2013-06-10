Cleanlog for Sublime Text 2
============

Delete console.log's you used for testing before committing.


###Usage
Mark your logging statements for testing purposes this way:
```
console.log(theVariableToLog);//t
```
Any amount of whitespace will be acceptable, but whitespace between the slashes are not acceptable since with that it's no longer legal commentting in JavaScript.

Change the string `regexp` to clean logs for other languages.

###Making it faster
Save the provided `log.sublime-snippet` to `<Sublime folder>/Packages/JavaScript`, enable the plugin, and then add the following entry to your user key binding:
```
{
  "keys": ["alt+c"],
  "command": "cleanlog"
}
```

After saving the user key binding file, you only need to enter `log` and then press `tab`, it will auto complete to `console.log();//t`. The cursor will appear between the brackets. After entering the variable or string you want to log, pressing tab again will bring the cursor to end of the line.
