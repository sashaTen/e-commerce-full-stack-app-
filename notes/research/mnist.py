from   transformers    import   pipeline 
classifier =   pipeline('sentiment-analysis')
classifier([
    'i  love   the   show   called    game  of thrones  even   dispite  the   bad   last   season' , 
    'that  was   interesting   move to   sell    toxic   player  ,  so the  team  is   performing   well   now  '
])