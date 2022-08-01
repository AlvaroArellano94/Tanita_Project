CREATE TABLE IF NOT EXISTS Body_Composition (
    User_id INT,
    Body_mass DECIMAL(4,1) NOT NULL,
    Body_mass_index DECIMAL(4,1) NOT NULL,
    Global_fat_percentage DECIMAL(4,1) NOT NULL,
    Fat_right_arm_perc DECIMAL(4,1) NOT NULL,
    Fat_left_arm_perc DECIMAL(4,1) NOT NULL,
    Fat_right_leg_perc DECIMAL(4,1) NOT NULL,
    Fat_left_leg_perc DECIMAL(4,1) NOT NULL,
    Fat_torso_perc DECIMAL(4,1) NOT NULL,
    Global_muscle_perc DECIMAL(4,1) NOT NULL,
    Muscle_right_arm_perc DECIMAL(4,1) NOT NULL,
    Muscle_left_arm_perc DECIMAL(4,1) NOT NULL,
    Muscle_right_leg_perc DECIMAL(4,1) NOT NULL,
    Muscle_left_leg_perc DECIMAL(4,1) NOT NULL,
    Muscle_torso_perc DECIMAL(4,1) NOT NULL,
    Bone_mass_estimated DECIMAL(4,1) NOT NULL,
    Fat_visceral_rating TINYINT NOT NULL,
    Calory_intake_daily SMALLINT NOT NULL,
    Metabolic_age_estimated TINYINT NOT NULL,
    Global_body_water_perc DECIMAL(4,1) NOT NULL,
    Date_Measurement DATE,
    Time_Measurement TIME,
    FOREIGN KEY (User_id) REFERENCES Users(User_id),
    PRIMARY KEY (User_id, Date_Measurement, Time_Measurement)
);

#drop table Body_Composition;