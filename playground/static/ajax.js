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

function getFact() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4) {
     document.getElementById("funFact").innerHTML = this.responseText;
    }
  };
  xhttp.open("GET", "/ajax/retxt", true);
  xhttp.send();
}
