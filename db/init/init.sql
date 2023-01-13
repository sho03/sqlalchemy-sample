create table if not exists user(
id int auto_increment primary key,
name varchar(30) not null,
email varchar(100)
);

insert into user (
    name, email
) values (
    'test', 'test@example.com'
);