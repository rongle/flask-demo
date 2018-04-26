#!/bin/sh

FILE="./api/models.py"

sqlacodegen postgresql://postgres@localhost/aiwei > $FILE
#sed -i '/from sqlalchemy.ext.decl/afrom flask.ext.login import UserMixin' $FILE
sed -i '/from sqlalchemy.ext.decl/afrom api import Base' $FILE
sed -i '/Base = declarative_base/d' $FILE
#sed -i 's/class Merchant(Base):/class Merchant(Base, UserMixin):/g' $FILE
#sed -i 's/class Staff(Base):/class Staff(Base, UserMixin):/g' $FILE
sed -i '/ARRAY(INTEGER())/s/INTEGER()/Integer/g' $FILE
