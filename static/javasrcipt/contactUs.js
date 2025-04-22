function validate()
{
    var a=document.myform4.Username.value;
    var b=document.myform4.Email.value;
    var c=document.myform4.ContactNumber.value;
    if(a=="")
    {
        alert("Please enter your username");
        return False;
    }
    if(b=="")
    {
        alert("Please enter your email");
        return False;
    }
    if(c=="")
    {
        alert("Please enter your contact");
        return False;
    }

}