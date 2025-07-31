### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
 JavaScript was originally designed for web development and primarily runs in the browser; whereas Python can run on a server or locally with a REPL and is more general purpose 

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
  1. use the get() method which will return a "default" if it is missing from the dictionary
  2. user the in operator if "c" _in_ {} to check if the key exists 

- What is a unit test?
 This is a test that checks a part or a component of the overall code and does it in isolation, so you don't have to complete everything. 

- What is an integration test?
 This checks to see if the different parts work together.

- What is the role of web application framework, like Flask?
 It provides a set of tools as an interface for builiding web applications in Python, making it easier to route requests, manage data, and render pages

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?

- How do you collect data from a URL placeholder parameter using Flask?
  To collect a parameter, you use angle brackets <> starting with the param type, colon, and then the param name as part of the route. For example you would write @app.route('users/<int:user_id>)

- How do you collect data from the query string using Flask?
  The text following a question mark (?) is setup up in key-value pairs. 

- How do you collect data from the body of the request using Flask?
  With a form and a post route, you can collect data from the form using the request.form.get()

- What is a cookie and what kinds of things are they commonly used for?
  A small piece of data stored on the computer that helps the website remember information about the user. This could include session management, shopping related info, preferences, etc. 

- What is the session object in Flask?
  It is an object that helps to remember information while using the browser

- What does Flask's `jsonify()` do?
 It turns data structures into JSON formatting
