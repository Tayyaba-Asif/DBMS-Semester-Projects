# Collaborators: Fill in names and SUNetIDs here

def query_one():
    """Query for Stanford's venue"""
    return """
       SELECT venue_name,venue_capacity 
       FROM `bigquery-public-data.ncaa_basketball.mbb_teams` 
       WHERE venue_city='Stanford' LIMIT 1000
    """

def query_two():
    """Query for games in Stanford's venue"""
    return """
       SELECT COUNT(venue_id) AS games_at_maples_pavilion 
       FROM `bigquery-public-data.ncaa_basketball.mbb_games_sr` 
       WHERE season=2013 AND venue_name='Maples Pavilion' LIMIT 1000
    """

def query_three():
    """Query for maximum-red-intensity teams"""
    return """
       SELECT market,color 
       FROM `bigquery-public-data.ncaa_basketball.team_colors` 
       WHERE LOWER(color) LIKE '#%ff__%' 
       ORDER BY market ASC  LIMIT 1000
    """

def query_four():
    """Query for Stanford's wins at home"""
    return """
       SELECT COUNT(win) AS number, ROUND(AVG(points),2) AS avg_stanford, ROUND(AVG(opp_points),2) AS avg_opponent 
       FROM `bigquery-public-data.ncaa_basketball.mbb_teams_games_sr` 
       WHERE market='Stanford' AND win=true  AND home_team=True AND (season BETWEEN 2013 AND 2017) LIMIT 1000
    """

def query_five():
    """Query for players for birth city"""
    return """
       SELECT  COUNT(DISTINCT player_id) AS num_players 
       FROM `bigquery-public-data.ncaa_basketball.mbb_players_games_sr` , `bigquery-public-data.ncaa_basketball.mbb_teams` 
       WHERE birthplace_city=venue_city AND birthplace_state=venue_state AND market=team_market LIMIT 1000
    """

def query_six():
    """Query for biggest blowout"""
    return """
       SELECT win_name, lose_name,win_pts,lose_pts, (win_pts-lose_pts) AS margin 
       FROM `bigquery-public-data.ncaa_basketball.mbb_historical_tournament_games` 
       ORDER BY margin DESC  LIMIT 1000
    """

def query_seven():
    """Query for historical upset percentage"""
    return """
       SELECT ROUND((COUNT(*)/(SELECT COUNT(*) FROM `bigquery-public-data.ncaa_basketball.mbb_historical_tournament_games`))*100,2) AS upset_percentage 
       FROM `bigquery-public-data.ncaa_basketball.mbb_historical_tournament_games` 
       WHERE win_seed>lose_seed LIMIT 1000
    """

def query_eight():
    """Query for teams with same states and colors"""
    return """
       SELECT a.name AS teamA,b.name AS teamB,a.venue_state 
       FROM `bigquery-public-data.ncaa_basketball.mbb_teams` a,
            `bigquery-public-data.ncaa_basketball.mbb_teams` b,
            `bigquery-public-data.ncaa_basketball.team_colors` c,
            `bigquery-public-data.ncaa_basketball.team_colors` d
             WHERE a.id=c.id AND b.id=d.id AND a.venue_state=b.venue_state AND c.color=d.color AND a.name<b.name 
             ORDER BY a.name LIMIT 1000
    """

def query_nine():
    """Query for top geographical locations"""
    return """
       SELECT birthplace_city AS city,birthplace_state AS state, birthplace_country AS country,SUM(points) AS total_points 
       FROM `bigquery-public-data.ncaa_basketball.mbb_players_games_sr`
       WHERE team_market='Stanford' AND season BETWEEN 2013 and 2017 
       GROUP BY birthplace_city,birthplace_state,birthplace_country 
       ORDER BY total_points DESC LIMIT 1000
    """

def query_ten():
    """Query for teams with lots of high-scorers"""
    return """
       SELECT team_market,COUNT(*) AS num_players 
       FROM (SELECT DISTINCT(player_id),team_market 
       FROM `bigquery-public-data.ncaa_basketball.mbb_pbp_sr` 
       WHERE season>=2013 AND period=1 
       GROUP BY game_id,player_id,team_market 
       HAVING SUM(points_scored)>=15) 
       GROUP BY team_market 
       ORDER BY COUNT(*) DESC,team_market
       LIMIT 5
    """

def query_eleven():
    """Query for highest-winner teams"""
    return """
       SELECT market AS team_market,COUNT(*) AS top_performer_count 
       FROM (SELECT season,MAX(wins) wins 
       FROM `bigquery-public-data.ncaa_basketball.mbb_historical_teams_seasons` SEASON1 
       WHERE season>=1900 AND season<=2000 GROUP BY season ORDER BY season)season1,
       `bigquery-public-data.ncaa_basketball.mbb_historical_teams_seasons` Season2 
       WHERE season1.season=season2.season AND season1.wins=season2.wins AND market IS NOT NULL GROUP BY market 
       ORDER BY COUNT(*) DESC,market LIMIT 5
    """