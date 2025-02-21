from .minirag_base import SQLAlchemyBase
from sqlalchemy import Column, Integer, DateTime, func
from sqlalchemy.dialects.postgresql import UUID
import uuid
from sqlalchemy.orm import relationship

class Project(SQLAlchemyBase):
    __tablename__ = "projects"
    project_id = Column(Integer, primary_key=True, autoincrement=True)
    project_uuid = Column(UUID(as_uuid=True), unique=True, default=uuid.uuid4, nullable=False)

    project_created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    project_updated_at = Column(DateTime(timezone=True), onupdate=func.now(), nullable=False)

    chunks = relationship("DataChunk", back_populates="project")
    assets = relationship("Asset", back_populates="project")