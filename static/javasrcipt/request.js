function valid()
{
    var a=document.myform.name.value;
    var d=document.myform.email.value;
    var e=document.myform.ContactNumber.value;
    if(a=="")
    {
        alert("Please enter your name");
        return false;
    }
    if(d=="")
    {
        alert("Please enter your email");
        return false;
    }
    if(e=="")
    {
        alert("Please enter your contact number");
            return false;
    }
}