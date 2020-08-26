var mongo = require('mongodb'),
    Server = mongo.Server,
    Db = mongo.Db;
var server = new Server("mongodb+srv://sameerc:<omitted>@cluster0.cfzih.mongodb.net/test?authSource=admin&replicaSet=atlas-faaf84-shard-0&readPreference=primary&appname=MongoDB%20Compass%20Community&ssl=true", 27017, { 
    auto_reconnect: true
});