import sublime
import sublime_plugin


class ConsoleLogCommandsCommand(sublime_plugin.ApplicationCommand):

    def run(self, flag):
        sublime.log_commands(flag)


class ConsoleLogInputCommand(sublime_plugin.ApplicationCommand):

    def run(self, flag):
        sublime.log_input(flag)
