import allure
from selene import browser, have


class CartPage:
    def add_product_to_cart(self):
        with allure.step('Добавить товар в корзину.'):
            browser.element('.cart-button').click()

    def move_to_cart(self):
        with allure.step('Перейти в корзину.'):
            browser.element('.mv-main-button--content').element_by(have.text('В корзину')).click()

    def remove_product_from_cart(self):
        with allure.step('Удалить продукт из корзины.'):
            browser.all('[type="button"]').element_by(have.text('Удалить')).click()

    def clear_cart(self):
        with allure.step('Очистить корзину.'):
            browser.element('.cart-list__delete-selected-button').click()

    def check_product_in_cart(self, product_name):
        with allure.step('Проверить продукт в корзине.'):
            browser.element('.cart-item__name').should(have.exact_text(product_name))

    def check_empty_cart(self):
        with allure.step('Проверить, что корзина пустая.'):
            browser.all('.cart-empty__title').first.should(have.exact_text("Корзина пуста"))


cart_page = CartPage()
