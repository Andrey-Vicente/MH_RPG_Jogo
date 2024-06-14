import flet as ft
from functools import partial

def main(page: ft.Page):
    page.title = "Barra de HP Interativa"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_min_height = 700
    page.window_min_width = 500
    page.bgcolor = "#8C8F7A"

    def update_vida(nova_vida, player, hp):
        hp.value = f"HP: {nova_vida}"
        player.value = nova_vida/20
        page.update()


    def altera_hp(e, c, player, hp):
        vida_atual = int(hp.value.split()[1])
        nova_vida = min(max(vida_atual + c, 0), 20)
        update_vida(nova_vida, player, hp)


    estetica_texto = [
        "HP: 20", #Texto
        ft.colors.BLACK, #cor do Texto
        20, #Tamanho
    ]

    estetica_barra = [
        1, # value
        300, # width
        20, #height
        ft.border_radius.all(30), #Border_radius
        ft.colors.RED, #color
        "#353535" #bgcolor
    ]

    estetica_botao = [
        "+1", # texto
        "+5", # texto
        "-1", # texto
        "-5", # texto
        50, # width
        1, # valor do botão
        5, # valor do botão
        -1, # valor do botão
        -5 # valor do botão
    ]
    

    lis_vida = [
    ft.Text(value=estetica_texto[0], color=estetica_texto[1], size=estetica_texto[2]),
    ft.Text(value=estetica_texto[0], color=estetica_texto[1], size=estetica_texto[2]),
    ft.Text(value=estetica_texto[0], color=estetica_texto[1], size=estetica_texto[2]),
    ft.Text(value=estetica_texto[0], color=estetica_texto[1], size=estetica_texto[2]),
    ft.Text(value=estetica_texto[0], color=estetica_texto[1], size=estetica_texto[2]),
    ft.Text(value=estetica_texto[0], color=estetica_texto[1], size=estetica_texto[2])
    
    ]

    barras_Vida = [
        ft.ProgressBar(
            value=estetica_barra[0],
            width=estetica_barra[1], 
            height=estetica_barra[2], 
            border_radius=estetica_barra[3], 
            color=estetica_barra[4], 
            bgcolor=estetica_barra[5]    
            ),
            ft.ProgressBar(
            value=estetica_barra[0],
            width=estetica_barra[1],
            height=estetica_barra[2], 
            border_radius=estetica_barra[3], 
            color=estetica_barra[4], 
            bgcolor=estetica_barra[5]    
            ),
            ft.ProgressBar(
            value=estetica_barra[0],
            width=estetica_barra[1], 
            height=estetica_barra[2], 
            border_radius=estetica_barra[3], 
            color=estetica_barra[4], 
            bgcolor=estetica_barra[5]    
            ),
            ft.ProgressBar(
            value=estetica_barra[0],
            width=estetica_barra[1], 
            height=estetica_barra[2], 
            border_radius=estetica_barra[3], 
            color=estetica_barra[4], 
            bgcolor=estetica_barra[5]    
            ),
            ft.ProgressBar(
            value=estetica_barra[0],
            width=estetica_barra[1], 
            height=estetica_barra[2], 
            border_radius=estetica_barra[3], 
            color=estetica_barra[4], 
            bgcolor="#353535"    
            ),
            ft.ProgressBar(
            value=estetica_barra[0],
            width=estetica_barra[1], 
            height=estetica_barra[2], 
            border_radius=estetica_barra[3], 
            color=estetica_barra[4], 
            bgcolor="#353535"    
            )          

    ]

    lis_botao = [
        [
        ft.ElevatedButton(text=estetica_botao[0], on_click=partial(altera_hp, c=estetica_botao[5], player=barras_Vida[0], hp=lis_vida[0]), width=estetica_botao[4]), 
        ft.ElevatedButton(text=estetica_botao[1], on_click=partial(altera_hp, c=estetica_botao[6], player=barras_Vida[0], hp=lis_vida[0]), width=estetica_botao[4]),
        ft.ElevatedButton(text=estetica_botao[2], on_click=partial(altera_hp, c=estetica_botao[7], player=barras_Vida[0], hp=lis_vida[0]), width=estetica_botao[4]),
        ft.ElevatedButton(text=estetica_botao[3], on_click=partial(altera_hp, c=estetica_botao[8], player=barras_Vida[0], hp=lis_vida[0]), width=estetica_botao[4])
    ],
        [
        ft.ElevatedButton(text=estetica_botao[0], on_click=partial(altera_hp, c=estetica_botao[5], player=barras_Vida[1], hp=lis_vida[1]), width=estetica_botao[4]), 
        ft.ElevatedButton(text=estetica_botao[1], on_click=partial(altera_hp, c=estetica_botao[6], player=barras_Vida[1], hp=lis_vida[1]), width=estetica_botao[4]),
        ft.ElevatedButton(text=estetica_botao[2], on_click=partial(altera_hp, c=estetica_botao[7], player=barras_Vida[1], hp=lis_vida[1]), width=estetica_botao[4]),
        ft.ElevatedButton(text=estetica_botao[3], on_click=partial(altera_hp, c=estetica_botao[8], player=barras_Vida[1], hp=lis_vida[1]), width=estetica_botao[4])
    ],
        [
        ft.ElevatedButton(text=estetica_botao[0], on_click=partial(altera_hp, c=estetica_botao[5], player=barras_Vida[2], hp=lis_vida[2]), width=estetica_botao[4]), 
        ft.ElevatedButton(text=estetica_botao[1], on_click=partial(altera_hp, c=estetica_botao[6], player=barras_Vida[2], hp=lis_vida[2]), width=estetica_botao[4]),
        ft.ElevatedButton(text=estetica_botao[2], on_click=partial(altera_hp, c=estetica_botao[7], player=barras_Vida[2], hp=lis_vida[2]), width=estetica_botao[4]),
        ft.ElevatedButton(text=estetica_botao[3], on_click=partial(altera_hp, c=estetica_botao[8], player=barras_Vida[2], hp=lis_vida[2]), width=estetica_botao[4])
    ],
        [
        ft.ElevatedButton(text=estetica_botao[0], on_click=partial(altera_hp, c=estetica_botao[5], player=barras_Vida[3], hp=lis_vida[3]), width=estetica_botao[4]), 
        ft.ElevatedButton(text=estetica_botao[1], on_click=partial(altera_hp, c=estetica_botao[6], player=barras_Vida[3], hp=lis_vida[3]), width=estetica_botao[4]),
        ft.ElevatedButton(text=estetica_botao[2], on_click=partial(altera_hp, c=estetica_botao[7], player=barras_Vida[3], hp=lis_vida[3]), width=estetica_botao[4]),
        ft.ElevatedButton(text=estetica_botao[3], on_click=partial(altera_hp, c=estetica_botao[8], player=barras_Vida[3], hp=lis_vida[3]), width=estetica_botao[4])
    ],
        [
        ft.ElevatedButton(text=estetica_botao[0], on_click=partial(altera_hp, c=estetica_botao[5], player=barras_Vida[4], hp=lis_vida[4]), width=estetica_botao[4]), 
        ft.ElevatedButton(text=estetica_botao[1], on_click=partial(altera_hp, c=estetica_botao[6], player=barras_Vida[4], hp=lis_vida[4]), width=estetica_botao[4]),
        ft.ElevatedButton(text=estetica_botao[2], on_click=partial(altera_hp, c=estetica_botao[7], player=barras_Vida[4], hp=lis_vida[4]), width=estetica_botao[4]),
        ft.ElevatedButton(text=estetica_botao[3], on_click=partial(altera_hp, c=estetica_botao[8], player=barras_Vida[4], hp=lis_vida[4]), width=estetica_botao[4])
    ],
        [
        ft.ElevatedButton(text=estetica_botao[0], on_click=partial(altera_hp, c=estetica_botao[5], player=barras_Vida[5], hp=lis_vida[5]), width=estetica_botao[4]), 
        ft.ElevatedButton(text=estetica_botao[1], on_click=partial(altera_hp, c=estetica_botao[6], player=barras_Vida[5], hp=lis_vida[5]), width=estetica_botao[4]),
        ft.ElevatedButton(text=estetica_botao[2], on_click=partial(altera_hp, c=estetica_botao[7], player=barras_Vida[5], hp=lis_vida[5]), width=estetica_botao[4]),
        ft.ElevatedButton(text=estetica_botao[3], on_click=partial(altera_hp, c=estetica_botao[8], player=barras_Vida[5], hp=lis_vida[5]), width=estetica_botao[4])
    ],





    ]

            
    #lis_vida[0] = ft.Text(value="HP: 20", color=ft.colors.BLACK, size=20,)



    linha1 = ft.Container(
        expand=1,
        padding=ft.padding.only(left=20),
        content=ft.Row(
            controls=[
                ft.Column(
                    expand=1,
                    controls=[

                        lis_vida[0],
                        barras_Vida[0],        
                        ft.Row(
                            controls=[
                        lis_botao[0][0],
                        lis_botao[0][1],
                        lis_botao[0][2],
                        lis_botao[0][3],
                            ]
                        ),

                        ft.Text(
                            value="Estamina",
                            color=ft.colors.BLACK,
                            size=20,
                        ),
                        ft.Text(
                            value="Dano",
                            color=ft.colors.BLACK,
                            size=20,
                        ),
                    ],
                    
                ),
                ft.Column(
                    expand=1,
                    controls=[

                        lis_vida[1],
                        barras_Vida[1],        
                        ft.Row(
                            controls=[
                        lis_botao[1][0],
                        lis_botao[1][1],
                        lis_botao[1][2],
                        lis_botao[1][3],
                            ]
                        ),
                        ft.Text(
                            value="Estamina",
                            color=ft.colors.BLACK,
                            size=20,
                        ),
                        ft.Text(
                            value="Dano",
                            color=ft.colors.BLACK,
                            size=20,
                        ),
                    ],
                ),
                ft.Column(
                    expand=1,
                    controls=[

                        lis_vida[2],
                        barras_Vida[2],        
                        ft.Row(
                            controls=[
                        lis_botao[2][0],
                        lis_botao[2][1],
                        lis_botao[2][2],
                        lis_botao[2][3],
                            ]
                        ),
                        ft.Text(
                            value="Estamina",
                            color=ft.colors.BLACK,
                            size=20,
                        ),
                        ft.Text(
                            value="Dano",
                            color=ft.colors.BLACK,
                            size=20,
                        ),
                    ],
                ),
            ],
        ),

    )
    linha2 = ft.Container(
        expand=1,
        padding=ft.padding.only(left=20),
        content=ft.Row(
            controls=[
                ft.Column(
                    expand=1,
                    controls=[

                        lis_vida[3],
                        barras_Vida[3],        
                        ft.Row(
                            controls=[
                        lis_botao[3][0],
                        lis_botao[3][1],
                        lis_botao[3][2],
                        lis_botao[3][3],
                            ]
                        ),
                        ft.Text(
                            value="Estamina",
                            color=ft.colors.BLACK,
                            size=20,
                        ),
                        ft.Text(
                            value="Dano",
                            color=ft.colors.BLACK,
                            size=20,
                        ),
                    ],
                ),
                ft.Column(
                    expand=1,
                    controls=[

                        lis_vida[4],
                        barras_Vida[4],        
                        ft.Row(
                            controls=[
                        lis_botao[4][0],
                        lis_botao[4][1],
                        lis_botao[4][2],
                        lis_botao[4][3],
                            ]
                        ),
                        ft.Text(
                            value="Estamina",
                            color=ft.colors.BLACK,
                            size=20,
                        ),
                        ft.Text(
                            value="Dano",
                            color=ft.colors.BLACK,
                            size=20,
                        ),
                    ],
                ),
                ft.Column(
                    expand=1,
                    controls=[

                        lis_vida[5],
                        barras_Vida[5],        
                        ft.Row(
                            controls=[
                        lis_botao[5][0],
                        lis_botao[5][1],
                        lis_botao[5][2],
                        lis_botao[5][3],
                            ]
                        ),
                        ft.Text(
                            value="Estamina",
                            color=ft.colors.BLACK,
                            size=20,
                        ),
                        ft.Text(
                            value="Dano",
                            color=ft.colors.BLACK,
                            size=20,
                        ),
                    ],
                ),
            ],
        ),

    )



    layout = ft.Container(
        expand=1,
        gradient=ft.LinearGradient(
            begin=ft.alignment.bottom_left,
            end=ft.alignment.top_right,
            colors=["#5C79F2", "#FF63AF"],
        ),
        
        border_radius=ft.border_radius.all(30),
        content=ft.Column(
            controls=[
                linha1,
                linha2,
            ]
        ) 
    
    )

    page.add(layout)

if __name__ == "__main__":
    ft.app(target=main)


