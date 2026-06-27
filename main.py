from kivymd.uix.fitimage.fitimage import Container
import flet as ft
import flet_video as ftv
from page_explore import page_explore

def main(page: ft.Page):
    page.title = "Publications"
    page.bgcolor = "black"
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 390
    page.window.height = 844
    page.window.resizable = False
    page.window.center()
    # 🔥 IMPORTANT (supprime tous les espaces)
    page.padding = 0
    page.spacing = 0
    selected_index = 0
    video_url = None
    running = False
    stories = []
    state = {"explore_tab": "découvrir"}
    publications = [
        {   "etat":1,
            "id":1,
            "creator_nom":"Alice Martin",
            "avatar":"https://i.pravatar.cc/100?img=1",
            "contenu":"https://picsum.photos/1080/1080?3",
            "description":"Motivation 💪🔥 #motivation",
            "profil":[
                {
                    "nom":"Alice Martin",
                    "avatar":"https://i.pravatar.cc/100?img=1",
                    "contenu":"https://picsum.photos/1080/1080",
                    "description":"Motivation 💪🔥",
                    "likes":12,
                    "comments":20,
                    "shares":10,
                },
                {
                    "nom":"Alice Martin",
                    "avatar":"https://i.pravatar.cc/100?img=1",
                    "contenu":"https://picsum.photos/1080/1080?4",
                    "description":"Motivation 💪🔥",
                    "likes":12,
                    "comments":20,
                    "shares":10,
                },
            ],
            "likes":12,
            "comments":20,
            "shares":10,
        },
        {   "etat":0,
            "id":2,
            "creator_nom":"Alice Martin",
            "avatar":"https://i.pravatar.cc/100?img=1",
            "contenu": """
Chaque petit pas compte.

Ne compare pas ton chapitre 1 au chapitre 20 de quelqu'un d'autre.
Continue d'avancer, même lentement.

#mindset #motivation #developpementpersonnel
""",
            #"description":"Motivation 💪🔥",
            "profil":[
                {
                    "nom":"Alice Martin",
                    "avatar":"https://i.pravatar.cc/100?img=1",
                    "contenu":"Engagé pour une Europe forte, verte et souveraine. Ensemble, construisons l’avenir durable de notre continent. 🇫🇷🇪🇺",
                    "description":"Motivation 💪🔥",
                    "likes":12,
                    "comments":20,
                    "shares":10,
                },
                {
                    "nom":"Alice Martin",
                    "avatar":"https://i.pravatar.cc/100?img=1",
                    "contenu":"https://picsum.photos/1080/1080?4",
                    "description":"Motivation 💪🔥",
                    "likes":12,
                    "comments":20,
                    "shares":10,
                },
            ],
            "likes":12,
            "comments":20,
            "shares":10,
        },
        {   "etat":1,
            "id":3,
            "creator_nom":"Alice Martin",
            "avatar":"https://i.pravatar.cc/100?img=1",
            "contenu":"https://www.w3schools.com/html/mov_bbb.mp4",
            "description":"Motivation 💪🔥",
            "profil":[
                {
                    "nom":"Alice Martin",
                    "avatar":"https://i.pravatar.cc/100?img=1",
                    "contenu":"Engagé pour une Europe forte, verte et souveraine. Ensemble, construisons l’avenir durable de notre continent. 🇫🇷🇪🇺",
                    "description":"Motivation 💪🔥",
                    "likes":12,
                    "comments":20,
                    "shares":10,
                },
                {
                    "nom":"Alice Martin",
                    "avatar":"https://i.pravatar.cc/100?img=1",
                    "contenu":"https://picsum.photos/1080/1080?4",
                    "description":"Motivation 💪🔥",
                    "likes":12,
                    "comments":20,
                    "shares":10,
                },
            ],
            "likes":12,
            "comments":20,
            "shares":10,
        },
        {   "etat":0,
            "id":3,
            "creator_nom":"bella",
            "avatar":"https://picsum.photos/id/64/200/200",
            "contenu":"https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=500",
            "description": """
Il y a des personnes qui n’ont pas besoin de parler fort pour être remarquées. Leur présence suffit. Entre douceur et confiance, ce portrait capture un instant simple mais puissant, celui où l’on est pleinement soi-même, sans filtre ni artifice. ✨ 
            #portrait #naturel #beauté #authenticité #lifestyle #confidence #photography
""",
            "profil":[
                {
                    "nom":"Alice Martin",
                    "avatar":"https://i.pravatar.cc/100?img=1",
                    "contenu":"https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=500",
                    "description":"Motivation 💪🔥",
                    "likes":12,
                    "comments":20,
                    "shares":10,
                },
                {
                    "nom":"Alice Martin",
                    "avatar":"https://i.pravatar.cc/100?img=1",
                    "contenu":"https://picsum.photos/1080/1080?4",
                    "description":"Motivation 💪🔥",
                    "likes":12,
                    "comments":20,
                    "shares":10,
                },
            ],
            "likes":12,
            "comments":20,
            "shares":10,
        },
    ]
    videos = [
        {"creator_nom": "Bianca Herrera", "contenu": "https://www.w3schools.com/html/mov_bbb.mp4", "likes": "36.6K", "medias": "104", "videos": "9"},
        {"creator_nom": "Lovina", "contenu": "https://interactive-examples.mdn.mozilla.net/media/cc0-videos/flower.mp4", "likes": "12.4K", "medias": "45", "videos": "2"}
    ]
    decouvrir_data = [
        {
            "nom": "Bianca Herrera",
            "username": "@biancaherrera",
            "avatar": "https://picsum.photos/100/100?img=10",
            "cover": "https://picsum.photos/400/600?img=15",
            "large": True
        },
        {
            "nom": "Lovina",
            "username": "@lovina",
            "avatar": "https://picsum.photos/100/100?img=11",
            "cover": "https://picsum.photos/400/600?img=16",
            "large": False
        }
    ]
    recommandes_data = [
        {"avatar": "https://picsum.photos/600/400?img=21", "nom": "Aria Sky", "username": "@ariasky"},
        {"avatar": "https://picsum.photos/600/400?img=22", "nom": "Eva Moon", "username": "@evamoon"}
    ]
    historique_recherche = [
        {"nom": "gina", "username": "@your.fav.bunny", "avatar": "https://picsum.photos/100/100?img=30"},
        {"nom": "Emjayplays", "username": "@emjayplays", "avatar": "https://picsum.photos/100/100?img=31"},
        {"nom": "Ava Skye", "username": "@avaskyee", "avatar": "https://picsum.photos/100/100?img=32"}
    ]
    def story(s):
        return ft.Column(
            horizontal_alignment="center",
            controls=[
                ft.Container(
                    padding=3,
                    border=ft.border.Border(
                    top=ft.BorderSide(3, "pink"),
                    bottom=ft.BorderSide(3, "pink"),
                    left=ft.BorderSide(3, "pink"),
                    right=ft.BorderSide(3, "pink"),
                    ),
                    border_radius=50,
                    content=ft.CircleAvatar(
                        foreground_image_src=s["avatar"],
                        radius=30
                    ),
                    #on_click=lambda e: page.run_task(on_avatar_click, e, s)
                    #on_click=lambda e: on_avatar_click(e, s),
                ),
                ft.Text(s["nom"], size=12)
            ]
        )
    def hashtags(txt):
        spans = []
        for mot in txt.split():
            color = "blue" if mot.startswith("#") else "white"
            spans.append(
                ft.TextSpan(text=mot + " ", style=ft.TextStyle(color=color))
            )
        return ft.Text(spans=spans)
    
    def video_preview(url):
        def play_video(e):
            nonlocal video_url
            video_url = url
            page.go("/video_message")

        return ft.Container(
            content=ft.Stack(
                alignment=ft.Alignment.CENTER,
                controls=[
                    ft.Image(src="https://picsum.photos/1080/1080?video", width=float("inf"), border_radius=12, height=300, fit="cover"),  
                    ft.IconButton(  
                        icon=ft.Icons.PLAY_CIRCLE_FILL,  
                        icon_size=60,  
                        icon_color="#00AFF0",
                        on_click=play_video  
                    )
                ]
            )
        )
    async def open_drawer(e):
        await page.show_drawer()
    def debloquer(p):
        p["etat"]=1
        update_page()
    def publication(p):
        liked = False

        like_count = ft.Text(str(p["likes"]), weight="bold")
        comm_count=ft.Text("12", weight="bold")
        part_count=ft.Text("12", weight="bold")
        like_icon = ft.IconButton(icon=ft.Icons.FAVORITE_BORDER)
        def toggle_like(e):
            nonlocal liked
            if liked:
                like_icon.icon = ft.Icons.FAVORITE_BORDER
                like_icon.icon_color = "white"
                like_count.value = str(int(like_count.value) - 1)
            else:
                like_icon.icon = ft.Icons.FAVORITE
                like_icon.icon_color = "red"
                like_count.value = str(int(like_count.value) + 1)

            liked = not liked
            page.update()

        like_icon.on_click = toggle_like
        contenu = p["contenu"]
        etat = p["etat"]

        if etat == 1:
            if contenu.endswith(".mp4"):
                media = video_preview(contenu)
            elif contenu.startswith("https"):
                media = ft.Container(
                content=ft.Image(
                src=contenu,
                width=float("inf"),
                height=350,
                fit="cover", # Version propre avec l'énumération Flet
                ),
                border_radius=20,
                clip_behavior=ft.ClipBehavior.ANTI_ALIAS, # 🔥 Obligatoire pour couper l'image aux angles
                )

            else:
                media = ft.Container(
                content=hashtags(contenu)
                )
        else:
            media = ft.Container(  
                height=320,  
                border_radius=12,  
                clip_behavior=ft.ClipBehavior.ANTI_ALIAS,  
                content=ft.Stack(  
                    controls=[  
                        ft.Image(  
                            src="https://picsum.photos/1080/1080?blur",  
                            fit="cover",  
                            width=float("inf"),  
                            height=320,
                            #blur=ft.Blur(15, 15, ft.BlurTileMode.CLAMP) # Effet flouté
                        ),  
                        ft.Container(bgcolor=ft.Colors.with_opacity(0.75, "black"), expand=True),  
                        ft.Container(  
                            alignment=ft.Alignment.CENTER,  
                            content=ft.Column(  
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,  
                                alignment=ft.MainAxisAlignment.CENTER,  
                                controls=[  
                                    ft.Container(  
                                        padding=12,  
                                        bgcolor=ft.Colors.with_opacity(0.75, "black"),  
                                        border_radius=50,  
                                        content=ft.Icon(ft.Icons.LOCK_OUTLINED, color="#00AFF0", size=30),  
                                    ),  
                                    ft.Text("Contenu Premium", size=18, weight=ft.FontWeight.BOLD, color="white"),  
                                    ft.Text("Abonnez-vous pour débloquer", size=12, color="white70"),  
                                    ft.Container(height=5),  
                                    ft.FilledButton(  
                                        "Débloquer (4.99€)",  
                                        #icon=ft.Icons.STAR_PURPLE_554,  
                                        style=ft.ButtonStyle(  
                                            bgcolor="#00AFF0",  
                                            color="white",  
                                            shape=ft.RoundedRectangleBorder(radius=20),  
                                        ),  
                                        height=40,  
                                        on_click=lambda e: debloquer(p)
                                    ),  
                                ],  
                            ),  
                        ),  
                    ]  
                ),  
            )  
        return ft.Container(
        #bgcolor=CARD_BG,
        border_radius=15,
        padding=15,
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.Row(
                            [
                                ft.CircleAvatar(
                                    radius=18,
                                    foreground_image_src=p["avatar"],
                                ),
                                ft.Text(
                                    p["creator_nom"],
                                    color="white",
                                    weight=ft.FontWeight.BOLD,
                                ),
                            ]
                        ),
                        ft.Icon(
                            ft.Icons.MORE_HORIZ,
                            #color=TEXT_GRAY,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                *[ [hashtags(p["description"])] if p.get("description") else [] ][0],
                media,
                ft.Row(
                    [
                        like_icon,
                        ft.IconButton(
                            icon=ft.Icons.CHAT_BUBBLE_OUTLINE,
                            #icon_color=TEXT_GRAY,
                        ),
                        ft.IconButton(
                            icon=ft.Icons.MONETIZATION_ON_OUTLINED,
                            #icon_color=PINK,
                        ),
                        ft.Column(expand=True)
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                ft.Row(
                [
                    like_count,
                    ft.Text("likes"),
                    comm_count,
                    ft.Text("comments"),
                ],
                spacing=5,
            )
            ]
        ),
    )

    # EXCLUSIVE CONTENT
    exclusive_title = ft.Container(
        content=ft.Text(
            "EXCLUSIVE CONTENT",
            #color=TEXT_GRAY,
            weight=ft.FontWeight.BOLD,
        ),
        padding=ft.Padding.symmetric(horizontal=15),
    )
    
    page.drawer = ft.NavigationDrawer(
    bgcolor="#121212",
    controls=[
        ft.Container(
            padding=20,
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.CircleAvatar(
                        radius=40,
                        foreground_image_src="https://i.pravatar.cc/150?img=1"
                    ),
                    ft.Text(
                        "@alicemartin",
                        size=18,
                        weight=ft.FontWeight.BOLD
                    ),
                    ft.Text(
                        "Créatrice de contenu",
                        color="grey"
                    ),
                ]
            )
        ),

        ft.Divider(color="#222"),

        ft.ListTile(
            leading=ft.Icon(ft.Icons.PERSON, color="#00AFF0"),
            title=ft.Text("Mon profil"),
        ),

        ft.ListTile(
            leading=ft.Icon(ft.Icons.BOOKMARK_BORDER, color="#00AFF0"),
            title=ft.Text("Collections"),
        ),

        ft.ListTile(
            leading=ft.Icon(ft.Icons.ACCOUNT_BALANCE, color="#00AFF0"),
            title=ft.Text("Devenir Createur"),
        ),

        ft.ListTile(
            leading=ft.Icon(ft.Icons.LANGUAGE, color="#00AFF0"),
            title=ft.Text("Language"),
        ),

        ft.ListTile(
            leading=ft.Icon(ft.Icons.QUESTION_MARK, color="#00AFF0"),
            title=ft.Text("Help"),
        ),

        ft.ListTile(
            leading=ft.Icon(ft.Icons.SETTINGS, color="#00AFF0"),
            title=ft.Text("Paramètres"),
        ),

        ft.Divider(color="#222"),

        ft.ListTile(
            leading=ft.Icon(ft.Icons.LOGOUT, color="red"),
            title=ft.Text("Déconnexion"),
        ),
    ],
)
    header = ft.AppBar(
        leading=ft.IconButton(icon=ft.Icons.MENU, icon_color="white",on_click=open_drawer,),
        title=ft.Text("SocialFlow", size=22, weight=ft.FontWeight.BOLD, font_family="sans-serif"),
        center_title=True,
        bgcolor="#121212",
        elevation=2,
        actions=[
            ft.IconButton(icon=ft.Icons.NOTIFICATIONS_NONE, icon_color="white"),
            ft.Container(
                content=ft.Icon(ft.Icons.PERSON, color="white", size=16),
                bgcolor="purple",
                shape=ft.BoxShape.CIRCLE,
                margin=ft.Margin.only(right=15),
                padding=6
            )
        ]
    )
    posts_column = ft.Column(scroll=ft.ScrollMode.HIDDEN)
    def suggestion_card(user):
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
                                foreground_image_src=user["avatar"],
                                radius=22,
                            ),
                            ft.Column(
                                spacing=2,
                                controls=[
                                    ft.Text(
                                        user["nom"],
                                        color="white",
                                        weight=ft.FontWeight.BOLD,
                                    ),
                                    ft.Text(
                                        user["username"],
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
    def page_accueil():
        if stories:
            section_stories = ft.Container(
            padding=ft.Padding.only(top=5, bottom=5),
            bgcolor="#121212",
            content=ft.Row(
                controls=[
                    ft.Container(width=5),
                    *[story(s) for s in stories]
                ],
                scroll=ft.ScrollMode.AUTO
            )
        )
        else:
            section_stories = None

        controls = [header]

        if section_stories:
            controls.append(section_stories)

            controls.append(
            ft.Container(
                height=1,
                bgcolor=ft.Colors.GREY_800
            )
        )

        suggestion = [
            {
            "nom": "Bianca Herrera",
            "username": "@biancaherrera",
            "avatar": "https://picsum.photos/100/100?img=10",
            "cover": "https://picsum.photos/400/600?img=15",
            "large": True
            },
            {
            "nom": "Lovina",
            "username": "@lovina",
            "avatar": "https://picsum.photos/100/100?img=11",
            "cover": "https://picsum.photos/400/600?img=16",
            "large": False
            }
        ]

        index_mot = 0

        for i, p in enumerate(publications):
            controls.append(publication(p))

            if (i + 1) % 2 == 0:
                controls.append(ft.Text("Suggestion",color="white",size=18,weight=ft.FontWeight.BOLD,))
                controls.append(
                ft.Column(
                controls=[
                suggestion_card(suggestion[index_mot % len(suggestion)]),
                suggestion_card(suggestion[(index_mot + 1) % len(suggestion)]),
            ]
        )
    )
            index_mot += 2

        posts_column.controls = controls

        return ft.Container(
        expand=True,
        padding=0,
        margin=0,
        content=posts_column
    )
    
    def set_index(i):
        nonlocal selected_index
        selected_index = i
        update_page()
    def update_page():
        if selected_index == 0:
            contenu.content = page_accueil()
        elif selected_index == 1:
            contenu.content = page_explore(recommandes_data,decouvrir_data,videos,historique_recherche,state,update_page)
        elif selected_index == 4:
            contenu.content = ft.Text("Send")
        elif selected_index == 5:
            contenu.content = ft.Text("Send")

        page.update()
    nav_bar = ft.Container(
    content=ft.Row(
        [
            ft.IconButton(
                icon=ft.Icons.HOME,
                icon_color="white",
                on_click=lambda e: set_index(0)
            ),
            ft.IconButton(
                icon=ft.Icons.EXPLORE,
                icon_color="white",
                on_click=lambda e: set_index(1)
            ),
            ft.IconButton(
                icon=ft.Icons.CHAT,
                icon_color="white",
                on_click=lambda e: set_index(4)
            ),
            ft.IconButton(ft.Icons.PERSON_OUTLINE, icon_color="white",on_click=lambda e: set_index(5)),
        ],
        alignment=ft.MainAxisAlignment.SPACE_AROUND,
    ),
    padding=ft.Padding.only(top=10, bottom=12),
    bgcolor="#121212",
    border=ft.Border.only(
        top=ft.BorderSide(1, "#222222")
    ),
)
    page.navigation_bar = nav_bar
    def route_change(e):
        if page.route.startswith("/video"):
            page.views.append(
            ft.View(
            route=page.route,
            appbar=ft.AppBar(title=ft.Text("Lecture vidéo")),
            padding=0,
            controls=[
                ftv.Video(
                    playlist=[
                        ftv.VideoMedia(video_url)
                    ],
                    autoplay=True,
                    expand=True,
                    show_controls=True
                )
            ]
        )
    )
    def view_pop(e):
        nonlocal running
        running = False
        if page.views:
            page.views.pop()
        page.go("/")
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    contenu = ft.Container(expand=True, content=page_accueil())
    page.add(contenu)
ft.app(target=main)
