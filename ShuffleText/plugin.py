import sublime, sublime_plugin, random

class ShuffleSelectionCommand(sublime_plugin.TextCommand):
    '''
        Extremely basic plugin to answer SO question:
        https://stackoverflow.com/questions/28966185/reverse-all-line-of-text-in-sublime-text
    '''
    def run(self, edit):
        for region in self.view.sel():
            stringContents = self.view.substr(region)
            self.view.replace(edit, region, ''.join(random.sample(stringContents,len(stringContents))))