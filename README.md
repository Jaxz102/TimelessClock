# Timeless Clock
![](https://github.com/ryan-lam/TimelessClock/blob/main/logo.jpg)
## Inspiration
Our inspiration came from the fact that we wanted to create something that was simultaneously useful and not useful at the same time. We also wanted to compete in the "most useless hack" prize category and looked into how we can over-complicate a simple tool to make it inefficient.

## What it does
The timeless clock tells you the current time relative to the time of a past event. For example, it'll tell you that the time is 57 days, 4 hours, and 30 minutes relative to the start of the 2010 winter Olympics. This way, it is able to tell you the current time without telling you the current time!

## How we built it
We compiled a database of past events and their date+time. Then we built a backend that calculates the time difference between the current time and the past event. We then have a website (frontend) to display the time relative to the event and to change the background image

## Challenges we ran into
- Finding data of events that had date and time (HH:MM:SS)
- Connected the backend to the frontend with Flask

## Accomplishments that we're proud of
- Having a responsive frontend and a time counter
- Having an idea that's so stupid that it works

## What we learned
- Learned how to make a responsive frontend
- Learned how to connect front and backend using Flask

## What's next for The Timeless Clock
- Make it work for times/events that are in the future
- Make it work with times/events that happened in BC (before AD)
- Make events editable so people can use it as a deadline counter

## Demo Link
[The Timeless Clock Demo](https://youtu.be/C5vK3TcPIcA)

## Built by:
- Ryan Lam
- Jax Wang
- Ming Zhang
