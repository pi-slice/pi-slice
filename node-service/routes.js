module.exports = function (app, express) {
  app.get('/', (req, res) => {
    console.log(req)
    res.status(200).send('Hello world!')
  })

  return app
}
