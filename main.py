import sqlalchemy
from sqlalchemy.orm import sessionmaker
from model.user import User

user = 'user'
password = 'password'
db = 'db'
port = 3306

engine = sqlalchemy.create_engine(f'mysql+pymysql://{user}:{password}@localhost:{port}/{db}?charset=utf8')

SessionClass = sessionmaker(engine)
session = SessionClass()

new_user = User(name = "user1", email = "sample1@example.com")
# add ~ commitをすることでDBに反映される
session.add(new_user)
session.commit()

# 下記のように、連続してadd()を実行しても最後のcommit()で全てDBに反映される
user2 = User(name = "user2", email = "sample2@example.com")
user3 = User(name = "user3", email = "sample3@example.com")
session.add(user2)
session.add(user3)
session.commit()

# userテーブルのレコード全て取得
users = session.query(User).all()
print(users)

