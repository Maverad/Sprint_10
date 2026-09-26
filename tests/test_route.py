import allure
import test_data
import pytest


class TestRoute:

    @pytest.mark.xfail(reason='Добавляется лишний текст в точке назначения "Куда"')
    @allure.title('Проверка отрисовки маршрута')
    def test_route_visible(self, controller):
        controller.fill_destination_from(test_data.destination['from'])
        controller.fill_destination_to(test_data.destination['to'])

        assert controller.check_destination_present_on_map(test_data.destination['from'])
        assert controller.check_destination_present_on_map(test_data.destination['to'])
        assert controller.check_type_picker_form_presents()

    @allure.title('Проверка ввода одинакового маршрута')
    def test_same_destination(self, controller):
        controller.fill_destination_from(test_data.destination['from'])
        controller.fill_destination_to(test_data.destination['from'])

        assert controller.check_same_destination_cost()
        assert controller.check_same_destination_duration()

    @allure.title('Проверка выбора типа маршрута')
    @pytest.mark.parametrize('dest_type', [*test_data.destination_types])
    def test_types_active(self, controller, dest_type):
        controller.fill_destination_from(test_data.destination['from'])
        controller.fill_destination_to(test_data.destination['to'])
        controller.choose_mode('own')
        controller.choose_type(dest_type)

        assert controller.check_type_active(dest_type)

    @allure.title('Проверка появления кнопки "Забронировать" при выборе типа "Драйв"')
    def test_drive_order_button_active(self, controller):
        controller.fill_destination_from(test_data.destination['from'])
        controller.fill_destination_to(test_data.destination['to'])
        controller.choose_mode('own')
        controller.choose_type('drive')

        assert controller.check_drive_order_button()
