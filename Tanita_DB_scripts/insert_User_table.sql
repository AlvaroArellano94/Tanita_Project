INSERT INTO Users(User_name, User_surnames, Gender, Age, Height, File_name) VALUES ('Álvaro', 'Arellano Navarro', 'Male', 28, 1.80,'DATA2.CSV');
INSERT INTO Users(User_name, User_surnames, Gender, Age, Height, File_name)  VALUES ('Ana', 'González Tejerina', 'Female', 28, 1.65,'DATA1.CSV');

select * from Users;

#delete statement to delete test rows
DELETE FROM Users WHERE (User_id = 6 or User_id = 7 or User_id = 9)  