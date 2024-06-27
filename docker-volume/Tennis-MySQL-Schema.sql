-- MariaDB dump 10.19-11.1.2-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: tennisdb
-- ------------------------------------------------------
-- Server version	11.1.2-MariaDB-1:11.1.2+maria~ubu2204

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `GameInfo`
--

DROP TABLE IF EXISTS `GameInfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `GameInfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `match_id` int(11) NOT NULL,
  `set_id` int(11) DEFAULT NULL,
  `game_id` int(11) DEFAULT NULL,
  `point_id` int(11) DEFAULT NULL,
  `home_point` varchar(255) DEFAULT NULL,
  `away_point` varchar(255) DEFAULT NULL,
  `point_description` int(11) DEFAULT NULL,
  `home_point_type` int(11) DEFAULT NULL,
  `away_point_type` int(11) DEFAULT NULL,
  `home_score` int(11) DEFAULT NULL,
  `away_score` int(11) DEFAULT NULL,
  `serving` int(11) DEFAULT NULL,
  `scoring` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1467014 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `MatchAwayScoreInfo`
--

DROP TABLE IF EXISTS `MatchAwayScoreInfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `MatchAwayScoreInfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `match_id` int(11) NOT NULL,
  `current_score` int(11) DEFAULT NULL,
  `display_score` int(11) DEFAULT NULL,
  `period_1` int(11) DEFAULT NULL,
  `period_2` int(11) DEFAULT NULL,
  `period_3` int(11) DEFAULT NULL,
  `period_4` int(11) DEFAULT NULL,
  `period_5` int(11) DEFAULT NULL,
  `period_1_tie_break` int(11) DEFAULT NULL,
  `period_2_tie_break` int(11) DEFAULT NULL,
  `period_3_tie_break` int(11) DEFAULT NULL,
  `period_4_tie_break` int(11) DEFAULT NULL,
  `period_5_tie_break` int(11) DEFAULT NULL,
  `normal_time` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19677 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `MatchAwayTeamInfo`
--

DROP TABLE IF EXISTS `MatchAwayTeamInfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `MatchAwayTeamInfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `match_id` int(11) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `slug` varchar(255) DEFAULT NULL,
  `gender` varchar(255) DEFAULT NULL,
  `user_count` int(11) DEFAULT NULL,
  `residence` varchar(255) DEFAULT NULL,
  `birthplace` varchar(255) DEFAULT NULL,
  `height` float DEFAULT NULL,
  `weight` int(11) DEFAULT NULL,
  `plays` varchar(255) DEFAULT NULL,
  `turned_pro` int(11) DEFAULT NULL,
  `current_prize` int(11) DEFAULT NULL,
  `total_prize` int(11) DEFAULT NULL,
  `player_id` int(11) DEFAULT NULL,
  `current_rank` int(11) DEFAULT NULL,
  `name_code` varchar(255) DEFAULT NULL,
  `country` varchar(255) DEFAULT NULL,
  `full_name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12956 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `MatchEventInfo`
--

DROP TABLE IF EXISTS `MatchEventInfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `MatchEventInfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `match_id` int(11) NOT NULL,
  `first_to_serve` int(11) DEFAULT NULL,
  `home_team_seed` varchar(20) DEFAULT NULL,
  `away_team_seed` varchar(20) DEFAULT NULL,
  `custom_id` varchar(50) DEFAULT NULL,
  `winner_code` int(11) DEFAULT NULL,
  `default_period_count` int(11) DEFAULT NULL,
  `start_datetime` int(11) DEFAULT NULL,
  `match_slug` varchar(255) DEFAULT NULL,
  `final_result_only` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19677 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `MatchHomeScoreInfo`
--

DROP TABLE IF EXISTS `MatchHomeScoreInfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `MatchHomeScoreInfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `match_id` int(11) NOT NULL,
  `current_score` int(11) DEFAULT NULL,
  `display_score` int(11) DEFAULT NULL,
  `period_1` int(11) DEFAULT NULL,
  `period_2` int(11) DEFAULT NULL,
  `period_3` int(11) DEFAULT NULL,
  `period_4` int(11) DEFAULT NULL,
  `period_5` int(11) DEFAULT NULL,
  `period_1_tie_break` int(11) DEFAULT NULL,
  `period_2_tie_break` int(11) DEFAULT NULL,
  `period_3_tie_break` int(11) DEFAULT NULL,
  `period_4_tie_break` int(11) DEFAULT NULL,
  `period_5_tie_break` int(11) DEFAULT NULL,
  `normal_time` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19677 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `MatchHomeTeamInfo`
--

DROP TABLE IF EXISTS `MatchHomeTeamInfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `MatchHomeTeamInfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `match_id` int(11) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `slug` varchar(255) DEFAULT NULL,
  `gender` varchar(255) DEFAULT NULL,
  `user_count` int(11) DEFAULT NULL,
  `residence` varchar(255) DEFAULT NULL,
  `birthplace` varchar(255) DEFAULT NULL,
  `height` float DEFAULT NULL,
  `weight` int(11) DEFAULT NULL,
  `plays` varchar(255) DEFAULT NULL,
  `turned_pro` int(11) DEFAULT NULL,
  `current_prize` int(11) DEFAULT NULL,
  `total_prize` int(11) DEFAULT NULL,
  `player_id` int(11) DEFAULT NULL,
  `current_rank` int(11) DEFAULT NULL,
  `name_code` varchar(255) DEFAULT NULL,
  `country` varchar(255) DEFAULT NULL,
  `full_name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14091 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `MatchRoundInfo`
--

DROP TABLE IF EXISTS `MatchRoundInfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `MatchRoundInfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `match_id` int(11) NOT NULL,
  `round_id` int(11) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `slug` varchar(255) DEFAULT NULL,
  `cup_round_type` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12088 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `MatchSeasonInfo`
--

DROP TABLE IF EXISTS `MatchSeasonInfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `MatchSeasonInfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `match_id` int(11) NOT NULL,
  `season_id` int(11) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `year` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19677 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `MatchTimeInfo`
--

DROP TABLE IF EXISTS `MatchTimeInfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `MatchTimeInfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `match_id` int(11) NOT NULL,
  `period_1` int(11) DEFAULT NULL,
  `period_2` int(11) DEFAULT NULL,
  `period_3` int(11) DEFAULT NULL,
  `period_4` int(11) DEFAULT NULL,
  `period_5` int(11) DEFAULT NULL,
  `current_period_start_timestamp` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19677 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `MatchTournamentInfo`
--

DROP TABLE IF EXISTS `MatchTournamentInfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `MatchTournamentInfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `match_id` int(11) NOT NULL,
  `tournament_id` int(11) DEFAULT NULL,
  `tournament_name` varchar(255) DEFAULT NULL,
  `tournament_slug` varchar(255) DEFAULT NULL,
  `tournament_unique_id` int(11) DEFAULT NULL,
  `tournament_category_name` varchar(255) DEFAULT NULL,
  `tournament_category_slug` varchar(255) DEFAULT NULL,
  `user_count` int(11) DEFAULT NULL,
  `ground_type` varchar(255) DEFAULT NULL,
  `tennis_points` int(11) DEFAULT NULL,
  `has_event_player_statistics` tinyint(1) DEFAULT NULL,
  `crowd_sourcing_enabled` tinyint(1) DEFAULT NULL,
  `has_performance_graph_feature` tinyint(1) DEFAULT NULL,
  `display_inverse_home_away_teams` tinyint(1) DEFAULT NULL,
  `priority` int(11) DEFAULT NULL,
  `competition_type` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19677 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `MatchVenueInfo`
--

DROP TABLE IF EXISTS `MatchVenueInfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `MatchVenueInfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `match_id` int(11) NOT NULL,
  `city` varchar(255) DEFAULT NULL,
  `stadium` varchar(255) DEFAULT NULL,
  `venue_id` int(11) DEFAULT NULL,
  `country` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19590 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `MatchVotesInfo`
--

DROP TABLE IF EXISTS `MatchVotesInfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `MatchVotesInfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `match_id` int(11) NOT NULL,
  `home_vote` int(11) DEFAULT NULL,
  `away_vote` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19678 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `OddsInfo`
--

DROP TABLE IF EXISTS `OddsInfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `OddsInfo` (
  `match_id` int(11) NOT NULL,
  `market_id` int(11) DEFAULT NULL,
  `market_name` varchar(255) DEFAULT NULL,
  `is_live` tinyint(1) DEFAULT NULL,
  `suspended` tinyint(1) DEFAULT NULL,
  `initial_fractional_value` varchar(255) DEFAULT NULL,
  `fractional_value` varchar(255) DEFAULT NULL,
  `choice_name` varchar(255) DEFAULT NULL,
  `choice_source_id` int(11) DEFAULT NULL,
  `winnig` tinyint(1) DEFAULT NULL,
  `change` int(11) DEFAULT NULL,
  PRIMARY KEY (`match_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `PeriodInfo`
--

DROP TABLE IF EXISTS `PeriodInfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `PeriodInfo` (
  `match_id` int(11) NOT NULL,
  `period` varchar(255) DEFAULT NULL,
  `statistic_category_name` varchar(255) DEFAULT NULL,
  `statistic_name` varchar(255) DEFAULT NULL,
  `home_stat` varchar(255) DEFAULT NULL,
  `away_stat` varchar(255) DEFAULT NULL,
  `compare_code` int(11) DEFAULT NULL,
  `statistic_type` varchar(255) DEFAULT NULL,
  `value_type` varchar(255) DEFAULT NULL,
  `home_value` int(11) DEFAULT NULL,
  `away_value` int(11) DEFAULT NULL,
  `home_total` int(11) DEFAULT NULL,
  `away_total` int(11) DEFAULT NULL,
  PRIMARY KEY (`match_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Players`
--

DROP TABLE IF EXISTS `Players`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Players` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `slug` varchar(255) DEFAULT NULL,
  `gender` varchar(1) DEFAULT NULL,
  `user_count` int(11) DEFAULT NULL,
  `residence` varchar(255) DEFAULT NULL,
  `birthplace` varchar(100) DEFAULT NULL,
  `height` float DEFAULT NULL,
  `weight` int(11) DEFAULT NULL,
  `plays` varchar(50) DEFAULT NULL,
  `turned_pro` int(11) DEFAULT NULL,
  `current_prize` int(11) DEFAULT NULL,
  `total_prize` int(11) DEFAULT NULL,
  `player_id` int(11) DEFAULT NULL,
  `current_rank` int(11) DEFAULT NULL,
  `name_code` varchar(10) DEFAULT NULL,
  `country` varchar(20) DEFAULT NULL,
  `full_name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `slug_index` (`slug`)
) ENGINE=InnoDB AUTO_INCREMENT=2354 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `PowerInfo`
--

DROP TABLE IF EXISTS `PowerInfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `PowerInfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `match_id` int(11) NOT NULL,
  `set_num` int(11) DEFAULT NULL,
  `game_num` int(11) DEFAULT NULL,
  `value` float DEFAULT NULL,
  `break_occurred` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=269695 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-06-27  6:49:17
