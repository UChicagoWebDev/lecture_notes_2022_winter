-- create table posts_and_comments (
--   id INT AUTO_INCREMENT PRIMARY KEY,
--   title VARCHAR(255),
--   slug VARCHAR(30),
--   body TEXT,
--   author VARCHAR(30),
--   post_id INT
-- );

use weblog;

-- migrate the posts first

insert into posts_and_comments (id, slug, title, body)
select id, slug, title, body
from posts;

-- then migrate the comments

insert into posts_and_comments (body, author, post_id)
select body, author, post_id
from comments;
