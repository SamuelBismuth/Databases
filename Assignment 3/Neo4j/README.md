# Neo4J

Here is a query in Cypher for neo4j :

// Match movies that at least two of Gal's friends liked or watched.

MATCH (g:student{ name:'Gal' })-[:friend*1..3]-(s:student)-[:like |:watch]- >(m:movie)
WITH m, COUNT(DISTINCT s) as num_student
WHERE num_student >= 2
WITH COLLECT(m) as team_movies

// Match movies that Gal watched AND liked that also include in team_movies.

MATCH (movies:movie)<-[:watch]-(gal:student{name:'Gal'})-[:like]- >(movies:movie)
WHERE (movies IN team_movies)
return movies

# Configuration

To verify our query we used deo4j Desktop.
After creating an account, you may be able to create your own database and run our query.


We add screenshots of the results.
