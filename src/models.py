from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, MetaData, Table, Boolean


metadata = MetaData()

# region User
users = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("email", String, unique=True, index=True),
    Column("hashed_password", String),
    Column("first_name", String),
    Column("surname", String),
    Column("is_active", Boolean, default=True),
    Column("is_superuser", Boolean, default=False),
    Column("is_verified", Boolean, default=False)
)

# endregion

# region Task
tasks = Table(
    "task",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("title", String),
    Column("description", String),
    Column("created_at", DateTime, default=datetime.utcnow()),
    Column("updated_at", DateTime, default=datetime.utcnow(), onupdate=datetime.utcnow()),
    Column("completed_at", DateTime),
    Column("status", String),
    Column("user_id", Integer, ForeignKey("user.id")),
)

# endregion
