use admin;
 
map = function() {
    var book_words = this.Book.split(" ");  // split with your logic.
    for (var i = 0; i < book_words.length; i++) 
    {
        emit(book_words[i].length, 1);
    }
};
 
reduce = function(key, value) {
    return value.length;
};
 
db.Library.mapReduce(map, reduce, {out:'reducing'});
 
db.reducing.find();
