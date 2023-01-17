from model.user import User
from settings import session

# 起動させるたびにデータが増え続けてしまうため、Userテーブルのデータは全て消す
session.query(User).delete()

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
