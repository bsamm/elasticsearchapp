import rumps
import os

class ElasticSearchApp(object):
    def __init__(self):
        self.config = {
            "app_name": "Elastic Search App",
            "about": "About",
            "start": "Start Server",
            "stop": "Stop Server",
            "port": "View Port 9200",
            "logs": "View Logs"
        }
        self.app = rumps.App(self.config["app_name"])
        self.set_up_menu()
        self.about_button      = rumps.MenuItem(title=self.config["about"], callback=self.about_elastic_search_app)
        self.start_button      = rumps.MenuItem(title=self.config["start"], callback=self.start_elastic_search)
        self.quit_button       = rumps.MenuItem(title=self.config["stop"], callback=self.quit_elastic_search)
        self.view_port_button  = rumps.MenuItem(title=self.config["port"], callback=self.view_port_in_browser)
        self.logs_button       = rumps.MenuItem(title=self.config["logs"], callback=self.view_logs)
        self.app.menu          = [self.about_button, self.start_button, self.quit_button, self.view_port_button, self.logs_button]

    def set_up_menu(self):
        self.app.title = "ES"

    def about_elastic_search_app(self, sender):
        rumps.alert("Install elastic search services using homebrew by following the instructions here: https://www.elastic.co/guide/en/elasticsearch/reference/current/brew.html")

    def start_elastic_search(self, sender):
        os.system('brew services start elasticsearch')
        rumps.notification("Awesome title", "amazing subtitle", "hi!!1")

    def quit_elastic_search(self, sender):
        os.system('brew services stop elasticsearch')
        rumps.notification("Awesome title", "amazing subtitle", "hi!!1")

    def view_port_in_browser(self, sender):
        os.system('open http://localhost:9200/')

    def view_logs(self, sender):
        os.system('open /usr/local/var/log/elasticsearch')

    def run(self):
        self.app.run()

if __name__ == '__main__':
    app = ElasticSearchApp()
    app.run()
