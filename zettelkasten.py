import sublime
import sublime_plugin
import os
import datetime

def getPath():
    s = sublime.load_settings("Zettelkasten.sublime-settings")
    save_path = s.get("save_path", "~/Documents/notes")
    save_path = os.path.expanduser(save_path)
    return save_path

def getExtension():
    s = sublime.load_settings("Zettelkasten.sublime-settings")
    save_extension = s.get("extension", ".md")
    return save_extension

class TitleHandler(sublime_plugin.TextInputHandler):
    @staticmethod
    def placeholder():
        return "Title"

    @staticmethod
    def confirm(text):
        return text

class ZettelkastenCommand(sublime_plugin.WindowCommand):
    def run(self, title_handler):
        save_path = getPath()
        save_extension = getExtension()
        try:
            os.mkdir(getPath())
        except OSError:
            pass

        now = datetime.datetime.now()
        date = now.strftime("%Y-%m-%d-%H%M")
        title = title_handler.lower().replace(' ', '-')
        filename = save_path + "/" + date + '-' + title + save_extension

        self.window.open_file(filename)

    @staticmethod        
    def input(args):
        return TitleHandler()
        