# Generate Football Matches among teams

teams = ['Gulu Winterbury', 'National Youth', 'U-Touch', 'Gulu Soccer Legends']
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print("First Leg: " + home_team + " Vs " + away_team)
            print("Second Leg: " + away_team + " Vs " + home_team)
    print()