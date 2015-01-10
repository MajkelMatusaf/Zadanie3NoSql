var map = function(){
    var alfabet = this.key.split("").sort().join("");
    emit(alfabet,{"words":[this.key]})
}

var reduce = function(key,value){
    var lista = {"words":[]};
    value.forEach(function(word){
    lista["words"] = lista["words"].concat(word["words"]);
    })
    return lista;
}

db.kolekcja.mapReduce(
	map,
	reduce,
	{out:"rezultat"}
);

db.rezultat.find()