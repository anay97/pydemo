var express = require('express');
var router = express.Router();
/* GET home page. */
router.get('/', function(req, res, next) {
	var spawn = require("child_process").spawn;
	var pythonProcess = spawn('python',["pyscripts/b.py",'Sony']);
	pythonProcess.stdout.on('data', function (data){
		// Do something with the data returned from python script
		var x=JSON.parse(data);//Convert data to JSON
		console.log(x);
		res.render('index', { title: 'Python Demo', sum,diff,prod,quotient });
	});
});

module.exports = router;
