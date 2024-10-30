CREATE DATABASE CourseworkMaterial;

USE CourseworkMaterial;

-- Table to store user information
CREATE TABLE IF NOT EXISTS Users (
    SRN VARCHAR(20) PRIMARY KEY,
    Username VARCHAR(50) NOT NULL,
    Password VARCHAR(64) NOT NULL
);


INSERT INTO Users (SRN, Username, Password) 
VALUES ('PES2UG22CS546', 'JohnDoe', SHA2('password123', 256));



-- -- Table to store course information
-- CREATE TABLE Courses (
--     CourseID INT AUTO_INCREMENT PRIMARY KEY,
--     CourseName VARCHAR(100) NOT NULL,
--     Description TEXT,
--     CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
-- );

-- -- Table to store study materials
-- CREATE TABLE Materials (
--     MaterialID INT AUTO_INCREMENT PRIMARY KEY,
--     CourseID INT,
--     UploadedBy INT,
--     FilePath VARCHAR(255) NOT NULL,
--     CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
--     FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE,
--     FOREIGN KEY (UploadedBy) REFERENCES Users(UserID) ON DELETE CASCADE
-- );

-- -- Table to store assignments
-- CREATE TABLE Assignments (
--     AssignmentID INT AUTO_INCREMENT PRIMARY KEY,
--     CourseID INT,
--     Title VARCHAR(100) NOT NULL,
--     Description TEXT,
--     DueDate DATETIME NOT NULL,
--     CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
--     FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE
-- );

-- -- Table to store student submissions for assignments
-- CREATE TABLE Submissions (
--     SubmissionID INT AUTO_INCREMENT PRIMARY KEY,
--     AssignmentID INT,
--     StudentID INT,
--     FilePath VARCHAR(255) NOT NULL,
--     SubmittedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
--     Grade ENUM('A', 'B', 'C', 'D', 'F'),
--     Feedback TEXT,
--     FOREIGN KEY (AssignmentID) REFERENCES Assignments(AssignmentID) ON DELETE CASCADE,
--     FOREIGN KEY (StudentID) REFERENCES Users(UserID) ON DELETE CASCADE
-- );

-- -- Table to store notifications
-- CREATE TABLE Notifications (
--     NotificationID INT AUTO_INCREMENT PRIMARY KEY,
--     UserID INT,
--     Message TEXT NOT NULL,
--     CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
--     IsRead BOOLEAN DEFAULT FALSE,
--     FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE
-- );

-- -- Table to store discussion forums
-- CREATE TABLE Forums (
--     ForumID INT AUTO_INCREMENT PRIMARY KEY,
--     CourseID INT,
--     CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
--     FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE
-- );

-- -- Table to store posts in discussion forums
-- CREATE TABLE ForumPosts (
--     PostID INT AUTO_INCREMENT PRIMARY KEY,
--     ForumID INT,
--     PostedBy INT,
--     Content TEXT NOT NULL,
--     CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
--     FOREIGN KEY (ForumID) REFERENCES Forums(ForumID) ON DELETE CASCADE,
--     FOREIGN KEY (PostedBy) REFERENCES Users(UserID) ON DELETE CASCADE
-- );
