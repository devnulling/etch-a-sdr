var express = require("express");
var bodyParser = require('body-parser');
var app = express();
var port = 7200;
var fs = require("fs");
var redis = require("redis");
var channel = [];
var channels = ['etch'];

app.use(bodyParser.json());       // to support JSON-encoded bodies
app.use(bodyParser.urlencoded({// to support URL-encoded bodies
    extended: true
}));

var http = require('http');
http.createServer(function (req, res) {
});

app.set('views', __dirname + '/jade');
app.set('view engine', "jade");
app.engine('jade', require('jade').__express);

app.get("/", function (req, res) {
    res.render("etch");
});
app.get("/post", function (req, res) {
    var channel = req.query.c,
            msg = req.query.m;

    publishMsg(channel, msg);
    var status = 200;
    var body = 'OK';
    res.status(status).send(body);
});

app.use(express.static(__dirname + '/public'));
var io = require('socket.io').listen(app.listen(port));
console.log("Listening on port " + port);

for (var i in channels) {
    channel[i] = redis.createClient();
    channel[i].subscribe(channels[i]);
    channel[i].on("message", function (channel, message) {
        console.log("client channel recieve from channel : %s, the message : %s", channel, message);
        io.sockets.emit('message', {message: message, channel: channel});
    });
}

function publishMsg(channel, message) {
    var redisClient = redis.createClient();
    redisClient.publish(channel, message);
}
