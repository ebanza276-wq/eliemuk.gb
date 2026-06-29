import flet as ft
import flet_video as ftv
def creer_message(msg):
    return ft.Container(
        margin=ft.Margin.symmetric(horizontal=8, vertical=4),
        padding=10,
        border_radius=12,
        ink=True,
        # on_click=lambda e: open_message(msg["nom"]),

        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                # Partie gauche
                ft.Row(
                    spacing=12,
                    controls=[
                        ft.CircleAvatar(
                            foreground_image_src=msg["avatar"],
                            radius=26,
                        ),

                        ft.Column(
                            spacing=4,
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                ft.Text(
                                    msg["nom"],
                                    size=16,
                                    weight=ft.FontWeight.BOLD,
                                ),

                                ft.Text(
                                    msg["secondary_text"],
                                    size=13,
                                    color=ft.Colors.GREY_600,
                                    max_lines=1,
                                    overflow=ft.TextOverflow.ELLIPSIS,
                                ),
                            ],
                        ),
                    ],
                ),

                # Partie droite
                ft.Column(
                    spacing=6,
                    horizontal_alignment=ft.CrossAxisAlignment.END,
                    controls=[
                        ft.Text(
                            msg.get("heure", "12:30"),
                            size=11,
                            color=ft.Colors.GREY_500,
                        ),

                        (
                            ft.Container(
                                width=20,
                                height=20,
                                bgcolor=ft.Colors.BLUE,
                                border_radius=20,
                                alignment=ft.Alignment.CENTER,
                                content=ft.Text(
                                    str(msg["non_lus"]),
                                    size=10,
                                    color=ft.Colors.WHITE,
                                    weight=ft.FontWeight.BOLD,
                                ),
                            )
                            if msg.get("non_lus", 0) > 0
                            else ft.Container(height=20)
                        ),
                    ],
                ),
            ],
        ),
    )
col = ft.Column(scroll="auto")
search_msg = ft.TextField(
    hint_text="Rechercher une conversation...",
    prefix_icon=ft.Icons.SEARCH,
    border_radius=20,
    filled=True,
    bgcolor="#2a2a2a",
    #on_change=lambda e: filter_messages(e.control.value)
    )
def page_message(messages):
    col.controls = [
        ft.Text("❤️ Messages", size=24, weight="bold"),
        search_msg,
        ft.Divider(),
        *[creer_message(m) for m in messages]
        ]
    return ft.Container(
            alignment=ft.Alignment.TOP_CENTER,
            content=ft.Container(
                content=col
            )
        )
