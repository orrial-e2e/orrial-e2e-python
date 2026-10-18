"""Entry point: build a cart and print its total."""

from shop.models import Cart, Product
from shop.pricing import PriceCalculator


def main() -> None:
    """Create a cart with two products and print the total."""
    cart = Cart()
    cart.add(Product(name="notebook", price_cents=450), quantity=2)
    cart.add(Product(name="pen", price_cents=120), quantity=5)
    calculator = PriceCalculator(tax_percent=23)
    print(f"Total: {calculator.total_cents(cart)} cents")

if __name__ == "__main__":
    main()
