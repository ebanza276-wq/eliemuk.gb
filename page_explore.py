import flet as ft
import flet_video as ftv
def item_recent(user):
    return ft.Container(
        padding=12,
        border_radius=12,
        bgcolor="#1E1E1E",
        content=ft.Row(
            controls=[
                ft.CircleAvatar(
                    radius=22,
                    foreground_image_src=user["avatar"],
                ),

                ft.Column(
                    spacing=2,
                    expand=True,
                    controls=[
                        ft.Text(
                            user["nom"],
                            color="white",
                            weight=ft.FontWeight.W_600,
                        ),
                        ft.Text(
                            f"@{user['username']}",
                            color="grey",
                            size=12,
                        ),
                    ],
                ),

                ft.Icon(
                    ft.Icons.CHEVRON_RIGHT,
                    color="grey",
                ),
            ],
        ),
    )
def view_decouvrir(recommandes_data,decouvrir_data):
    def creator_card(c):
        return ft.Container(
            width=185,
            height=320,
            border_radius=24,
            clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
            border=ft.Border.all(1, "#2A2A2A"),
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color="#00000060",
            ),
            content=ft.Stack(
                controls=[
                    ft.Image(
                        src=c["cover"],
                        fit="cover",
                        expand=True,
                    ),

                    ft.Container(
                        gradient=ft.LinearGradient(
                            begin=ft.Alignment.TOP_CENTER,
                            end=ft.Alignment.BOTTOM_CENTER,
                            colors=[
                                ft.Colors.TRANSPARENT,
                                "#000000DD",
                            ],
                        )
                    ),

                    ft.Container(
                        padding=15,
                        alignment=ft.Alignment.BOTTOM_LEFT,
                        content=ft.Column(
                            alignment=ft.MainAxisAlignment.END,
                            spacing=8,
                            controls=[

                                ft.Row(
                                    spacing=8,
                                    controls=[
                                        ft.Stack(
                                            controls=[
                                                ft.CircleAvatar(
                                                    foreground_image_src=c["avatar"],
                                                    radius=18,
                                                ),
                                                ft.Container(
                                                    width=10,
                                                    height=10,
                                                    bgcolor="#00FF66",
                                                    border_radius=10,
                                                    right=0,
                                                    bottom=0,
                                                    border=ft.Border.all(
                                                        2,
                                                        "black",
                                                    ),
                                                ),
                                            ]
                                        ),

                                        ft.Column(
                                            spacing=0,
                                            controls=[
                                                ft.Text(
                                                    c["nom"],
                                                    color="white",
                                                    size=13,
                                                    weight=ft.FontWeight.BOLD,
                                                ),
                                                ft.Text(
                                                    c["username"],
                                                    color="white70",
                                                    size=11,
                                                ),
                                            ],
                                        ),
                                    ],
                                ),

                                ft.Row(
                                    spacing=10,
                                    controls=[
                                        ft.Icon(
                                            ft.Icons.FAVORITE,
                                            color="red",
                                            size=14,
                                        ),
                                        ft.Text(
                                            "24K",
                                            color="white70",
                                            size=11,
                                        ),
                                        ft.Icon(
                                            ft.Icons.VIDEOCAM,
                                            color="white70",
                                            size=14,
                                        ),
                                        ft.Text(
                                            "128",
                                            color="white70",
                                            size=11,
                                        ),
                                    ],
                                ),

                                ft.Container(
                                    bgcolor="#FF2D55",
                                    border_radius=20,
                                    padding=ft.Padding.symmetric(
                                        horizontal=12,
                                        vertical=6,
                                    ),
                                    content=ft.Text(
                                        "Suivre",
                                        color="white",
                                        size=11,
                                        weight=ft.FontWeight.BOLD,
                                    ),
                                ),
                            ],
                        ),
                    ),
                ]
            ),
        )
    def top_creator_item(c):
        return ft.Container(
            padding=10,
            border_radius=15,
            bgcolor="#111111",
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    ft.Row(
                        spacing=10,
                        controls=[
                            ft.CircleAvatar(
                                foreground_image_src=c["avatar"],
                                radius=22,
                            ),
                            ft.Column(
                                spacing=2,
                                controls=[
                                    ft.Text(
                                        c["nom"],
                                        color="white",
                                        weight=ft.FontWeight.BOLD,
                                    ),
                                    ft.Text(
                                        c["username"],
                                        color="white60",
                                        size=12,
                                    ),
                                ],
                            ),
                        ],
                    ),
                    ft.TextButton(
                        "Suivre",
                        style=ft.ButtonStyle(
                            color="white",
                            bgcolor="#FF2D55",
                        ),
                    ),
                ],
            ),
        )
    recommended_section = ft.Column(
        spacing=10,
        controls=[
            ft.Text(
                "Créateurs recommandés",
                color="white",
                size=18,
                weight=ft.FontWeight.BOLD,
            ),
            ft.Row(
                scroll=ft.ScrollMode.HIDDEN,
                #scroll=ft.ScrollMode.AUTO,
                spacing=10,
                controls=[
                    ft.Container(
                        #width=300,
                        height=160,
                        border_radius=20,
                        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                        content=ft.Stack(
                            controls=[
                                ft.Image(
                                    src=r["avatar"],
                                    fit="cover",
                                    expand=True,
                                ),
                                ft.Container(
                                    gradient=ft.LinearGradient(
                                        begin=ft.Alignment.TOP_CENTER,
                                        end=ft.Alignment.BOTTOM_CENTER,
                                        colors=[
                                            ft.Colors.TRANSPARENT,
                                            "#000000CC",
                                        ],
                                    )
                                ),
                                ft.Container(
                                    alignment=ft.Alignment.BOTTOM_LEFT,
                                    padding=15,
                                    content=ft.Text(
                                        r["nom"],
                                        color="white",
                                        size=16,
                                        weight=ft.FontWeight.BOLD,
                                    ),
                                ),
                            ]
                        ),
                    )
                    for r in recommandes_data
                ],
            ),
        ],
        )
    top_section = ft.Column(
        spacing=10,
        controls=[
            ft.Text(
                "🏆 Top créateurs",
                color="white",
                size=18,
                weight=ft.FontWeight.BOLD,
            ),
            *[top_creator_item(c) for c in decouvrir_data],
        ],
        )
    creator_grid = ft.Row(
        scroll=ft.ScrollMode.HIDDEN,
        spacing=12,
        controls=[creator_card(c) for c in decouvrir_data],
        )
    return ft.Column(
        expand=True,
        scroll=ft.ScrollMode.HIDDEN,
        spacing=15,
        controls=[

            # Bannière tendance
            ft.Container(
                margin=10,
                height=190,
                border_radius=25,
                clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                content=ft.Stack(
                    controls=[
                        ft.Image(
                            src="https://picsum.photos/900/500?blur=1",
                            fit="cover",
                            expand=True,
                        ),
                        ft.Container(
                            gradient=ft.LinearGradient(
                                begin=ft.Alignment.TOP_CENTER,
                                end=ft.Alignment.BOTTOM_CENTER,
                                colors=[
                                    ft.Colors.TRANSPARENT,
                                    "#000000EE",
                                ],
                            )
                        ),
                        ft.Container(
                            padding=20,
                            alignment=ft.Alignment.BOTTOM_LEFT,
                            content=ft.Column(
                                alignment=ft.MainAxisAlignment.END,
                                spacing=5,
                                controls=[
                                    ft.Text(
                                        "🔥 Tendances du jour",
                                        color="white",
                                        size=24,
                                        weight=ft.FontWeight.BOLD,
                                    ),
                                    ft.Text(
                                        "Découvrez les créateurs les plus populaires",
                                        color="white70",
                                        size=13,
                                    ),
                                ],
                            ),
                        ),
                    ]
                ),
            ),
            ft.Container(
                padding=ft.Padding.symmetric(horizontal=10),
                content=ft.Text(
                    "Créateurs populaires",
                    color="white",
                    size=18,
                    weight=ft.FontWeight.BOLD,
                ),
            ),
            creator_grid,
            ft.Container(
                padding=10,
                content=recommended_section,
            ),

            ft.Container(
                padding=10,
                content=top_section,
            ),

            ft.Container(height=30),
        ],
    )
def view_video(videos):
    return ft.PageView(
            horizontal=False,
            expand=True,
            controls=[
                ft.Container(
                    expand=True,
                    content=ft.Stack(
                        controls=[
                            ftv.Video(
                                playlist=[ftv.VideoMedia(v["contenu"])],
                                autoplay=True,
                                expand=True,
                                show_controls=False,
                            ),
                            # Dégradé supérieur pour masquer la barre d'onglets proprement
                            ft.Container(
                                top=0, left=0, right=0, height=80,
                                gradient=ft.LinearGradient(
                                    begin=ft.Alignment.TOP_CENTER,
                                    end=ft.Alignment.BOTTOM_CENTER,
                                    colors=[ft.Colors.BLACK54, ft.Colors.TRANSPARENT]
                                )
                            ),
                            # Infos en overlay inférieur
                            ft.Container(
                                bottom=20,
                                left=15,
                                right=15,
                                content=ft.Row(
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                    vertical_alignment=ft.CrossAxisAlignment.END,
                                    controls=[
                                        ft.Row(
                                            spacing=10,
                                            controls=[
                                                ft.CircleAvatar(foreground_image_src="https://picsum.photos/100/100?img=10", radius=20),
                                                ft.Column(
                                                    spacing=2,
                                                    controls=[
                                                        ft.Text(v["creator_nom"], color="white", weight="bold", size=15),
                                                        ft.Row(
                                                            spacing=10,
                                                            controls=[
                                                                ft.Row([ft.Icon(ft.Icons.IMAGE_OUTLINED, size=14, color="white70"), ft.Text(v["medias"], color="white70", size=12)]),
                                                                ft.Row([ft.Icon(ft.Icons.VIDEOCAM_OUTLINED, size=14, color="white70"), ft.Text(v["videos"], color="white70", size=12)]),
                                                                ft.Row([ft.Icon(ft.Icons.FAVORITE_ROUNDED, size=14, color="white70"), ft.Text(v["likes"], color="white70", size=12)]),
                                                            ]
                                                        )
                                                    ]
                                                )
                                            ]
                                        ),
                                        ft.IconButton(icon=ft.Icons.PERSON_ADD_ROUNDED, icon_color="white", icon_size=24)
                                    ]
                                )
                            )
                        ]
                    )
                ) for v in videos
            ]
        )
def view_rechercher(historique_recherche):
    return ft.Container(
        padding=20,
        expand=True,
        content=ft.Column(
            spacing=15,
            scroll=ft.ScrollMode.HIDDEN,
            controls=[
                ft.Text(
                    "Recherche",
                    size=24,
                    weight=ft.FontWeight.BOLD,
                    color="white",
                ),

                ft.TextField(
                    hint_text="Rechercher des créateurs...",
                    prefix_icon=ft.Icons.SEARCH,
                    bgcolor="#1E1E1E",
                    border_radius=20,
                    border_color=ft.Colors.TRANSPARENT,
                    focused_border_color="#3A3A3A",
                    cursor_color="white",
                    text_style=ft.TextStyle(color="white"),
                    hint_style=ft.TextStyle(color="#888888"),
                    filled=True,
                    content_padding=15,
                    expand=True,
                ),

                ft.Container(height=10),

                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Text(
                            "Récemment consultés",
                            color="white",
                            size=16,
                            weight=ft.FontWeight.BOLD,
                        ),
                        ft.TextButton(
                            "Tout voir",
                            style=ft.ButtonStyle(
                                color="#00BFFF",
                            ),
                        ),
                    ],
                ),

                ft.Divider(color="#2A2A2A", height=1),

                # Liste des créateurs récents
                ft.Column(
                    spacing=10,
                    controls=[
                        item_recent(u)
                        for u in historique_recherche
                    ],
                ),

            ],
        ),
    )
def build_explore_tabs(state,update_page):
    def set_tab(tab_name):
        state["explore_tab"] = tab_name # Modification persistante
        update_page()

    def tab_style(target_tab):
        is_active = state["explore_tab"] == target_tab
        return ft.TextStyle(
            color="white" if is_active else "grey600",
            weight=ft.FontWeight.BOLD if is_active else ft.FontWeight.NORMAL,
            size=18 if is_active else 16
            )

    return ft.Container(
        padding=ft.Padding.only(top=15, bottom=15, left=10, right=10),
        bgcolor="#000000",
        content=ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
            ft.TextButton(
                    content=ft.Text("Découvrir", style=tab_style("découvrir")),
                    on_click=lambda _: set_tab("découvrir")
                ),
            ft.Text("|", color="grey800", size=14),
            ft.TextButton(
                content=ft.Text("Vidéo", style=tab_style("vidéo")),
                on_click=lambda _: set_tab("vidéo")
                ),
            ft.Text("|", color="grey800", size=14),
            ft.TextButton(
                content=ft.Text("Rechercher", style=tab_style("rechercher")),
                on_click=lambda _: set_tab("rechercher")
                    ),
                ]
            )
        )

def page_explore(recommandes_data,decouvrir_data,videos,historique_recherche,state,update_page,):
    tab_actuel = state.get("explore_tab")
    
    if tab_actuel == "découvrir":
        sub_content = view_decouvrir(recommandes_data, decouvrir_data)
    elif tab_actuel == "vidéo":
        sub_content = view_video(videos)
    else: # Pour "rechercher"
        sub_content = view_rechercher(historique_recherche) 
        
    return ft.Column(
        spacing=0,
        controls=[
            build_explore_tabs(state, update_page),
            ft.Container(content=sub_content, expand=True)
        ],
        expand=True
    )
