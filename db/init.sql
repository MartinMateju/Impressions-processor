CREATE DATABASE MYSQLTEST;
-- CREATE DATABASE knights;
-- use knights;

CREATE TABLE favorite_colors (
  name VARCHAR(20),
  color VARCHAR(10)
);

-- INSERT INTO favorite_colors
--   (name, color)
-- VALUES
--   ('Lancelot', 'blue'),
--   ('Galahad', 'yellow');

CREATE TABLE impressions (
  impressionTime DATETIME,
  impressionId INT,
  adId INT,
  visitorHash VARCHAR(100)
);


CREATE TABLE clicks (
    clickTimestamp DATETIME,
    impressionId INT
);


INSERT INTO clicks
  (clickTimestamp, impressionId)
VALUES
  ('2021-04-20 10:50:07', 2);


INSERT INTO impressions
  (impressionTime, impressionId, adId, visitorHash)
VALUES
  ('2021-04-20 10:48:07', 1, 2, '8VTYLnaJZW7dfQH72tPXAbvyNIWeWLU7');


