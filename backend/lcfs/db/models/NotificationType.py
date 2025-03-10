import enum
from lcfs.db.base import BaseModel, Auditable
from sqlalchemy import Column, Integer, Enum, Text

class NotificationTypeEnum(enum.Enum):
     CREDIT_TRANSFER_CREATED = "Credit Transfer Proposal Created"
     CREDIT_TRANSFER_SIGNED_1OF2 = "Credit Transfer Proposal Signed 1/2"
     CREDIT_TRANSFER_SIGNED_2OF2 = "Credit Transfer Proposal Signed 2/2"
     CREDIT_TRANSFER_PROPOSAL_REFUSED = "Credit Transfer Proposal Refused"
     CREDIT_TRANSFER_PROPOSAL_ACCEPTED = "Credit Transfer Proposal Accepted"
     CREDIT_TRANSFER_RECOMMENDED_FOR_APPROVAL = \
          "Credit Transfer Proposal Recommended For Approval"
     CREDIT_TRANSFER_RECOMMENDED_FOR_DECLINATION = \
          "Credit Transfer Proposal Recommended For Declination"
     CREDIT_TRANSFER_DECLINED = "Credit Transfer Proposal Declined"
     CREDIT_TRANSFER_APPROVED = "Credit Transfer Proposal Approved"
     CREDIT_TRANSFER_RESCINDED = "Credit Transfer Proposal Rescinded"
     CREDIT_TRANSFER_COMMENT = \
          "Credit Transfer Proposal Comment Created Or Updated"
     CREDIT_TRANSFER_INTERNAL_COMMENT = \
          "Credit Transfer Proposal Internal Comment Created Or Updated"

     PVR_CREATED = "PVR Created"
     PVR_RECOMMENDED_FOR_APPROVAL = "PVR Recommended For Approval"
     PVR_RESCINDED = "PVR Rescinded"
     PVR_PULLED_BACK = "PVR Pulled Back"
     PVR_DECLINED = "PVR Declined"
     PVR_APPROVED = "PVR Approved"
     PVR_COMMENT = "PVR Comment Created Or Updated"
     PVR_INTERNAL_COMMENT = "PVR Internal Comment Created Or Updated"
     PVR_RETURNED_TO_ANALYST = "PVR Returned to Analyst"

     DOCUMENT_PENDING_SUBMISSION = "Document Pending Submission"
     DOCUMENT_SUBMITTED = "Document Submitted"
     DOCUMENT_SCAN_FAILED = "Document Security Scan Failed"
     DOCUMENT_RECEIVED = "Document Received"
     DOCUMENT_ARCHIVED = "Document Archived"

     COMPLIANCE_REPORT_DRAFT = "Compliance Report Draft Saved"
     COMPLIANCE_REPORT_SUBMITTED = "Compliance Report Submitted"
     COMPLIANCE_REPORT_RECOMMENDED_FOR_ACCEPTANCE_ANALYST = \
          "Compliance Report Recommended for Acceptance - Analyst"
     COMPLIANCE_REPORT_RECOMMENDED_FOR_REJECTION_ANALYST = \
          "Compliance Report Recommended for Rejection - Analyst"
     COMPLIANCE_REPORT_RECOMMENDED_FOR_ACCEPTANCE_MANAGER = \
          "Compliance Report Recommended for Acceptance - Manager"
     COMPLIANCE_REPORT_RECOMMENDED_FOR_REJECTION_MANAGER = \
          "Compliance Report Recommended for Rejection - Manager"
     COMPLIANCE_REPORT_ACCEPTED = "Compliance Report Accepted"
     COMPLIANCE_REPORT_REJECTED = "Compliance Report Rejected"
     COMPLIANCE_REPORT_REQUESTED_SUPPLEMENTAL = \
          "Compliance Report Requested Supplemental"

     EXCLUSION_REPORT_DRAFT = "Exclusion Report Draft Saved"
     EXCLUSION_REPORT_SUBMITTED = "Exclusion Report Submitted"
     EXCLUSION_REPORT_RECOMMENDED_FOR_ACCEPTANCE_ANALYST = \
          "Exclusion Report Recommended for Acceptance - Analyst"
     EXCLUSION_REPORT_RECOMMENDED_FOR_REJECTION_ANALYST = \
          "Exclusion Report Recommended for Rejection - Analyst"
     EXCLUSION_REPORT_RECOMMENDED_FOR_ACCEPTANCE_MANAGER = \
          "Exclusion Report Recommended for Acceptance - Manager"
     EXCLUSION_REPORT_RECOMMENDED_FOR_REJECTION_MANAGER = \
          "Exclusion Report Recommended for Rejection - Manager"
     EXCLUSION_REPORT_ACCEPTED = "Exclusion Report Accepted"
     EXCLUSION_REPORT_REJECTED = "Exclusion Report Rejected"
     EXCLUSION_REPORT_REQUESTED_SUPPLEMENTAL = \
          "Exclusion Report Requested Supplemental"


class NotificationType(BaseModel, Auditable):
     __tablename__ = 'notification_type'
     __table_args__ = {'comment': "Represents a Notification type"}

     notification_type_id = Column(Integer, primary_key=True, autoincrement=True)
     name = Column(Enum(NotificationTypeEnum, name='notification_type_enum', create_type=True), nullable=False)
     description = Column(Text, nullable=True)
     email_content = Column(Text)