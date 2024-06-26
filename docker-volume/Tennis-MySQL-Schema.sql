CREATE TABLE `MatchEventInfo` (
  `match_id` integer NOT NULL PRIMARY KEY,
  `first_to_serve` integer,
  `home_team_seed` integer,
  `away_team_seed` integer,
  `custom_id` integer,
  `winner_code` integer,
  `default_period_count` integer,
  `start_datetime` integer,
  `match_slug` varchar(255),
  `final_result_only` boolean
);

CREATE TABLE `PeriodInfo` (
  `match_id` integer NOT NULL PRIMARY KEY,
  `period` varchar(255),
  `statistic_category_name` varchar(255),
  `statistic_name` varchar(255),
  `home_stat` varchar(255),
  `away_stat` varchar(255),
  `compare_code` integer,
  `statistic_type` varchar(255),
  `value_type` varchar(255),
  `home_value` integer,
  `away_value` integer,
  `home_total` integer,
  `away_total` integer
);

CREATE TABLE `MatchVotesInfo` (
  `match_id` integer NOT NULL PRIMARY KEY,
  `home_vote` integer,
  `away_vote` integer
);

CREATE TABLE `MatchTournamentInfo` (
  `match_id` integer NOT NULL PRIMARY KEY,
  `tournament_id` integer,
  `tournament_name` varchar(255),
  `tournament_slug` varchar(255),
  `tournament_unique_id` integer,
  `tournament_category_name` varchar(255),
  `tournament_category_slug` varchar(255),
  `user_count` integer,
  `ground_type` varchar(255),
  `tennis_points` integer,
  `has_event_player_statistics` boolean,
  `crowd_sourcing_enabled` boolean,
  `has_performance_graph_feature` boolean,
  `display_inverse_home_away_teams` boolean,
  `priority` integer,
  `competition_type` integer
);

CREATE TABLE `MatchSeasonInfo` (
  `match_id` integer NOT NULL PRIMARY KEY,
  `season_id` integer,
  `name` integer,
  `year` integer
);

CREATE TABLE `MatchRoundInfo` (
  `match_id` integer NOT NULL PRIMARY KEY,
  `round_id` integer,
  `name` varchar(255),
  `slug` varchar(255),
  `cup_round_type` integer
);

CREATE TABLE `MatchVenueInfo` (
  `match_id` integer NOT NULL PRIMARY KEY,
  `city` varchar(255),
  `stadium` varchar(255),
  `venue_id` integer,
  `country` varchar(255)
);

CREATE TABLE `MatchHomeTeamInfo` (
  `match_id` integer NOT NULL PRIMARY KEY,
  `name` varchar(255),
  `slug` varchar(255),
  `gender` varchar(255),
  `user_count` integer,
  `residence` varchar(255),
  `birthplace` varchar(255),
  `height` float,
  `weight` integer,
  `plays` varchar(255),
  `turned_pro` integer,
  `current_prize` integer,
  `total_prize` integer,
  `player_id` integer,
  `current_rank` integer,
  `name_code` varchar(255),
  `country` varchar(255),
  `full_name` varchar(255)
);

CREATE TABLE `MatchAwayTeamInfo` (
  `match_id` integer NOT NULL PRIMARY KEY,
  `name` varchar(255),
  `slug` varchar(255),
  `gender` varchar(255),
  `user_count` integer,
  `residence` varchar(255),
  `birthplace` varchar(255),
  `height` float,
  `weight` integer,
  `plays` varchar(255),
  `turned_pro` integer,
  `current_prize` integer,
  `total_prize` integer,
  `player_id` integer,
  `current_rank` integer,
  `name_code` varchar(255),
  `country` varchar(255),
  `full_name` varchar(255)
);

CREATE TABLE `MatchHomeScoreInfo` (
  `match_id` integer NOT NULL PRIMARY KEY,
  `current_score` integer,
  `display_score` integer,
  `period_1` integer,
  `period_2` integer,
  `period_3` integer,
  `period_4` integer,
  `period_5` integer,
  `period_1_tie_break` integer,
  `period_2_tie_break` integer,
  `period_3_tie_break` integer,
  `period_4_tie_break` integer,
  `period_5_tie_break` integer,
  `normal_time` integer
);

CREATE TABLE `MatchAwayScoreInfo` (
  `match_id` integer NOT NULL PRIMARY KEY,
  `current_score` integer,
  `display_score` integer,
  `period_1` integer,
  `period_2` integer,
  `period_3` integer,
  `period_4` integer,
  `period_5` integer,
  `period_1_tie_break` integer,
  `period_2_tie_break` integer,
  `period_3_tie_break` integer,
  `period_4_tie_break` integer,
  `period_5_tie_break` integer,
  `normal_time` integer
);

CREATE TABLE `MatchTimeInfo` (
  `match_id` integer NOT NULL PRIMARY KEY,
  `period_1` integer,
  `period_2` integer,
  `period_3` integer,
  `period_4` integer,
  `period_5` integer,
  `current_period_start_timestamp` integer
);

CREATE TABLE `GameInfo` (
  `match_id` integer NOT NULL PRIMARY KEY,
  `set_id` integer,
  `game_id` integer,
  `point_id` integer,
  `home_point` varchar(255),
  `away_point` varchar(255),
  `point_description` integer,
  `home_point_type` integer,
  `away_point_type` integer,
  `home_score` integer
);

CREATE TABLE `OddsInfo` (
  `match_id` integer NOT NULL PRIMARY KEY,
  `market_id` integer,
  `market_name` varchar(255),
  `is_live` boolean,
  `suspended` boolean,
  `initial_fractional_value` varchar(255),
  `fractional_value` varchar(255),
  `choice_name` varchar(255),
  `choice_source_id` integer,
  `winnig` boolean,
  `change` integer
);

CREATE TABLE `PowerInfo` (
  `match_id` integer NOT NULL PRIMARY KEY,
  `set_num` integer,
  `game_num` integer,
  `value` float,
  `break_occurred` boolean
);

ALTER TABLE `MatchTournamentInfo` ADD FOREIGN KEY (`match_id`) REFERENCES `MatchEventInfo` (`match_id`);

ALTER TABLE `MatchVotesInfo` ADD FOREIGN KEY (`match_id`) REFERENCES `MatchEventInfo` (`match_id`);

ALTER TABLE `MatchSeasonInfo` ADD FOREIGN KEY (`match_id`) REFERENCES `MatchEventInfo` (`match_id`);

ALTER TABLE `MatchRoundInfo` ADD FOREIGN KEY (`match_id`) REFERENCES `MatchEventInfo` (`match_id`);

ALTER TABLE `MatchVenueInfo` ADD FOREIGN KEY (`match_id`) REFERENCES `MatchEventInfo` (`match_id`);

ALTER TABLE `MatchHomeTeamInfo` ADD FOREIGN KEY (`match_id`) REFERENCES `MatchEventInfo` (`match_id`);

ALTER TABLE `MatchAwayTeamInfo` ADD FOREIGN KEY (`match_id`) REFERENCES `MatchEventInfo` (`match_id`);

ALTER TABLE `MatchHomeScoreInfo` ADD FOREIGN KEY (`match_id`) REFERENCES `MatchEventInfo` (`match_id`);

ALTER TABLE `MatchAwayScoreInfo` ADD FOREIGN KEY (`match_id`) REFERENCES `MatchEventInfo` (`match_id`);

ALTER TABLE `MatchTimeInfo` ADD FOREIGN KEY (`match_id`) REFERENCES `MatchEventInfo` (`match_id`);

ALTER TABLE `GameInfo` ADD FOREIGN KEY (`match_id`) REFERENCES `MatchEventInfo` (`match_id`);

ALTER TABLE `OddsInfo` ADD FOREIGN KEY (`match_id`) REFERENCES `MatchEventInfo` (`match_id`);

ALTER TABLE `PowerInfo` ADD FOREIGN KEY (`match_id`) REFERENCES `MatchEventInfo` (`match_id`);

ALTER TABLE `PeriodInfo` ADD FOREIGN KEY (`match_id`) REFERENCES `MatchEventInfo` (`match_id`);


-- 
CREATE TABLE Players (
    `id` INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(255),
    `slug` VARCHAR(255),
    `gender` VARCHAR(1),
    `user_count` INTEGER,
    `residence` VARCHAR(255),
    `birthplace` VARCHAR(100),
    `height` FLOAT,
    `weight` INTEGER,
    `plays` VARCHAR(50),
    `turned_pro` INTEGER,
    `current_prize` INTEGER,
    `total_prize` INTEGER,
    `player_id` INTEGER,
    `current_rank` INTEGER,
    `name_code` VARCHAR(10),
    `country` VARCHAR(20),
    `full_name` VARCHAR(50)
); CREATE INDEX slug_index ON players (slug);

