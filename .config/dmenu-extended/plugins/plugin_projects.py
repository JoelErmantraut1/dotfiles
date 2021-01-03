import dmenu_extended
import sys
import os

file_prefs = dmenu_extended.path_prefs + '/dmenu_projects.json'

class extension(dmenu_extended.dmenu):

    title = 'Projects'
    is_submenu = True


    def create_projects_menu(self):
        default = { 'Open Home': {'type': 'Directory', 'commands': ['exo-open /home'] } }
        self.save_json(file_prefs, default)
        return default


    def load_projects(self):
        prjs = self.load_json(file_prefs)
        if prjs == False:
            prjs = self.create_projects_menu()
        return prjs


    def run(self, inputText):
        """
        Each project has:

        1. a name (displayed by dmenu, the key of the dict)
        2. a type (optional, displayed by dmenu)
        3. commands (list of commands that will be executed if selected)
        """
        data = self.load_projects()

        items, commands = [], []

        for prj in data:
            if 'commands' not in data[prj]:
                continue
            line = prj.ljust(40) + data[prj].get('type', '')
            items.append(line)
            commands.append(data[prj]['commands'])

        item_editPrefs = self.prefs['indicator_edit'] + ' Edit projects'
        items.append(item_editPrefs)

        project = self.menu(items, prompt='Select project: ')
        try:
            ix = items.index(project)
        except:
            ix = -1

        if project == item_editPrefs:
            self.open_file(file_prefs)
        elif project == '' or ix == -1:
            sys.exit()
        else:
            for c in commands[ix]:
                self.execute(c)

