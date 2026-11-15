from pathlib import Path
from sqlite3 import Connection, Cursor
from typing import Literal

from sqlalchemy import URL, Engine, create_engine, event
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.pool import ConnectionPoolEntry

from .base import Base
from . import models


def _enable_foreign_keys(
    connection: Connection,
    connection_record: ConnectionPoolEntry,
) -> None:
    """Enable SQLite foreign key enforcement on a new pooled connection.

    Parameters
    ----------
    connection : sqlite3.Connection
        Newly opened connection whose autocommit mode is restored afterward.
    connection_record : sqlalchemy.pool.ConnectionPoolEntry
        Pool entry supplied by SQLAlchemy's connect event; unused here.
    """
    previous_autocommit: bool | Literal[-1] = connection.autocommit
    # SQLite ignores this PRAGMA inside a transaction, so enable autocommit first.
    connection.autocommit = True
    try:
        cursor: Cursor = connection.execute("PRAGMA foreign_keys=ON")
        cursor.close()
    finally:
        connection.autocommit = previous_autocommit


def initialize_database(database_path: Path) -> sessionmaker[Session]:
    """Create the SQLite schema and return a configured session factory.

    Parameters
    ----------
    database_path : pathlib.Path
        SQLite database file path. Missing parent directories are created.

    Returns
    -------
    sqlalchemy.orm.sessionmaker[sqlalchemy.orm.Session]
        Factory bound to an engine that enforces foreign keys. Sessions keep
        loaded attribute values after a commit.

    Notes
    -----
    Tables registered in ``Base.metadata`` are created if missing. If schema
    creation fails, the engine is disposed and the exception is propagated.
    """
    database_path.parent.mkdir(parents=True, exist_ok=True)

    engine: Engine = create_engine(
        URL.create("sqlite+pysqlite", database=str(database_path)),
        connect_args={"autocommit": False},
    )
    event.listen(engine, "connect", _enable_foreign_keys)

    try:
        Base.metadata.create_all(engine)
    except Exception:
        engine.dispose()
        raise

    return sessionmaker(bind=engine, expire_on_commit=False)
