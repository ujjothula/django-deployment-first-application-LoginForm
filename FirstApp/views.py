from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def hello(request):
    print("hello/ url is requested & hello() is executed");
    ss = '''
	<!DOCTYPE html>
<html>
    <head>
        <title>login form</title>
    </head>
    <style>
        fieldset{
            background-color: aqua;
        }
        legend{
            background: red;
        }
        
    </style>
    <body>
        
        <fieldset>
            <legend>Login Form</legend>
            <input type="text" id="uname" placeholder="Enter user name">
            <br><br>
            <input type="password" id="upwd" placeholder="Enter password">
            <br><br>
            <button onclick="login()">Login</button>
            <h1 id="res"></h1>
        </fieldset>
        <script>
            let login=()=>{
            let x=document.getElementById("uname").value;
            let y=document.getElementById("upwd").value;
            if(x=="sathya" && y=="sathya@123"){
                document.getElementById("res").innerHTML="login sucess";
               
             }else{
                document.getElementById("res").innerHTML="Login Fail"; 
             }
            }
        </script>
        
    </body>
</html>
	''';
    return HttpResponse(ss);
def loginform(request):
    print("loginform/url is requested & loginform() is executed");
    ss = '''
    <!DOCTYPE html>
<html>

<head>
    <title>products</title>
</head>
<body>
    <label>Enter p value</label>
    <input type="text"id="uname1"placeholder="Enter p value">
    <br><br>
    <label>Enter q value</label>
    <input type="text"id="uname2"placeholder="Enter q value">
    <br><br>
    <label>product</label>
    <input type="text"id="uname3"placeholder="Enter product">
    <br><br>
    <button onclick="product1()">product</button>
    <button onclick="product2()">product</button>
    <h1 id="res"></h1>
    <script>
        let product1=()=>{
            let x=parseInt(document.getElementById("uname1").value);
            let y=parseInt(document.getElementById("uname2").value);
            let z=parseInt(document.getElementById("uname3").value);
                 document.getElementById("res").innerHTML="sprite";
        }
        let product2=()=>{
            let x=parseInt(document.getElementById("uname1").value);
            let y=parseInt(document.getElementById("uname2").value);
            let z=parseInt(document.getElementById("uname3").value);
            document.getElementById("res").innerHTML="kingfisher";
                 
        
            }
        
    
    </script>

</body>
</html>
       ''';
    return HttpResponse(ss);

