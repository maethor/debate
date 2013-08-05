# Debate

Debate is an online discussion and commenting service.

It allows anybody to host his own discussion service on his own server, beside a blog. It can effectively replace Disqus to manage comments on static blogs or websites.

**Warning** : There is still some work to do before this tool can be used in prod. For example, access to administration panel is not limited, anybody can go there and remove or edit comments.

## How it works

It is very easy to use. You can go on any url `http://debate.example/thread/<id>` where `<id>` can be any string. If the discussion is not created yet, it will be at the first comment added.

So the use it, the best way is to include a thread url using JQuery Ajax request on the bottom of your blog posts. The file `template/test.hml` provide an example of this :

    <html>
      <head>
        somestuff, including JQuery
      </head>
      <body>
        <article>
          Article content
          <div id="comment-section">
          </div>
        </article>
      </body>
      <script type="text/javascript">
        $.get("{{ url_for('print_thread', thread_id='something') }}", function(data) {
            $('#comment-section').html(data);
            });
      </script>
    </html>

I repeat, "something" can be anything. The idea is typically to use the URL of your blog post to ensure the ID will be unique and "linked" to your the subjet.

The template is using Bootstrap 2.3 classes, so feel free to include it on your website or to add some lines of CSS to style the comment list and the form.

### Administration

You have an administration panel on `http://debate.example/admin/` where you can admin threads and comments. For now, **the access is not secure**.

## Install

    cp settings.py.example settings.py
    pip install -r requirements.txt
    python main.py

Then, you can access it with a browser at the url http://localhost:5000

In the next version, port will be configurable and a wsgi file will be provided to host it with an Apache or Nginx frontend.

## Technologies used

- Python_
- `The Flask Python Web microframework`_, with Admin, Gravatar, Markdown, SQLAlchemy and WTForms extensions
- Bootstrap_, the Twitter HTML5/CSS3 framework
- jQuery_ (not used by Debate but usefull to include a thread)

## TODO / Ideas

* Limit access to administration panel
* Put some vars in settings
* Display administration buttons directly on comments
* Secure inclusion, for example by checking the referer before accepting new comments
* Secure post by using some antispam system (Captcha, whatever)
* Notifications on new comments on a thread
* Allow admin to close a thread
* Respond to other comments
* REST API


.. _Python: https://en.wikipedia.org/wiki/Python_(programming_language)
.. _The Flask Python Web microframework: http://flask.pocoo.org/
.. _Bootstrap 2.3: http://getbootstrap.com/2.3.2/
.. _jQuery: http://jquery.com/
.. _WTF licence: http://en.wikipedia.org/wiki/WTFPL

