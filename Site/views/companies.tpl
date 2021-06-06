% rebase('layout.tpl', year=year)
<form method="post" action="/companies" class="form">
<h2>{{ "Companies" }}</h2>


<style>

.center {
    position: absolute;
    top: 15%;
    left: 10%;
}

.form label {
    width: 180px;
    float: left;
}

.form label {
    width: 180px;
    float: left;                
    color: #008080;
    
}


.form textarea {
    width: 400px;
    resize:none;
}



</style>

<div class=center id=left>
<p>

<label for="Partners">Partner:</label>

<input type="text" name="Partners" id="parthners" />

</p>

<p>

<label for="PartnersAbout">About partner:</label>

<textarea name="PartnersAbout" id="PartnersAbout" class="textarea"  ></textarea>

</p>

<p>

<label for="Mail">Mail:</label>

<input type="text" name="Mail" id="mail" />

</p>

<p>

<label for="Phonenumber">Phone:</label>

<input type="text" name="Phonenumber" id="phone" />

</p>

</br>

<p>

<input type="submit" class="btn btn-default" value="Add" />

<a href="/home" class="btn btn-default">Back</a>

</p>

<h2> Our parthners: </h2>

<br>

%f = open('static/content/test.txt', 'r')
%a=''
%for line in f:
%a = (line)
<p>{{a}}</p>
%end


<address>
    <strong>Support:</strong>   <a href="mailto:Support@example.com">23FoodSupport@gmail.com</a><br />
    <strong>Marketing:</strong> <a href="mailto:Marketing@example.com">23FoodMarketing@gmail.com</a>
</address>
 <footer>
            <p>&copy; {{ year }} - 23Food Corp.</p>
            <a href = "vk.com"><img src = "static/image/img5.jpg" width = "40" height = "40"><a href = "instagramm.com"><img src = "static/image/img6.jpg" width = "40" height = "40"><a href = "facebook.com"><img src = "static/image/img7.jpg" width = "40" height = "40"></a>
</footer>
</div>

</body>

</form>