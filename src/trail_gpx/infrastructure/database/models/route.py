from sqlalchemy import CheckConstraint, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .. import Base
from .folder import Folder


class Route(Base):
    """Represent a route and its summary metrics in the database.

    Attributes
    ----------
    id : int
        Primary key of the route.
    name : str
        Route name, limited to 100 characters.
    folder_id : int or None
        Foreign key of the containing folder, or None for an unfiled route.
    folder : Folder or None
        Containing folder, or None for an unfiled route.
    distance_km : float
        Non-negative route distance in kilometers.
    elevation_gain_m : int
        Non-negative cumulative elevation gain in meters.
    elevation_loss_m : int
        Non-negative cumulative elevation loss in meters.
    map_weight : float
        Weight associated with the route on the map; defaults to 0.0 on insert.
    """

    __tablename__: str = "route"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    folder_id: Mapped[int | None] = mapped_column(ForeignKey("folder.id"))
    folder: Mapped[Folder | None] = relationship()
    distance_km: Mapped[float] = mapped_column(nullable=False)
    elevation_gain_m: Mapped[int] = mapped_column(nullable=False)
    elevation_loss_m: Mapped[int] = mapped_column(nullable=False)
    map_weight: Mapped[float] = mapped_column(nullable=False, default=0.0)

    # Enforce name length and non-negative metrics at the database level.
    __table_args__: tuple[CheckConstraint, ...] = (
        CheckConstraint("length(name) <= 100", name="route_name_length"),
        CheckConstraint("distance_km >= 0", name="route_distance_km_non_negative"),
        CheckConstraint("elevation_gain_m >= 0", name="route_elevation_gain_m_non_negative"),
        CheckConstraint("elevation_loss_m >= 0", name="route_elevation_loss_m_non_negative"),
    )
