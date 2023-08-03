/**
 * @param { String } path - Module Path
 * @param { String } main - Main Filename - For Node_Modules (optional)
 */

window.require = (path, main) => {
    let exports = {};
    let jsonData = null;
    let isJson = false;
  
    if (!path.startsWith(".")) {
      if (path.includes(".")) {
        path = "../node_modules/" + path;
      } else {
        path = `../node_modules/${path}/${main}`;
      }
    }
  
    if (path.endsWith(".json")) {
      isJson = true;
    }
  
    const xhr = new XMLHttpRequest();
    xhr.open("GET", path, false); // Set the request to be synchronous
  
    xhr.onreadystatechange = function () {
      if (xhr.readyState === 4) {
        if (xhr.status === 200) {
          if (isJson) {
            jsonData = JSON.parse(xhr.responseText);
          } else {
            eval(xhr.responseText);
          }
        } else {
          throw new Error("Error loading file: " + path);
        }
      }
    };
  
    xhr.send();
  
    if (isJson) {
      return jsonData;
    } else {
      return exports;
    }
  };
  