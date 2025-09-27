import abc


class Button(abc.ABC):
    @abc.abstractmethod
    def render(self): ...

    def on_click(self):
        print("CLICK")


class WindowsButton(Button):
    def render(self):
        return "<xml><button></xml>"


class HtmlButton(Button):
    def render(self):
        return "<button>Кнопка</button>"


class AbstractDialogFactory(abc.ABC):
    def render(self):
        btn = self.create_button()
        code = btn.render()
        print(code)
        btn.on_click()

    @abc.abstractmethod
    def create_button(self) -> Button: ...


class WindowsDialogFactory(AbstractDialogFactory):
    def create_button(self) -> Button:
        return WindowsButton()


class HtmlDialogFactory(AbstractDialogFactory):
    def create_button(self) -> Button:
        return HtmlButton()


if __name__ == '__main__':
    window = WindowsDialogFactory()
    window.render()

    html = HtmlDialogFactory()
    html.render()

