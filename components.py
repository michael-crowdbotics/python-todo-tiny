import flet as ft


class FormContainer(ft.Container):
    """Create form for creating new task."""

    def __init__(self, func):
        self.func = func
        super().__init__()

        self.text_field = ft.TextField(
            label="New task",
            height=58,
            width=255,
            color=ft.colors.BLACK,
            border_color=ft.colors.BLUE_GREY_100,
            hint_style=ft.TextStyle(color=ft.colors.BLUE_GREY_100, size=12),
        )

        self.add_button = ft.IconButton(
            content=ft.Text("Add task"),
            width=180,
            height=44,
            on_click=self.func,
            style=ft.ButtonStyle(
                color=ft.colors.BLACK12,
                bgcolor={"": ft.colors.BLACK},
                shape={"": ft.RoundedRectangleBorder(radius=8)},
            ),
        )

        self.form_column = ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[self.text_field, self.add_button],
        )

        self.content = self.form_column
        self.width = 280
        self.height = 80
        self.bgcolor = ft.colors.BLUE_GREY_500
        self.opacity = 0
        self.border_radius = ft.border_radius.all(40)
        self.margin = ft.margin.only(left=-20, right=-20)
        self.animate = ft.animation.Animation(400, ft.AnimationCurve.DECELERATE)
        self.animate_opacity = 200
        self.padding = ft.padding.only(top=45, bottom=45)


class CreateTask(ft.Container):
    """Class to create new task by user."""

    def __init__(self, task: str, date: str, func1, func2):
        self.task = task
        self.date = date
        self.func1 = func1
        self.func2 = func2
        super().__init__()

        self.width = 280
        self.height = 64
        self.border = ft.border.all(0.85, ft.colors.WHITE54)
        self.border_radius = ft.border_radius.all(8)
        self.on_hover = self.hover_show_icon
        self.clip_behavior = ft.ClipBehavior.HARD_EDGE
        self.padding = ft.padding.all(10)
        self.content = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.Column(
                    spacing=1,
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Text(value=self.task, size=12),
                        ft.Text(value=self.date, size=9, color=ft.colors.WHITE54),
                    ],
                ),
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=0,
                    controls=[
                        self.task_delete_edit(ft.icons.DELETE_ROUNDED, ft.colors.RED_500, self.func1),
                        self.task_delete_edit(ft.icons.EDIT_ROUNDED, ft.colors.WHITE70, self.func2),
                    ],
                ),
            ],
        )

    def task_delete_edit(self, name: str, color: str, func):
        return ft.IconButton(
            icon=name,
            icon_size=18,
            icon_color=color,
            opacity=0,
            animate_opacity=200,
            on_click=lambda e: func(self),
        )

    def hover_show_icon(self, e):
        """Show icon while hovering over task."""
        if e.data == "true":
            e.control.content.controls[1].controls[0].opacity = 1
            e.control.content.controls[1].controls[1].opacity = 1
            e.control.content.update()
        else:
            e.control.content.controls[1].controls[0].opacity = 0
            e.control.content.controls[1].controls[1].opacity = 0
            e.control.content.update()
