django => 
webapplication => request, response

1- urls.py (request)
2- view (response: (model, template))
3- model (database)
3- template (html, css, js)

templates/base.html

extent, block, include


blog -> url, view, template
account -> url, view, template



web app -> blog (post, comment, user, ...)
web app (x, ins, digi, ....) -> site > blog


django => url (request), response(view, model, template) 

function, classbase, mvt

view(render[template(html) + model(data)])

index.html 


base.html (navbar, footer)

login.html (extend base.html) (block) (include)


blog => table(users, posts, comment)
ecommerce => table(users, products, orders, comments, invoice, terminal, address, )


view => render(re, html, data)
login.html (extend base.html) (block) (include)

model => class Prodcuts:
                name
                price

model => class Post:
                id
                title
                content
                image





local   => pip freeze > requirements.txt
server  => pip install -r requirements.txt


python manage.py createsuperuser



template (html => قالب ظاهری)
model (داده و بانک داده)
url (ادرس های درخواست)
view (ظاهر میسازه (با رندر کردن داده داخل قالب))

