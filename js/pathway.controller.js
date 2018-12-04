var xhr = new XMLHttpRequest();
xhr.open("GET", "/js/pathway.py", true);
xhr.responseType = "json";
xhr.onload = function(e) {
    console.log("xhr response");
    console.log(xhr.response);
  var arrOfStrings = JSON.parse(xhr.response);
//   console.log(arrOfStrings);
}
xhr.send();