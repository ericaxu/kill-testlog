import sublime, sublime_plugin

class CleanlogCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		regexp = '^\s*c\s*o\s*n\s*s\s*o\s*l\s*e\s*.\s*l\s*o\s*g\s*\(.*\)\s*;\s*/\s*/\s*t\s*\n'
		regions = self.view.find_all(regexp)
		while regions :
			print(regions[0])
			self.view.erase(edit, regions[0])
			regions = self.view.find_all(regexp)
