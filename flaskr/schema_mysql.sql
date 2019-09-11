CREATE TABLE user(
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    username char(30) UNIQUE NOT NULL,
    password char(20) NOT NULL
);

CREATE TABLE post(
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    author_id INTEGER NOT NULL,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    title varchar(100) NOT NULL,
    body varchar(4000) NOT NULL,
    FOREIGN KEY (author_id) REFERENCES user(id)
);

