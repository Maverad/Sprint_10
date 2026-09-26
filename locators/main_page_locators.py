from selenium.webdriver.common.by import By


class MainPageLocators:
    def get_destination_locator(self, address:str):
        return (By.XPATH, f".//ymaps[text()='{address}']")

    # From / To 
    from_input = (By.XPATH, ".//input[@id='from']")
    from_close_button = (By.XPATH, "(.//button[@class='close-button input-close-button'])[1]")
    to_input = (By.XPATH, ".//input[@id='to']")
    to_close_button = (By.XPATH, "(.//button[@class='close-button input-close-button'])[2]")

    # Map 
    from_location = (By.XPATH, ".//ymaps[text()='Зубовский бульвар, 37']")
    to_location = (By.XPATH, ".//ymaps[text()='Зубовский бульвар, 37']")

    # Modes
    mode_optimal = (By.XPATH, "(.//div[@class='modes-container']/div)[1]")
    mode_fast = (By.XPATH, "(.//div[@class='modes-container']/div)[2]")
    mode_own = (By.XPATH, "(.//div[@class='modes-container']/div)[3]")

    # Types
    type_car = (By.XPATH, "(.//div[@class='types-container']/div)[1]")
    type_walk = (By.XPATH, "(.//div[@class='types-container']/div)[2]")
    type_taxi = (By.XPATH, "(.//div[@class='types-container']/div)[3]")
    type_bicycle = (By.XPATH, "(.//div[@class='types-container']/div)[4]")
    type_scooter = (By.XPATH, "(.//div[@class='types-container']/div)[5]")
    type_drive = (By.XPATH, "(.//div[@class='types-container']/div)[6]")
    type_taxi_call_taxi_button = (By.XPATH, ".//button[text()='Вызвать такси']")
    type_drive_book_button = (By.XPATH, ".//button[text()='Забронировать']")

    # Types results
    type_result = (By.XPATH, ".//div[@class='results-text']/div[@class='text']")

    # Taxi rate
    taxi_rate_work = (By.XPATH, "(.//div[@class='tariff-cards']/div)[1]")
    taxi_rate_sleep = (By.XPATH, "(.//div[@class='tariff-cards']/div)[2]")
    taxi_rate_vacation = (By.XPATH, "(.//div[@class='tariff-cards']/div)[3]")
    taxi_rate_talk = (By.XPATH, "(.//div[@class='tariff-cards']/div)[4]")
    taxi_rate_consoling = (By.XPATH, "(.//div[@class='tariff-cards']/div)[5]")
    taxi_rate_glossy = (By.XPATH, "(.//div[@class='tariff-cards']/div)[6]")

    # Taxi rate i_icon buttons
    taxi_rate_work_i_icon = (By.XPATH, "(.//button[@class='i-button tcard-i active'])[1]")
    taxi_rate_sleep_i_icon = (By.XPATH, "(.//button[@class='i-button tcard-i active'])[2]")
    taxi_rate_vacation_i_icon = (By.XPATH, "(.//button[@class='i-button tcard-i active'])[3]")
    taxi_rate_talk_i_icon = (By.XPATH, "(.//button[@class='i-button tcard-i active'])[4]")
    taxi_rate_consolling_i_icon = (By.XPATH, "(.//button[@class='i-button tcard-i active'])[5]")
    taxi_rate_glossy_i_icon = (By.XPATH, "(.//button[@class='i-button tcard-i active'])[6]")

    # Taxi rate i_icon describe
    taxi_rate_work_i_icon_describe = (By.XPATH, "(.//div[@class='i-dPrefix'])[1]")
    taxi_rate_sleep_i_icon_describe = (By.XPATH, "(.//div[@class='i-dPrefix'])[2]")
    taxi_rate_vacation_i_icon_describe = (By.XPATH, "(.//div[@class='i-dPrefix'])[3]")
    taxi_rate_talk_i_icon_describe = (By.XPATH, "(.//div[@class='i-dPrefix'])[4]")
    taxi_rate_consolling_i_icon_describe = (By.XPATH, "(.//div[@class='i-dPrefix'])[5]")
    taxi_rate_glossy_i_icon_describe = (By.XPATH, "(.//div[@class='i-dPrefix'])[6]")

    # Taxi form
    taxi_form_number = (By.XPATH, ".//div[@class='np-text' and text()='Телефон']")
    taxi_form_number_modal = (By.XPATH, ".//input[@id='phone']")
    taxi_form_number_modal_accept = (By.XPATH, ".//button[@class='button full' and text()='Далее']")
    taxi_form_payment_method = (By.XPATH, ".//div[@class='pp-text' and text()='Способ оплаты']")
    taxi_form_driver_comment = (By.XPATH, ".//input[@id='comment']")
    taxi_form_order_requirements = (By.XPATH, ".//div[@class='reqs-head' and text()='Требования к заказу']")
    taxi_form_call_taxi_button = (By.XPATH, ".//div[@class='smart-button-wrapper']/button[@class='smart-button']")
    taxi_form_desk_for_desktop_toggle_activate = (By.XPATH, ".//span[@class='slider round']")

    # Drive rate
    drive_rate_daily = (By.XPATH, "(.//div[@class='tariff-cards']/div)[1]")
    drive_rate_expedition = (By.XPATH, "(.//div[@class='tariff-cards']/div)[2]")
    drive_rate_luxurious = (By.XPATH, "(.//div[@class='tariff-cards']/div)[3]")

    # Drive form
    drive_form_add_driver_licence = (By.XPATH, "(.//div[@class='np-text' and text()='Добавить права']")
    drive_form_payment_method = (By.XPATH, "(.//div[@class='pp-text' and text()='Способ оплаты']")
    drive_form_order_requirements = (By.XPATH, "(.//div[@class='reqs-head' and text()='Требования к заказу']")

    # Checks
    free_ride_auto_cost = (By.XPATH, ".//div[@class='results-text']/div[@class='text' and text()='Авто Бесплатно']")
    free_ride_duration = (By.XPATH, ".//div[text()='В пути 0 мин.']")
    taxi_search_car_check = (By.XPATH, ".//div[@class='order-header-title' and text()='Поиск машины']")
    taxi_details_button = (By.XPATH, "(.//div[@class='order-btn-group'])[2]")
    taxi_cancel_button = (By.XPATH, "(.//div[@class='order-btn-group'])[1]")
    taxi_details_cost = (By.XPATH, "(.//div[@class='o-d-sh'])[last()]")
    taxi_success_modal_title = (By.XPATH, ".//div[@class='order-header-title']")
    taxi_success_modal_rating = (By.XPATH, ".//div[@class='order-btn-rating']")