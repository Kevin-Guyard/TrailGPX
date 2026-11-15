from sqlalchemy import CheckConstraint, ForeignKey, Index, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .. import Base


class Folder(Base):
    """Represent a folder in the database hierarchy.

    Attributes
    ----------
    id : int
        Primary key of the folder.
    name : str
        Folder name, limited to 100 characters and unique within its parent.
    parents_id : int or None
        Foreign key of the parent folder, or None for a root folder.
    parents : Folder or None
        Parent folder, or None for a root folder.
    """

    __tablename__: str = "folder"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    parents_id: Mapped[int | None] = mapped_column(ForeignKey("folder.id"))
    parents: Mapped[Folder | None] = relationship(remote_side=[id])

    __table_args__: tuple[CheckConstraint | Index, ...] = (
        CheckConstraint("length(name) <= 100", name="folder_name_length"),
        Index("folder_parent_name_unique", parents_id, name, unique=True),
        # SQLite treats NULL values as distinct, so root names need a separate index.
        Index(
            "folder_root_name_unique",
            name,
            unique=True,
            sqlite_where=parents_id.is_(None),
        ),
        CheckConstraint(
            "parents_id IS NULL OR parents_id <> id",
            name="folder_not_own_parent",
        ),
    )
