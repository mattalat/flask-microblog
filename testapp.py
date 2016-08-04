from flask import Flask, render_template, Markup
import markdown
import glob

# Setup flask, include Jade processing
app = Flask(__name__)
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')

# Retrieve info on .md posts
def get_posts():
    posts = []
    allPosts = glob.glob('./posts/*.md')
    for thisPost in allPosts:
        f = open(thisPost, 'r')
        file_contents = f.read()

        meta_ind = file_contents.index('\n')
        meta = file_contents[0:meta_ind].split(', ')
        contents = file_contents[meta_ind+2:len(file_contents)]
        url = meta[0].lower().replace(' ', '-')

        print(url)

        posts.append({
            'dir': thisPost,
            'title': meta[0],
            'url': url,
            'author': meta[1],
            'contents': contents
        })
    return posts

# store this for the app to use
posts = get_posts();

# Route index
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Route post index
@app.route('/posts/')
def jade(someString=None):
    return render_template('postIndex.jade', posts=posts)

# Route post
@app.route('/posts/<post_url>')
def render_post(post_url=None):
    i = -1
    for index in range(len(posts)):
        if (posts[index]['url'] == post_url):
            i = index
    if i != -1:
        thisPost = posts[i]
        title = thisPost['title']
        text = Markup(markdown.markdown(thisPost['contents']))
        return render_template('post.jade', text=text)
    else:
        return 'Post not found'


# Force app to run on specific port?
app.run(debug=True, host='0.0.0.0', port=5001)
