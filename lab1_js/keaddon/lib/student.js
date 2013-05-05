var lang = require("language");
var util = require("utility");

var eng = ["the","and","it","is","be","he","she"];
var ger = ["der","die","das","und","ist"];
var fr	= ["aux","avec","dans","elle","ces"];
var esp	= ["la","que","el","los","con","como"]

var threshold = 2;

function isLang( text, stopwords)
{
	var x=0;
	for (i=0; i < stopwords.length; i++)
  	{
  		if ( text.indexOf(stopwords[i]) != -1 ) 
  		{
  			x = x +1;
  		}
  	}
	return x;
}

function student(text) {
	var ratings = [0,0,0,0];
	
	text = util.tokenize(text);
	
	ratings[0] = isLang(text,eng);
	if ( ratings[0] > threshold ){
		return lang.english;
	}
	ratings[1] = isLang(text,ger);
	if ( ratings[1] > threshold ){
		return lang.german;
	}
	ratings[2] = isLang(text,fr);
	if ( ratings[2] > threshold ){
		return lang.french;
	}
	ratings[3] = isLang(text,esp);
	if ( ratings[3] > threshold ){
		return lang.spanish;
	}
	console.log("Did not pass threshold. Try to find best match.");
	var max_index = -1;
	var max_value = 0;
	for(var i = 0; i < 3; i++)
	{
   		if(ratings[i] > max_value)
    			{
        			max_value = ratings[i];
        			max_index = i;
    			}
	}
	
	switch(max_index)
	{
		case 0:
			return lang.english;
		case 1:
			return lang.german;
		case 2:
			return lang.french;
		case 3:
			return lang.spain;
		default:
			console.log("No language found. Fallback.");
			return 0;
	}
	
	return 0;	
}

exports.student = student;
