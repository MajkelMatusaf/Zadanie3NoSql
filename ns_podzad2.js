var map = function(){
  emit(this.word,1)
}

var reduce = function(key,value){
  return Array.sum(value);
}

db.ns.mapReduce(
	map,
	reduce,
	{
	out:"nswynik"
	}
);

db.nswynik.find().sort({ value: -1 })