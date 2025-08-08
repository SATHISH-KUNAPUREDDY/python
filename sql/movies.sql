use sathish;

CREATE TABLE Movies (
    movie_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(255) NOT NULL,
    release_year YEAR NOT NULL,
    genre VARCHAR(100) NOT NULL,
    language VARCHAR(50) DEFAULT 'Telugu',
    duration_minutes INT NOT NULL,
    rating DECIMAL(3,1),
    director_id INT,
    FOREIGN KEY (director_id) REFERENCES Directors(director_id)
);

CREATE TABLE Directors (
    director_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    dob DATE,
    nationality VARCHAR(100),
    awards TEXT
);

CREATE TABLE Actors (
    actor_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    dob DATE,
    gender CHAR(1),
    nationality VARCHAR(100),
    debut_year YEAR
);

CREATE TABLE Movie_Cast (
    movie_id INT,
    actor_id INT,
    role_name VARCHAR(255),
    screen_time_minutes INT,
    FOREIGN KEY (movie_id) REFERENCES Movies(movie_id),
    FOREIGN KEY (actor_id) REFERENCES Actors(actor_id),
    PRIMARY KEY (movie_id, actor_id)
    );

CREATE TABLE Box_Office (
    movie_id INT,
    budget BIGINT,
    box_office_collection BIGINT,
    domestic_collection BIGINT,
    international_collection BIGINT,
    FOREIGN KEY (movie_id) REFERENCES Movies(movie_id),
    PRIMARY KEY (movie_id)
    );
    
    

INSERT INTO Movies (title, release_year, genre, duration_minutes, rating, director_id) VALUES
('Baahubali', 2015, 'Action', 160, 8.8, 1),
('Pushpa', 2021, 'Thriller', 179, 8.0, 2);

INSERT INTO Directors (name, dob, nationality, awards) VALUES
('Rajamouli', '1973-10-10', 'Indian', 'National Award'),
('Sukumar', '1970-01-02', 'Indian', 'Filmfare Award');

INSERT INTO Actors (name, dob, gender, nationality, debut_year) VALUES
('Prabhas', '1979-10-23', 'M', 'Indian', 2002),
('Allu Arjun', '1983-04-08', 'M', 'Indian', 2003);

INSERT INTO Movie_Cast (movie_id, actor_id, role_name, screen_time_minutes) VALUES
(1, 1, 'Amarendra Baahubali', 120),
(2, 2, 'Pushpa Raj', 140);

INSERT INTO Box_Office (movie_id, budget, box_office_collection, domestic_collection, international_collection) VALUES
(1, 1800000000, 6500000000, 4000000000, 2500000000),
(2, 1300000000, 3500000000, 2000000000, 1500000000);

select * from directors, actors;



