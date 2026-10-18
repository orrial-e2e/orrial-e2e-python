"""Data classes for the shop."""

from dataclasses import dataclass, field


@dataclass(frozen=True)
class Product:
    """A product with a price in cents."""

    name: str
    price_cents: int

@dataclass
class Cart:
    """A cart holding products and their quantities."""

    items: list[tuple[Product, int]] = field(default_factory=list)

    def add(self, product: Product, quantity: int = 1) -> None:
        """Add a product to the cart."""
        self.items.append((product, quantity))

    def subtotal_cents(self) -> int:
        """Return the cart total before tax."""
        return sum(product.price_cents * quantity for product, quantity in self.items)
