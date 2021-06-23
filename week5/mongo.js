// READ
let query = {"type": "red"};
let numberOfRedWines = db.products.find(query).length();
let numberOfWhiteWines = db.products.find({"type": "white"}).length();
numberOfRedWines;
numberOfWhiteWines;

// CREATE

//let newWine = { 
//"_id" : 119, 
//"name" : "BAD WINE",
//"type" : "RED", 
//"available_quantity" : 5
//};

//let result = db.products.insert(newWine);
//result.nInserted == 1;

//db.products.find({"name":"BAD WINE"});

//db.products.findAndModify({
//    query: { "name": "BAD WINE" },
//    update: { "name": "GOOD WINE" },
//});

db.products.find({ "name": "GOOD WINE" });


