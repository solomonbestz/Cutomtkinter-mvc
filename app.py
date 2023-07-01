from model import Model
from view import TodoApp
from controller import Controller


def main() -> None:
    app_model = Model()
    app_view = TodoApp(app_model)
    app_controller = Controller(app_model, app_view)
    app_controller.run()


if __name__=='__main__':
    main()