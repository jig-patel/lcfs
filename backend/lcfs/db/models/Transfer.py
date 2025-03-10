from sqlalchemy import Column, Integer, Sequence, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy import UniqueConstraint
from lcfs.db.base import BaseModel, Auditable, EffectiveDates

class Transfer(BaseModel, Auditable, EffectiveDates):
    __tablename__ = 'transfer'
    __table_args__ = (UniqueConstraint('transfer_id'),
                      {'comment': "Records of tranfer from Organization to Organization"}
    )


    transfer_id = Column(Integer, Sequence('issuance_id'), comment="Unique identifier for the org to org transfer record", primary_key=True, autoincrement=True)
    from_organization_id = Column(Integer, ForeignKey('organization.organization_id'))
    to_organization_id = Column(Integer, ForeignKey('organization.organization_id'))
    transaction_id = Column(Integer, ForeignKey('transaction.transaction_id'))
    transaction_effective_date = Column(DateTime, comment="transaction effective date")
    # compliance_period = Column(Integer, )
    comment_id = Column(Integer, ForeignKey('comment.comment_id'))
    transfer_status_id = Column(Integer, ForeignKey('transfer_status.transfer_status_id'))
    transfer_category_id = Column(Integer, ForeignKey('category.category_id'))

    category = relationship('Category')
    transaction = relationship('Transaction')
    transfer_status = relationship('TransferStatus')
    comments = relationship('Comment', back_populates='transfer')
    transfer_history_records = relationship('TransferHistory', back_populates='transfer')

    from_organization = relationship(
        'Organization', 
        foreign_keys=[from_organization_id]
    )
    to_organization = relationship(
        'Organization', 
        foreign_keys=[to_organization_id]
    )



