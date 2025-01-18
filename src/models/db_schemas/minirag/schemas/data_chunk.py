from .minirag_base import SQLAlchemyBase
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, DateTime, func, ForeignKey, Index
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import relationship
import uuid

class DataChunk(SQLAlchemyBase):
    __tablename__ = "data_chunks"
    chunk_id = Column(Integer, primary_key=True, autoincrement=True)
    chunk_uuid = Column(UUID(as_uuid=True), unique=True, default=uuid.uuid4, nullable=False)

    chunk_text = Column(String, nullable=False)
    chunk_metadata = Column(JSONB, nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), nullable=False)

    chunk_project_id = Column(Integer, ForeignKey("projects.project_id"), nullable=False)
    project = relationship("Project", back_populates="data_chunks")
    
    chunk_asset_id = Column(Integer, ForeignKey("assets.asset_id"), nullable=False)
    asset = relationship("Asset", back_populates="data_chunks")


    __table_args__ = (
        Index("idx_chunk_asset_id", chunk_asset_id),
        Index("idx_chunk_project_id", chunk_project_id),
    )
    
class RetrievedDocument(BaseModel):
    text: str
    score: float