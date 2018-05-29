# MongoDB

Here a code in Java using Maven Central which insert some data in mongoDB.
The query look like this :

use admin;

db.Library.insert( {Book_name : "Harry Potter", Author : "JK Rollwing", Editor : "Folio Junior", Edit_year : 2004, Book : "The book himself download from pdf file in java."} ); 

# Attention 

See the code in java for the insert of the entire book.

# mapReduce

A javascript file is also add to this folder with a mapReduce implemetation :
please run 
mongo < mapReduce.js
from your linux terminal to run the mapReduce.
