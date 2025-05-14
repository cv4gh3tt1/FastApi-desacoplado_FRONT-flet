import flet as ft

from services import CarApi


def main(page: ft.Page):
    page.window.height = 600
    page.window.width = 350

    car_api = CarApi()
    cars = car_api.get_cars()

    data_table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("marca")),
            ft.DataColumn(ft.Text("modelo")),
            ft.DataColumn(ft.Text("ano"), numeric=True),
        ],
    )

    for car in cars:
        data_table.rows.append(
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(car.get("marca"))),
                    ft.DataCell(ft.Text(car.get("modelo"))),
                    ft.DataCell(ft.Text(car.get("ano"))),
                ],
            ),
        )

    page.add(
        data_table,
    )


ft.app(main)
