function valid1()
{
    var a=document.myform2.name.value;
    var d=document.myform2.fname.value;
    var e=document.myform2.lname.value;
    var b=document.myform2.email.value;
    var c=document.myform2.n1.value;
    var f=document.myform2.n2.value
    if(a=="")  
    {
        alert("Please  enter your Username")
        return false;
    }
   
    if(d=="")  
    {
        alert("Please  enter your fname") 
        return false;
    }
    if(e=="")  
    {
        alert("Please  enter your lname") 
        return false;
    }
    if(c=="")  
    {
        alert("Please  enter your Comment")
        return false;
    } if(f=="")  
    {
        alert("Please  enter your comments")
        return false;
    }
}