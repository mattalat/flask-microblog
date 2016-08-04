## Simple-as-dirt Flask Microblog

Add posts to `posts/` to have them automatically show up in the post index

### Md file metadata
Post metadata is communicated via the first line of the markdown file, which uses the following template: `<Title>, <Author>, <Date Added>`
* Example first line of .md file:
  > Wooden Posts All The Way, Old Man, 1925

* Becomes:
  1. Title: "Wooden Posts All The Way"
  2. url: `wooden-posts-all-the-way`
  3. Author: "Old Man"
  4. Date: 01-01-1925


### Templating
Templating using Jade
