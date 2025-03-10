from sqlalchemy import Column, Integer, Sequence, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy import UniqueConstraint
from lcfs.db.base import BaseModel, Auditable, EffectiveDates

class Comment(BaseModel, Auditable, EffectiveDates):
    __tablename__ = 'comment'
    __table_args__ = (UniqueConstraint('comment_id'),
                      {'comment': "Comment for transaction"}
    )


    comment_id = Column(Integer, Sequence('issuance_id'), comment="Unique identifier for comment", primary_key=True, autoincrement=True)
    comment = Column(String(500), comment="Transfer category")

    transfer = relationship('Transfer', back_populates='comments')
    issuance = relationship('Issuance', back_populates='comments')


    def __repr__(self):
        return self.comment

