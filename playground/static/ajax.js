/*function getFact() {
  $.ajax({
    url: 'localhost:8000/',
    type: 'get', // This is the default though, you don't actually need to always mention it
    success: function(data) {
        alert(data);
    },
    failure: function(data) {
        alert('Got an error dude');
    }
  });
};*/
var oldfactindex = null
function getFact() {
  var xhttp = new XMLHttpRequest();
  var data = new FormData();
  xhttp.onload = function() {
    var sptxt = this.responseText.split("__")
    oldfactindex = sptxt[0]
    document.getElementById("funFact").innerHTML = sptxt[1];
  };
  xhttp.open("POST", "/ajax/retxt/", true);
  data.append('index', oldfactindex);
  xhttp.send(data);
}
