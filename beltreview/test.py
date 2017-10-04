<!DOCTYPE html>
<html lang="en">
    <head>
        <title></title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        {% load staticfiles %}
        <link href="{% static 'review/style.css' %}" rel="stylesheet">
    </head>
    <body>
        <p><a href="/books">Home</a> | <a href="/logout">Logout</a></p>
        <h1>{{book.title}}</h1>
        <h2>{{book.author}}</h2>
        <div class="reviews">
            <h3>Reviews:</h3>
            <hr>
            {% for review in book.reviews.all %}
                <p>Rating: {{review.rating}}</p>
                <p><a href="/user/{{review.reviewer.id}}">{{review.reviewer.name}}</a> says: {{review.review}}</p>
            <p>Posted on: {{review.created_at}}</p>
            <hr>
            {% endfor %}
        </div>
        <form action="/books/{{book.id}}/create" method="POST">
            {% csrf_token %}
            <div class="form-group">
                <label for="review">Review:</label>
                <textarea rows="5" cols="40" type="text" name="review"></textarea>
            </div>
            <div class="form-group">
                <label for="rating">Rating</label>
                <select name="rating">
                    <option value="1">1</option>
                    <option value="2">2</option>
                    <option value="3">3</option>
                    <option value="4">4</option>
                    <option value="5">5</option>
                </select>
            </div>
            <input type="submit" value="Submit Review">
        </form>
    </body>
</html>

Files
beltreview.zip 	August 29, 2017 	
No file chosen
or
Privacy Policy