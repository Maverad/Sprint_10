import allure
import test_data
import pytest


class TestTaxi:

    @allure.title('Положительный сценарий вызова такси')
    def test_call_taxi_positive(self, controller):
        taxi_cost = controller.call_taxi_positive_flow(test_data.destination['from'], test_data.destination['to'])

        assert controller.check_search_car_in_progress()
        assert controller.check_taxi_cost(taxi_cost)

    @allure.title('Проверка закрытия окна заказа такси')
    def test_call_taxi_close_order_screen(self, controller):
        controller.call_taxi_positive_flow(test_data.destination['from'], test_data.destination['to'])
        controller.click_on_cancel_search_taxi_button()

        assert controller.check_taxi_order_is_visible() is False

    @allure.title('Проверка описания тарифов такси')
    @pytest.mark.parametrize('rate', [*test_data.taxi_rate_description])
    def test_taxi_rates(self, controller, rate):
        controller.fill_destination_from(test_data.destination['from'])
        controller.fill_destination_to(test_data.destination['to'])
        controller.choose_mode('fast')
        controller.click_on_call_taxi_button()
        controller.disable_animations()
            
        assert controller.check_taxi_rate_description(rate)
    
    @allure.title('Проверка отображения формы заказа такси')
    def test_taxi_form_presents(self, controller):
        controller.fill_destination_from(test_data.destination['from'])
        controller.fill_destination_to(test_data.destination['to'])
        controller.choose_mode('fast')
        controller.click_on_call_taxi_button()
    
        assert controller.check_taxi_order_form_number()
        assert controller.check_taxi_order_form_payment_method()
        assert controller.check_taxi_order_form_driver_comment()
        assert controller.check_taxi_order_form_order_requirements()
    
    @allure.title('Проверка успешного заказа такси')
    def test_taxi_success_modal(self, controller):
        controller.call_taxi_positive_flow(test_data.destination['from'], test_data.destination['to'])
    
        assert controller.check_success_taxi_modal_title()
        assert controller.check_success_taxi_modal_rating()