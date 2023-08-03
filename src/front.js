let stack = []
let events = []

function send(event, message) {
    window.pywebview.api.send(event, message);
    return;
}

function on(event, callback) {
    events.push({ event, callback });
    return;
}
    
exports.stack = {
    stack, events
};
exports.send = send;
exports.on = on;