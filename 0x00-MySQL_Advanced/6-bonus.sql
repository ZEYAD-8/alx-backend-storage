-- Creates a stored procedure AddBonus that adds a new
-- correction for a student.
DROP procedure IF EXISTS AddBonus;
DELIMITER //
CREATE procedure AddBonus(user_id INT, project_name VARCHAR(255), score FLOAT)
BEGIN
    DECLARE project_id INT DEFAULT 0;
    DECLARE project_counts INT DEFAULT 0;

    SELECT COUNT(*) INTO project_counts FROM projects WHERE name = project_name;
    IF project_counts = 0 THEN
        INSERT INTO projects (name) VALUES (project_name);
    END IF;

    SELECT id 
    INTO project_id 
    FROM projects 
    WHERE name = project_name;
    INSERT INTO corrections (user_id, project_id, score) 
    VALUES (user_id, project_id, score);
END;
//
