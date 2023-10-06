function call_me(){
    var base_value=$("#formGroupExampleInput").val();
    var base_currency=$("#form-select-base").val();
    var to_currency=$("#form-select-to").val();
    console.log(base_value);
    console.log(base_currency);
    console.log(to_currency);
    const settings = {
	    async: true,
	    crossDomain: true,
	    url: `https://currency-exchange.p.rapidapi.com/exchange?from=${base_currency}&to=${to_currency}&q=${base_value}`,
	    method: 'GET',
	    headers: {
		    'X-RapidAPI-Key': '2be85388b9msh873d41f7f0cb2c7p127ef4jsn34f1e34ec9c2',
		    'X-RapidAPI-Host': 'currency-exchange.p.rapidapi.com'
	    }
    };

    $.ajax(settings).done(function (response) {
	    console.log(response);
        $('#show').html(response);
    });
}