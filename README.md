# Debate

Debate is an online discussion and commenting service.

It allow anybody to host his own discussion service on his own server, beside a blog. It can effectively replace Disqus to manage comments on static blogs or websites.

**Warning** : There is still some work to do before this tool can be used in prod. For example, access to administration panel is not limited.

## How it works

Utilisation is very simple. You can go on any url `http://debate/thread/<id>` where <id> can be any string. If the discussion is not created yet, it will be at the first comment added.

So the use it, the best way is to include one of these pages using JQuery Ajax request on the bottom of your blog posts. The file `template/test.hml` provide an example of this :

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

I repeat, "something" can be anything. The ID is typically to provide here the URL of your blog post to ensure the ID will be unique and "linked" to your the subjet.

### Administration

You have an administration panel on `http://debate/admin/` where you can admin threads and comments. For now, **the access is not secure**.

## Install

    cp settings.py.example settings.py
    python main.py 5000

## Technologies used

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
