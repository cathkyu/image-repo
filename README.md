# image-repo
## :camera: Image Repository Demo - Catherine Chen

This is an image repository project implemented with *Django* and Python! It updates dynamically from the sqlite3 database.

The project has the following features:

- **Create a new image to sell:** setting the title, price, quantity, image file
- **Discounts:** adding/editing a discount percentage to take off the total money earned
- **Handle money:** keep track of total money earned from sellings
- **Manage inventory**
- **Delete an image object**
- **Reset money/discounts**

### :eyes: Usage

1. In the command line, run `source bin/activate` to start a virtual environment

2. Next, run `cd src`

3. You may need to run `pip install django` and `pip install pillow` if not already installed (run `pip freeze` to see installed modules).

4. Then, run `python3 manage.py runserver`

5. After starting the server, open a web browser at the specified address. By default, the server runs on port 8000 on the IP address 127.0 (http://127.0.0.1:8000/).

6. To deactivate the virtual env, run `deactivate`

### :thought_balloon: Thoughts & Improvements

An improvement to this project could be to use cookies to keep track of images sold and to handle the money, rather than creating a separate money model in the database to store these variables. 

This project is based on a seller perspective, giving them full control on image objects to sell and money. Considering that, the project could be use different user access control for customers with user authentication. The customers would have a different view (with less freedom) to buy images using payment information linked to their user account.

### :zap: Extras

If you'd like, you can look at the objects in the database from Django admin (http://127.0.0.1:8000/admin) with username: `shopify` and password: `challenge` :)
