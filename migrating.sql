/* Migrate data from original database to new schema */

-- Users:
INSERT INTO users (username)
SELECT DISTINCT username
 FROM bad_posts

        UNION

INSERT INTO users (username)
SELECT DISTINCT username
 FROM bad_comments;


-- Topics:
INSERT INTO topics (name)
SELECT DISTINCT b.topic
 FROM bad_posts b;


-- Posts:
INSERT INTO posts (
        user_id, 
        id, 
        title, 
        topic,
        url,
        text_content
)
SELECT u.id user_id, 
       b.id post_id, 
       SUBSTRING(b.title, 1, 100),
       b.topic, 
       b.url, 
       b.text_content
 FROM users u
 JOIN bad_posts b
 ON b.username = u.username;


-- Comments:
INSERT INTO comments (user_id, post_id, text_content)
SELECT u.id, b.id, b.text_content
 FROM users u
 JOIN bad_posts b
 ON u.username = b.username;


-- Votes

WITH vote_table AS (
        SELECT id, 
               REGEXP_SPLIT_TO_TABLE("upvotes", ',') username,
               1 AS vote
         FROM bad_posts

                UNION
        
        SELECT id, 
               REGEXP_SPLIT_TO_TABLE("downvotes", ',') username,
               -1 AS vote
         FROM bad_posts
)
INSERT INTO votes (post_id, user_id, value)
SELECT DISTINCT v.id, p.user_id, v.vote
 FROM vote_table v
 JOIN posts p
 ON p.id = v.id;
