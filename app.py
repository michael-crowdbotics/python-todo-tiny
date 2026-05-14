import flet as ft
from datetime import datetime

from database import Database
from components import FormContainer, CreateTask


def main(page: ft.Page):
    """Main flet app."""
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.CrossAxisAlignment.CENTER

    def add_task_to_screen(e):
        task_created_date = datetime.now().strftime("%b %d, %Y, %H:%M ")
        db = Database()
        db.connect_to_db()

        task_value = form.text_field.value
        print(f"Task value: {task_value}, Date: {task_created_date}")

        if task_value:
            db.insert_db((task_value, task_created_date))
            db.close_db()

            __main_column__.controls.append(
                CreateTask(
                    task_value,
                    task_created_date,
                    delete_function,
                    update_function,
                )
            )
            __main_column__.update()
            create_to_do_task(e)
        else:
            db.close_db()

    def delete_function(e):
        __main_column__.controls.remove(e)
        __main_column__.update()

    def update_function(e):
        form.height, form.opacity = 200, 1
        form.text_field.value = e.task
        form.add_button.content.value = "Update"
        form.add_button.on_click = lambda _: finalize_update(e)
        form.update()

    def finalize_update(e):
        """Update task value and date."""
        e.task = form.text_field.value
        e.date = datetime.now().strftime("%b %d, %Y, %H:%M ")

        e.content.controls[0].controls[0].value = e.task
        e.content.controls[0].controls[1].value = e.date

        e.content.update()
        create_to_do_task(e)

    def create_to_do_task(e):
        if form.height != 200:
            form.height, form.opacity = 200, 1
            form.update()
        else:
            form.height, form.opacity = 80, 0
            form.text_field.value = None
            form.add_button.content.value = "Add task"
            form.add_button.on_click = lambda _: add_task_to_screen(e)
            form.update()

    __main_column__ = ft.Column(
        scroll=ft.ScrollMode.HIDDEN,
        expand=True,
        alignment=ft.MainAxisAlignment.START,
        controls=[
            ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    ft.Text(
                        "Todo List",
                        color=ft.colors.BLUE_50,
                        size=18,
                        weight=ft.FontWeight.BOLD,
                    ),
                    ft.IconButton(
                        icon=ft.icons.ADD_CIRCLE_ROUNDED,
                        icon_size=18,
                        on_click=create_to_do_task,
                    ),
                ],
            ),
            ft.Divider(
                height=8,
                color=ft.colors.WHITE24,
            ),
        ],
    )

    page.add(
        ft.Container(
            width=1500,
            height=1024,
            bgcolor=ft.colors.BLUE_GREY_900,
            margin=10,
            content=ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Container(
                        width=280,
                        height=600,
                        bgcolor="#0f0f0f",
                        border_radius=ft.border_radius.all(40),
                        border=ft.border.all(0.5, ft.colors.WHITE),
                        padding=ft.padding.only(top=35, left=20, right=20),
                        clip_behavior=ft.ClipBehavior.HARD_EDGE,
                        content=ft.Column(
                            alignment=ft.MainAxisAlignment.CENTER,
                            expand=True,
                            controls=[
                                __main_column__,
                                FormContainer(add_task_to_screen),
                            ],
                        ),
                    )
                ],
            ),
        )
    )

    page.update()
    form = page.controls[0].content.controls[0].content.controls[1]

    # Load existing tasks from the database.
    db = Database()
    db.connect_to_db()
    tasks = db.read_db()
    db.close_db()

    for task, date in tasks:
        __main_column__.controls.append(
            CreateTask(
                task,
                date,
                delete_function,
                update_function,
            )
        )
    __main_column__.update()


if __name__ == "__main__":
    ft.app(target=main, port=8000)
