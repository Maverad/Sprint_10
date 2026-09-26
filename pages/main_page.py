from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators as locator
import allure
import test_data
from helpers import digit_checker


class MainPage(BasePage):

    @allure.step('Заполнение поля "Откуда"')
    def fill_destination_from(self, address):
        self.wait_for_element(locator.from_input)
        self.input_text(locator.from_input, address)
        
    @allure.step('Заполнение поля "Куда"')
    def fill_destination_to(self, address):
        self.wait_for_element(locator.to_input)
        self.input_text(locator.to_input, address)

    @allure.step('Выбор режима маршрута')
    def choose_mode(self, mode:str):
        MODES = {
            'fast': locator.mode_fast,
            'optimal': locator.mode_optimal,
            'own': locator.mode_own
        }
        try:
            new_mode = MODES[mode]
        except KeyError:
            raise ValueError(f'No such mode')
        self.wait_for_element(new_mode)
        self.click_on_element(new_mode)

    @allure.step('Выбор типа маршрута')
    def choose_type(self, type:str):
        TYPES = {
            'walk': locator.type_walk,
            'car': locator.type_car,
            'drive': locator.type_drive,
            'taxi': locator.type_taxi,
            'scooter': locator.type_scooter,
            'bicycle': locator.type_bicycle
        }
        try:
            new_type = TYPES[type]
        except KeyError:
            raise ValueError('No such type')
        self.wait_for_element(new_type)
        self.click_on_element(new_type)
        
    # Taxi methods
    
    @allure.step('Клик на кнопку вызова такси')
    def click_on_call_taxi_button(self):
        self.wait_for_element(locator.type_taxi_call_taxi_button)
        self.click_on_element(locator.type_taxi_call_taxi_button)
        self.wait_for_element(locator.taxi_rate_work)

    @allure.step('Выбор тарифа такси')
    def choose_taxi_rate(self, rate:str):
        RATES = {
            'work': locator.taxi_rate_work,
            'sleep': locator.taxi_rate_sleep,
            'consoling': locator.taxi_rate_consoling,
            'glossy': locator.taxi_rate_glossy,
            'talk': locator.taxi_rate_talk,
            'vacation': locator.taxi_rate_vacation
        }
        try:
            new_rate = RATES[rate]
        except KeyError:
            raise ValueError('No such taxi rate')
        self.wait_for_element(new_rate)
        self.click_on_element(new_rate)

    @allure.step('Заполнение поля "Комментарий водителю"')
    def fill_taxi_form_comment(self, comment:str):
        self.wait_for_element(locator.taxi_form_driver_comment)
        self.input_text(locator.taxi_form_driver_comment, comment)

    @allure.step('Заполнение требований к заказу')
    def fill_taxi_form_requirements(self):
        self.wait_for_element(locator.taxi_form_order_requirements)
        self.click_on_element(locator.taxi_form_order_requirements)
        self.wait_for_element(locator.taxi_form_desk_for_desktop_toggle_activate)
        self.click_on_element(locator.taxi_form_desk_for_desktop_toggle_activate)

    @allure.step('Клик на финальную кнопку вызова такси')
    def click_on_final_call_taxi_button(self):
        self.wait_for_element(locator.taxi_form_call_taxi_button)
        self.click_on_element(locator.taxi_form_call_taxi_button)
        self.wait_for_element(locator.taxi_details_button)

    @allure.step('Клик на кнопку отмены заказа такси')
    def click_on_cancel_search_taxi_button(self):
        self.wait_for_element(locator.taxi_cancel_button)
        self.click_on_element(locator.taxi_cancel_button)

    @allure.step('Клик на кнопку "Детали"')
    def click_on_taxi_details_button(self):
        self.wait_for_element(locator.taxi_details_button)
        self.click_on_element(locator.taxi_details_button)

    @allure.step('Полный позитивный флоу заказа такси')
    def call_taxi_positive_flow(self, from_, to_):
        self.fill_destination_from(from_)
        self.fill_destination_to(to_)
        self.choose_mode('fast')
        taxi_cost = self.find_element(locator.type_result).text
        self.click_on_call_taxi_button()
        self.wait_for_element(locator.taxi_rate_work)
        self.choose_taxi_rate('work')
        self.fill_taxi_form_comment('Тестовый комментарий водителю')
        self.fill_taxi_form_requirements()
        self.click_on_final_call_taxi_button()
        result = digit_checker(taxi_cost)
        return result

    # Drive methods

    @allure.step('Клик на кнопку бронирования машины')
    def click_on_book_drive_button(self):
        self.wait_for_element(locator.type_drive_book_button)
        self.click_on_element(locator.type_drive_book_button)

    @allure.step('Выбор тарифа драйва')
    def choose_drive_rate(self, rate:str):
        RATES = {
            'daily': locator.drive_rate_daily,
            'expedition': locator.drive_rate_expedition,
            'luxurious': locator.drive_rate_luxurious
        }
        try:
            new_rate = RATES[rate]
        except KeyError:
            raise ValueError('No such drive rate')
        self.wait_for_element(new_rate)
        self.click_on_element(new_rate)

    # Checks

    def check_search_car_in_progress(self):
        self.wait_for_element(locator.taxi_search_car_check)
        return self.check_visibility(locator.taxi_search_car_check)

    def check_taxi_cost(self, cost):
        self.click_on_taxi_details_button()
        self.wait_for_element(locator.taxi_details_cost)
        details_cost = self.find_element(locator.taxi_details_cost).text
        result = digit_checker(details_cost)
        return cost == result
    
    def check_destination_present_on_map(self, address:str):
        loc = locator()
        return self.check_visibility(loc.get_destination_locator(address))
    
    def check_same_destination_duration(self):
        self.wait_for_element(locator.free_ride_duration)
        return self.check_visibility(locator.free_ride_duration)

    def check_same_destination_cost(self):
        self.wait_for_element(locator.free_ride_auto_cost)
        return self.check_visibility(locator.free_ride_auto_cost)

    def check_type_active(self, dest_type):
        return test_data.destination_types[dest_type] in self.find_element(locator.type_result).text

    def check_type_picker_form_presents(self):
        return self.check_visibility(locator.mode_own)

    def check_taxi_order_is_visible(self):
        return self.check_visibility(locator.taxi_cancel_button)

    def check_drive_order_button(self):
        self.wait_for_element(locator.type_drive_book_button)
        return self.check_visibility(locator.type_drive_book_button)

    def check_taxi_rate_description(self, rate):
        i_icon = {
            'work': locator.taxi_rate_work_i_icon,
            'sleep': locator.taxi_rate_sleep_i_icon,
            'consoling': locator.taxi_rate_consolling_i_icon,
            'glossy': locator.taxi_rate_glossy_i_icon,
            'talk': locator.taxi_rate_talk_i_icon,
            'vacation': locator.taxi_rate_vacation_i_icon
        }
        i_icon_describe = {
            'work': locator.taxi_rate_work_i_icon_describe,
            'sleep': locator.taxi_rate_sleep_i_icon_describe,
            'consoling': locator.taxi_rate_consolling_i_icon_describe,
            'glossy': locator.taxi_rate_glossy_i_icon_describe,
            'talk': locator.taxi_rate_talk_i_icon_describe,
            'vacation': locator.taxi_rate_vacation_i_icon_describe
        }
        self.choose_taxi_rate(rate)
        self.wait_for_element(i_icon[rate])
        self.move_to_element(i_icon[rate])
        self.wait_for_element(i_icon_describe[rate])
        rate_description = self.find_element(i_icon_describe[rate]).text
        return test_data.taxi_rate_description[rate] in rate_description

    def check_taxi_order_form_number(self):
        self.wait_for_element(locator.taxi_form_number)
        return self.check_visibility(locator.taxi_form_number)

    def check_taxi_order_form_payment_method(self):
        self.wait_for_element(locator.taxi_form_payment_method)
        return self.check_visibility(locator.taxi_form_payment_method)

    def check_taxi_order_form_driver_comment(self):
        self.wait_for_element(locator.taxi_form_driver_comment)
        return self.check_visibility(locator.taxi_form_driver_comment)

    def check_taxi_order_form_order_requirements(self):
        self.wait_for_element(locator.taxi_form_order_requirements)
        return self.check_visibility(locator.taxi_form_order_requirements)

    def check_success_taxi_modal_rating(self):
        self.wait_for_element(locator.taxi_success_modal_rating)
        return self.check_visibility(locator.taxi_success_modal_rating)

    def check_success_taxi_modal_title(self):
        self.wait_for_element(locator.taxi_success_modal_title)
        return self.check_visibility(locator.taxi_success_modal_title)
