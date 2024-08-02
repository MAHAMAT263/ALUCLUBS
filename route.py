from flask import Flask, render_template , url_for, request, redirect  
import datetime
blogs = [
    {'club_name': 'Francophonie club', 'blog_title': 'Today session', 'icon':'img/ahmat.JPG' ,'blog_description': 'The Francophonie Club is a club that promotes the French language and culture. We host events such as French movie nights, French cooking classes, and French conversation hours. We also have a French book club and a French poetry club. Our goal is to create a community of people who love French and want to learn more about French culture.', 'comments': []},
          {'club_name': 'Robotic club',  'blog_title': 'Today session','icon':'img/ahmat.JPG' ,'blog_description': 'The Francophonie Club is a club that promotes the French language and culture. We host events such as French movie nights, French cooking classes, and French conversation hours. We also have a French book club and a French poetry club. Our goal is to create a community of people who love French and want to learn more about French culture.' ,'comments': []},
            {'club_name': 'Debate club', 'blog_title': 'Today session', 'icon':'img/ahmat.JPG' ,'blog_description': 'The Francophonie Club is a club that promotes the French language and culture. We host events such as French movie nights, French cooking classes, and French conversation hours. We also have a French book club and a French poetry club. Our goal is to create a community of people who love French and want to learn more about French culture.', 'comments': []},
             {'club_name': 'music club', 'blog_title': 'Today session', 'icon':'img/ahmat.JPG' ,'blog_description': 'The Francophonie Club is a club that promotes the French language and culture. We host events such as French movie nights, French cooking classes, and French conversation hours. We also have a French book club and a French poetry club. Our goal is to create a community of people who love French and want to learn more about French culture.', 'comments': []},
          {'club_name': 'science club', 'blog_title': 'Today session', 'icon':'img/ahmat.JPG' ,'blog_description': 'The Francophonie Club is a club that promotes the French language and culture. We host events such as French movie nights, French cooking classes, and French conversation hours. We also have a French book club and a French poetry club. Our goal is to create a community of people who love French and want to learn more about French culture.', 'comments': []},
            {'club_name': 'dance club', 'blog_title': 'Today session', 'icon':'img/ahmat.JPG' ,'blog_description': 'The Francophonie Club is a club that promotes the French language and culture. We host events such as French movie nights, French cooking classes, and French conversation hours. We also have a French book club and a French poetry club. Our goal is to create a community of people who love French and want to learn more about French culture.', 'comments': []},
             {'club_name': 'Coding club', 'blog_title': 'Today session', 'icon':'img/ahmat.JPG' ,'blog_description': 'The Francophonie Club is a club that promotes the French language and culture. We host events such as French movie nights, French cooking classes, and French conversation hours. We also have a French book club and a French poetry club. Our goal is to create a community of people who love French and want to learn more about French culture.', 'comments': []},
          {'club_name': 'English club', 'blog_title': 'Today session', 'icon':'img/ahmat.JPG' ,'blog_description': 'The Francophonie Club is a club that promotes the French language and culture. We host events such as French movie nights, French cooking classes, and French conversation hours. We also have a French book club and a French poetry club. Our goal is to create a community of people who love French and want to learn more about French culture.', 'comments': []},
            {'club_name': 'Germany club', 'blog_title': 'Today session', 'icon':'img/ahmat.JPG' ,'blog_description': 'The Francophonie Club is a club that promotes the French language and culture. We host events such as French movie nights, French cooking classes, and French conversation hours. We also have a French book club and a French poetry club. Our goal is to create a community of people who love French and want to learn more about French culture.', 'comments': []}
             
        ]
clubs = [{'name': 'Francophonie club', 'icon':'img/club.jpg' , 'president':'kevin', 'profile': 'profile' ,'president_pic':'img/ahmat.JPG' , 'whatssap':'join whatssap' , 'facebook':'join facebook' , 'instagram':'join instagram' , 'members': 100 , 'club_description': 'The Francophonie Club is a club that promotes the French language and culture. We host events such as French movie nights, French cooking classes, and French conversation hours. We also have a French book club and a French poetry club. Our goal is to create a community of people who love French and want to learn more about French culture.'},
         {'name': 'Science club', 'icon':'img/club.jpg' , 'president':'kevin', 'profile': 'profile', 'president_pic':'img/ahmat.JPG' ,'whatssap':'join whatssap' , 'facebook':'join facebook' , 'instagram':'join instagram' ,'members': 70 , 'club_description': 'The Francophonie Club is a club that promotes the French language and culture. We host events such as French movie nights, French cooking classes, and French conversation hours. We also have a French book club and a French poetry club. Our goal is to create a community of people who love French and want to learn more about French culture.'},
         {'name': 'Robotic club', 'icon':'img/club.jpg' , 'president':'kevin', 'profile': 'profile', 'president_pic':'img/ahmat.JPG' ,'whatssap':'join whatssap' , 'facebook':'join facebook' , 'instagram':'join instagram' ,'members': 50 , 'club_description': 'The Francophonie Club is a club that promotes the French language and culture. We host events such as French movie nights, French cooking classes, and French conversation hours. We also have a French book club and a French poetry club. Our goal is to create a community of people who love French and want to learn more about French culture.'},
         {'name': 'Dance club', 'icon':'img/club.jpg' , 'president':'kevin', 'profile': 'profile', 'president_pic':'img/ahmat.JPG' , 'whatssap':'join whatssap' , 'facebook':'join facebook' , 'instagram':'join instagram' ,'members': 30 , 'club_description': 'The Francophonie Club is a club that promotes the French language and culture. We host events such as French movie nights, French cooking classes, and French conversation hours. We also have a French book club and a French poetry club. Our goal is to create a community of people who love French and want to learn more about French culture.'},
         {'name': 'Music club', 'icon':'img/club.jpg' , 'president':'kevin', 'profile': 'profile', 'president_pic':'img/ahmat.JPG' , 'whatssap':'join whatssap' , 'facebook':'join facebook' , 'instagram':'join instagram' , 'members': 20 , 'club_description': 'The Francophonie Club is a club that promotes the French language and culture. We host events such as French movie nights, French cooking classes, and French conversation hours. We also have a French book club and a French poetry club. Our goal is to create a community of people who love French and want to learn more about French culture.'},
         {'name': 'Coding club', 'icon':'img/club.jpg' , 'president':'kevin', 'profile': 'profile', 'president_pic':'img/ahmat.JPG' , 'whatssap':'join whatssap' , 'facebook':'join facebook' , 'instagram':'join instagram' , 'members': 10 , 'club_description': 'The Francophonie Club is a club that promotes the French language and culture. We host events such as French movie nights, French cooking classes, and French conversation hours. We also have a French book club and a French poetry club. Our goal is to create a community of people who love French and want to learn more about French culture.'},]


app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
    now = datetime.datetime.now()
    total_blogs = len(blogs)
    per_page = 3
    start_index = (now.second // 5) % (total_blogs // per_page)
    start_index *= per_page
    end_index = start_index + per_page
    limited_blogs = blogs[start_index:end_index]
    for blog in limited_blogs:
        blog['publish_datetime'] = now.strftime('%Y-%m-%d %H:%M:%S')

    return render_template('Home.html',  title = 'Home' , blogs = limited_blogs , clubs = clubs)

@app.route('/like/<int:blog_id>', methods=['POST'])
def like_blog(blog_id):
    # Increment like count logic here
    # For simplicity, assuming we store likes directly in the blog dictionary
    if blog_id < len(blogs):
        # Example: Increment like count (could be a separate field)
        # blogs[blog_id]['likes'] += 1
        pass
    return redirect(url_for('index'))

@app.route('/comment/<int:blog_id>', methods=['POST'])
def comment_blog(blog_id):
    if blog_id < len(blogs):
        comment = request.form.get('comment')
        if comment:
            if 'comments' not in blogs[blog_id]:
                blogs[blog_id]['comments'] = []
            blogs[blog_id]['comments'].append(comment)
    return redirect(url_for('index'))

@app.route('/login')
def login():
    return render_template('login.html', title = 'Login')
@app.route('/signup')
def signup():
    
    return render_template('sign_up.html', title = 'Signup' )
@app.route('/contact')
def contact():
    now = datetime.datetime.now()
    total_blogs = len(blogs)
    per_page = 3
    start_index = (now.second // 5) % (total_blogs // per_page)
    start_index *= per_page
    end_index = start_index + per_page
    limited_blogs = blogs[start_index:end_index]
    for blog in limited_blogs:
        blog['publish_datetime'] = now.strftime('%Y-%m-%d %H:%M:%S')
         
    return render_template('Home.html', title = 'contact', blogs = limited_blogs, clubs = clubs)
@app.route('/about_us')
def about():
    now = datetime.datetime.now()
    total_blogs = len(blogs)
    per_page = 3
    start_index = (now.second // 5) % (total_blogs // per_page)
    start_index *= per_page
    end_index = start_index + per_page
    limited_blogs = blogs[start_index:end_index]
    for blog in limited_blogs:
        blog['publish_datetime'] = now.strftime('%Y-%m-%d %H:%M:%S')
         
    return render_template('Home.html', title = 'about_us', blogs = limited_blogs ,clubs = clubs)

@app.route('/club')
def club():
    
         
    return render_template('club.html', title = 'club' , blogs = blogs, clubs = clubs)




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500, debug=True)

if __name__ == '__main__':
    app.run(debug=True)