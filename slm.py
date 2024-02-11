from   transformers    import   pipeline 
classifier =   pipeline('sentiment-analysis')
classifier([
    'i  love   the   show   called    game  of thrones  even   dispite  the   bad   last   season' , 
    'that  was   interesting   move to   sell    toxic   player  ,  so the  team  is   performing   well   now  '
])

qa      =   pipeline('question-answering')
qa({ "question" : 'when is best  time   to   invest ? ' ,  "context" : "there   definite   answer  that   one  size fits   all    .    it  depends  on  many  factors   such   as   your risk tolerance   and  desired  returns  and   many  more "})




