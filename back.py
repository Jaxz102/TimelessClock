from flask import Flask, redirect, url_for, render_template, request
import random
import datetime
import sys


app = Flask(__name__)

useless_list = [['since Barack Obama first become president', '2009-01-20 12:00:00', '0.jpg'], 
                ["since NASA's Perseverance rover landed on Mars", '2021-02-18 15:55:00', '1.jpg'], 
                ['since John Harvey Kellogg filed a patent for his cereals', '1895-05-31 10:36:00', '2.jpg'], 
                ['since the infamous NASDAQ flash crash', '2013-08-22 12:14:00', '3.jpg'], 
                ['since Elon Musk launched a Tesla Roadster into Space', '2018-02-06 20:45:00', '4.jpg'], 
                ['since the Wedding of Prince Carl Philip, Duke of Värmland, and Sofia Hellqvist took place', '2015-06-13 16:30:00', '5.jpg'], 
                ['since Bill Gates got smashed in the face with a pies', '1998-02-04 13:00:00', '6.jpg'], 
                ['since Rapper Drake was born', '1986-10-24 02:31:00', '7.jpg'], 
                ['since the Titanic first hit an iceberg', '1912-04-14 23:40:00', '8.jpg'], 
                ['since Neil Armstrong first planted his foot on the moon', '1969-07-20 22:56:00', '9.jpg'], 
                ['since Gangnam Style became the first youtube video to surpass 1 billion views', '2012-12-21 10:50:00', '10.jpg'], 
                ["since Donald Trump's second impreachment trial", '2021-02-09 09:00:00', '11.jpg'], 
                ['since Germany scored the 7th goal against Brazil in the FIFA World Cup', '2014-07-08 17:19:00', '12.jpg'], 
                ['since PewDiePie uploaded his first video', '2010-10-02 19:16:45', '13.jpg'], 
                ['since Burj Khalifa completed construction', '2009-10-01 16:25:12', '14.jpg'], 
                ['since people started Naruto running at Area 51', '2019-09-20 03:00:00', '15.jpg'], 
                ['since Pog champ got removed from Twitch.tv', '2021-01-06 21:12:32', '16.jpg'], 
                ['since Bitcoin hit 40K USD', '2021-01-07 18:15:00', '17.jpg'], 
                ['since Trump tweeted his first tweet on Twitter', '2009-05-04 14:54:25', '18.jpg'], 
                ['since Pokemon aired its first episode', '1997-04-01 18:00:00', '19.jpg'], 
                ['since the 2008 Beijing Olympics Ceremony', '2008-08-08 07:00:00', '20.jpg'], 
                ['since the first video was uploaded to Youtube', '2005-04-23 14:36:11', '21.jpg'], 
                ['since Gamestop stock hit $468.49 USD', '2021-01-28 09:55:00', '22.jpg'], 
                ['since the first WannaCry ransomeware attack', '2017-05-12 21:41:38', '23.jpg'], 
                ['since Gothic St. Peter and St. Paul Cathedral burned', '2019-04-15 19:20:00', '24.jpg'], 
                ['since "Youtuber" first added to the Oxford dictionary', '2016-12-28 11:00:00', '25.jpg'], 
                ['since Steve Jobs announced the first iPhone', '2007-01-09 12:00:00', '26.jpg'], 
                ['since Kim Kardashian and Kanye West first got married', '2014-05-24 18:00:00', '27.jpg'], 
                ['since Toronto Raptors won the 2019 NBA finals', '2019-06-13 23:11:12', '28.jpg'], 
                ['since Flappy Bird was first released', '2013-05-24 09:00:00', '29.jpg']]

def change():
    return random.randint(1,100)

def change2():
    return random.randint(1,100)

def generate():
  # Choose list of options
  list_of_options = useless_list
  num = random.randint(0, len(list_of_options)-1)
  option = list_of_options[num]

  # Which image to use
  img = option[2]

  # Get passed event date
  text_date = option[1] 
  date_time_obj = datetime.datetime.strptime(text_date, '%Y-%m-%d %H:%M:%S')

  # Calculate time difference
  delta = datetime.datetime.now() - date_time_obj

  # Convert datetime obj to str and format into list
  years = delta.days // 365
  days = delta.days % 365
  hours = int(str(datetime.timedelta(seconds=delta.seconds)).split(":")[0])
  minutes = int(str(datetime.timedelta(seconds=delta.seconds))[-5:-3])
  seconds = int(str(datetime.timedelta(seconds=delta.seconds))[-2:])
  delta_list = [years, days, hours, minutes, seconds]

  return [delta_list, option[0], option[2]]

@app.route('/', methods=['GET', 'POST'])
def home2():
    if request.method == 'POST':
        results = generate()
        dateResult = results[0]
        eventResult = results[1]
        image = results[2]
        return render_template('index.html', year=dateResult[0], day = dateResult[1], hour = dateResult[2], minute = dateResult[3], second = dateResult[4], event = eventResult, picture = image)
    else:   
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, port=8080)



#pip3 install virtualenv
#virtualenv env
#source env/bin/activate
#pip3 install flask 

# return render_template('my_other_template.html', 
#                        firstname=firstname,
#                        lastname=lastname,
#                        cellphone=cellphone)