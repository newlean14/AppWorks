var a = document.getElementById("loginBtn");
var b = document.getElementById("registerBtn");
var x = document.getElementById("login");
var y = document.getElementById("register");

function login() {
  x.style.left = "4px";
  y.style.right = "-520px";
  a.className += " white-btn";
  b.className = "btn";
  x.style.opacity = 1;
  y.style.opacity = 0;
}

function register() {
  x.style.left = "-510px";
  y.style.right = "5px";
  a.className = "btn";
  b.className += " white-btn";
  x.style.opacity = 0;
  y.style.opacity = 1;
}

function loginPage() {
  var username = document.getElementById("username").value;
  var password = document.getElementById("password").value;
  
  if (username === "admin" && password === "12345") {
    window.location.href = "other_pages/index-帳號資訊.html";
  } else {
    alert("Error");
  }
}