const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');

//initiating express
const app = express();
app.use(cors());
app.use(bodyParser.json())

// getting challenge
app.post('/challenge', (req, res) =>{
    if(req.body.challenge){
        console.log(req.body.challenge)
        res.send(req.body.challenge)
    }
})


const port = process.env.PORT || 4390;
app.listen(port, () => console.log(`Listening on port ${port}...`))