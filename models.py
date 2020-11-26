from app import db #импорт склалкхими
from datetime import datetime #для таблицы керек нарсе ол
import re #чтобы норм слаги делать параметры ставим какие слаги можно какие нельзя


def slugify(s):
    pattern = r'[^\w+]'
    return re.sub(pattern, '-', s) #тут указывается что меняем переменная патерн на что на дифисы и на патрны мы указали что меняем пробелы потом меняем с помощью локальной переменной что мы передали снизу когда вызывали этот класс

post_tags = db.Table('post_tags',
                    db.Column('post_id', db.Integer, db.ForeignKey('post.id')),
                    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'))
    )

class Post(db.Model):#создаетм таблицуs
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    slug = db.Column(db.String(140), unique=True)
    body = db.Column(db.Text)
    created = db.Column(db.DateTime, default=datetime.now() ) #время тут

    def __init__(self, *args, **kwargs):
        super(Post, self).__init__(*args, **kwargs)
        self.generate_slug()

    tags = db.relationship('Tag', secondary=post_tags, backref=db.backref('posts', lazy='dynamic'))
    def generate_slug(self):#генерировать ссылки еогда мы пишем тайтл то то все идет в ссылку но это сылка через слаги фай редактируется убирается пробелы и заменяются дифизами
        if self.title:
            self.slug = slugify(self.title)

    def __repr__(self):#чтобы нормально создавалась таблица и можно было понимать его
        return '<Post id:{}, title: {}>'.format(self.id, self.title)


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    slug = db.Column(db.String(100))


    def __init__(self, *args, **kwargs):
        super(Tag, self).__init__(*args, **kwargs)
        self.slug = slugify(self.name)

    def __repr__(self):#чтобы нормально создавалась таблица и можно было понимать его
        return '<Tag id:{}, name: {}>'.format(self.id, self.name)
