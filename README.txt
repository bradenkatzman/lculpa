README.txt

. env/bin/activate

deactivate


check database:

BradenKzmansMBP:~ stormfootball4life$ mongo
MongoDB shell version: 3.0.2
connecting to: test
Welcome to the MongoDB shell.
For interactive help, type "help".
For more comprehensive documentation, see
	http://docs.mongodb.org/
Questions? Try the support group
	http://groups.google.com/group/mongodb-user
Server has startup warnings: 
2015-05-01T22:22:22.550-0400 I CONTROL  [initandlisten] 
2015-05-01T22:22:22.550-0400 I CONTROL  [initandlisten] ** WARNING: soft rlimits too low. Number of files is 256, should be at least 1000
> db.use
test.use
> use lculpa
switched to db lculpa
> show collections
review
system.indexes
> review.objects
2015-05-01T22:48:35.515-0400 E QUERY    ReferenceError: review is not defined
    at (shell):1:1
> db.review
lculpa.review
> .find
2015-05-01T22:48:50.779-0400 E QUERY    SyntaxError: Unexpected token .
> db.review.find
function ( query , fields , limit , skip, batchSize, options ){
    var cursor = new DBQuery( this._mongo , this._db , this ,
                        this._fullName , this._massageObject( query ) , fields , limit , skip , batchSize , options || this.getQueryOptions() );

    var connObj = this.getMongo();
    var readPrefMode = connObj.getReadPrefMode();
    if (readPrefMode != null) {
        cursor.readPref(readPrefMode, connObj.getReadPrefTagSet());
    }

    return cursor;
}
> db.review.find()
{ "_id" : ObjectId("55443ab1a1cd640616980d28"), "name" : "Braden" }
{ "_id" : ObjectId("55443abda1cd640617243d3f"), "name" : "Braden" }
{ "_id" : ObjectId("55443ac3a1cd640617243d40"), "name" : "gilad" }
> 
