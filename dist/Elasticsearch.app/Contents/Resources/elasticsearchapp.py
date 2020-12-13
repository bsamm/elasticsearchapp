import rumps
import os

class ElasticSearchApp(object):
    def __init__(self):
        self.config = {
            "app_name": "Elastic Search App",
            "about": "About",
            "start": "Start Server",
            "stop": "Stop Server",
            "port": "Open Port 9200",
            "logs": "Open Logs Directory"
        }
        self.app = rumps.App(self.config["app_name"])
        self.set_up_menu()
        self.start_button      = rumps.MenuItem(title=self.config["start"], callback=self.start_elastic_search)
        self.stop_button       = rumps.MenuItem(title=self.config["stop"], callback=self.stop_elastic_search)
        self.view_port_button  = rumps.MenuItem(title=self.config["port"], callback=self.view_port_in_browser)
        self.logs_button       = rumps.MenuItem(title=self.config["logs"], callback=self.view_logs)
        self.about_button      = rumps.MenuItem(title=self.config["about"], callback=self.about_elastic_search_app)
        self.app.menu          = [self.start_button, self.stop_button, self.view_port_button, self.logs_button, self.about_button]
        self.check_status_of_elastic_search()

    def set_up_menu(self):
        self.app.icon = "./icon-white.png"

    def start_elastic_search(self, sender):
        os.system('brew services start elasticsearch')
        self.check_status_of_elastic_search()

    def stop_elastic_search(self, sender):
        os.system('brew services stop elasticsearch')
        self.check_status_of_elastic_search()

    def check_status_of_elastic_search(self):
        if 'stopped' in os.popen('brew services list | grep elasticsearch').read():
            self.stop_button.set_callback(None)
            self.view_port_button.set_callback(None)
            self.start_button.set_callback(self.start_elastic_search)
        else:
            self.start_button.set_callback(None)
            self.stop_button.set_callback(self.stop_elastic_search)
            self.view_port_button.set_callback(self.view_port_in_browser)

    def view_port_in_browser(self, sender):
        os.system('open http://localhost:9200/')

    def view_logs(self, sender):
        os.system('open /usr/local/var/log/elasticsearch')

    def about_elastic_search_app(self, sender):
        rumps.alert("Install elastic search services using homebrew by following the instructions here: https://www.elastic.co/guide/en/elasticsearch/reference/current/brew.html")

    def run(self):
        self.app.run()

if __name__ == '__main__':
    app = ElasticSearchApp()
    app.run()
