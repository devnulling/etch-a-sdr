window.onload = function () {
    var socket = io.connect('http://localhost:7200');
    socket.on('message', function (data) {
        if (data.message) {
            parent.processSocket(data.message);
            console.log(JSON.stringify(data));
        } else {
            console.log("There is a problem:", data);
        }
    });
};
