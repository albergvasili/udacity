/* Create DDL for new schema */

-- Users:
CREATE TABLE users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(25) NOT NULL,
        last_login DATE,
        CONSTRAINT "unique_username" UNIQUE (username)
);


-- Topics:
CREATE TABLE topics (
        id SERIAL PRIMARY KEY,
        user_id INTEGER NOT NULL
          REFERENCES users (id),
        name VARCHAR(30) NOT NULL,
        description VARCHAR(500) DEFAULT NULL,
        CONSTRAINT "unique_name" UNIQUE (name)
);

CREATE INDEX "topic_name" ON topics (name);


-- Posts:
CREATE TABLE posts (
        id SERIAL,
        user_id INTEGER 
          REFERENCES users (id) ON DELETE SET NULL, 
        title VARCHAR(100) NOT NULL,
        topic VARCHAR(30) NOT NULL
          REFERENCES topics (name) ON DELETE CASCADE,
        url VARCHAR(4000),
        text_content TEXT,
        post_date TIMESTAMP,
        CONSTRAINT "unique_id_posts" UNIQUE (id)
);

ALTER TABLE posts
  ADD CONSTRAINT "url_or_text_check" 
   CHECK (url IS NOT NULL OR text_content IS NOT NULL),
  ADD CONSTRAINT "posts_composite_primary_key" PRIMARY KEY (id, user_id);

CREATE INDEX "post_topic" ON posts (topic);
CREATE INDEX "post_by_user" ON posts (user_id);


-- Comments:
CREATE TABLE comments (
        id SERIAL,
        post_id INTEGER NOT NULL 
          REFERENCES posts (id) ON DELETE CASCADE,
        user_id INTEGER 
          REFERENCES users (id) ON DELETE SET NULL, 
        text_content TEXT NOT NULL,
        parent_comment INTEGER,
        CONSTRAINT "unique_comments_id" UNIQUE (id)
);

ALTER TABLE comments
  ADD CONSTRAINT "comments_composite_key" 
   PRIMARY KEY (id, post_id, user_id);

CREATE INDEX "parent_comment" ON comments (parent_comment);


-- Votes:
CREATE TABLE votes (
        post_id INTEGER NOT NULL
          REFERENCES posts (id) ON DELETE CASCADE,
        user_id INTEGER 
          REFERENCES users (id) ON DELETE SET NULL,
        value INTEGER,
        CONSTRAINT "unique_vote" UNIQUE (post_id, user_id)
);

ALTER TABLE votes
  ADD CONSTRAINT "votes_composite_key" 
   PRIMARY KEY (post_id, user_id),
  ADD CONSTRAINT "up_or_down_vote_check" 
   CHECK (value IN (-1, 1));
