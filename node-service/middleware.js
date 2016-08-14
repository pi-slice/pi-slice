const bodyParser = require('body-parser')
const morgan = require('morgan')

module.exports = function (app, express) {
  app.use(morgan('dev'))
  app.use(bodyParser.json())

  return app
}
