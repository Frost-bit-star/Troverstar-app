from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy_garden.webview import WebView
import urllib.request


class SplashScreen(Screen):
    def __init__(self, **kwargs):
        super(SplashScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=10, padding=20)
        self.img = Image(source='splash.jpeg')
        self.status = Label(text="Loading...", font_size='18sp')
        self.retry_btn = Button(text="Retry", size_hint=(None, None), size=(200, 50))
        self.retry_btn.bind(on_press=self.check_connection)
        self.retry_btn.opacity = 0

        layout.add_widget(self.img)
        layout.add_widget(self.status)
        layout.add_widget(self.retry_btn)
        self.add_widget(layout)

        Clock.schedule_once(lambda dt: self.check_connection(), 2)

    def check_connection(self, *args):
        self.status.text = "Checking internet connection..."
        self.retry_btn.opacity = 0
        try:
            urllib.request.urlopen('https://www.google.com', timeout=5)
            self.manager.current = 'web'
        except Exception:
            self.status.text = "No internet connection."
            self.retry_btn.opacity = 1


class WebScreen(Screen):
    def __init__(self, **kwargs):
        super(WebScreen, self).__init__(**kwargs)
        web = WebView(url="https://trover.42web.io/app.php")
        self.add_widget(web)


class TroverApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(SplashScreen(name='splash'))
        sm.add_widget(WebScreen(name='web'))
        return sm


if __name__ == '__main__':
    TroverApp().run()
