"""Price calculation."""

from shop.models import Cart


class PriceCalculator:
    """Adds tax to a cart's subtotal."""

    def __init__(self, tax_percent: int) -> None:
        self.tax_percent = tax_percent

    def tax_cents(self, cart: Cart) -> int:
        """Return the tax on the cart's subtotal."""
        return cart.subtotal_cents() * self.tax_percent // 100

    def total_cents(self, cart: Cart) -> int:
        """Return the cart total including tax."""
        return cart.subtotal_cents() + self.tax_cents(cart)
