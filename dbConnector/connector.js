let express = require('express');
let app = express();

app.get('/', function(req, res) {
	
	let sql = require("mssql");
	//ADD CREDENTIALS
	let config = {
		user: '',
		password: '',
		server: 'localhost',
		database: 'testBill'
	}
	
	sql.connect(config, function(err){
		if (err) console.log(err);
		
		let request = new sql.Request();
		
		request.query('select * from one', function (err, recordset) {
            console.log(recordset);
            if (err) console.log(err)

            // send records as a response
            res.send(recordset);
            
        });
	})
})

const server = app.listen(5000, function () {
    console.log('Server is running..');
});
