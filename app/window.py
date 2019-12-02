from kivy.app import App
from kivy.config import Config, ConfigParser
import scenes.gamescene
import scenes.menuscene
import scenes.settingsscene

from scenes.settingsscene import SettingsScene

Config.set('modules', 'monitor', '') #FPS meter


class Window(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.use_kivy_settings = False
        self.settings_scene = SettingsScene()

    def build_config(self, config):
        config.setdefaults("General", {'width': 768, 'height': 1024})

    def build_settings(self, settings):
        user_config = ConfigParser()
        user_config.read('window.ini')
        settings.add_json_panel("Settings", user_config, data=self.settings_scene.json_settings)

    def on_config_change(self, config, section, key, value):
        self.settings_scene.update_changes(key, value)
        value = 6
        print(value)


if __name__ == '__main__':
    w = Window()
    w.run()
