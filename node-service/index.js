const dotenv = require('dotenv').config()
const express = require('express')
const middleware = require('./middleware')
const routes = require('./routes')

const { PORT = 9999 } = process.env

let app = express()

app = middleware(app)
app = routes(app)

app.listen(PORT, console.log.bind(console, `Listening on ${PORT}!`))
