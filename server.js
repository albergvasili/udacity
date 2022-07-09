/* LOCAL SERVER FOR WEATHER APP */

/* Start Express */
const express = require("express");
const app = express();

/* Middleware */
const bodyParser = require("body-parser");
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

const cors = require("cors");
app.use(cors());

/* Initialize main project folder */
//app.use(express.static("app"));

/* Create Server */
const port = 2001;
const server = app.listen(port, () => {
        console.log(`running on localhost: ${port}`);
});
