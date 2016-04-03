// Taken from https://stackoverflow.com/questions/8486099/how-do-i-parse-a-url-query-parameters-in-javascript
function urlParameters() {
  var query = location.search.substr(1);
  var result = {};
  query.split("&").forEach(function(part) {
    var item = part.split("=");
    result[item[0]] = decodeURIComponent(item[1]);
  });
  return result;
}

function confirm() {
  params = urlParameters();
  params = JSON.stringify(params);
  $.ajax({
    type: "POST",
    url: "/confirm_relation",
    data: params
  });
}
