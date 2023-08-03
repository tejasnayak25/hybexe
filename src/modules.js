export let receiver = function(stack) {
    window.receiver = (event, message) => {
        stack.stack.push({event, message});
        call(event);
    }

    function call(event) {
        let item = stack.stack.find(item => { return item.event === event; });
        let reqEvent = stack.events.find(stkitm => { return stkitm.event === event; });
        let callback = reqEvent.callback;
        callback(item.message);
        return;
    }

    return;
}