import { receiver } from "./modules.js";

window.addEventListener("pywebviewready", () => {
    let { send, on, stack } = require("./front.js");

    on("Bye", function (data) {
        send("Bye", "Hey " + data);
    });

    on("Hi", function(data) {
        console.log(data);
    });

    receiver(stack);
});