# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, Text, text
from sqlalchemy.ext.declarative import declarative_base
from api import Base


metadata = Base.metadata


class AiweiCampaignEnroll(Base):
    __tablename__ = 'aiwei_campaign_enroll'

    id = Column(Integer, primary_key=True, server_default=text("nextval('aiwei_campaign_enroll_id_seq'::regclass)"))
    name = Column(Text)
    phone = Column(Text)
    age = Column(Integer)
    created_at = Column(DateTime)
