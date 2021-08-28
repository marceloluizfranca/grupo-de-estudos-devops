const express = require('express')
const app = express()
const cors = require('cors')
var dateTime = new Date();

const status = {
                "datetime": dateTime,
                "status": "up",
                "title": "API 02",
                "version": "1.0.0"
                }

app.use(cors())

app.get('/', function (req, res) { 
  res.send(status)
})

app.listen(81)