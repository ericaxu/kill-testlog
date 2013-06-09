import sublime, sublime_plugin

class CleanlogCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		regions = self.view.find_all('^\s*console.log\(.*\);//t\n')
		while regions :
			print(regions[0])
			self.view.erase(edit, regions[0])
			regions = self.view.find_all('^\s*console.log\(.*\);//t\n')
