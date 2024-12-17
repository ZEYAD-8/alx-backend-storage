-- creates a stored procedure ComputeAverageWeightedScoreForUser that computes and store the average weighted score for a student.

DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id_param INT)
BEGIN
    DECLARE total_weighted_score FLOAT;
    DECLARE total_weight INT;
    
    -- Initialize variables
    SET total_weighted_score = 0;
    SET total_weight = 0;
    
    -- Calculate weighted average for the given user_id
    SELECT 
        SUM(c.score * p.weight) AS total_weighted_score,
        SUM(p.weight) AS total_weight
    INTO 
        total_weighted_score, total_weight
    FROM corrections c
    JOIN projects p ON c.project_id = p.id
    WHERE c.user_id = user_id_param;

    -- Update the average_score for the user
    UPDATE users
    SET average_score = total_weighted_score / total_weight
    WHERE id = user_id_param;

END //

DELIMITER ;
