import flet as ft

def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_min_height = 800
    page.window_min_width = 500
    page.bgcolor = ft.colors.BLACK

    image = ft.Container(
        expand=2,
        clip_behavior= ft.ClipBehavior.NONE,
        border_radius=ft.border_radius.vertical(top=20),
        gradient=ft.LinearGradient(
            begin=ft.alignment.bottom_left,
            end=ft.alignment.top_right,
            colors=[ft.colors.BROWN, ft.colors.SURFACE],
        ),
        content=ft.Image(
            src = r'C:\Users\user\OneDrive\Documentos\RPGs\MH Diario dos caçadores\Monstros\Yian kut-ku\Yian kut-ku bgr.png',
            scale=ft.Scale(scale=1.3),
        )
    )

    info = ft.Container(
        expand=2,
        padding=ft.padding.all(30),
        alignment=ft.alignment.center,
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text(value='Ameaça baixa', color=ft.colors.AMBER),
                ft.Text(
                    value='Yian Kut-Ku',
                    weight=ft.FontWeight.BOLD,
                    size=40,
                    color=ft.colors.BLACK,
                ),
                ft.Text(
                    value='Nada a comentar',
                    color=ft.colors.GREY,
                    text_align=ft.TextAlign.CENTER,
                )
            ]
        )

    )
    skills = ft.Container(
        expand=1,
        bgcolor=ft.colors.ORANGE,
        padding=ft.padding.symmetric(horizontal=20),
        border_radius=ft.border_radius.vertical(bottom=20),
        content=ft.Row(
            controls=[
                ft.Column(
                    expand=1,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Text(
                            value='90',
                            color=ft.colors.WHITE,
                            weight=ft.FontWeight.BOLD,
                            size=40,                            
                        ),
                        ft.Text(
                            value="HP",
                            color=ft.colors.WHITE,
                            
                        )
                    ]
                ),           
                ft.VerticalDivider(opacity=0),
                ft.Column(
                    expand=1,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Text(
                            value='4d10 (3)',
                            
                            color=ft.colors.WHITE,
                            weight=ft.FontWeight.BOLD,
                            size=40,
                        ),
                        ft.Text(
                            value="Dano",
                            color=ft.colors.WHITE,

                        )
                    ]
                ), 
                ft.VerticalDivider(opacity=0),
                ft.Column(
                    expand=1,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Text(
                            value='3',
                            color=ft.colors.WHITE,
                            weight=ft.FontWeight.BOLD,
                            size=40,
                        ),
                        ft.Text(
                            value="Ameaçã",
                            color=ft.colors.WHITE,
                            
                        )
                    ]
                ),
            ]
        )

    )



    layout = ft.Container(
        height= 700,
        width= 400,
        shadow=ft.BoxShadow(blur_radius=100, color=ft.colors.BROWN),
        clip_behavior= ft.ClipBehavior.NONE,
        border_radius=ft.border_radius.all(30),
        bgcolor=ft.colors.WHITE,
        content=ft.Column(
            spacing=0,
            controls=[
                image,
                info,
                skills,
            ]
        )
    
    )

    page.add(layout)

if __name__ == '__main__':
    ft.app(target = main)